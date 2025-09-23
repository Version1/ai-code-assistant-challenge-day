# Level 7: Performance Investigation & System Resilience

**Theme: AI-powered performance forensics and proactive system reliability design**

## Challenge Overview

Government digital services must maintain consistent performance under varying citizen demand, particularly during peak usage periods like tax deadlines, school application windows, and benefit renewal cycles. Under the Government Service Standard Point 8 ("Make your service's performance meet user needs") and the Technology Code of Practice Point 9 ("Define your procurement needs and assess the market"), departments must implement comprehensive performance monitoring and incident response capabilities that ensure service reliability for citizens who depend on government digital services.

The 2023 Central Digital and Data Office Service Assessment Annual Report found that "performance-related service failures disproportionately impact vulnerable citizens who rely on digital government services" with manual incident investigation processes creating "extended resolution times that compound citizen exclusion and service inequality."

**The problems with reactive performance management:**

- Manual incident investigation cannot rapidly identify root causes in complex government service architectures
- Performance issues often have non-obvious underlying causes requiring systematic analysis of multiple data sources
- Limited correlation between infrastructure metrics and citizen impact during service degradation
- Inconsistent incident response approaches across government departments leading to variable resolution times
- No systematic learning from performance incidents to prevent similar issues in future service design
- Resource allocation decisions based on surface symptoms rather than actual bottlenecks and system constraints
- Difficulty maintaining service resilience during unexpected demand surges or system component failures

**The specific challenge of complex performance investigation:**

Modern government digital services exhibit performance problems that require sophisticated analysis:
- **Multi-layered architectures:** Issues may originate in application logic, database queries, caching layers, or infrastructure components
- **Interdependent systems:** Performance degradation cascades across multiple service components making root cause identification challenging
- **Citizen impact correlation:** Technical metrics must be connected to actual citizen experience and service accessibility
- **Temporal patterns:** Performance issues may only manifest under specific usage patterns, time periods, or system states
- **False correlation:** Surface symptoms often mislead investigation toward infrastructure scaling rather than addressing underlying inefficiencies

**The opportunity:** AI tools can rapidly analyse complex performance data sources, identify non-obvious root causes, and design comprehensive monitoring architectures that enable proactive system resilience rather than reactive incident response. This approach transforms performance management from manual firefighting into systematic, predictive service reliability engineering.

## The Challenge

**Objective:** Use AI tools to conduct comprehensive performance forensics on a government service incident, identifying the true root cause and designing systematic monitoring and resilience improvements

- Analyse realistic performance incident materials from a Local Council Community Centre Booking System outage
- Use AI tools to correlate multiple data sources and identify the non-obvious root cause behind apparent scaling issues
- Design comprehensive monitoring architecture that would have detected this issue proactively
- Create systematic resilience improvements preventing similar performance failures across government services
- Demonstrate AI-powered incident investigation workflows that can be applied across different government digital services

## Success Criteria

### Core Requirements

- **Root cause identification:** Accurate identification of the underlying performance issue through systematic analysis of multiple data sources
- **Comprehensive incident investigation:** Complete correlation between infrastructure metrics, application behavior, and citizen impact during the performance degradation
- **Monitoring architecture design:** Proactive monitoring strategy that would detect similar issues before they impact citizen services
- **Performance resilience planning:** Systematic improvements preventing this class of performance issue and enhancing overall service reliability
- **Investigation methodology:** Reusable AI-assisted investigation workflow that can be applied to different government service performance incidents
- **Citizen impact assessment:** Clear understanding of how technical performance issues translate to citizen service disruption and accessibility barriers

### Government-Specific Requirements

- **Cross-government applicability:** Investigation methodology and monitoring approaches that can be adapted across different government digital services and departments
- **Service continuity planning:** Performance resilience strategies that maintain citizen service availability during component failures or demand surges
- **Resource optimisation:** Evidence-based recommendations for infrastructure and application improvements that address actual bottlenecks rather than surface symptoms
- **Operational readiness:** Monitoring and alerting strategies appropriate for government operational teams with varying technical expertise levels

## Source Materials: Community Centre Booking System Performance Incident

**Investigation Materials Repository:** performance-incident-materials/

