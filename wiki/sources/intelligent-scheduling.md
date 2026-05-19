---
title: "Intelligent Scheduling"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/智能排产.md
last_updated: 2026-05-19
---

## Summary

Intelligent scheduling augments traditional APS with machine learning prediction, operations research optimization, and real-time data feedback. The architecture comprises an ML prediction engine (order lead-time, equipment availability, processing time), an OR optimization engine (MIP, constraint programming, meta-heuristics), and a rule constraint engine. A progressive implementation path ranges from rule-based scheduling (L1) through heuristics (L2) and hybrid optimization (L3) to reinforcement learning (L4), with event-triggered real-time rescheduling for exceptions like equipment failure or rush orders.

## Key Claims

- Traditional scheduling suffers from static rules, inability to respond to anomalies, ignoring real-time equipment state, and reliance on individual dispatcher expertise.
- Key input data comes from ERP (orders), SCADA/MES (equipment status/OEE), WMS (material availability), PLM (process routes), and MES historical data (changeover times).
- Big-data engineers are responsible for data integration across ERP/MES/WMS/SCADA silos, feature engineering from historical production data, training prediction models, maintaining real-time data pipelines, and building scheduling accuracy dashboards.

## Connections

- [[DataWarehouse]] -- integrates order, equipment, material, and process data from the warehouse for scheduling optimization
- [[SparkPerformance]] -- large-scale scheduling optimization with millions of constraints mirrors distributed computing performance tuning
- [[RAG]] -- intelligent scheduling assistants could retrieve historical scheduling decisions and their outcomes to improve future plans
