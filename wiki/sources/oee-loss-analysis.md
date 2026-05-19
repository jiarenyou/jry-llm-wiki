---
title: "OEE Loss Analysis"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/设备综合效率损失分析.md
last_updated: 2026-05-19
---

## Summary

OEE loss analysis structurally decomposes and quantifies the losses behind the OEE metric, answering "where did efficiency go, how much was lost, and how to recover it." The six major losses map to OEE's three dimensions: availability losses (equipment failure, setup/adjustment), performance losses (idling/minor stops, reduced speed), and quality losses (process defects, startup rejects). Analysis methods include loss waterfall charts (decomposing from 100% theoretical capacity) and Pareto analysis to prioritize improvement efforts on the highest-impact losses.

## Key Claims

- Focusing improvement on the top 3 losses typically covers over 50% of the total improvement potential.
- Each loss category has specific improvement strategies: fault prediction and SMED for downtime losses, tooling improvement and parameter optimization for speed losses, SPC/Cpk control and first-article inspection for quality losses.
- Big-data-driven loss analysis replaces manual daily reports with second-level SCADA acquisition, real-time ML-based loss classification, live loss waterfall dashboards, and automatic root-cause correlation with equipment health and material batches.
- Loss cost quantification (loss time x unit time output value) translates percentages into monetary terms for management attention.

## Connections

- [[DataWarehouse]] -- loss analysis aggregates equipment status, production counts, and quality data from the warehouse
- [[DataGovernance]] -- consistent loss classification codes and standardized downtime reason categorization are governance prerequisites
- [[DataSkew]] -- loss distribution is itself skewed (Pareto principle), and analysis must account for this imbalance
