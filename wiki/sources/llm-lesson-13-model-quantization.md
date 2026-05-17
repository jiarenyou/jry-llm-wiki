---
title: "模型量化：从FP32到INT4的压缩之旅"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/13-模型量化.md
last_updated: 2026-05-18
---

## Summary
本课全面讲解了大语言模型的量化技术。从精度等级体系（FP32到INT4）讲起，介绍了后训练量化（PTQ）的主要方法包括GPTQ和AWQ，GGUF格式在CPU部署中的应用（llama.cpp和LM Studio），AWQ保护显著权重的策略，以及量化感知训练（QAT）的前沿思路。量化是让大模型在资源受限环境中运行的核心技术。

## Key Claims
- FP32每个参数占4字节，INT4仅占0.5字节，7B模型从28GB压缩到3.5GB即可在消费级设备运行
- PTQ（Post-Training Quantization）无需重新训练，直接对已训练模型的权重进行量化
- GPTQ基于近似二阶信息逐层量化，利用Hessian矩阵确定最优量化参数，精度损失较小
- AWQ（Activation-aware Weight Quantization）保护对激活值影响最大的1%显著权重不量化或高精度量化
- GGUF格式是llama.cpp的原生模型格式，支持CPU+GPU混合推理，可在笔记本上运行大模型
- QAT（Quantization-Aware Training）在训练过程中模拟量化误差，让模型主动适应低精度，精度损失最小但成本最高
- LM Studio是基于GGUF格式的一站式模型部署工具，提供图形界面降低使用门槛

## Key Quotes
> "量化的核心矛盾是：你想用更少的数字表示同样的信息，必然会有信息丢失——问题只在于丢哪些。" -- 总结量化的本质挑战

> "AWQ的洞察是：不是所有权重都一样重要，保护好那1%的'关键先生'，剩下的随便量化。" -- 解释AWQ的核心策略

> "GGUF让大模型跑在笔记本上不再是梦想——虽然慢一点，但至少能跑。" -- 强调CPU部署的实用价值

## Connections
- [[ModelQuantization]] — 本课核心主题，从高精度到低精度的压缩技术
- [[LoRA]] — 量化后的模型仍然可以使用LoRA进行微调
- [[QLoRA]] — QLoRA结合了量化和LoRA两者的优势

## Contradictions
