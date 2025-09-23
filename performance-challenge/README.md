# Community Centre Booking System - Performance Incident Investigation Materials

**Incident Date:** Monday, 15th January 2025  
**Duration:** 09:00 AM - 2:00 PM (5 hours)  
**Service:** Local Council Community Centre Booking System  
**Impact Level:** High - Service Degradation to Near-Complete Outage  

## Incident Overview

This repository contains realistic investigation materials for a significant performance degradation incident that affected the community centre booking system. The incident began during peak morning hours and escalated to near-complete service unavailability before being resolved through manual intervention.

### Service Context
- **Service:** Online booking system for community centres, sports halls, and meeting rooms
- **Scale:** ~50 community facilities across the council area
- **Normal Usage:** 200-300 bookings per day, peak during evenings and weekends
- **Criticality:** Non-critical service (booking failures don't impact essential services)

## Incident Timeline

### Phase 1: Early Warning Signs (09:00 - 09:30)
- **09:00:45** - First slow query warning (1.8s execution time)
- **09:15:33** - Response times exceed 3 seconds
- **09:26:12** - Critical query performance alert (15.6s execution time)
- **09:30:23** - Booking success rate drops below 95%

### Phase 2: Escalating Performance Issues (09:30 - 10:30)
- **09:35:44** - Multiple slow queries detected
- **09:45:33** - Response times exceed 25 seconds
- **09:45:58** - Database connection pool stress detected
- **10:06:18** - First query timeouts occur
- **10:30:45** - System still responsive for some queries

### Phase 3: System Overload (10:30 - 11:30)
- **10:35:12** - Database connection pool exhausted
- **11:00:12** - Booking success rate drops to 3.1%
- **11:15:55** - Health check endpoints failing
- **11:20:12** - System performance critically degraded
- **11:25:23** - Service returning 503 errors

### Phase 4: Complete Service Failure (11:30 - 12:20)
- **11:30:34** - Memory pressure and frequent garbage collection
- **11:45:12** - Error rate reaches 99.9%
- **12:00:34** - Critical alerts for extended outage (90+ minutes)
- **12:15:56** - Manual intervention initiated

### Phase 5: Recovery (12:20 - 14:00)
- **12:20:17** - Database connection pool restarted (increased from 10 to 15 connections)
- **12:25:23** - First successful queries after restart
- **13:00:09** - Performance metrics showing improvement
- **13:45:48** - Performance normalized
- **14:00:10** - Service fully recovered

## Investigation Materials

### Log Files (`/logs/`)
- **`app.log`** - Application server logs showing gradual performance degradation
- **`db.log`** - Database performance logs with slow query details
- **`access.log`** - Load balancer access logs with request patterns and response times

### Monitoring Data (`/monitoring/`)
- **`metrics.csv`** - Infrastructure monitoring data (5-minute intervals)
- **`dashboard-data.json`** - Application performance metrics and KPIs
- **`alerts.json`** - System alerts triggered during the incident

### Citizen Impact (`/citizen-impact/`)
- **`service-desk-tickets.json`** - Customer service tickets with citizen complaints
- **`social-media-mentions.txt`** - Social media monitoring report

## Key Metrics Summary

| Metric | Normal | Peak Impact | Recovery |
|--------|---------|-------------|----------|
| Response Time (95th percentile) | ~200ms | 174,789ms | ~500ms |
| Booking Success Rate | 99%+ | 0.1% | 99%+ |
| Database Connection Pool | 20% utilized | 100% + 219 waiting | 13% utilized |
| Error Rate | <1% | 99.9% | <3% |
| CPU Utilization | 15-25% | 99.9% | 20% |
| Memory Usage | 45-55% | 99.9% | 45% |


## File Structure
```
performance-incident-materials/
├── logs/
│   ├── app.log                 # Application server logs
│   ├── db.log                  # Database performance logs
│   └── access.log              # Load balancer access logs
├── monitoring/
│   ├── metrics.csv             # Infrastructure monitoring data
│   ├── dashboard-data.json     # Application metrics dashboard
│   └── alerts.json             # System alerts
├── citizen-impact/
│   ├── service-desk-tickets.json    # Customer service tickets
│   └── social-media-mentions.txt   # Social media monitoring
└── README.md                   # This incident summary
```

---

**Note:** All data in these materials is synthetic and created for training purposes. No real citizen data or actual system information is included.