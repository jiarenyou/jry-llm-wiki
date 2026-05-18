---
title: "DataGovernance"
type: concept
tags: [big-data, data-governance]
sources:
  - data-governance-sla
  - alibaba-big-data-path-notes
last_updated: 2026-05-18
---

# DataGovernance (数据治理)

## Definition
数据治理是通过组织架构、制度流程和技术工具，对数据资产进行系统化管理的过程，目标是确保数据的质量、安全、合规和有效利用。核心控制机制之一是SLA（服务水平协议）。

## SLA Framework
- **SLI（Service Level Indicator）**：测量的指标（响应时间、错误率、数据完整性）
- **SLO（Service Level Objective）**：目标值（99%请求200ms内返回）
- **SLA（Service Level Agreement）**：合同级承诺 + 未达标后果

## Five SLA Dimensions in Data Governance
1. **时效性/新鲜度**：数据就绪时间、最大延迟（如T+1报表8:00前完成）
2. **数据质量**：准确性、完整性、一致性、有效性、唯一性
3. **可用性**：系统月度可用性（如99.9%）
4. **性能**：查询响应时间（P95/P99延迟）
5. **安全合规**：访问控制、脱敏率、审计覆盖率

## Four Types of Data SLA
- **数据平台级SLA**：面向整个数据平台使用者
- **数据产品/数据集SLA**：面向具体数据产品、报表、API
- **数据质量SLA**：面向某类/某表的数据质量目标
- **治理流程SLA**：面向数据治理流程本身（权限审批、工单响应）

## SLA Lifecycle
明确需求 -> 确定范围与角色 -> 设计指标与目标 -> 编写评审 -> 签署发布 -> 监控告警 -> 定期复盘 -> 持续改进

## Key Benefits
- 让数据质量从"口头要求"变成"工程可管理的目标"
- 明确责任边界，减少部门间推诿
- 增强业务对数据的信任
- 支撑合规与风险控制

## Related Concepts
- [[DataWarehouse]] -- 数仓建模需要根据SLA目标设计分层架构
- [[HiveSQL]] -- SQL是数据质量校验和SLA监控的基础工具
- [[SparkPerformance]] -- 性能优化是达成SLA时效性目标的关键手段
