---
title: "Scaling Law：规模就是力量"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/03-Scaling-Law.md
last_updated: 2026-05-18
---

## Summary
本课深入讲解了大语言模型中的Scaling Law（缩放定律），即模型性能与参数量N、数据量D之间的幂律关系 L(N,D)=E+A/N^α+B/D^β。课程介绍了Chinchilla Law提出的最优数据配比 D≈20×N，以及FLOPs计算公式 C≈6×N×D。内容还涵盖了从BERT到GPT-4的模型参数演进历程，以及从FP32到INT4的精度等级体系。

## Key Claims
- 模型损失与参数量N和数据量D呈幂律关系，增加两者均可降低损失但收益递减
- Chinchilla Law表明最优训练数据量约为参数量的20倍（D≈20×N），此前很多模型训练不充分
- FLOPs近似计算公式为 C≈6×N×D，可用于估算训练所需算力资源
- GPT-3的175B参数、GPT-4的估计1.8T参数体现了模型规模的指数级增长趋势
- 精度等级从FP32（32位浮点）到FP16、BF16、INT8、INT4，每降一级内存减半但精度损失递增
- Scaling Law不仅适用于语言建模，也在多模态和推理任务中观察到类似规律

## Key Quotes
> "在深度学习里，暴力美学依然有效——堆更多的数据、更大的模型，性能就是会变好。" -- 总结Scaling Law的核心观察

> "Chinchilla的发现让所有人意识到：不是模型不够大，而是数据喂得不够多。" -- 解释Chinchilla Law的影响

> "FLOPs公式 C≈6×N×D 是算力账单的快捷算法：参数量乘以数据量再乘6。" -- 实用的算力估算方法

## Connections
- [[ScalingLaw]] — 本课核心主题，模型规模与性能的量化关系
- [[FLOPs]] — 浮点运算量计算，衡量训练和推理的算力消耗
- [[ModelQuantization]] — 精度等级体系，从FP32到INT4的压缩策略

## Contradictions
