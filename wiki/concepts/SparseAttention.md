---
title: "SparseAttention"
type: concept
tags:
  - attention
  - efficiency
  - long-context
sources:
  - llm-lesson-10-sparse-infini-attention
last_updated: 2026-05-18
---

## Overview

稀疏注意力通过限制注意力计算中 token 之间的连接模式，将标准注意力的 O(N^2) 计算复杂度降低到 O(N x sqrt(N))。其核心思想是大多数 token 之间不需要直接交互，只需维护三类关键连接：Random（随机长程连接）、Window（局部滑动窗口）和 Global（全局关键 token），即可在大幅减少计算量的同时保持模型质量。

## Key Ideas

- **Random 连接**：随机选择少量远程 token 建立注意力连接，捕获长程依赖关系
- **Window 连接**：只关注附近的 token（如前后 w 个位置），捕获局部上下文信息
- **Global 连接**：少量特殊 token（如 [CLS]）与所有位置建立连接，提供全局信息汇聚
- **复杂度降低**：通过稀疏连接模式将注意力矩阵从稠密的 N x N 减少到 O(N x sqrt(N)) 个非零元素
- **实际应用**：Longformer、BigBird、Sparse Transformer 等模型均采用不同形式的稀疏注意力

## Related Concepts
- [[FlashAttention]] — Flash Attention 从 IO 优化角度加速注意力，稀疏注意力从计算模式角度降低复杂度
- [[InfiniAttention]] — 无限注意力从另一个角度解决长上下文问题
- [[MultiHeadAttention]] — 稀疏注意力是对多头注意力计算模式的优化
