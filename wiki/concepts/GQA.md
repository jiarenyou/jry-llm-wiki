---
title: "GQA"
type: concept
tags:
  - attention
  - memory-optimization
  - transformer
sources:
  - llm-lesson-09-mha-mqa-gqa
last_updated: 2026-05-18
---

## Overview

Grouped-Query Attention（GQA）是一种介于 Multi-Head Attention（MHA）和 Multi-Query Attention（MQA）之间的注意力变体，通过按组共享 Key/Value 头来平衡模型质量与推理效率。MHA 中每个注意力头拥有独立的 KV，MQA 中所有头共享单个 KV，GQA 则将头划分为若干组，组内共享 KV。Llama 2/3 系列广泛采用 GQA，将 KV Cache 内存从 536MB 降至 130MB。

## Key Ideas

- **三种变体对比**：MHA（每头独立 KV，质量最高但内存最大）、MQA（全局共享 1 个 KV，内存最小但质量下降）、GQA（按组共享 KV，兼顾质量与效率）
- **分组机制**：将 n_heads 个 Query 头划分为 n_kv_groups 个组，每组内的 Query 头共享同一组 KV
- **实际效果**：Llama 系列采用 GQA 后，KV Cache 内存从 536MB 降至 130MB，推理速度显著提升
- **组数选择**：n_kv_groups = 1 退化为 MQA，n_kv_groups = n_heads 退化为 MHA，中间值即为 GQA
- **质量保持**：实验表明 GQA 在大幅降低内存的同时，模型质量下降非常有限

## Related Concepts
- [[MultiHeadAttention]] — GQA 是多头注意力机制的优化变体
- [[KVCache]] — GQA 的主要目的就是减少 KV Cache 的显存占用
- [[FlashAttention]] — Flash Attention 和 GQA 是互补的优化策略
