---
title: "SPC -- Statistical Process Control"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/SPC-统计过程控制.md
last_updated: 2026-05-19
---

## Summary

SPC (Statistical Process Control) uses statistical methods to monitor and control manufacturing processes in real time, distinguishing between common-cause variation (inherent random fluctuation) and special-cause variation (anomalous interference). In smart manufacturing, SPC evolves from manual sampling to full-population monitoring powered by IoT sensors and stream computing (Flink/Spark Streaming), enabling sub-second anomaly alerts.

## Key Claims

- SPC's core tool is the control chart (CL/UCL/LCL), which flags out-of-control conditions via Western Electric and Nelson rules (e.g., 9 consecutive points on one side of center line, 6 consecutive increasing/decreasing points).
- SPC must precede process capability analysis -- calculating Cpk on an out-of-control process yields meaningless results.
- In the big-data era, SPC upgrades from single-variable charts to multivariate monitoring (T-squared charts) and ML-augmented anomaly detection, with automatic root-cause correlation to OEE, equipment status, and material batches.

## Connections

- [[DataWarehouse]] -- SPC data flows from SCADA/MES into the warehouse for historical trend analysis
- [[DataGovernance]] -- consistent data quality (timestamps, measurement systems) is prerequisite for reliable SPC
- [[DataSkew]] -- anomaly detection in SPC parallels techniques for identifying data distribution anomalies
- [[RAG]] -- intelligent SPC assistants could use retrieval-augmented generation to suggest corrective actions from historical defect databases
