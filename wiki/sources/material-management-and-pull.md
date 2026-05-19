---
title: "Material Management and Pull"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/物料管理与拉动.md
last_updated: 2026-05-19
---

## Summary

Material management connects the supply chain to the production line, with material costs typically comprising 50-70% of product cost. The lean "pull" paradigm replaces traditional MPS-driven "push" by having downstream processes signal demand upstream via Kanban systems. The article covers push-pull hybrid strategies (CODP separation), Kanban types and quantity calculation, JIT delivery modes (frequency, kit, sequence), WMS functionality (inbound/outbound/warehouse management), and traceability systems (batch/serial/container level using barcodes, RFID, and laser marking). Digital transformation introduces electronic Kanban, AGV scheduling, AI demand forecasting, and digital twin warehouse simulation.

## Key Claims

- Push-pull hybrid is the practical approach: long-lead raw materials are forecast-driven (push), while short-lead standard parts and semi-finished goods are Kanban-driven (pull), with the Customer Order Decoupling Point (CODP) as the strategic switching node.
- ABC classification drives differentiated inventory strategy: A-class (high-value, 10-20% of items, 70-80% of cost) gets tight control; C-class gets simplified management with high safety stock.
- WMS core functions span inbound (receipt, quality inspection, put-away), storage (location management, cycle counting, age analysis), outbound (wave planning, pick-path optimization, verification), and traceability (forward/reverse tracking by batch or serial number).

## Connections

- [[DataWarehouse]] -- material consumption, inventory levels, and delivery data feed into the warehouse for supply chain analytics
- [[DataGovernance]] -- standardized material coding, BOM structures, and unit-of-measure conversions are governance prerequisites
- [[SparkPerformance]] -- real-time inventory updates and AGV scheduling parallel streaming data processing challenges
