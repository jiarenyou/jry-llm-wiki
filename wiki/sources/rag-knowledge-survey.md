---
title: "面向知识的检索-增强生成综述"
type: source
tags: [ai, rag, nlp, knowledge-retrieval, survey]
date: 2026-04-10
source_file: raw/杂记/面向知识的检索-增强生成综述.md
last_updated: 2026-05-18
---

## Summary
RAG（Retrieval-Augmented Generation，检索增强生成）的综合性综述，覆盖RAG的基本原理、核心组件和高级方法。RAG框架由三部分组成：LLM内部知识处理、外部知识检索、知识集成生成。文章系统介绍了RAG管线中的关键环节（意图理解、知识嵌入/索引/检索/集成/生成/引用），以及四种高级方法：RAG训练优化、多模态RAG、Memory RAG（隐式/显式/工作记忆三层架构）、Agentic RAG（自主代理+迭代优化）。论文来源：https://arxiv.org/html/2503.10677v2

## Key Claims
- RAG核心：将外部知识作为改进语言生成的关键因素，解决LLM受训练数据限制、无法访问动态知识的问题
- RAG起源于2020年Facebook的RAG论文和Google的REALM
- 基本RAG管线：意图理解 -> 知识源/解析 -> 知识嵌入 -> 知识索引 -> 知识检索 -> 知识集成 -> 答案生成 -> 知识引用
- 检索策略三类：稀疏检索（BM25/TF-IDF）、密集检索（向量相似度）、混合检索
- 知识集成三种方式：输入层集成（文本级/特征级）、中间层集成、输出层集成
- 高级RAG四方向：训练优化（静态/单向引导/协同训练）、多模态RAG、Memory RAG、Agentic RAG
- Memory RAG三层记忆：隐式（模型参数）、显式（键值缓存中间层）、工作记忆（原始文本块）
- Agentic RAG：自主代理负责查询理解、工具利用、推理优化，动态管理检索策略
- 评估维度：有效性（Query-Context相关性、Context-Answer一致性、Query-Answer准确性）和效率（延迟/吞吐/资源利用率）

## Key Quotes
> "RAG的核心是以知识为中心的方法，该方法将外部知识作为改进语言生成的关键因素" -- RAG的核心定义

> "知识集成有三种类型：输入层集成、中间层集成和输出层集成" -- 知识集成的层次划分

> "Agentic RAG是一个高级框架，它将自主代理与RAG技术集成在一起，显著提高了信息检索和生成过程的性能" -- Agentic RAG的价值

## Connections
- [[RAG]] -- RAG检索增强生成概念页
- [[Transformer]] -- RAG系统底层依赖Transformer架构
- [[MoE]] -- Agentic RAG中的多代理协作与MoE多专家路由思路相通
- [[FlashAttention]] -- RAG中的密集检索和注意力计算需要FlashAttention优化
- [[KVCache]] -- Memory RAG中的显式记忆采用键值缓存形式
- [[FineTuning]] -- RAG训练优化涉及检索器和生成器的微调

## Contradictions
