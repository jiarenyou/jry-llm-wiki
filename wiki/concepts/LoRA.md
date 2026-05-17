---
title: "LoRA"
type: concept
tags:
  - fine-tuning
  - parameter-efficient
  - lora
sources:
  - llm-lesson-12-lora-qlora
last_updated: 2026-05-18
---

## Overview

LoRA（Low-Rank Adaptation）是一种参数高效微调方法，核心思想是冻结预训练模型的原始权重，仅训练注入的低秩分解矩阵 Delta_W = B x A。其中 A 是降维矩阵（d_model x r），B 是升维矩阵（r x d_model），秩 r 通常取 4-32。这种方法可将可训练参数量减少 99% 以上，同时保持与全参数微调相当的性能。

## Key Ideas

- **低秩假设**：模型适配过程中的权重变化 Delta_W 具有低秩特性，可以用远小于原始维度的秩来近似
- **矩阵分解**：Delta_W = B x A，A 初始化为随机高斯，B 初始化为零，训练初期 Delta_W 为零不影响预训练权重
- **秩的选择**：r 通常取 4-32，较低的秩即可捕获任务适配所需的主要变化方向
- **参数效率**：以 r=8、d_model=4096 为例，原始权重 16M 参数，LoRA 仅需 65K 可训练参数，减少 99.6%
- **推理无额外开销**：训练完成后将 B x A 合并到原始权重中，推理时无额外计算成本

## Related Concepts
- [[QLoRA]] — QLoRA 在 LoRA 基础上引入量化，进一步降低显存需求
- [[FineTuning]] — LoRA 是高效微调的主流方法
- [[TrainingPipeline]] — LoRA 修改了训练管线中的参数更新部分
