---
title: "ScalingLaw"
type: concept
tags:
  - scaling-law
  - model-performance
  - training
sources:
  - llm-lesson-03-scaling-law
last_updated: 2026-05-18
---

## Overview

Scaling Law 揭示了大语言模型性能与模型规模、数据量和计算资源之间的幂律关系。核心公式为 L(N,D) = E + A/N^alpha + B/D^beta，其中 N 为参数量，D 为数据量，损失随两者增加而幂律下降。Chinchilla Law 进一步指出最优数据量约为参数量的 20 倍，这一发现深刻影响了后续大模型的训练策略。

## Key Ideas

- **核心公式**：L(N,D) = E + A/N^alpha + B/D^beta，其中 E 为不可约损失，alpha 约 0.34，beta 约 0.28
- **Chinchilla Law**：最优训练数据量 D 约为模型参数量 N 的 20 倍（D approx 20 x N），即小模型需要更多数据才能充分发挥
- **FLOPs 估算**：训练总计算量 C 约等于 6 x N x D，其中 6 来自前向（2ND）加反向传播（4ND）
- **三大 scaling 维度**：模型参数量 N（宽度 x 深度）、训练数据量 D（token 数）、训练计算量 C（FLOPs）
- **实践意义**：给定计算预算，存在最优的模型大小和数据量的分配方案

## Related Concepts
- [[FLOPs]] — 浮点运算量是衡量 Scaling Law 中计算需求的核心指标
- [[TrainingPipeline]] — 训练管线的规模需要遵循 Scaling Law 的指导
- [[Transformer]] — Transformer 架构的参数量 N 是 Scaling Law 的关键变量
