---
title: "Cpk -- Process Capability Index"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/CPK-过程能力指数.md
last_updated: 2026-05-19
---

## Summary

Cpk (Process Capability Index) quantifies a manufacturing process's ability to consistently produce within specification limits, accounting for both process spread (sigma) and mean shift from target. A Cpk of 1.33 or higher is typically required in automotive and other precision industries. The article details the calculation formula, evaluation benchmarks (from excellent at >= 1.67 to inadequate below 1.0), and two improvement paths: reducing variation (improves both Cp and Cpk) and eliminating mean shift (brings Cpk closer to Cp).

## Key Claims

- Cpk = min[(USL - mu)/(3 sigma), (mu - LSL)/(3 sigma)]; it must be computed only after SPC confirms the process is statistically in control and data approximates normality.
- A high Cp but low Cpk indicates the process has low spread but is off-target -- adjusting the mean to center is the most efficient correction.
- Big-data applications include real-time Cpk dashboards per machine/station in MES, trend-based early warning as Cpk degrades, and automatic root-cause correlation with equipment state, material batch, and environmental parameters.

## Connections

- [[DataWarehouse]] -- Cpk computation requires integrating measurement data, specification limits, and process metadata from the warehouse
- [[DataGovernance]] -- reliable Cpk depends on calibrated measurement systems and clean, time-aligned data
- [[SparkPerformance]] -- real-time Cpk calculation across hundreds of stations mirrors Spark streaming performance challenges