You will work with comprehensive performance investigation materials from a realistic government service outage representing common performance challenges found in local government digital services.

### Service Context
- **Local Council Community Centre Booking System:** Online booking for community centres, sports halls, and meeting rooms
- **Normal operational capacity:** 200-300 bookings per day with peak usage during evenings and weekends
- **Incident timeframe:** Monday 15th January 2025, 9:00 AM - 2:00 PM
- **Citizen impact:** Page load times increased from 2 seconds to 45+ seconds, booking failures, citizen service disruption
- **Surface symptoms:** Database connection exhaustion, memory pressure, CPU spikes - typical scaling problem indicators

### Investigation Materials Available
- **Application server logs:** Performance degradation patterns, error traces, and system resource warnings
- **Database performance logs:** Query execution times, connection pool metrics, and resource contention indicators
- **Infrastructure monitoring data:** CPU, memory, network, and response time metrics with 5-minute granularity
- **Citizen service desk tickets:** Impact reports and complaint patterns correlated with the technical incident
- **Load balancer access logs:** Request patterns, response codes, and user behavior during the incident
- **Application metrics:** Booking success rates, search performance, and feature usage patterns during degradation

### Performance Investigation Challenge
The incident materials contain **multiple red herrings** that suggest obvious scaling solutions (more servers, larger connection pools, additional memory) but hide a **subtle root cause** that requires systematic AI-assisted analysis to discover. The true issue is non-obvious and would not be resolved by traditional infrastructure scaling approaches.

## Supporting Resources

This challenge requires **AI-powered performance forensics** - using AI tools to systematically analyse complex performance incidents and identify non-obvious root causes that traditional investigation approaches might miss. The key principle is: **systematic incident analysis reveals hidden performance bottlenecks**.

### Approach 1: Prompt-Driven Development ("Performance Detective Work")

This approach uses AI tools to systematically analyse performance incident data, correlate multiple data sources, and identify root causes through pattern recognition and anomaly detection.

**When to use:** Complex performance incidents with non-obvious causes, time-sensitive root cause analysis, systematic learning from performance patterns across government services.

#### Phase 1: Meta-Prompting for Performance Investigation Planning

Use AI tools to develop systematic approaches for analysing complex performance incidents:

```
"I have comprehensive performance incident materials from a government digital service 
that experienced significant performance degradation. Help me create the most effective 
approach for using AI tools to conduct thorough incident investigation and identify 
the true root cause behind apparent scaling issues.

The incident materials include:
- Application and database logs showing performance degradation patterns
- Infrastructure monitoring data with CPU, memory, and response time metrics
- Citizen impact reports and service desk tickets correlating with technical issues
- Access logs showing request patterns and user behavior during the incident
- Multiple data sources that need correlation and systematic analysis

Can you help me:
1. Design systematic approaches for correlating multiple performance data sources
2. Create investigation methodologies that identify non-obvious root causes rather than surface symptoms
3. Plan analysis strategies that connect technical metrics to actual citizen impact
4. Develop approaches for learning from performance incidents to prevent future issues
5. Design AI-assisted investigation workflows that can be applied across different government services

What systematic questions should I ask AI tools to ensure thorough performance 
investigation that identifies actual bottlenecks rather than misleading symptoms? 
Help me create a performance forensics methodology that produces actionable insights 
for government service reliability improvement."
```

**Benefits of this planning approach:**

- Leverages AI expertise in pattern recognition and anomaly detection across complex datasets
- Creates systematic approaches to correlating technical metrics with citizen service impact
- Ensures comprehensive investigation beyond obvious scaling solutions
- Enables learning from performance incidents to improve proactive monitoring and resilience
- Produces reusable investigation methodologies applicable across government digital services

#### Phase 2: Comprehensive Performance Incident Analysis

Once you understand your investigation approach, systematically analyse the incident materials:

