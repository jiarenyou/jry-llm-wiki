---
title: "SCADA - 数据采集与监视"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/SCADA-数据采集与监视.md
last_updated: 2026-05-19
---

## Summary
SCADA（Supervisory Control And Data Acquisition）是工业自动化中用于实时采集现场设备数据并进行集中监视与控制的系统，位于 ISA-95 架构的第1-2层（感知与控制层）。它相当于遍布工厂的"神经网络"，感知设备的每一个状态变化，是智能制造底层数据采集的核心基础设施。

## Key Claims
- SCADA 采用分层分布式架构：SCADA Server -> 通信网络 -> RTU/PLC -> 传感器与执行器
- 关键通信协议包括 Modbus TCP/RTU、OPC UA、Profinet、EtherNet/IP、MQTT，其中 OPC UA 正在成为工业4.0标准协议
- SCADA 是 MES 最重要的底层数据来源，提供设备状态（1-5秒）、实时产量（1-10秒）、工艺参数（1-60秒）等数据
- SCADA 正在向开放、智能、云端协同方向演进，趋势包括边缘计算、云 SCADA、数字孪生
- 工控安全是核心挑战，需遵循 IEC 62443 标准，实施纵深防御策略

## Connections
- [[MES - 制造执行系统]] — SCADA 是 MES 最重要的底层数据来源
- [[CMMS - 设备维护管理]] — SCADA 设备异常可自动触发 CMMS 工单
- [[可用率]] — SCADA 采集设备运行状态数据，用于计算可用率
- [[性能率]] — SCADA 实时产量数据用于计算性能率
- [[MTBF - 平均故障间隔时间]] — SCADA 报警记录用于故障分析和 MTBF 计算
- [[SparkPerformance]] — SCADA 高频时序数据的处理可类比大数据流式计算的性能优化挑战
