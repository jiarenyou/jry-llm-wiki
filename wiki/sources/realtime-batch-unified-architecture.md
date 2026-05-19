---
title: "实时与离线统一架构"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/实时与离线统一架构.md
last_updated: 2026-05-19
---

## Summary
解析Lambda、Kappa与湖仓一体（Data Lakehouse）三种架构范式在工厂场景的适用性，阐述推荐的混合架构方案（Kappa为主、批处理为辅、湖仓一体为基座），详解数据新鲜度分级策略（秒级/分钟级/小时级/天级）和SLA设计，以及Iceberg+Flink+Doris的核心技术栈落地路径。

## Key Claims
- Lambda架构代码重复和运维成本高，Kappa架构简洁但历史重计算效率低，湖仓一体是未来方向
- 推荐混合架构：实时告警和指标走Flink CEP/SQL，实时同步走Flink到Iceberg，批量分析走Spark，统一通过Doris查询
- 数据新鲜度分四级：秒级（设备看板）、分钟级（异常告警）、小时级（班组报表）、天级（经营报表）
- 湖仓一体的关键技术：Iceberg支持ACID事务和时间旅行，Flink流批一体，Doris毫秒级OLAP查询
- 演进路径建议：Kappa先行 -> 引入数据湖 -> 全面统一

## Connections
- [[工厂数据平台总体架构]] — 实时与离线统一是数据平台的核心设计命题
- [[实时数据流水线]] — 实时侧的具体实现
- [[工厂数据仓库建模]] — 离线侧的数仓建模方法
- [[SparkPerformance]] — Spark作为离线计算引擎的性能优化与湖仓一体的协同
- [[DataWarehouse]] — 湖仓一体架构模糊了数据湖和数据仓库的边界
