---
title: "FlashAttention"
type: concept
tags:
  - attention
  - gpu-optimization
  - memory-efficiency
sources:
  - llm-lesson-07-flash-attention
last_updated: 2026-05-18
---

## Overview

Flash Attention 是由 Tri Dao（Stanford）提出的一种注意力计算优化方法，通过 Tiling 分块计算和 Online Softmax 技术，将注意力计算对 GPU 高带宽内存（HBM）的访问复杂度从 O(N^2) 降低到 O(N)。其核心思想是充分利用 GPU 片上 SRAM 的高速缓存，减少缓慢的 HBM 读写操作，在保持计算结果精确等价的同时大幅提升速度。

## Key Ideas

- **核心问题**：标准注意力计算需要将 N x N 的注意力矩阵完整写入 HBM，内存访问成为瓶颈
- **Tiling 分块**：将 Q、K、V 切分为小块（tile），在 SRAM 中完成分块内的注意力计算，避免完整存储注意力矩阵
- **Online Softmax**：通过增量式计算 softmax 的分子和分母（维护 running max 和 running sum），支持分块计算而无需回溯
- **IO 复杂度**：HBM 访问从 O(N^2 d) 降低到 O(N^2 d^2 / M)，其中 M 为 SRAM 大小，实际效果接近 O(N)
- **精确等价**：Flash Attention 不是近似方法，计算结果与标准注意力数学上完全一致

## Related Concepts
- [[MultiHeadAttention]] — Flash Attention 优化的是多头注意力的计算过程
- [[KVCache]] — KV Cache 与 Flash Attention 都是注意力机制的重要优化
- [[SparseAttention]] — 稀疏注意力从另一个角度降低注意力计算复杂度
