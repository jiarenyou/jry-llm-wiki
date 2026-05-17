---
title: "Transformer"
type: concept
tags:
  - transformer
  - architecture
  - deep-learning
sources:
  - llm-lesson-01-linear-transformation
  - llm-lesson-04-model-py
last_updated: 2026-05-18
---

## Overview

Transformer 是一种基于自注意力机制的序列处理架构，由 Vaswani 等人在 2017 年提出。它摒弃了传统的循环结构，完全依靠注意力机制来建模序列中的依赖关系，实现了高度并行化。Transformer 采用编码器-解码器结构，包含多头自注意力、前馈网络、残差连接和层归一化等核心组件，是 GPT、BERT、LLaMA 等现代大语言模型的基础架构。

## Key Ideas

- **编码器-解码器结构**：编码器处理输入序列提取特征，解码器自回归生成输出序列；GPT 仅使用解码器，BERT 仅使用编码器
- **多头自注意力机制**：将 Q、K、V 拆分为多个头并行计算注意力，捕获不同子空间的特征表示
- **前馈网络（FFN）**：每个位置独立应用两层全连接变换（通常带 GELU 激活），提供非线性建模能力
- **残差连接 + 层归一化**：Residual Connection 缓解梯度消失，LayerNorm 稳定训练过程，两者组合（Pre-Norm 或 Post-Norm）影响训练稳定性
- **位置编码**：由于自注意力本身不具备位置感知能力，需要通过位置编码注入序列顺序信息

## Related Concepts
- [[LinearTransformation]] — Transformer 中的 QKV 投影和 FFN 本质上是线性变换
- [[MultiHeadAttention]] — 多头注意力是 Transformer 的核心创新
- [[PositionalEncoding]] — 位置编码为 Transformer 注入序列顺序信息
- [[TrainingPipeline]] — Transformer 的训练涉及完整的工程管线
- [[ScalingLaw]] — Transformer 架构的性能遵循 Scaling Law 的规律
