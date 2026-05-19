---
title: "Production Cost Metrics"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/生产成本指标体系.md
last_updated: 2026-05-19
---

## Summary

Production cost metrics translate technical manufacturing indicators (OEE, yield, MTBF) into the economic language of money that management cares about. The framework structures costs in three layers: direct costs (materials, labor, energy), manufacturing overhead (equipment depreciation, maintenance, utilities, tooling, quality costs), and hidden costs (capacity waste, inventory carrying, stockout losses, latent quality risks, changeover waste). A key innovation is the mapping table that links each technical indicator change to its quantified cost impact.

## Key Claims

- Typical manufacturing cost structure: direct materials 50-60%, manufacturing overhead 25-35%, direct labor 10-15%.
- Quality cost (COQ) follows a curve where increasing prevention investment reduces failure costs disproportionately -- the optimal point is not at zero defects but where total quality cost is minimized.
- Big-data-driven cost management enables real-time cost collection per shift/product/order (vs. traditional monthly车间-level aggregation), dynamic equipment depreciation allocation by actual runtime, automatic cost root-cause tracing, and cost simulation for scheduling alternatives, investment evaluation, and process optimization scenarios.

## Connections

- [[DataWarehouse]] -- cost metrics integrate data from SCADA, MES, ERP, QMS, and CMMS through the warehouse
- [[DataGovernance]] -- consistent cost center coding, allocation rules, and time-period definitions are governance essentials
- [[SparkPerformance]] -- real-time cost calculation across multiple dimensions (product, shift, equipment, customer) mirrors OLAP performance challenges
