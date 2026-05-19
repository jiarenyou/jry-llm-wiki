---
title: "MTTR - 平均修复时间"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/MTTR-平均修复时间.md
last_updated: 2026-05-19
---

## Summary
MTTR（Mean Time To Repair）衡量设备从故障发生到恢复正常运行所需的平均时间，反映维护团队的响应速度和修复能力。MTTR 不仅包含"修设备"的时间，而是从故障发现、响应、诊断、修复到验证的全链路，其中诊断阶段（占 20-30%）是大数据最能发力的地方。

## Key Claims
- 计算公式：MTTR = 所有故障修复时间之和 / 故障次数
- MTTR 的五阶段构成：发现（5%）-> 响应（15-20%）-> 诊断（20-30%）-> 修复（30-40%）-> 验证（10%）
- 诊断阶段是大数据最能发力的地方：基于历史故障数据和传感器特征可缩短故障定位时间
- 降低 MTTR 的策略：故障知识库与诊断决策树、备件预判、AR 辅助维修、预防性维护
- MTTR 与 MTBF 共同影响可用率：故障可用率 = MTBF / (MTBF + MTTR)

## Connections
- [[MTBF - 平均故障间隔时间]] — 两者共同决定设备可用率
- [[可用率]] — MTTR 直接影响可用率
- [[OEE - 设备综合效率]] — 可用率是 OEE 的组成部分
- [[CMMS - 设备维护管理]] — CMMS 详细记录 MTTR 各阶段的数据
- [[SparkPerformance]] — 故障诊断阶段的实时数据分析类比流计算性能优化
