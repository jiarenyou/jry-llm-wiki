---
title: "Flash Attention：突破内存墙"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/07-Flash-Attention.md
last_updated: 2026-05-18
---

## Summary
本课深入讲解Flash Attention技术，该技术通过优化GPU内存访问模式解决了标准注意力机制O(N²)的内存瓶颈。课程从GPU内存层次结构（高带宽HBM vs 片上SRAM）讲起，介绍了Kernel Fusion、Tiling分块计算和Online Softmax等核心技术。Flash Attention由Stanford的Tri Dao创建，V2版本进一步优化了并行策略和工作分区。

## Key Claims
- 标准注意力需要在HBM中存储完整的N×N注意力矩阵，长序列时内存消耗急剧膨胀
- GPU内存层次：HBM容量大但带宽低（~2TB/s），SRAM容量小但带宽极高（~19TB/s）
- Flash Attention的核心思想是分块（Tiling）计算注意力，在SRAM中完成softmax避免读写中间矩阵
- Kernel Fusion将多个CUDA kernel合并为一个，减少HBM读写次数
- Online Softmax通过前缀和技巧实现分块计算中的精确softmax，无需完整注意力矩阵
- Flash Attention V2改进了线程块分配策略，减少了非矩阵乘法运算的FLOPs
- Flash Attention在数学上与标准注意力完全等价，不引入任何近似

## Key Quotes
> "标准注意力的瓶颈不是计算量，而是反反复复地在HBM里读写那个巨大的注意力矩阵。" -- 点明问题本质

> "Flash Attention的魔法在于：不去存那个N×N的矩阵，而是在SRAM里一小块一小块地算完就扔。" -- 解释核心策略

> "Tri Dao用数学证明了：你可以既快又精确，不需要在速度和正确性之间做选择。" -- 强调Flash Attention的精确性

## Connections
- [[FlashAttention]] — 本课核心主题，突破注意力机制内存瓶颈
- [[KVCache]] — KV Cache与Flash Attention共同加速推理
- [[MultiHeadAttention]] — Flash Attention优化的目标对象

## Contradictions
