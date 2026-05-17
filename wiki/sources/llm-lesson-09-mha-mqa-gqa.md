---
title: "MHA vs MQA vs GQA：注意力机制的内存博弈"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/09-MHA-MQA-GQA.md
last_updated: 2026-05-18
---

## Summary
本课对比了三种注意力机制的内存效率与模型表现：标准多头注意力MHA使用完全独立的K/V头，多查询注意力MQA极端共享单个K/V头，分组查询注意力GQA在两者之间取得平衡。课程给出了具体的内存占用对比（MHA 536MB vs GQA 130MB vs MQA 16MB），并分析了Llama、GPT、PaLM等主流模型的选用策略。

## Key Claims
- MHA（Multi-Head Attention）每个注意力头拥有独立的K和V投影，表达能力最强但KV Cache内存开销最大
- MQA（Multi-Query Attention）所有头共享同一组K和V，KV Cache内存降至1/n_heads，但可能损失精度
- GQA（Grouped-Query Attention）将头分为若干组，组内共享K/V，是MHA和MQA的折中方案
- 内存对比示例（Llama 2 70B）：MHA 536MB、GQA 130MB、MQA 16MB，差异悬殊
- Llama 2 70B使用GQA（8组），在推理效率和模型质量之间取得最佳平衡
- PaLM使用MQA追求极致推理速度，GPT-4推测使用GQA，不同模型根据部署场景选择不同策略

## Key Quotes
> "MHA是'每个人用自己的笔记本'，MQA是'全班共用一个笔记本'，GQA是'小组共用一个笔记本'。" -- 形象化对比三种策略

> "从536MB到16MB，你只需要做一件事：让更多的头共享同一份K和V。" -- 量化MQA的内存节省

> "GQA的哲学是：不需要最省，也不需要最好，够用就行。" -- 总结GQA的设计理念

## Connections
- [[MultiHeadAttention]] — 三种注意力机制的共同基础
- [[KVCache]] — MHA/MQA/GQA直接影响KV Cache的内存占用
- [[GQA]] — 本课重点讨论的折中方案

## Contradictions
