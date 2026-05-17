---
title: "InfiniAttention"
type: concept
tags:
  - attention
  - long-context
  - memory
sources:
  - llm-lesson-10-sparse-infini-attention
last_updated: 2026-05-18
---

## Overview

无限注意力（InfiniAttention）是一种支持无限上下文长度处理的注意力机制，核心思想是将历史信息压缩为紧凑的摘要（Compressed Memory），用固定大小的内存存储任意长度的上下文信息。它使用线性注意力 Q(K^T V) 替代标准的 (QK^T) V 计算方式，将注意力的内存占用与序列长度解耦，使模型能够处理超长甚至无限长的输入序列。

## Key Ideas

- **Compressed Memory**：将历史上下文信息压缩为固定大小的内存矩阵，不受序列长度影响
- **线性注意力**：用 Q(K^T V) 替代 (QK^T) V，先计算 K^T V 得到固定大小的内存更新，再由 Q 查询
- **内存读写**：支持从压缩内存中检索（retrieve）相关信息，并将新信息写入（update）内存
- **无限上下文**：通过压缩内存机制，理论上可以处理任意长度的序列，突破固定上下文窗口的限制
- **混合注意力**：结合局部标准注意力和全局压缩内存注意力，兼顾精确的局部建模和高效的全局信息整合

## Related Concepts
- [[SparseAttention]] — 稀疏注意力从另一个角度解决长上下文效率问题
- [[KVCache]] — KV Cache 是传统注意力处理长序列的缓存方案，但内存随序列线性增长
- [[MultiHeadAttention]] — 无限注意力是对标准注意力计算方式的根本性改进
