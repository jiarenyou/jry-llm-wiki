---
title: "SWIFT"
type: entity
tags: [ai, tools, finetuning]
sources: [swift-output-explained]
last_updated: 2026-05-18
---

## Overview
SWIFT（Scalable lightWeight Infrastructure for Fine-Tuning）是阿里巴巴达摩院开发的大模型微调框架。支持LoRA、QLoRA等PEFT方法，训练产出的swift_output文件夹中存储的是轻量级适配器（增量权重），需与基础模型合并后才能独立使用。

## Key Concepts
- **swift_output**：微调后生成的适配器权重文件，通常几十到几百MB
- **适配器（Adapter）**：记录模型为适应新任务而进行的"增量调整"，仅训练约0.1%参数
- **合并（Merge）**：将适配器权重合并到基础模型中，生成完整的可用模型

## Merge Strategies
- **加载时合并（Inference-time Merge）**：推理时同时加载基础模型和适配器
- **物理合并（Physical Merge）**：预先合并为完整模型，简化部署和推理

## Standard Practice
"训练时分离，部署时合并"（Train separate, merge for deployment）

## Relationships
- [[LoRA]] -- SWIFT支持LoRA低秩适配
- [[QLoRA]] -- SWIFT支持QLoRA量化适配
- [[FineTuning]] -- SWIFT是PEFT微调框架
- [[XTuner]] -- 另一个大模型微调工具，功能定位类似

## Sources
- [[swift-output-explained]] -- swift_output输出内容的详细解释
