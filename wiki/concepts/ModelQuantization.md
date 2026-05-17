---
title: "ModelQuantization"
type: concept
tags:
  - quantization
  - model-compression
  - deployment
sources:
  - llm-lesson-13-model-quantization
last_updated: 2026-05-18
---

## Overview

模型量化是通过降低模型参数的数值精度来减少模型体积和推理成本的技术，典型的如从 FP32 降至 INT4 可将模型体积压缩 8 倍。主要分为后训练量化（PTQ）和量化感知训练（QAT）两大类。GPTQ 和 AWQ 是主流的 PTQ 方法，GGUF 格式支持 CPU 部署，使得在资源受限的设备上运行大模型成为可能。

## Key Ideas

- **精度等级**：FP32（32位）> FP16/BF16（16位）> INT8（8位）> INT4（4位），精度越低体积越小、推理越快，但质量可能下降
- **PTQ（后训练量化）**：在模型训练完成后直接量化权重，不需要重新训练，GPTQ 和 AWQ 是代表方法
- **GPTQ**：基于近似二阶信息的逐层量化方法，通过 Hessian 矩阵引导量化误差补偿
- **AWQ**：基于激活感知的量化方法，保护对模型输出影响最大的权重通道不被过度量化
- **GGUF 格式**：专为 CPU/边缘部署设计的量化格式，支持多种量化等级，可在 CPU 上高效推理
- **QAT（量化感知训练）**：在训练过程中模拟量化误差，使模型学习适应低精度表示

## Related Concepts
- [[QLoRA]] — QLoRA 结合了量化和 LoRA 微调
- [[TrainingPipeline]] — QAT 在训练管线中引入量化模拟
- [[DecodingStrategy]] — 量化后的模型在解码策略上可能有不同表现
