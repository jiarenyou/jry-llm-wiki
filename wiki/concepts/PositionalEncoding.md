---
title: "PositionalEncoding"
type: concept
tags:
  - transformer
  - position
  - encoding
sources:
  - llm-lesson-11-positional-encoding
last_updated: 2026-05-18
---

## Overview

位置编码是 Transformer 架构中为输入序列注入位置信息的关键机制。由于自注意力计算本身是排列不变的（permutation invariant），模型无法区分 token 的先后顺序。位置编码通过在输入嵌入上叠加位置信息来解决这个问题，主要分为三大类：正弦编码（绝对位置编码）、RoPE（旋转相对位置编码）和 ALiBi（线性偏置位置编码）。

## Key Ideas

- **为什么需要位置编码**：自注意力计算 QK^T 时交换任意两个 token 的位置不影响结果，因此需要额外注入位置信息
- **正弦编码（Sinusoidal）**：原始 Transformer 使用不同频率的正弦和余弦函数编码绝对位置，具有一定的外推性
- **RoPE（旋转位置编码）**：通过旋转变换编码相对位置关系，是目前大模型的主流选择，被 LLaMA、Qwen 等采用
- **ALiBi（线性偏置）**：在注意力分数上直接加上与距离成比例的负偏置，简单高效且具有较好的外推性
- **绝对 vs 相对**：绝对编码为每个位置分配固定向量，相对编码编码 token 之间的距离关系

## Related Concepts
- [[RoPE]] — RoPE 是目前最主流的位置编码方案
- [[Transformer]] — 位置编码是 Transformer 架构不可或缺的组件
- [[LinearTransformation]] — 位置编码中的旋转变换本质上是特殊的线性变换
