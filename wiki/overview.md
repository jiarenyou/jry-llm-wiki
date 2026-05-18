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
  - transformer-deep-dive
  - qkv-matrices-explained
  - transformer-vs-moe
  - xtuner-quickstart
  - pytorch-basics
  - warmup-ratio
  - ai-language-inflation
  - datalab-llm-bi-platform
  - rag-knowledge-survey
  - swift-output-explained
  - spark-performance-optimization-panorama
  - spark-wide-narrow-dependency-optimization
  - spark-small-files-problem
  - spark-data-skew
  - spark-resource-parallelism-optimization
  - spark-memory-management
  - hive-sql-syntax-guide
  - data-warehouse-modeling-core
  - data-warehouse-modeling-methodology
  - data-compression
  - data-governance-sla
  - alibaba-big-data-path-notes
  - performance-optimization-three-layers
  - brain-consultant-guide
  - brain-learning-system
  - brain-self-study-roadmap
  - dong-xue-zhi-yu
  - ping-yong-zhi-e
  - gong-di-de-bei-ju
  - jing-ji-xue-da-shi-ha-ye-ke
  - dang-xia-de-li-liang
  - huo-chu-sheng-ming-de-yi-yi
  - claude-code-practice-1-obsidian-skills
  - claude-code-practice-2-tutorial
last_updated: 2026-05-18
---

# Overview

*本页面由 LLM 维护，每次摄入后更新，反映所有来源文档的综合理解。*

本 wiki 收录了 **5 大知识领域**的笔记与学习资料，覆盖 LLM/AI、大数据工程、量化金融、哲学经济学、个人成长与读书笔记。

---

## 一、LLM 与 AI 技术

### 张老师课程全景（13课）

涵盖从数学基础到部署优化的完整知识链路，分四个阶段递进：

**第一阶段：数学基础（第1-3课）** — 从 [[LinearTransformation|线性变换]] 的几何直观出发，理解 [[Transformer]] 中 WQ/WK/WV 权重矩阵的本质。掌握 [[DecodingStrategy|解码策略]]（Temperature/Top-K/Top-P/Beam Search）。通过 [[ScalingLaw]] 理解幂律关系——**Chinchilla Law：数据量应约为参数量的 20 倍**。

**第二阶段：代码实现（第4-6课）** — 从零手写 [[Transformer]] 架构（[[TrainingPipeline|Model.py → Train.py → Inference.py]]），掌握 [[PyTorch]] 训练管线：tiktoken 分词 → 批次构建 → 前向传播 → 交叉熵损失 → AdamW 参数更新。

**第三阶段：推理优化（第7-10课）** — 聚焦三大瓶颈：
- [[FlashAttention]]：Tiling + Online Softmax，HBM 访问 O(N²) → O(N)
- [[KVCache]]：缓存 Key/Value，**56 倍推理加速**
- [[MultiHeadAttention|MHA]] → [[GQA]] → MQA：536MB → 130MB → 16MB
- [[SparseAttention|稀疏注意力]] 与 [[InfiniAttention|无限注意力]]：长上下文方案

**第四阶段：微调与部署（第11-13课）** — [[PositionalEncoding|位置编码]] 演进（正弦 → [[RoPE]] → [[ALiBi]]），[[LoRA]]/[[QLoRA]] 低秩适配（参数减少 99%+），[[ModelQuantization|模型量化]]（GPTQ/AWQ/GGUF）。

### 补充专题

- [[Transformer|Transformer 深入理解]]：编解码与注意力机制深度拆解
- QKV 矩阵：Query/Key/Value 含义与计算流程
- [[MoE|Transformer vs MoE]]：混合专家架构对比
- [[XTuner]] 快速上手：上海 AI Lab 微调工具库实战
- [[PyTorch]] 初级：Tensor → 数据加载 → 模型搭建 → 训练循环 → ONNX 部署
- warmup_ratio：学习率预热比例参数
- AI 语言通胀：人机交互中语言通胀与高效 Prompt 原则
- [[RAG]] 综述：面向知识的检索增强生成
- SWIFT 框架：swift_output 输出解析
- Claude Code 实践：Obsidian Skills MCP 技能包 + 完整教程阅读心得（Plan Mode / CLAUDE.md / Subagents / MCP 工作流）

---

## 二、大数据工程与数仓

### Spark 性能优化体系

六篇 Spark 优化笔记构成完整体系，从宏观到微观逐层深入：

