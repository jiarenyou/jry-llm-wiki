---
title: "QLoRA"
type: concept
tags:
  - fine-tuning
  - quantization
  - parameter-efficient
sources:
  - llm-lesson-12-lora-qlora
last_updated: 2026-05-18
---

## Overview

QLoRA 是一种结合 4-bit 量化和 LoRA 低秩适配的微调方法，使得在消费者级 GPU 上微调大语言模型成为可能。它在 LoRA 的基础上引入三种关键创新：4-bit NormalFloat 量化格式、双重量化和分页优化器，将 65B 参数模型的微调显存需求从 780GB 降至 48GB 以内，同时保持与全精度微调相当的性能。

## Key Ideas

- **4-bit NormalFloat（NF4）**：针对正态分布权重优化的 4-bit 量化格式，比传统 INT4 更适合神经网络权重分布
- **双重量化**：对量化常数本身再次量化（从 FP32 量化到 FP8），进一步减少显存占用
- **分页优化器**：利用 GPU 统一内存机制，在显存不足时自动将优化器状态换出到 CPU 内存
- **计算流程**：反向传播时将 4-bit 权重动态反量化到 BF16 进行计算，梯度只更新 LoRA 的低秩矩阵
- **民主化 AI**：QLoRA 使普通开发者可以在单张消费级 GPU（如 RTX 3090/4090）上微调数十亿参数的大模型

## Related Concepts
- [[LoRA]] — QLoRA 在 LoRA 基础上引入量化技术
- [[ModelQuantization]] — QLoRA 使用了 4-bit 量化技术
- [[FineTuning]] — QLoRA 使大模型微调在消费级硬件上成为可能
