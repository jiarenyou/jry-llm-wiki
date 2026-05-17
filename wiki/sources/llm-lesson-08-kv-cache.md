---
title: "KV Cache：自回归推理的加速利器"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/08-KV-Cache.md
last_updated: 2026-05-18
---

## Summary
本课讲解KV Cache技术的原理与实现，该技术通过缓存已计算的Key和Value矩阵来减少自回归推理中的冗余计算。课程详细推导了KV Cache的内存计算公式，并通过示例展示提速高达56倍的效果。最后指出KV Cache在长序列场景下的内存瓶颈，自然引出MHA、MQA、GQA等不同注意力机制的演进方向。

## Key Claims
- 自回归生成每一步都需要对所有历史token计算注意力，导致大量重复的K/V矩阵计算
- KV Cache将已计算的Key和Value矩阵缓存起来，新token只需计算自身的Q并与缓存的K/V做注意力
- KV Cache内存占用公式：2 × batch_size × n_layers × seq_len × d_model × dtype_bytes
- 示例中KV Cache将推理速度提升56倍，从逐token重算变为O(1)增量计算
- KV Cache的代价是显存占用随序列长度线性增长，长序列成为瓶颈
- 长序列场景下KV Cache的内存压力直接催生了MQA和GQA等减少K/V头数的技术方案

## Key Quotes
> "没有KV Cache的话，生成第100个token时要把前99个token重新算一遍K和V——简直是浪费生命。" -- 解释冗余计算问题

> "KV Cache的本质就是'好记性不如烂笔头'——算过的东西记下来，下次直接查。" -- 形象化解释缓存策略

> "56倍的提速不是魔法，只是避免了重复劳动。" -- 总结KV Cache的效果

## Connections
- [[KVCache]] — 本课核心主题，自回归推理的关键优化
- [[FlashAttention]] — Flash Attention与KV Cache结合可进一步提升推理效率
- [[MultiHeadAttention]] — KV Cache作用于多头注意力的K/V矩阵

## Contradictions
