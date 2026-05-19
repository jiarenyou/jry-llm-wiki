---
title: "工业数据平台"
type: concept
tags: [smart-manufacturing, data-engineering]
sources:
  - factory-data-platform-architecture
  - data-collection-layer-architecture
  - tsdb-selection
  - realtime-batch-unified-architecture
  - realtime-data-pipeline
  - factory-data-warehouse-modeling
  - data-service-api-layer
  - data-lineage-and-metadata-management
last_updated: 2026-05-19
---

## Overview
工业数据平台是智能制造的数字底座，采用五层分层架构（采集 → 存储 → 计算 → 服务 → 应用），处理从毫秒级传感数据到天级经营报告的全频谱数据需求。

## Key Ideas
- **五层架构**：数据采集层 → 存储层 → 计算层 → 服务层 → 应用层
- **实时+离线统一**：Flink 流处理 + Spark 批处理双引擎
- **时序数据库**选型：TDengine/InfluxDB 用于高频设备数据
- **数据血缘**：从设备到报表的全链路可追溯
- **主数据管理**：统一设备、物料、工艺等核心实体定义

## Related Concepts
- [[DataWarehouse]] — 工厂数仓建模复用维度建模方法论
- [[DataGovernance]] — 工业数据治理框架
- [[SparkPerformance]] — 离线计算引擎调优
- [[HiveSQL]] — 工厂数仓SQL查询

## Related Entities
- [[ISA95]] — 数据平台对应 ISA-95 Level 2-3
