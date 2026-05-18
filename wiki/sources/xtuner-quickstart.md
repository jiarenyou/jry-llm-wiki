---
title: "XTuner：大模型微调快速上手"
type: source
tags: [ai, llm, finetuning, tools]
date: 2026-04-10
source_file: raw/杂记/Xtuner：大模型微调快速上手.md
last_updated: 2026-05-18
---

## Summary
介绍上海人工智能实验室开发的XTuner微调工具库，其核心设计理念是"用一个配置文件搞定一切"。文章详细演示了使用QLoRA微调InternLM2-1.8B模型的完整流程：安装 -> 选配置 -> 跑训练 -> 转模型 -> 去聊天。XTuner支持LoRA/QLoRA/全量微调，集成FlashAttention和DeepSpeed，可与LMDeploy、OpenCompass形成"微调-评测-部署"全流程。

## Key Claims
- XTuner是配置文件驱动+命令行工具的微调框架，支持InternLM、Llama、Qwen、ChatGLM等主流模型
- QLoRA微调流程：xtuner list-cfg -> xtuner copy-cfg -> xtuner train -> xtuner convert pth_to_hf -> xtuner convert merge -> xtuner chat
- 训练产出的是适配器（Adapter）权重而非完整模型，需要与基础模型合并才能独立使用
- 集成FlashAttention、Triton Kernels等优化技术，降低显存占用
- 支持自定义JSONL格式数据集，修改配置文件dataset部分即可

## Key Quotes
> "XTuner通过'配置文件驱动'和'命令行工具'，将复杂的大模型微调流程变得标准化和简单化" -- XTuner核心价值

> "你只需要：选配置、跑训练、转模型、去聊天" -- XTuner四步流程

## Connections
- [[FineTuning]] -- 微调技术概念页
- [[LoRA]] -- XTuner支持的LoRA低秩适配方法
- [[QLoRA]] -- XTuner支持的QLoRA量化低秩适配方法
- [[FlashAttention]] -- XTuner集成的注意力优化技术
- [[TrainingPipeline]] -- XTuner实现了完整的训练管线
- [[PyTorch]] -- XTuner基于PyTorch生态
- [[ModelQuantization]] -- 量化技术与微调的互补关系

## Contradictions
