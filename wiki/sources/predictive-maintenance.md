---
title: "Predictive Maintenance"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/预测性维护.md
last_updated: 2026-05-19
---

## Summary

Predictive maintenance (PdM) analyzes equipment operational data to predict health state and schedule maintenance before failures occur, reducing maintenance costs by 30-50% and unplanned downtime by 70-75%. The technology roadmap spans four phases: statistical methods (MTBF trends, Weibull distribution), rule engines (threshold-based alerts), machine learning (classification, RUL regression, anomaly detection), and deep learning (LSTM, 1D-CNN, Transformer, PINN). End-to-end implementation covers data collection from SCADA sensors, feature engineering (time/frequency/time-frequency domains), model training with time-series cross-validation, edge/cloud deployment, and continuous model monitoring for data drift.

## Key Claims

- Data requirements are demanding: vibration data at 1-10kHz sampling, temperature at 1-60s intervals, combined with maintenance records from CMMS and operational context (load rate, product type, cumulative runtime).
- Model types serve different purposes: binary classification for fault prediction (prioritize recall over precision), regression for Remaining Useful Life estimation, and anomaly detection for zero-fault-sample scenarios.
- Implementation should start with high-criticality equipment with well-defined failure modes, accumulate at least 6 months of data before modeling, begin with simple statistical baselines, and ensure predictions feed into CMMS work-order workflows.

## Connections

- [[DataWarehouse]] -- sensor data, maintenance records, and operational context are integrated in the warehouse for model training
- [[DataGovernance]] -- standardized fault codes (ISO 14224), consistent sensor calibration records, and clean time-series data are governance foundations
- [[RAG]] -- retrieval-augmented systems could match predicted failure modes with historical repair procedures and spare part availability
