---
title: "MultiHeadAttention"
type: concept
tags:
  - attention
  - transformer
  - architecture
sources:
  - llm-lesson-04-model-py
  - llm-lesson-09-mha-mqa-gqa
last_updated: 2026-05-18
---

## Overview

多头注意力机制将查询（Query）、键（Key）、值（Value）向量拆分为多个头，在每个头的子空间中独立计算注意力，再将结果拼接合并。这种设计使模型能够同时关注不同位置的不同表示子空间中的信息，捕获丰富的语义特征。多头注意力后续演化出 MHA（多头独立 KV）、MQA（全局共享单 KV）和 GQA（分组共享 KV）三种变体。

## Key Ideas

- **拆分与并行**：将维度 d_model 拆分为 h 个头，每个头维度 d_k = d_model / h，各头独立计算 Attention(Q_i, K_i, V_i)
- **拼接与投影**：多头结果 Concat 后通过输出投影矩阵 W_O 映射回 d_model 维度
- **多头优势**：不同头可以关注不同类型的依赖关系（如语法、语义、位置），提供更丰富的表示
- **三种变体**：MHA 每头独立 KV（质量最高）、MQA 全局共享单个 KV（效率最高）、GQA 按组共享 KV（平衡方案）
- **因果注意力掩码**：在自回归生成中使用下三角掩码，防止看到未来位置的信息

## Related Concepts
- [[Transformer]] — 多头注意力是 Transformer 的核心组件
- [[LinearTransformation]] — QKV 投影本质上是线性变换
- [[GQA]] — Grouped-Query Attention 是多头注意力在效率上的优化变体
- [[FlashAttention]] — Flash Attention 优化了多头注意力的计算效率
- [[KVCache]] — KV Cache 缓存多头注意力中的 Key/Value 矩阵
