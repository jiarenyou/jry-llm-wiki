---
title: "ALiBi"
type: concept
tags:
  - transformer
  - position
  - attention
sources:
  - llm-lesson-11-positional-encoding
last_updated: 2026-05-18
---

## Overview

ALiBi（Attention with Linear Biases）是一种位置编码方案，由 Press 等人于 2022 年提出。与传统的位置编码不同，ALiBi 不在词嵌入上加位置向量，而是在注意力分数矩阵上直接加上与 token 距离成比例的负偏置——距离越远的 token 被"扣分"越多。这种设计极其简洁，无需任何可学习参数，且具有优秀的外推性，被 MPT、BLOOM 等模型采用。

## Key Ideas

- **原理**：在 QK^T 计算出的注意力分数上，对第 i 个查询和第 j 个键加上偏置 m × (j - i)，其中 m 是各注意力头特定的斜率
- **无参数**：偏置完全由预设的几何斜率决定，不需要训练，模型零额外参数开销
- **相对位置**：偏置仅依赖于 token 之间的相对距离 (j - i)，天然具备相对位置编码的特性
- **外推性**：由于偏置是线性的，模型在推理时可以自然地扩展到比训练时更长的序列
- **与 RoPE 对比**：RoPE 通过旋转变换编码位置，ALiBi 通过加法偏置编码位置，两者是目前最主流的两种位置编码方案

## Related Concepts
- [[PositionalEncoding]] — 位置编码总览，ALiBi 是其中之一
- [[RoPE]] — 旋转位置编码，与 ALiBi 并列的另一种主流方案
- [[Transformer]] — ALiBi 所服务的核心架构
- [[MultiHeadAttention]] — ALiBi 直接作用于多头注意力的分数矩阵