```
"You are conducting comprehensive performance forensics on a government digital service 
incident using these investigation materials from: https://github.com/stevewalton28/ai-native-performance-exercise/tree/main

This is a Local Council Community Centre Booking System that experienced significant 
performance degradation on Monday 15th January 2025, 9:00 AM - 2:00 PM, with page 
load times increasing from 2 seconds to 45+ seconds and widespread booking failures.

PERFORMANCE INVESTIGATION REQUIREMENTS:
Systematically analyse all provided incident materials to identify:

ROOT CAUSE ANALYSIS:
- True underlying cause of the performance degradation (not just surface symptoms)
- Technical factors that created the performance bottleneck and system instability
- Correlation between different system components and their contribution to the incident
- Timeline analysis showing how the issue developed and cascaded through the system
- Differentiation between symptoms (connection exhaustion, memory pressure) and actual causes

CITIZEN IMPACT ASSESSMENT:
- How technical performance issues translated to citizen service disruption
- Analysis of booking failure patterns and user experience degradation
- Correlation between infrastructure metrics and actual citizen service accessibility
- Assessment of which citizen groups were most affected by the performance issues

PATTERN RECOGNITION:
- Identification of performance patterns that preceded and indicated the developing issue
- Analysis of system behavior that could have provided early warning indicators
- Recognition of performance signatures that could help identify similar issues in future

TECHNICAL CORRELATION:
- Systematic analysis of application logs, database performance, infrastructure metrics
- Cross-referencing of error patterns, resource utilization, and citizen impact timing
- Identification of specific system components and processes contributing to degradation
- Analysis of why traditional scaling approaches would not resolve this particular issue

INVESTIGATION METHODOLOGY:
- Document your systematic approach to analysing the multiple data sources
- Explain how you correlated different types of performance indicators
- Describe the analysis techniques that led to identifying the actual root cause
- Create reusable investigation patterns for similar government service incidents

WARNING: The obvious explanation (need more servers/connections/memory) is likely incorrect. 
This incident has a subtle root cause that requires careful analysis to identify. 
Look for non-obvious patterns and correlations in the data that reveal the true issue.

Generate comprehensive incident analysis including:
- Detailed root cause identification with supporting evidence from multiple data sources
- Timeline reconstruction showing how the issue developed and impacted citizen services
- Technical explanation of why the true cause created the observed symptoms
- Analysis of why obvious scaling solutions would not resolve this particular performance issue
- Investigation methodology that can be applied to similar government service performance incidents
- Clear documentation of analysis approaches and pattern recognition techniques used
```

#### Phase 3: Monitoring Architecture and Resilience Design

With root cause identified, design comprehensive monitoring and prevention strategies:

```
"Based on your analysis of the Community Centre Booking System performance incident, 
design comprehensive monitoring architecture and resilience improvements that would 
have detected this issue proactively and prevented similar performance failures.

MONITORING ARCHITECTURE REQUIREMENTS:
Create systematic monitoring strategy that includes:

PROACTIVE DETECTION:
- Monitoring alerts and metrics that would have identified this specific issue before citizen impact
- Early warning indicators that could trigger investigation before performance degradation
- Automated anomaly detection for the performance patterns you identified in the incident
- Service level objectives (SLOs) appropriate for government citizen-facing services

COMPREHENSIVE OBSERVABILITY:
- Application performance monitoring covering the specific technical areas involved in this incident
- Infrastructure monitoring that correlates with actual service performance and citizen experience
- Database performance monitoring that would detect the underlying issues you identified
- User experience monitoring that connects technical metrics to citizen service quality

GOVERNMENT SERVICE RESILIENCE:
- Architectural improvements that would prevent this class of performance issue
- Circuit breaker and graceful degradation strategies appropriate for government services
- Load management and resource allocation improvements based on the root cause analysis
- Performance optimization strategies addressing the specific bottlenecks identified

OPERATIONAL READINESS:
- Alerting strategies appropriate for government operational teams
- Investigation runbooks based on the analysis methodology you developed
- Performance baseline establishment and deviation detection for ongoing operations
- Cross-government applicability ensuring these approaches work across different departments

PREVENTION STRATEGIES:
- Code quality and testing improvements that would catch similar issues during development
- Capacity planning approaches that consider the actual performance characteristics discovered
- Regular performance validation strategies preventing the identified issue class
- Knowledge transfer approaches enabling government teams to apply these monitoring strategies

Generate comprehensive system resilience design including:
- Complete monitoring architecture with specific metrics, alerts, and thresholds
- Proactive detection strategies that would have identified this issue before citizen impact
- Systematic resilience improvements preventing the identified performance issue class
- Operational procedures and runbooks for ongoing performance management
- Cross-government monitoring patterns applicable to different digital services
- Technical implementation guidance for government development and operations teams
```

