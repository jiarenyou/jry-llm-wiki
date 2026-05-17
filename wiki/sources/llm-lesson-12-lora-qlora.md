---
title: "LoRA与QLoRA：参数高效微调"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/12-LoRA与QLoRA.md
last_updated: 2026-05-18
---

## Summary
本课讲解了LoRA（Low-Rank Adaptation）和QLoRA两种参数高效微调技术。LoRA通过低秩分解将权重更新量表示为Delta(W)=B×A，冻结原始权重只训练两个小矩阵，大幅降低可训练参数量。课程详细介绍了秩r参数（通常4-32）和Alpha缩放因子的作用。QLoRA在LoRA基础上引入4-bit量化，使消费级GPU也能微调大模型。

## Key Claims
- LoRA将权重更新分解为低秩形式 Delta(W)=B×A，其中B∈R^{d×r}，A∈R^{r×d}，r远小于d
- 冻结原始预训练权重，仅训练LoRA适配器的A和B矩阵，可训练参数量通常仅占原模型的0.1%-1%
- 秩r是LoRA的核心超参数，r越大表达能力越强但可训练参数越多，通常在4-32之间选取
- Alpha缩放因子控制LoRA更新的"学习率"，实际缩放为 alpha/r，平衡预训练知识与适配信号
- QLoRA在LoRA基础上使用4-bit NormalFloat量化冻结权重，训练时动态反量化到BF16
- QLoRA使单张24GB显存的消费级GPU（如RTX 4090）可以微调7B-13B参数的大模型

## Key Quotes
> "LoRA的哲学是：大模型已经学会了99%的知识，微调时只需要调整那1%的差异。" -- 解释低秩假设的合理性

> "秩r就像一个旋钮：往左拧更省参数但表达力弱，往右拧更强但更费资源。" -- 比喻秩参数的权衡

> "QLoRA让'穷人也能炼大模型'——一张4090就能搞定7B模型的微调。" -- 强调QLoRA的民主化意义

## Connections
- [[LoRA]] — 本课核心主题，低秩适配参数高效微调
- [[QLoRA]] — LoRA与量化的结合，进一步降低微调硬件门槛
- [[FineTuning]] — LoRA和QLoRA都是参数高效微调的具体方法

## Contradictions
