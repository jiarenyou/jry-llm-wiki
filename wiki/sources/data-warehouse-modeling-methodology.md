---
title: "数仓建模：核心方法和方法论"
type: source
tags: [big-data, data-warehouse]
date: 2026-04-10
source_file: raw/杂记/数仓建模：核心方法和方法论.md
last_updated: 2026-05-18
---

## Summary
数仓建模的扩展版本，在核心方法基础上补充了完整的电商订单域建模案例（ODS/DIM/DWD/DWS/ADS各层表结构设计）、实时数仓流量域建模案例、系统学习方法论（业务线+数仓线+技术线三主线）以及实战练习模板。包含详细的指标体系梳理和分层建模设计。

## Key Claims
- 完整电商订单域建模案例：从业务背景到指标体系到五层表结构设计
- 实时数仓流量域：Kafka -> Flink DWD清洗 -> Flink DWS窗口聚合 -> Doris/ClickHouse ADS
- 学习三主线：业务线（流程->主题域->指标）、数仓线（分层->维度建模->迭代）、技术线（离线/实时/调度/治理）
- 实践中注意：指标口径变更需版本控制、维度表变更需生效/失效时间、ETL任务需保证幂等
- 实时与离线两套链路应共享同一套维度/指标体系，保证口径一致

## Key Quotes
> "数仓建模 = 理解业务 + 设计分层/维度模型 + 指标体系落地 + 用技术栈（离线/实时）把这一套跑起来，支撑业务决策。"

## Connections
- [[DataWarehouse]] -- 本文是数仓建模的详细方法论来源
- [[HiveSQL]] -- 电商案例中大量使用Hive SQL建表和ETL
- [[DataGovernance]] -- 指标口径统一和数据质量管理是数据治理的重要组成

## Contradictions
