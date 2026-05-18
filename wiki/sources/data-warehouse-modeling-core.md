---
title: "数仓建模：核心方法"
type: source
tags: [big-data, data-warehouse]
date: 2026-04-10
source_file: raw/杂记/数仓建模：核心方法.md
last_updated: 2026-05-18
---

## Summary
数据仓库建模的精简版全景指南。数仓建模本质是理解业务、设计分层/维度模型、指标体系落地并用技术栈跑起来的过程。三大理论流派：Inmon（3NF企业级）、Kimball（维度建模快速迭代）、Data Vault（可扩展可追溯）。国内互联网公司常用ODS/DIM/DWD/DWS/ADS五层架构结合Kimball维度建模。

## Key Claims
- 数仓建模做三件事：理解业务流转、按层次+主题+维度+指标组织数据、支撑报表分析决策
- Kimball维度建模（星型/雪花）是互联网公司最常用的核心方法
- 五层架构：ODS贴源 -> DIM维度 -> DWD明细 -> DWS汇总 -> ADS应用
- 维度建模四步法：确定业务过程 -> 确定粒度 -> 确定维度 -> 确定度量
- 指标体系：原子指标 + 派生指标 + 维度组合指标，需统一口径和命名规范
- 离线数仓(T+1)与实时数仓(Kafka+Flink+OLAP)建模思路相似但关注点不同

## Key Quotes
> "很多实战经验的差距，其实是'会不会梳理业务和设计指标体系'的差距，而不仅仅是SQL/Hive会不会写。"

## Connections
- [[DataWarehouse]] -- 本文是数仓建模概念的核心来源
- [[HiveSQL]] -- 数仓建模中大量使用Hive SQL进行数据分层处理
- [[DataGovernance]] -- 数据治理中的SLA需要数仓建模支撑

## Contradictions
