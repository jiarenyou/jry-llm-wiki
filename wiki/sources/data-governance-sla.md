---
title: "数据治理之服务水平协议（SLA）"
type: source
tags: [big-data, data-governance]
date: 2026-04-10
source_file: raw/杂记/数据治理之服务水平协议（SLA）.md
last_updated: 2026-05-18
---

## Summary
基于DAMA数据治理体系，系统阐述SLA（Service Level Agreement）在数据治理中的应用。SLA本质是"服务承诺+可量化指标+未达标后果"。文章区分了SLI（尺子）、SLO（刻度目标）、SLA（合同承诺）三个层次，详解四种SLA类型（平台级、数据产品级、数据质量级、流程级），以及设计落地八步法和常见误区。

## Key Claims
- SLA = SLI（指标） + SLO（目标值） + 未达标后果的合同级约定
- 数据SLA关注五大维度：时效性/新鲜度、数据质量（准确/完整/一致/有效/唯一）、可用性、性能、安全合规
- 四种类型：数据平台级SLA、数据产品/数据集SLA、数据质量SLA、治理流程SLA
- SLA设计八步：识别关键资产 -> 识别业务期望 -> 选取SLI -> 设定SLO -> 设计监控告警 -> 编写评审 -> 签署发布 -> 定期回顾
- 常见误区：只签不监控、指标太多太激进、只谈技术不谈业务、所有数据同一级别

## Key Quotes
> "SLI是'尺子'，SLO是'尺子上的刻度目标'，SLA是'写在合同里的承诺+如果达不到要怎么办'。"

> "好的SLA能帮助组织把数据质量从'口头要求'变成'工程可管理的目标'。"

## Connections
- [[DataGovernance]] -- 本文是数据治理概念的核心来源
- [[DataWarehouse]] -- 数仓分层架构设计需根据SLA目标确定
- [[HiveSQL]] -- SQL是数据质量校验和SLA监控的基础工具

## Contradictions
