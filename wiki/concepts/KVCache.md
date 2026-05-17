---
title: "KVCache"
type: concept
tags:
  - inference
  - memory-optimization
  - attention
sources:
  - llm-lesson-08-kv-cache
last_updated: 2026-05-18
---

## Overview

KV Cache 是大语言模型自回归推理中的关键优化技术，通过缓存已计算的 Key 和 Value 矩阵，避免在每个生成步中重复计算之前所有 token 的 KV 表示。这一技术可实现高达 56 倍的推理加速，是现代 LLM 推理部署的标配。但 KV Cache 占用的显存随序列长度线性增长，在长上下文场景下成为主要瓶颈。

## Key Ideas

- **核心原理**：自回归生成中，每生成一个新 token 只需要新的 Query 与所有历史 token 的 Key/Value 做注意力计算
- **缓存复用**：历史 token 的 KV 在之前的步骤中已经计算过，直接从缓存读取即可，无需重复计算
- **加速效果**：避免了每步对全部历史 token 的 KV 矩阵重复投影，推理速度可提升 56 倍
- **显存瓶颈**：KV Cache 显存占用 = 2 x 层数 x 序列长度 x 隐藏维度 x 精度字节数，随序列长度线性增长
- **优化方向**：GQA 减少头数、量化降低精度、PagedAttention 分页管理都是缓解 KV Cache 显存压力的方法

## Related Concepts
- [[MultiHeadAttention]] — KV Cache 缓存的是多头注意力中的 Key 和 Value 矩阵
- [[GQA]] — GQA 通过共享 KV 头显著降低 KV Cache 的显存占用
- [[FlashAttention]] — Flash Attention 和 KV Cache 是互补的推理优化技术
