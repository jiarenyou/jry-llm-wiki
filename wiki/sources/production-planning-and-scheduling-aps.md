---
title: "Production Planning and Scheduling -- APS"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/生产计划与排产-APS.md
last_updated: 2026-05-19
---

## Summary

Advanced Planning and Scheduling (APS) bridges ERP and MES by introducing finite capacity modeling, multi-constraint optimization, and real-time data-driven scheduling. APS operates at two levels: Advanced Planning (AP) for medium-term demand-capacity balancing, and Detailed Scheduling (DS) for shop-floor-level sequencing. Key algorithms include heuristic dispatching rules (SPT, EDD, CR), meta-heuristics (genetic algorithms, simulated annealing, particle swarm optimization), and constraint programming (IBM ILOG CP Optimizer). Implementation follows a four-phase path from basic modeling through rule-based, optimized, to intelligent scheduling.

## Key Claims

- APS must simultaneously satisfy equipment, personnel, material, tooling, and changeover constraints while optimizing for objectives like minimum makespan, minimum changeovers, or maximum utilization.
- System integration is critical: APS receives demand/BOM/inventory from ERP and delivers production plans back; it sends dispatch orders to MES and receives real-time progress and exceptions in return.
- Success factors include data quality (process route accuracy >= 95%, standard time deviation <= 10%), organizational alignment, change management, and continuous algorithm tuning.

## Connections

- [[DataWarehouse]] -- APS requires clean, integrated data from ERP, PLM, and MES, all flowing through the warehouse
- [[DataGovernance]] -- accurate process routes, standard times, and capacity calendars are governance fundamentals
- [[SparkPerformance]] -- solving large combinatorial optimization problems for scheduling parallels distributed computing challenges
