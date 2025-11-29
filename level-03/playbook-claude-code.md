# Claude Code Playbook: Database-Backed CRUD Operations

Your starter kit for building multi-tenant government enquiry systems. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start. It sets expectations for every prompt.

```markdown
## Project: GOV.UK Enquiries Platform

Multi-tenant enquiry management system for government departments.

### PostgreSQL multi-tenant patterns
- Use row-level security (RLS) policies for tenant isolation - never rely on application code alone
- Every table with tenant data must have a `tenant_id` column
- Set `current_setting('app.current_tenant')` at connection start, use in RLS policies
- Test tenant isolation explicitly - verify user A cannot see user B's data

### Audit trail requirements
- Audit tables are append-only - never UPDATE or DELETE audit records
- Use database triggers, not application code, to populate audit trails
- Capture: who (user_id), what (action, old_value, new_value), when (timestamp with timezone)
- Include request_id for correlating actions across tables

### Naming conventions
- Primary keys: UUIDs using `gen_random_uuid()`, column name `id`
- Timestamps: `created_at`, `updated_at` (with timezone), populated by triggers
- User tracking: `created_by`, `updated_by` referencing users table
- Foreign keys: `{table_name}_id` (e.g., `enquiry_id`, `department_id`)
- Boolean columns: `is_` prefix (e.g., `is_active`, `is_resolved`)

### Schema organisation
- `public` schema for application tables
- `audit` schema for audit trail tables
- `auth` schema for users, roles, permissions
- Migrations must be idempotent - safe to run multiple times
```

---

## Custom slash commands

Save these files in `.claude/commands/` for quick access during the challenge.

### `.claude/commands/schema-review.md`

```markdown
---
description: Check migration for multi-tenant compliance and audit requirements
---

Review $ARGUMENTS for multi-tenant database compliance. Check:

**Tenant isolation:**
- Does every data table have a tenant_id column?
- Are RLS policies defined and enabled on all tenant tables?
- Do policies use current_setting('app.current_tenant') correctly?
- Is there a FORCE ROW LEVEL SECURITY on each table?

**Audit trail:**
- Is there a corresponding audit table for this entity?
- Does a trigger capture INSERT, UPDATE, DELETE actions?
- Are old and new values stored as JSONB?
- Is the audit table append-only (no UPDATE/DELETE grants)?

**Naming and types:**
- Are primary keys UUIDs with gen_random_uuid() default?
- Do timestamps use TIMESTAMPTZ (not TIMESTAMP)?
- Are created_at/updated_at triggers in place?
- Do foreign key columns follow {table}_id convention?

**Indexes:**
- Is tenant_id indexed (critical for RLS performance)?
- Are foreign keys indexed?
- Is there a composite index on (tenant_id, commonly_filtered_column)?

Report each issue with severity (critical/warning) and specific SQL fix.
```

### `.claude/commands/generate-sample-data.md`

