---
title: "FLOPs"
type: concept
tags:
  - compute
  - scaling-law
  - training-cost
sources:
  - llm-lesson-03-scaling-law
last_updated: 2026-05-18
---

## Overview

FLOPs（Floating Point Operations）是衡量模型计算需求的指标，表示完成一次训练或推理所需的浮点运算次数。对于 Transformer 模型，训练总计算量 C 约等于 6 x N x D，其中 N 为模型参数量，D 为训练 token 数。FLOPs 是 Scaling Law 中的关键变量，也是估算训练成本和硬件需求的基础。

## Key Ideas

- **训练 FLOPs**：C 约等于 6 x N x D，其中系数 6 来自前向传播约 2ND 加上反向传播约 4ND
- **推理 FLOPs**：单次前向传播约 2 x N（每参数两次运算：乘法和加法），与序列长度相关
- **与 Scaling Law 的关系**：给定计算预算 C，Scaling Law 指导如何分配模型大小 N 和数据量 D 以获得最优性能
- **硬件估算**：GPU 算力（TFLOPS）除以模型 FLOPs 可估算训练时间，是资源规划的基础
- **MFU（Model FLOPs Utilization）**：实际计算效率占理论峰值的比例，是衡量训练工程优化水平的核心指标

## Related Concepts
- [[ScalingLaw]] — FLOPs 是 Scaling Law 公式中的核心变量
- [[TrainingPipeline]] — 训练管线的每一步都贡献 FLOPs
- [[Transformer]] — Transformer 架构的 FLOPs 可以精确估算
