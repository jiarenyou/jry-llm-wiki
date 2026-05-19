---
title: "MES - 制造执行系统"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/MES-制造执行系统.md
last_updated: 2026-05-19
---

## Summary
MES（Manufacturing Execution System）是位于企业计划层（ERP）与车间控制层（SCADA/PLC）之间的生产执行管理核心系统，处于 ISA-95 架构的第3层。它将上层生产计划转化为可执行的车间指令，并实时反馈执行结果，核心价值在于"知道现在在生产什么、生产得怎么样、还能生产什么"。

## Key Claims
- MES 覆盖 ISA-95 标准定义的四大领域：生产调度、生产执行、质量管理、库存管理
- MESA International 定义了 MES 的 11 个标准功能模块，涵盖从生产调度到绩效分析的完整闭环
- MES 是 OEE、FPY、良率、MTBF 等关键制造绩效指标的数据源头和计算引擎
- MES 向上连接 ERP 接收工单和 BOM，向下连接 SCADA 采集设备状态和产量数据
- MES 实施路径分为四阶段：数据采集 -> 生产可视化 -> 过程管控 -> 优化决策

## Connections
- [[ERP - 企业资源计划]] — MES 向上连接 ERP，接收生产计划和工单，反馈执行结果
- [[SCADA - 数据采集与监视]] — MES 向下连接 SCADA，下发工艺参数，接收实时设备数据
- [[OEE - 设备综合效率]] — MES 采集设备状态和产量数据，自动计算 OEE 三要素
- [[FPY - 直通率]] — MES 追踪每道工序的一次通过情况
- [[DataWarehouse]] — MES 产出的生产数据是制造数据仓库的核心数据源
- [[DataGovernance]] — MES 涉及设备主数据、BOM、工艺路线等核心主数据治理
