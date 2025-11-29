# Kiro Playbook: Database-Backed CRUD Operations

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for building multi-tenant database architecture.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Row Level Security policies need careful upfront design - mistakes leak data between departments
- Audit compliance requires documented decisions you can trace back to requirements
- Migration ordering affects whether your system even starts - design before you build
- Seven-year retention rules need explicit acceptance criteria, not afterthoughts

Vibe Mode works for generating sample data or tweaking queries, but your schema design needs Spec Mode rigour.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this platform does
GOV.UK Enquiries is a centralised system where government departments manage citizen
enquiries through a single, shared platform. Each department sees only their own data
while benefiting from shared infrastructure and consistent processes.

## Who uses this platform
- Caseworkers: handle enquiries day-to-day, need fast access to their queue
- Supervisors: monitor team performance, reassign cases, approve escalations
- Auditors: review historical records for compliance, never modify data

## Compliance requirements
- Seven-year retention for all enquiry records
- Complete audit trail: who did what, when, to which record
- Soft delete only: records are marked inactive, never physically removed
- Department isolation: users must never see another department's data

## Multi-tenant principles
- Tenant context set at session start, enforced by database
- No application code should filter by tenant - the database handles isolation
- Shared schema, isolated data: departments share table structures but not records
```

### tech.md

```markdown
# Technical Standards

## Database
- PostgreSQL 15+ with Row Level Security enabled
- Every table with tenant data includes tenant_id column
- RLS policies enforce tenant isolation at database level

## Audit trail design
- Trigger-based: application code cannot bypass audit logging
- Immutable: audit records cannot be updated or deleted
- Context capture: user_id, tenant_id, timestamp, action, before/after state

## Schema organisation
- core schema: shared reference data (enquiry types, status values)
- tenant schema: department-specific configuration
- audit schema: immutable audit trail tables

## Naming conventions
- Tables: plural, snake_case (enquiries, audit_logs)
- Foreign keys: singular_table_id (department_id, not departments_id)
- Timestamps: created_at, updated_at, deleted_at (for soft delete)
- Audit columns: created_by, updated_by (user references)
```

## Hooks for this challenge

Save these in `.kiro/hooks/` to catch schema problems before they reach production.

### sql-migration-validator.yaml

```yaml
name: sql-migration-validator
event: file_saved
match: "**/*.sql"
prompt: |
  Review this SQL migration for multi-tenant safety:
  - Tables with tenant data missing tenant_id column
  - Missing RLS policy for new tables
  - Missing audit trigger for tables that modify data
  - Foreign keys without ON DELETE constraints
  - Missing indexes on tenant_id columns
  - Migrations that drop columns (data loss risk)
  Report issues with line numbers and required fixes.
```

## Agents for this challenge

Save this in `.kiro/agents/` to get specialised database design help.

### database-architect.md

```markdown
# Database Architect Agent

You are a PostgreSQL specialist focused on multi-tenant SaaS architecture.

## Your expertise
- Row Level Security policy design and performance
- Audit trail patterns for compliance requirements
- Migration strategies that avoid downtime
- Tenant isolation testing approaches

## When reviewing schemas
- Check every table has appropriate RLS policies
- Verify audit triggers capture all required context
- Ensure soft delete is consistent across all entities
- Validate foreign key relationships respect tenant boundaries

## When asked about performance
- RLS adds overhead - suggest indexing strategies
- Audit tables grow fast - recommend partitioning approaches
- Tenant queries need tenant_id in WHERE clauses for index use
```

## Effective spec prompts

Use these prompts to guide Kiro through your database design.

### Initial requirements gathering

> I am building GOV.UK Enquiries - a multi-tenant platform where government departments manage citizen enquiries. Each department must only see their own data. I need complete audit trails for compliance and seven-year data retention.
>
> Please create requirements for the data model. Focus on: what entities we need, how tenant isolation works, and what audit information we must capture.

### Technical design from requirements

> Based on these requirements, design the PostgreSQL schema. Include:
> - Table definitions with all columns and constraints
> - Row Level Security policies for tenant isolation
> - Audit trigger functions that capture user and tenant context
> - Index strategy for common query patterns
>
> Explain the trade-offs in your design decisions.

### Task breakdown for implementation

> Break the database implementation into migration files. Consider:
> - Dependencies between tables (create referenced tables first)
> - RLS policies must be added after tables exist
> - Audit triggers depend on audit tables existing
> - Sample data depends on all structure being in place
>
> Order the tasks so each migration can run independently.

### Compliance verification queries

> Write SQL queries that verify our compliance requirements:
> - Query to confirm no records exist without audit trail entries
> - Query to check all tables have RLS policies enabled
> - Query to find any records with physical deletes (should be zero)
> - Query to verify tenant isolation (no cross-tenant references)

## Gotchas specific to database architecture

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| RLS tanks performance | Policies evaluated per row without indexes | Add tenant_id to every index; test with realistic data volumes |
| Audit loses context | Trigger fires but session variables not set | Set tenant_id and user_id at connection start; verify in application layer |
| Migrations fail ordering | Table references another table that does not exist yet | Draw dependency graph before writing migrations; test clean install |
| Soft delete breaks queries | WHERE clauses forget deleted_at IS NULL | Create views that filter deleted records; query views not tables |
| Foreign keys cross tenants | department_id references valid row in wrong tenant | Add tenant_id to all foreign key relationships |
| Sample data violates constraints | Generated data has orphaned references | Generate parent records before children; validate referential integrity |

## Quality checkpoints

### Schema design phase

- [ ] Every tenant-scoped table has tenant_id column
- [ ] RLS policy exists for every tenant-scoped table
- [ ] Audit trigger attached to every table that stores user data
- [ ] Soft delete columns (deleted_at, deleted_by) on appropriate tables
- [ ] Indexes include tenant_id for all tenant-scoped queries

### Audit completeness

- [ ] Audit captures: who, when, what table, what action, before state, after state
- [ ] Audit table has no UPDATE or DELETE permissions
- [ ] Audit records include tenant context
- [ ] Queries exist to reconstruct record state at any point in time

### Workflow integrity

- [ ] Enquiry status transitions follow defined workflow
- [ ] Status changes create audit records
- [ ] Reassignment captures both old and new assignee
- [ ] Escalation rules enforce supervisor approval

### Sample data verification

- [ ] Data spans multiple departments
- [ ] Enquiries exist in all workflow states
- [ ] Audit trail exists for every state change
- [ ] Running compliance queries returns expected results

## Reflection questions

When you finish, consider:

- How did Spec Mode affect your schema design compared to diving straight into SQL?
- Which RLS or audit gotchas caught you despite reading these tips?
- Did the migration ordering cause any failed deployments?
- How confident are you that tenant isolation actually works?
- What compliance queries would an auditor ask for that you have not written?
- What would you add to your steering files for your next multi-tenant system?
