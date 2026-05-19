---
title: "Anomaly Detection and Root Cause Analysis"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/异常检测与根因分析.md
last_updated: 2026-05-19
---

## Summary

Anomaly detection automatically identifies deviations from normal patterns in production data (time-series spikes, drifts, dead values; process parameter excursions, quality drops, pace anomalies). Root cause analysis then traces detected anomalies back to their fundamental causes. The pipeline integrates statistical methods (3-sigma rules, SPC control charts, IQR), machine learning (Isolation Forest, LOF, One-Class SVM), and deep learning (AutoEncoder, LSTM-AE, Transformer). Root cause analysis leverages knowledge graphs of factory entity relationships and causal inference methods (Granger causality, PC algorithm, do-calculus).

## Key Claims

- Method selection follows a decision tree: with labels use supervised classifiers; without labels, low-dimensional data suits statistical methods, while high-dimensional data with few samples favors One-Class SVM and many samples favor Isolation Forest or AutoEncoder.
- Knowledge graph-driven root cause analysis builds entity relationships (equipment, process, material, supplier) and traces anomalies along causal chains to identify the most probable root cause node.
- The end-to-end system uses Kafka and Flink for real-time anomaly detection, with offline training of root cause graphs and causal models, feeding alerts and dashboards at the application layer.

## Connections

- [[DataWarehouse]] -- anomaly detection integrates multi-source data (SCADA/MES/QMS) from the warehouse with time-aligned timestamps
- [[DataGovernance]] -- consistent entity naming, standardized fault codes, and clean timestamp alignment are prerequisites
- [[RAG]] -- root cause analysis could be enhanced by RAG systems that retrieve historical incident reports matching current anomaly patterns
