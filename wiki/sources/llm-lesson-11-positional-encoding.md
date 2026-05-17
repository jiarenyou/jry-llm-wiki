---
title: "位置编码：从正弦到旋转"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/11-位置编码.md
last_updated: 2026-05-18
---

## Summary
本课系统讲解了大语言模型中的位置编码技术演进。从绝对位置编码到相对位置编码的范式转换开始，分析了正弦编码在长文本上的外推性局限。重点介绍了当前主流的RoPE旋转位置编码（LLaMA、Qwen采用）和ALiBi线性偏置方法（MPT、BLOOM采用），以及用于扩展上下文窗口的YaRN NTK-aware缩放技术。

## Key Claims
- Transformer本身是位置无关的，位置编码是让模型区分token顺序的唯一信号
- 绝对位置编码为每个位置分配固定向量，正弦编码利用三角函数周期性但外推到更长序列时表现不佳
- RoPE（Rotary Position Embedding）通过旋转矩阵将位置信息编码到Q和K中，自然具备相对位置表达能力
- RoPE的核心性质：两个位置的内积仅依赖于它们的相对距离，与绝对位置无关
- ALiBi（Attention with Linear Biases）在注意力分数上直接加上与距离成比例的负偏置，无需学习参数
- YaRN通过NTK-aware缩放调整RoPE的频率基数，使模型在不重新训练的情况下扩展上下文窗口长度

## Key Quotes
> "没有位置编码的Transformer就像打乱的拼图——所有碎片都在，但不知道谁在谁旁边。" -- 说明位置编码的必要性

> "RoPE的巧妙之处在于：它不是在词向量上'贴标签'，而是让词向量'转个角度'来表达位置。" -- 解释RoPE的几何本质

> "ALiBi的想法非常暴力：距离越远的token，注意力分数直接扣越多分。" -- 描述ALiBi的简洁策略

## Connections
- [[PositionalEncoding]] — 本课核心主题，位置编码的多种方案
- [[RoPE]] — 旋转位置编码，当前主流方案
- [[ALiBi]] — 线性偏置注意力，一种替代的位置编码方案

## Contradictions