### Approach 2: Spec-Driven Development

This approach creates executable specifications for performance investigation and monitoring system design, following structured phases that ensure comprehensive incident analysis and systematic resilience improvement.

**When to use:** Formal incident investigation requiring documentation, systematic monitoring implementation across multiple government services, comprehensive performance management standards.

#### Setting Up Spec-Driven Performance Investigation

**Phase 1: Performance Investigation Specification (/specify)**

```
/specify Conduct comprehensive performance forensics on a government digital service incident, 
identifying the true root cause through systematic analysis of multiple data sources and 
designing proactive monitoring architecture that prevents similar performance failures.

The investigation must address:
- Complex performance incident with non-obvious root cause requiring systematic analysis 
  of application logs, database performance, infrastructure metrics, and citizen impact data
- Root cause identification that goes beyond surface symptoms to identify actual technical 
  bottlenecks and system inefficiencies causing citizen service disruption
- Comprehensive monitoring architecture design enabling proactive detection of similar 
  performance issues before they impact government digital service availability
- Systematic resilience improvements preventing this class of performance failure across 
  different government digital services and operational contexts
- Investigation methodology that can be applied across government departments for consistent 
  incident response and performance management approaches

Government operational teams currently struggle to rapidly identify performance issue root 
causes, leading to extended incident resolution times and repeated performance failures 
that impact citizen service accessibility and government service reliability.
```

**Phase 2: Investigation and Monitoring Architecture Planning (/plan)**

```
/plan The government service performance investigation and monitoring design must use:

SYSTEMATIC INVESTIGATION APPROACH:
- Multi-source data correlation techniques connecting application performance, infrastructure 
  metrics, and citizen impact indicators for comprehensive incident understanding
- Pattern recognition methodologies identifying non-obvious performance bottlenecks and 
  technical inefficiencies rather than surface scaling symptoms
- Root cause analysis techniques that differentiate between performance consequences and 
  actual underlying technical issues requiring systematic resolution
- Timeline reconstruction approaches showing incident development and citizen service impact 
  progression for complete performance failure understanding

MONITORING ARCHITECTURE DESIGN:
- Proactive detection strategies identifying performance degradation patterns before citizen 
  service impact through comprehensive application and infrastructure observability
- Service level objective definition and monitoring appropriate for government citizen-facing 
  digital services with performance requirements meeting user accessibility needs
- Automated anomaly detection for performance patterns indicating developing technical issues 
  requiring immediate investigation and potential intervention
- Cross-correlation monitoring connecting technical system metrics with actual citizen service 
  experience and accessibility during normal and degraded performance conditions

GOVERNMENT RESILIENCE REQUIREMENTS:
- Performance optimization strategies addressing actual technical bottlenecks identified through 
  systematic incident investigation rather than generic infrastructure scaling approaches
- System resilience architecture preventing identified performance failure classes while 
  maintaining government service availability during component failures or demand surges
- Operational procedures and investigation runbooks enabling government technical teams to 
  apply systematic performance analysis and resolution approaches consistently
- Cross-departmental monitoring patterns that work across different government digital services 
  while respecting departmental operational requirements and technical capabilities
```

**Phase 3: Implementation Tasks (/tasks)**

The tool will create structured implementation tasks covering incident analysis, root cause identification, monitoring architecture design, and systematic resilience improvement planning.

### Hybrid Approach

Combine both methodologies for comprehensive performance investigation and monitoring design:

- Use **forensics-driven analysis** for systematic incident investigation and root cause identification
- Use **spec-driven** for formal monitoring architecture design and cross-government resilience planning
- Use **forensics-driven analysis** for rapid investigation methodology development and pattern recognition
- Return to **spec-driven** for systematic monitoring implementation and formal operational procedure documentation

## Mini Prompt Library

Use these focused prompts for specific aspects of performance investigation and monitoring design:

### Performance Investigation Prompts

