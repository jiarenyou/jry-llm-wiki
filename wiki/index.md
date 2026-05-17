# Wiki Index

This file is maintained by the LLM. Updated on every ingest.

## Overview
- [Overview](overview.md) — LLM 张老师课程全景综合

## Sources
- [第1课 线性变换](sources/llm-lesson-01-linear-transformation.md) — 线性变换几何直观与矩阵表示，Transformer权重矩阵
- [第2课 解码策略](sources/llm-lesson-02-decoding-strategy.md) — Temperature/Top-K/Top-P/Beam Search解码策略
- [第3课 Scaling Law](sources/llm-lesson-03-scaling-law.md) — 幂律关系、Chinchilla Law、FLOPs计算
- [第4课 Model.py](sources/llm-lesson-04-model-py.md) — 从零搭建Transformer架构代码
- [第5课 Train.py](sources/llm-lesson-05-train-py.md) — 训练管线实现：分词、优化、评估
- [第6课 Inference.py](sources/llm-lesson-06-inference-py.md) — 推理管线：模型加载、文本生成、分布式训练
- [第7课 Flash Attention](sources/llm-lesson-07-flash-attention.md) — HBM/SRAM优化、Tiling分块、Online Softmax
- [第8课 KV Cache](sources/llm-lesson-08-kv-cache.md) — 自回归推理缓存，56倍加速
- [第9课 MHA/MQA/GQA](sources/llm-lesson-09-mha-mqa-gqa.md) — 注意力变种对比，内存536MB→16MB
- [第10课 稀疏/无限注意力](sources/llm-lesson-10-sparse-infini-attention.md) — Sparse Attention三组件、Infini-Attention压缩记忆
- [第11课 位置编码](sources/llm-lesson-11-positional-encoding.md) — Sinusoidal/RoPE/ALiBi位置编码方案
- [第12课 LoRA/QLoRA](sources/llm-lesson-12-lora-qlora.md) — 低秩适配微调，4-bit量化
- [第13课 模型量化](sources/llm-lesson-13-model-quantization.md) — GPTQ/AWQ/GGUF量化部署

## Entities
- [DeepMind](entities/DeepMind.md) — Google旗下AI实验室，Chinchilla Law
- [Google](entities/Google.md) — Big Bird稀疏注意力，Gemini长上下文
- [HuggingFace](entities/HuggingFace.md) — 开源ML平台，Transformers库
- [Kimi](entities/Kimi.md) — 中国AI公司，长上下文应用
- [Meta](entities/Meta.md) — LLaMA系列模型
- [MistralAI](entities/MistralAI.md) — 法国AI公司
- [OpenAI](entities/OpenAI.md) — GPT系列创建者
- [PyTorch](entities/PyTorch.md) — 深度学习框架
- [TriDao](entities/TriDao.md) — Flash Attention作者，Stanford
- [WeightsAndBiases](entities/WeightsAndBiases.md) — ML实验跟踪平台

## Concepts
- [ALiBi](concepts/ALiBi.md) — 线性偏置位置编码（概念页见PositionalEncoding）
- [DecodingStrategy](concepts/DecodingStrategy.md) — 解码策略：Greedy/Beam/Top-K/Top-P/Temperature
- [FineTuning](concepts/FineTuning.md) — 微调技术：全参数/LoRA/QLoRA
- [FlashAttention](concepts/FlashAttention.md) — Tiling分块+Online Softmax，HBM访问O(N²)→O(N)
- [FLOPs](concepts/FLOPs.md) — 浮点运算量 C≈6×N×D
- [GQA](concepts/GQA.md) — 分组查询注意力，LLaMA采用，内存536→130MB
- [InfiniAttention](concepts/InfiniAttention.md) — 压缩记忆实现无限上下文
- [KVCache](concepts/KVCache.md) — 推理加速缓存，56倍提速
- [LinearTransformation](concepts/LinearTransformation.md) — 线性变换几何直观
- [LoRA](concepts/LoRA.md) — 低秩适配，ΔW=B×A，参数减少99%+
- [ModelQuantization](concepts/ModelQuantization.md) — FP32→INT4量化，GPTQ/AWQ/GGUF
- [MultiHeadAttention](concepts/MultiHeadAttention.md) — 多头注意力，MHA/MQA/GQA演化
- [PositionalEncoding](concepts/PositionalEncoding.md) — 位置编码：正弦/RoPE/ALiBi
- [QLoRA](concepts/QLoRA.md) — 4-bit量化+LoRA，消费者GPU微调
- [RoPE](concepts/RoPE.md) — 旋转位置编码，LLaMA/Qwen采用
- [ScalingLaw](concepts/ScalingLaw.md) — 幂律关系 L(N,D)=E+A/N^α+B/D^β
- [SparseAttention](concepts/SparseAttention.md) — 稀疏注意力 O(N²)→O(N√N)
- [TrainingPipeline](concepts/TrainingPipeline.md) — 训练管线：分词→批次→前向→损失→反向→更新
- [Transformer](concepts/Transformer.md) — 编码器-解码器架构，自注意力+FFN

## Syntheses
