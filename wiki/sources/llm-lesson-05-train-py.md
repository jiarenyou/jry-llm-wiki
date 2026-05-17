---
title: "训练管线实现"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/05-训练代码实现.md
last_updated: 2026-05-18
---

## Summary
本课聚焦于Transformer模型的训练管线实现，从数据加载与预处理开始，到训练循环和模型评估的完整流程。课程使用tiktoken作为BPE分词器，AdamW作为优化器，并实现了自回归文本生成和梯度累积等关键技术。通过动手编写训练代码，学员能够理解大语言模型从原始文本到可训练数据的完整加工链路。

## Key Claims
- 训练数据需要经过分词（tokenization）、分块（chunking）、批次组装（batching）三步预处理
- tiktoken是OpenAI开源的BPE分词器，GPT-2和GPT-4均使用其变体，处理速度远超纯Python实现
- AdamW优化器通过解耦权重衰减与梯度更新，比标准Adam有更好的正则化效果
- 自回归生成逐token预测并自回填，每步将上一个预测结果拼入输入序列
- 梯度累积在显存不足时模拟更大batch size，每N步才执行一次参数更新
- 训练循环的核心是：前向传播计算损失 → 反向传播计算梯度 → 优化器更新参数 → 清零梯度

## Key Quotes
> "训练循环本质上就是四行代码的无限循环：前向、反向、更新、清零。" -- 概括训练循环的本质

> "梯度累积就是'先攒着，攒够了再一起更新'——穷人版的大batch训练。" -- 形象解释梯度累积

> "分词器是模型理解人类语言的第一道门，一个好的分词器能让模型少走很多弯路。" -- 强调分词的重要性

## Connections
- [[Transformer]] — 被训练的模型架构
- [[TrainingPipeline]] — 本课核心主题，完整的训练流程实现

## Contradictions
