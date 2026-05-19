---
title: "PLM - 产品生命周期管理"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/PLM-产品生命周期管理.md
last_updated: 2026-05-19
---

## Summary
PLM（Product Lifecycle Management）是管理产品从概念设计、研发、制造到退市全生命周期中所有数据与流程的集成化平台。在智能制造体系中，PLM 是产品知识的单一数据源（Single Source of Truth），管理 BOM、CAD 图纸、工艺规程、测试规范等全部产品数据。

## Key Claims
- PLM 管理产品全生命周期六个阶段：概念 -> 设计 -> 工程化 -> 制造 -> 服务 -> 退市
- BOM 管理是 PLM 连接设计与制造的纽带，负责 EBOM（设计BOM）到 MBOM（制造BOM）的转化
- 工程变更管理（ECN/ECO）是制造业最复杂的流程之一，变更未及时同步到 ERP 会导致严重后果
- PLM 在工业4.0中承担产品数字化主线（Digital Thread）的角色，支撑数字孪生和跨学科协同
- 主要厂商包括 Siemens Teamcenter、Dassault ENOVIA、PTC Windchill、SAP PLM

## Connections
- [[ERP - 企业资源计划]] — PLM 向 ERP 传递 MBOM、工艺路线、标准工时、物料主数据
- [[MES - 制造执行系统]] — PLM 向 MES 传递工艺规程、SOP 文档、质检标准
- [[QMS - 质量管理系统]] — PLM 提供检验规范和质量标准，QMS 质量数据反馈驱动设计改进
- [[SCADA - 数据采集与监视]] — PLM 的三维模型与 SCADA 实时数据结合构建数字孪生
- [[DataGovernance]] — PLM 管理的产品数据是制造企业数据治理的重要领域
