---
title: "MTBF - 平均故障间隔时间"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/MTBF-平均故障间隔时间.md
last_updated: 2026-05-19
---

## Summary
MTBF（Mean Time Between Failures）衡量设备两次故障之间的平均运行时间，是评估设备可靠性的核心指标。MTBF 与 MTTR 共同决定设备的故障可用率（= MTBF / (MTBF + MTTR)），提升可用率有两条路：降低故障频率（提高 MTBF）或加快修复速度（降低 MTTR）。

## Key Claims
- 计算公式：MTBF = 总运行时间 / 故障次数，示例：600 小时内 3 次故障 -> MTBF = 200 小时
- MTBF 和 MTTR 共同决定故障可用率：可靠但难修（MTBF=500h, MTTR=10h -> 98.0%）与不可靠但好修（MTBF=100h, MTTR=2h -> 98.0%）可以得到相同的可用率
- MTBF 是预测性维护的核心目标变量：历史分析 -> 异常检测 -> 预测模型（RUL剩余寿命预测）-> 维护优化
- 数据来源：SCADA 报警日志 + MES 维修工单 + CMMS 维护管理系统

## Connections
- [[MTTR - 平均修复时间]] — MTBF 决定"多久坏一次"，MTTR 决定"坏了修多久"
- [[可用率]] — MTBF 直接影响可用率
- [[OEE - 设备综合效率]] — 可用率是 OEE 的组成部分
- [[性能率]] — 频繁故障也会导致速度损失
- [[DataWarehouse]] — MTBF 趋势分析需要整合多系统的历史故障数据