```
"Analyse these application logs, database performance data, and infrastructure metrics 
from a government service performance incident to identify the true root cause rather 
than surface symptoms like connection exhaustion and memory pressure that suggest 
obvious scaling solutions."

"Correlate citizen service desk tickets and user impact reports with technical performance 
metrics to understand how the underlying technical issue translated to citizen service 
disruption and accessibility barriers during this incident."
```

### Root Cause Analysis Prompts

```
"Systematically analyse this performance incident data to identify non-obvious technical 
bottlenecks that would not be resolved by traditional infrastructure scaling approaches 
like adding servers, memory, or database connections."

"Create comprehensive timeline reconstruction showing how this government service performance 
issue developed, cascaded through system components, and impacted citizen service 
accessibility during the incident period."
```

### Monitoring Architecture Prompts

```
"Design proactive monitoring architecture that would have detected this specific performance 
issue before citizen impact, including appropriate alerts, metrics, and early warning 
indicators suitable for government operational teams."

"Create comprehensive observability strategy connecting technical system metrics with 
actual citizen service experience and accessibility during both normal operations and 
performance degradation scenarios."
```

### Resilience Design Prompts

```
"Design systematic performance resilience improvements for this government digital service 
that prevent the identified root cause while maintaining service availability during 
component failures and unexpected demand surges."

"Create operational procedures and investigation runbooks that enable government technical 
teams to apply this systematic performance analysis methodology to similar incidents 
across different digital services."
```

## Implementation Sequence

Follow this structured sequence to conduct comprehensive performance investigation and monitoring design:

### 1. Systematic Incident Analysis
- Use AI to analyse all provided incident materials with systematic correlation across multiple data sources
- Identify patterns and anomalies that reveal the true root cause rather than surface symptoms
- Create comprehensive timeline reconstruction connecting technical issues with citizen service impact

### 2. Root Cause Investigation and Validation
- Use AI to identify the non-obvious technical bottleneck causing the performance degradation
- Validate root cause through evidence correlation across application, database, and infrastructure data
- Document investigation methodology that can be applied to similar government service incidents

### 3. Monitoring Architecture Design
- Design comprehensive proactive monitoring that would have detected this issue before citizen impact
- Create appropriate service level objectives and alerting strategies for government operational teams
- Plan observability approaches connecting technical metrics with citizen service experience

### 4. Systematic Resilience Implementation
- Design performance optimization strategies addressing the identified root cause and technical bottlenecks
- Create resilience improvements preventing similar performance failures across government services
- Develop operational procedures enabling consistent performance investigation and resolution approaches

## Things to Reflect on in Your Evaluation

### During Development

- **Investigation Methodology:** How effectively did AI tools correlate multiple complex data sources to identify non-obvious performance patterns and root causes?
- **Pattern Recognition:** What prompting techniques worked best for identifying subtle technical issues rather than obvious surface symptoms?
- **Cross-Source Analysis:** Where did you need to provide additional context for connecting technical metrics with citizen service impact?
- **Root Cause Accuracy:** How well did AI tools differentiate between performance consequences and actual underlying technical bottlenecks?
- **Government Context Understanding:** What aspects of government service performance requirements and operational constraints required manual clarification?

### Post-Completion

- **Investigation Quality:** How accurately did the AI-assisted analysis identify the true root cause compared to obvious scaling solutions?
- **Monitoring Architecture Effectiveness:** How well would the designed monitoring approach have detected this issue proactively before citizen impact?
- **Cross-Government Applicability:** How easily could this investigation methodology and monitoring architecture be applied to other government digital services?
- **Operational Readiness:** How well do the designed resilience improvements address actual technical bottlenecks while maintaining government service operational requirements?
- **Systematic Learning:** How effectively does this approach enable learning from performance incidents to improve proactive system design?

### Team Discussion

- **AI-Powered Performance Forensics:** How does AI-assisted incident investigation compare to traditional performance analysis in terms of speed, accuracy, and comprehensiveness?
- **Complex Root Cause Identification:** What new capabilities does AI bring to identifying non-obvious performance bottlenecks that manual analysis might miss?
- **Investigation Methodology:** How could systematic AI-assisted performance investigation improve government incident response consistency and effectiveness?
- **Cross-Government Learning:** How might AI-powered performance analysis enable knowledge sharing and consistent investigation approaches across different government departments?