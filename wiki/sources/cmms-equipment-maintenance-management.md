---
title: "CMMS - 设备维护管理"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/CMMS-设备维护管理.md
last_updated: 2026-05-19
---

## Summary
CMMS（Computerized Maintenance Management System）是管理企业设备资产全生命周期维护活动的信息化平台，覆盖维护工单管理、预防性维护计划、备件库存、维修记录、设备档案等核心功能。在智能制造中核心趋势是从事后维护向预测性维护转变，利用 SCADA 设备数据和 AI 模型预测故障。

## Key Claims
- 维护策略从事后维护向预防性维护、预测性维护、以可靠性为中心的维护（RCM）演进
- 工单管理是 CMMS 的核心载体，支持纠正式、预防性、预测性、改善性四种工单类型
- 预防性维护计划的执行率直接影响 MTBF，规律性保养可有效延长设备无故障运行时间
- CMMS 是 MTBF 和 MTTR 数据的核心来源，详细记录故障发现、响应、诊断、修复、验证全链路
- 预测性维护是智能制造最具价值的 AI 应用之一：数据采集 -> 特征提取 -> 模型训练 -> 预警触发 -> 效果验证

## Connections
- [[SCADA - 数据采集与监视]] — SCADA 提供设备运行数据用于预测性维护，报警自动触发 CMMS 工单
- [[MES - 制造执行系统]] — MES 反馈设备异常状态触发 CMMS 工单，CMMS 通知计划停机时间影响排程
- [[ERP - 企业资源计划]] — CMMS 备件采购申请转 ERP 采购订单，维修成本回流 ERP 成本核算
- [[MTBF - 平均故障间隔时间]] — CMMS 记录每次故障时间，是 MTBF 数据的核心来源
- [[MTTR - 平均修复时间]] — CMMS 详细记录 MTTR 各阶段构成
- [[可用率]] — CMMS 通过降低非计划停机时间提升可用率
- [[DataWarehouse]] — CMMS 维修记录是设备数据分析的重要数据源
