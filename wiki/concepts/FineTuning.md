---
title: "FineTuning"
type: concept
tags:
  - fine-tuning
  - training
  - transfer-learning
sources:
  - llm-lesson-05-train-py
  - llm-lesson-12-lora-qlora
last_updated: 2026-05-18
---

## Overview

微调是指在预训练模型的基础上，针对特定任务或领域继续训练模型的过程。预训练阶段赋予模型通用的语言理解和生成能力，微调阶段则通过较小的学习率和较少的数据将这些能力适配到目标场景。根据可训练参数的范围，微调可分为全参数微调、LoRA 高效微调和 QLoRA 量化微调等不同策略。

## Key Ideas

- **全参数微调**：更新模型所有参数，效果最好但显存需求大，需要存储完整的优化器状态和梯度
- **LoRA 高效微调**：冻结原始权重，仅训练低秩适配矩阵，可训练参数减少 99% 以上
- **QLoRA 量化微调**：在 LoRA 基础上将模型权重量化为 4-bit，使消费级 GPU 可微调大模型
- **指令微调（Instruction Tuning）**：使用指令-回答格式的数据微调，使预训练模型具备对话和遵循指令的能力
- **领域适配**：在特定领域数据上微调可显著提升模型在该领域的表现，如医疗、法律、代码等

## Related Concepts
- [[LoRA]] — LoRA 是最常用的高效微调方法
- [[QLoRA]] — QLoRA 结合量化和 LoRA 实现极限显存优化
- [[TrainingPipeline]] — 微调复用训练管线，但学习率和数据策略不同
- [[ModelQuantization]] — 量化技术使微调后的模型可以高效部署
