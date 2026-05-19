---
title: "ERP - 企业资源计划"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/ERP-企业资源计划.md
last_updated: 2026-05-19
---

## Summary
ERP（Enterprise Resource Planning）是将企业所有核心业务流程整合到统一信息平台上的管理系统，覆盖财务、采购、库存、生产计划、销售、人力资源等模块。在 ISA-95 架构中位于第4层（企业业务规划与物流层），是智能制造的业务大脑。

## Key Claims
- ERP 核心功能模块包括财务管理、采购管理、销售管理、生产计划（MPS/MRP）、库存管理、人力资源
- MRP（物料需求计划）是 ERP 生产模块的核心引擎，根据成品需求逐层展开 BOM 计算物料需求
- ERP 与 MES 的数据接口是智能制造最关键的集成点之一，两者构成信息化"两条腿"
- ERP 正在向智能 ERP 演进，新特征包括基于机器学习的需求预测、实时库存优化、自动化采购决策
- 数据质量是 ERP 实施的关键挑战：BOM 准确率要求 >= 98%，库存账实相符率 >= 95%

## Connections
- [[MES - 制造执行系统]] — ERP 向 MES 下达生产计划，MES 向 ERP 反馈执行状态
- [[WMS - 仓储管理系统]] — ERP 库存模块与 WMS 深度集成，库存准确率影响 MRP 运算质量
- [[PLM - 产品生命周期管理]] — PLM 的 MBOM 传递到 ERP，确保 MRP 运算基于最新产品数据
- [[产能利用率]] — MRP 运算准确性直接影响产能利用率
- [[DataWarehouse]] — ERP 是企业级数据仓库的核心数据源之一
