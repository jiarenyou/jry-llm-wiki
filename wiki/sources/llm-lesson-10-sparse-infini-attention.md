---
title: "稀疏注意力与Infini-Attention"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/10-稀疏注意力与Infini-Attention.md
last_updated: 2026-05-18
---

## Summary
本课介绍处理长序列的两种注意力优化方案：稀疏注意力（Sparse Attention）和Infini-Attention。稀疏注意力通过Random、Window、Global tokens三个组件大幅降低计算复杂度。Infini-Attention则引入压缩记忆机制实现无限上下文长度。课程还对比了线性注意力（Q(K^T V)）与标准注意力（(QK^T)V）的计算顺序差异，并提及Kimi和Gemini 1.5的实际应用。

## Key Claims
- 稀疏注意力的三组件：Random attention随机连接远距离token、Window attention关注局部邻域、Global tokens作为信息枢纽连接全局
- 稀疏注意力将标准O(N^2)复杂度降低到O(N×√N)或更低，代价是损失部分token间的直接交互
- Infini-Attention在标准注意力基础上增加压缩记忆（Compressive Memory），将旧上下文压缩存入固定大小记忆
- 线性注意力改变计算顺序：标准注意力 (QK^T)V 先算token间相似度，线性注意力 Q(K^T V) 先算特征聚合
- 线性注意力的复杂度为O(N×d^2)，当序列长度N远大于维度d时比标准注意力高效得多
- Kimi和Gemini 1.5采用了类似Infini-Attention的压缩记忆机制来支持超长上下文窗口

## Key Quotes
> "稀疏注意力的核心思想是：不是每两个token都需要直接对话，大部分信息可以通过'中间人'传递。" -- 解释稀疏注意力的合理性

> "线性注意力的数学本质就是一个交换律：先算K^T V还是先算QK^T，结果一样但代价天差地别。" -- 揭示线性注意力的关键洞察

> "Infini-Attention让模型拥有了'遗忘旧事但保留印象'的能力——不需要记住每个字，但需要记住大致意思。" -- 比喻压缩记忆机制

## Connections
- [[SparseAttention]] — 本课核心主题之一，降低长序列注意力复杂度
- [[InfiniAttention]] — 压缩记忆机制，实现无限上下文
- [[MultiHeadAttention]] — 稀疏注意力和Infini-Attention都是在标准多头注意力基础上的优化

## Contradictions
