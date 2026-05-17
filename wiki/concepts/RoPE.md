---
title: "RoPE"
type: concept
tags:
  - positional-encoding
  - transformer
  - relative-position
sources:
  - llm-lesson-11-positional-encoding
last_updated: 2026-05-18
---

## Overview

旋转位置编码（Rotary Position Embedding, RoPE）是一种通过旋转变换编码相对位置信息的位置编码方案。它将位置信息融入 Query 和 Key 的内积计算中，使得内积结果自然地反映两个 token 之间的相对距离。RoPE 支持外推到比训练时更长的序列，配合 YaRN、NTK-aware 缩放等技术可进一步扩展上下文窗口。LLaMA、Qwen 等主流大模型均采用 RoPE。

## Key Ideas

- **旋转机制**：将向量视为二维平面上的点，根据位置角度进行旋转变换，位置 m 处的向量旋转 m x theta 角度
- **相对位置编码**：Q_m 与 K_n 的内积只依赖相对位置 m - n，而非绝对位置 m 和 n
- **外推能力**：RoPE 具有一定的长度外推性，可通过 NTK-aware 缩放、YaRN 等技术进一步增强
- **NTK-aware 缩放**：通过调整旋转频率的基础值，使模型能够处理更长的序列而不丢失近距离的位置分辨率
- **YaRN**：结合 NTK 缩放和注意力温度调节，在扩展上下文窗口时保持模型质量

## Related Concepts
- [[PositionalEncoding]] — RoPE 是位置编码的一种具体实现方案
- [[LinearTransformation]] — RoPE 的旋转变换本质上是正交线性变换
- [[Transformer]] — RoPE 被广泛应用于现代 Transformer 架构中