```markdown
---
description: Generate realistic GOV.UK enquiry data for testing
---

Generate sample data for $ARGUMENTS with these requirements:

**Departments to include:**
- HMRC (tax queries - high volume, often urgent)
- DVLA (vehicle/licence queries - transactional)
- HMCTS (court guidance - complex, sensitive)
- DWP (benefits queries - varied complexity)

**Data realism:**
- Enquiry subjects should reflect real citizen needs (tax refunds, driving licence renewals, court date queries, benefits eligibility)
- Use realistic UK names, postcodes, and reference numbers
- Include a mix of statuses: new, in_progress, awaiting_response, resolved, escalated
- Timestamps should span the last 90 days with realistic distribution (more weekdays, business hours)

**Volume:**
- At least 100 enquiries per department
- Multiple staff members per department handling cases
- Some enquiries with multiple updates/responses

**Edge cases to include:**
- Enquiries transferred between departments
- Escalated cases requiring senior review
- Reopened resolved enquiries
- Enquiries with attachments referenced

Output as executable SQL INSERT statements, respecting foreign key order.
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| Initial schema design | Opus | Complex relationships need careful thought |
| RLS policy writing | Opus | Security-critical - catches edge cases |
| Basic CRUD operations | Sonnet | Standard patterns, fast iteration |
| Audit trigger logic | Opus | Recursion risks need careful handling |
| Sample data generation | Sonnet | Volume task, patterns are straightforward |
| Performance analysis | Opus | Understands query planning trade-offs |
| Migration scripts | Sonnet | Mostly mechanical once schema is designed |

**Switch with `/model`** - use Opus for security and architecture, Sonnet for implementation.

---

## Effective prompts for this challenge

**Initial schema design:**
> "Design a PostgreSQL schema for a multi-tenant enquiry management system. Each department (tenant) manages citizen enquiries with workflow states. Include: departments, users, enquiries, enquiry_updates, and workflow_states tables. Use UUIDs for primary keys, add tenant_id to all tenant-scoped tables, and include created_at/updated_at/created_by/updated_by on every table. Show the CREATE TABLE statements with all constraints."

**RLS policy design:**
> "Create row-level security policies for the enquiries table. The tenant_id should be checked against current_setting('app.current_tenant'). Include policies for SELECT, INSERT, UPDATE, and DELETE. The INSERT policy must ensure new rows have the correct tenant_id. Add FORCE ROW LEVEL SECURITY so even table owners are subject to policies. Show how to set the session variable at connection time."

**Audit trigger implementation:**
> "Create an audit system for the enquiries table. The audit.enquiry_changes table should store: change_id (UUID), enquiry_id, action (INSERT/UPDATE/DELETE), old_values (JSONB), new_values (JSONB), changed_by, changed_at, and request_id. Create a trigger function that populates this on any change. Ensure the trigger cannot recurse and that the audit table has no UPDATE or DELETE permissions."

**Sample data generation:**
> "Generate 500 realistic enquiry records across 4 government departments. Include: HMRC tax queries with reference numbers like 'TAX-2024-XXXXX', DVLA licence queries with driver numbers, HMCTS court date enquiries with case references, and DWP benefits questions. Distribute created_at timestamps across the last 90 days, weighted towards weekdays. Assign to 3-5 staff members per department. Include a realistic mix of statuses."

**Performance validation:**
> "Analyse the query performance for this enquiry listing query with RLS enabled. Show the EXPLAIN ANALYZE output interpretation. Check if the tenant_id filter from RLS is using the index. Identify any sequential scans that should be index scans. Suggest index improvements if the query examines significantly more rows than it returns."

---

## Tips and gotchas

### Tenant isolation risks

| Issue | What to do |
|-------|------------|
| RLS bypassed by superuser | Create a non-superuser role for the application - superusers bypass RLS |
| Missing FORCE ROW LEVEL SECURITY | Always add this - otherwise table owners bypass policies |
| tenant_id not set | Application must set `app.current_tenant` before every query - add connection middleware |
| Direct SQL access | Ensure database tools and scripts also set the tenant context |

### CASCADE DELETE danger

| Issue | What to do |
|-------|------------|
| Deleting tenant removes all data | This may be intended, but audit trail should survive - store audits in separate schema with no CASCADE |
| Orphaned references | Use ON DELETE RESTRICT for enquiry references to prevent accidental data loss |
| Testing DELETE behaviour | Always test what happens when you delete a parent record before production |

### Audit trigger pitfalls

| Issue | What to do |
|-------|------------|
| Infinite recursion | Audit triggers must not fire on the audit table - use `WHEN (pg_trigger_depth() = 0)` or separate schema |
| Missing user context | Set `app.current_user` session variable alongside tenant for audit capture |
| Large JSONB values | Consider excluding large text fields from old_values/new_values or storing separately |
| Timestamp precision | Use `clock_timestamp()` not `now()` in triggers - `now()` returns transaction start time |

### Index mistakes

| Issue | What to do |
|-------|------------|
| No index on tenant_id | Every RLS-filtered table needs a tenant_id index - without it, every query is a seq scan |
| Wrong index order | For composite indexes, put tenant_id first: `(tenant_id, status)` not `(status, tenant_id)` |
| Missing foreign key indexes | PostgreSQL does not auto-index FKs - add them manually for JOIN performance |

### Session variable handling

| Issue | What to do |
|-------|------------|
| Variable not set | `current_setting('app.current_tenant')` throws error if not set - use `current_setting('app.current_tenant', true)` for NULL default |
| Variable leaks between requests | Reset session variables at connection start, not just when they change |
| Connection pooling issues | With pgBouncer, set variables in transaction mode - session mode persists across users |

---

## Reflection questions

After completing the challenge, consider:

- How confident are you that tenant A genuinely cannot access tenant B's data? How did you verify this?
- What would happen to your audit trail if someone with database access tried to cover their tracks?
- Where did you find yourself fighting PostgreSQL versus working with it?
- How did the RLS policies affect your query complexity and performance?
- What would you add to CLAUDE.md for a team inheriting this database?
- Did the schema design prompts give you a complete picture, or did you need multiple iterations?
