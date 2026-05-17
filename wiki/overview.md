---
title: "Overview"
type: synthesis
tags: []
sources:
  - llm-lesson-01-linear-transformation
  - llm-lesson-02-decoding-strategy
  - llm-lesson-03-scaling-law
  - llm-lesson-04-model-py
  - llm-lesson-05-train-py
  - llm-lesson-06-inference-py
  - llm-lesson-07-flash-attention
  - llm-lesson-08-kv-cache
  - llm-lesson-09-mha-mqa-gqa
  - llm-lesson-10-sparse-infini-attention
  - llm-lesson-11-positional-encoding
  - llm-lesson-12-lora-qlora
  - llm-lesson-13-model-quantization
last_updated: 2026-05-18
---

# Overview

*This page is maintained by the LLM. It is updated on every ingest to reflect the current synthesis across all sources.*

## LLM 张老师课程全景

本 wiki 目前收录了 **LLM 张老师的 13 节大模型课程**，涵盖从数学基础到部署优化的完整知识链路。课程按四个阶段递进：

### 第一阶段：数学基础（第1-3课）
从 [[LinearTransformation|线性变换]] 的几何直观出发，理解 [[Transformer]] 中 WQ/WK/WV 权重矩阵的本质。接着学习 [[DecodingStrategy|解码策略]]（Temperature/Top-K/Top-P/Beam Search），掌握大模型如何从概率分布生成文本。最后通过 [[ScalingLaw]] 理解模型规模、数据量、计算量之间的幂律关系——**Chinchilla Law 告诉我们：数据量应约为参数量的 20 倍**。

### 第二阶段：代码实现（第4-6课）
从零手写 [[Transformer]] 架构（[[TrainingPipeline|Model.py → Train.py → Inference.py]]），理解每个组件的实现细节：多头注意力、前馈网络、残差连接、层归一化、位置编码。掌握 [[PyTorch]] 训练管线的完整流程：tiktoken 分词 → 批次构建 → 前向传播 → 交叉熵损失 → 反向传播 → [[WeightsAndBiases|AdamW]] 参数更新。

### 第三阶段：推理优化（第7-10课）
这是课程的核心部分，聚焦大模型推理的 **三大瓶颈**：
1. **注意力内存** — [[FlashAttention]] 通过 Tiling 分块 + Online Softmax 将 HBM 访问从 O(N²) 降至 O(N)
2. **重复计算** — [[KVCache]] 缓存已计算的 Key/Value，实现 **56 倍推理加速**
3. **注意力变种** — [[MultiHeadAttention|MHA]] → [[GQA]] → MQA，在性能与内存间取平衡（536MB → 130MB → 16MB）
4. **长上下文** — [[SparseAttention|稀疏注意力]]（Random/Window/Global）和 [[InfiniAttention|无限注意力]]（压缩记忆）

### 第四阶段：微调与部署（第11-13课）
- [[PositionalEncoding|位置编码]] 演进：正弦编码 → [[RoPE|旋转位置编码]]（LLaMA/Qwen）→ ALiBi（MPT/BLOOM）
- [[LoRA]] 低秩适配：冻结原始权重，仅训练 ΔW=B×A，参数减少 **99%+**
- [[QLoRA]]：4-bit 量化 + LoRA，让消费级 GPU 也能微调大模型
- [[ModelQuantization|模型量化]]：GPTQ/AWQ/GGUF 等方案实现 FP32 → INT4 的精度压缩

### 关键洞察
1. **大模型训练**：Scaling Law 指导参数量与数据量的最优配比，FLOPs 估算硬件需求
2. **推理加速**：Flash Attention + KV Cache + GQA 构成推理优化的"三驾马车"
3. **高效微调**：LoRA/QLoRA 让个人开发者也能参与大模型训练
4. **工程落地**：量化技术（GGUF/llama.cpp）让大模型在 CPU 上也能运行

### 知识图谱连接
课程内容形成紧密的知识网络：[[LinearTransformation]] → [[Transformer]] → [[MultiHeadAttention]] → [[FlashAttention]] → [[KVCache]] → [[GQA]] → [[SparseAttention]]，每一步优化都建立在前一步的瓶颈分析之上。
