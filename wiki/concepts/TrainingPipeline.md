---
title: "TrainingPipeline"
type: concept
tags:
  - training
  - pipeline
  - deep-learning
sources:
  - llm-lesson-04-model-py
  - llm-lesson-05-train-py
  - llm-lesson-06-inference-py
last_updated: 2026-05-18
---

## Overview

训练管线是大语言模型从原始数据到可部署模型的完整工程流程。核心步骤包括：数据分词（使用 tiktoken 等 BPE 分词器）、批次构建（构造输入-目标对）、前向传播（计算 logits）、损失计算（交叉熵）、反向传播（计算梯度）和参数更新（使用 AdamW 优化器）。每个环节的工程实现对训练效率和模型质量都有直接影响。

## Key Ideas

- **数据分词**：使用 BPE 分词器（如 tiktoken）将原始文本转换为 token ID 序列，是数据预处理的第一步
- **批次构建**：将 token 序列切分为固定长度的输入-目标对，目标（target）是输入右移一位的结果
- **前向传播**：输入经过 Transformer 的多层注意力 + FFN 计算，输出每个位置的词表概率分布（logits）
- **损失计算**：使用交叉熵损失衡量模型预测的概率分布与真实 token 之间的差距
- **反向传播**：通过链式法则计算损失对各层参数的梯度，是参数更新的基础
- **AdamW 优化器**：在 Adam 基础上解耦权重衰减，是训练 Transformer 的标准优化器选择

## Related Concepts
- [[Transformer]] — Transformer 是训练管线中的模型核心
- [[ScalingLaw]] — 训练管线的规模需要遵循 Scaling Law 的指导
- [[FineTuning]] — 微调是在预训练基础上的特殊训练管线
- [[FLOPs]] — FLOPs 衡量训练管线的计算需求