- [[SparkPerformance|性能优化全景图]]：框架总览与优化层次
- [[HiveSQL|宽窄依赖优化]]：Shuffle 避免与算子选择策略
- 小文件问题：合并策略与文件数控制
- [[DataSkew|数据倾斜]]：诊断与解决方案（加盐、两阶段聚合）
- 资源配置与并行度优化：Executor/内存/并行度调优
- 内存管理：统一内存模型（Storage vs Execution）

### Hive SQL

- [[HiveSQL|Hive SQL 语法大全]]：完整语法参考

### 数仓建模

- [[DataWarehouse|数仓建模核心方法]]：维度建模、星型/雪花模型
- [[DataWarehouse|数仓建模方法论]]：Kimball/Inmon/Data Vault
- 阿里巴巴大数据之路笔记：阿里大数据实践经验

### 数据治理与基础设施

- [[DataGovernance|数据治理 SLA]]：服务水平协议与数据质量
- 数据压缩：压缩算法选择与存储优化
- [[DataLab]] 统一 BI 平台：腾讯 LLM-based 一站式 BI 平台，领域知识 + 多代理协作
- 性能优化三层框架：系统化性能优化方法论

---

## 三、量化金融（WorldQuant）

- [[BRAINPlatform|BRAIN 兼职顾问指南]]：从注册到成为顾问的完整流程，Challenge Score 达 Gold Level → 系统邀请 → 提交 alpha → 合同签署
- [[QuantLearningPath|BRAIN 量化学习体系]]：三阶段（入门/进阶/高阶），从 alpha 概念到遗传算法 + 大规模回测
- [[BRAINPlatform|BRAIN 自学路径图]]：四大模块入门资源汇总

---

## 四、哲学、经济学与文化

### 哲学主线：认知边界与存在追问

从 [[PlatosCave|洞穴之喻]] 出发：[[Plato|柏拉图]] 理念世界 vs 感官世界 → [[Aristotle|亚里士多德]] 目的论 → 康德 [[MetaphysicsAndEmpiricism|形而上与经验主义]] → [[CognitiveBoundaries|认知边界]]（希尔伯特、佛陀十四无忌、康德先天时空观）。[[IdentityProblem|同一性问题]] 以忒修斯之船追问事物本质。

### 经济学主线：资源配置与博弈

[[TragedyOfCommons|公地悲剧]] 是核心枢纽，连接 [[CoaseTheorem|科斯定律]]（产权与交易成本）、[[FairnessAndEfficiency|公平与效率]] 的权衡。[[Hayek|哈耶克]] 知识论论证计划经济的不可能性。

### 文化历史：儒学变迁与中西对比

[[EvolutionOfConfucius|孔子面孔的演变]] 展示六次形象转变；[[RuJiaDeShiShou|儒家的失守]] 分析宋代儒学应对佛道冲击；[[WeiHeXiFangLingXiuChangBeiDiaoKan|中西政教关系差异]] 揭示文化心理根源。

### 佛教思想：实践优先与悬置

[[FourteenUndetermined|十四无忌]] 和毒箭之喻构成实践维度——专注当下非追问终极。[[UnfalsifiabilityOfDivination|占卜的不可证伪性]] 与佛陀悬置形成对照。

### 个人成长与知识管理

[[WuJunGrowth|吴军成长三维度]]（看得远/透/开）与 [[RKStrategy|r/K 策略]] 呼应；[[ElectronicHamster|电子仓鼠]] IPO 模型克服数字囤积；[[DanKoeAudienceGrowth|Dan Koe]] 强调品味与使命导向；[[ReadingAndThinking1|读书与思考]] 用叔本华和边际分析探讨独立思考价值。

---

## 五、读书笔记：心灵与意义

- [[Mindfulness|《当下的力量》]]：从思维中觉醒，「强迫性思考」与「小我」的消解，与佛陀「十四无忌」一脉相承
- [[Logotherapy|《活出生命的意义》]]：弗兰克尔意义疗法——人永远拥有选择态度的自由，三种发现意义的途径

---

## 知识网络总览

五大领域之间存在深层联系：Spark 的性能优化理念（瓶颈分析、分层优化）与 LLM 推理优化（Flash Attention、KV Cache、GQA）共享相同的工程思维方式；公地悲剧中的公平与效率权衡在数仓 SLA 治理中重现；哈耶克的知识分散论与 AI 辅助决策形成思想张力。整个知识网络以**瓶颈分析、分层抽象、实践优先**为共同主题。
