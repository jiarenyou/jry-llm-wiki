---
title: "DataWarehouse"
type: concept
tags: [big-data, data-warehouse]
sources:
  - data-warehouse-modeling-core
  - data-warehouse-modeling-methodology
  - alibaba-big-data-path-notes
  - hive-sql-syntax-guide
last_updated: 2026-05-18
---

# DataWarehouse (数据仓库建模)

## Definition
数据仓库建模是将业务数据按"层次+主题+维度+指标"结构化组织的过程，目的是在原始数据和业务分析之间搭建一座清晰的桥梁，为报表、BI、运营分析、产品决策提供统一数据口径。

## Three Schools of Thought
- **Inmon**：企业级3NF建模，自上而下，数据结构稳定但建设周期长
- **Kimball**：维度建模（星型/雪花），自下而上快速迭代，互联网公司最常用
- **Data Vault**：Hub/Link/Satellite三组件，强调可扩展性和历史可追溯

## Five-Layer Architecture (ODS/DIM/DWD/DWS/ADS)
- **ODS**（贴源层）：原始数据同步，保持业务库结构
- **DIM**（维表层）：多源维表合并，补全属性和标签
- **DWD**（明细层）：按主题域组织，清洗、规范化、关联维度
- **DWS**（汇总层）：按分析场景和粒度预聚合
- **ADS**（应用层）：面向报表/需求的宽表

## Dimensional Modeling Four Steps
1. 确定业务过程（如用户下单、页面浏览）
2. 确定粒度（每订单一行、每次点击一行）
3. 确定维度（时间、地域、用户、商品）
4. 确定度量（金额、件数、次数）

## Indicator System
- 原子指标：订单数、GMV、支付用户数
- 派生指标：转化率、客单价、复购率
- 维度组合指标：某地区+某类目下的GMV
- 需统一口径和命名规范，建立指标字典

## Real-time vs. Offline
- 离线数仓（T+1）：Spark/Hive计算每日分区
- 实时数仓：Kafka -> Flink -> OLAP（Doris/ClickHouse）
- 两套链路共享维度/指标体系，保证口径一致

## Related Concepts
- [[HiveSQL]] -- 数仓开发的基础工具
- [[DataGovernance]] -- 数据治理保障数仓质量
- [[SparkPerformance]] -- Spark是离线数仓的核心计算引擎
