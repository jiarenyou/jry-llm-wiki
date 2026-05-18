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
  - dong-xue-zhi-yu
  - ping-yong-zhi-e
  - gong-di-de-bei-ju
  - jing-ji-xue-da-shi-ha-ye-ke
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

## 杂记：哲学、经济学与文化思考

本 wiki 收录了 **30 篇杂记**，横跨哲学、经济学、文化历史、佛教、个人成长等领域，形成一个密集互联的思想网络。

### 哲学主线：认知边界与存在追问

从 [[PlatosCave|洞穴之喻]] 出发，一条主线贯穿多个哲学概念：[[Plato|柏拉图]]的理念世界 vs 感官世界 → [[Aristotle|亚里士多德]]的目的论 → 康德在 [[MetaphysicsAndEmpiricism|形而上与经验主义]] 中的调和 → [[CognitiveBoundaries|认知边界]] 的多维度揭示（希尔伯特、佛陀十四无忌、康德先天时空观）。[[IdentityProblem|同一性问题]] 通过忒修斯之船、阿能诃鼓追问事物存在的本质。[[HayekKnowledge|哈耶克知识论]] 则从经济学角度论证了知识分散在每个人大脑中，AI 无法完全模拟人的世界。

### 经济学主线：资源配置与博弈

[[TragedyOfCommons|公地悲剧]] 是经济学部分的核心枢纽，连接着 [[CoaseTheorem|科斯定律]]（产权与交易成本）、[[FairnessAndEfficiency|公平与效率]] 的权衡，以及噪音交易者理论。[[Hayek|哈耶克]] 的知识论为计划经济的不可能性提供了逻辑论证。

### 文化历史主线：儒学的变迁与中西对比

[[EvolutionOfConfucius|孔子面孔的演变]] 是文化部分的核心，展示孔子形象从秦到今的六次转变。[[RuJiaDeShiShou|儒家的失守]] 分析宋代儒家应对佛教道教冲击的困境，[[WeiHeXiFangLingXiuChangBeiDiaoKan|中西政教关系差异]] 解释文化心理的深层根源。[[ThirteenInvitationsMaDong|对话马东]] 提供了审视文化变迁的宏观视角。

### 佛教思想主线：实践优先与悬置智慧

[[FourteenUndetermined|十四无忌]] 和 [[PoisonArrowParable|毒箭之喻]] 构成佛教思想的实践维度——专注于当下行动而非追问终极答案。[[HuinengAndMonism|慧能与一元论]] 探讨禅宗顿悟与一元论的关联。[[UnfalsifiabilityOfDivination|占卜的不可证伪性]] 中，佛陀悬置问题的态度与占卜系统让一切不可证伪形成鲜明对照。

### 个人成长与知识管理主线

[[WuJunGrowth|吴军：成长的三个维度]]（看得远、看得透、看得开）与 [[RKStrategy|r/K策略]] 互为呼应。[[ElectronicHamster|电子仓鼠]] 提出IPO模型（Input-Processing-Output）克服数字囤积。[[DanKoeAudienceGrowth|Dan Koe]] 在AI时代强调品味和使命导向。[[ReadingAndThinking1|读书与思考1]] 用叔本华论述独立思考的价值，[[ReadingAndThinking2|读书与思考2]] 用边际分析量化读书与思考的平衡。
