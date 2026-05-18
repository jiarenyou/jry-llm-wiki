---
title: "RAG"
type: concept
tags: [ai, rag, nlp, knowledge-retrieval]
sources: [rag-knowledge-survey, datalab-llm-bi-platform]
last_updated: 2026-05-18
---

## Definition
RAG（Retrieval-Augmented Generation，检索增强生成）是一种将外部知识检索与LLM生成相结合的范式。由Facebook于2020年提出，RAG通过将检索机制集成到生成管道中，解决LLM受训练数据限制、无法访问动态或领域特定知识的问题。

## Core Components
- **用户意图理解**：查询分解、查询重写、意图聚类
- **知识检索**：稀疏检索（BM25/TF-IDF）、密集检索（向量相似度）、混合检索
- **知识集成**：输入层集成（文本级/特征级）、中间层集成、输出层集成
- **答案生成**：降噪（显式/判别器/自反射）+ 推理（图推理/交叉注意/记忆增强）
- **知识引用**：同步引文生成、生成后引文检索

## Advanced Variants
- **多模态RAG**：整合图像/音频/视频等多种模态
- **Memory RAG**：三层记忆架构（隐式记忆/显式记忆/工作记忆），键值缓存中间层
- **Agentic RAG**：自主代理+迭代优化，动态管理检索策略，工具利用

## Key Formulas
- RAG基本流程：Query -> LLM内部知识处理 + 外部知识检索 -> 知识集成 -> 答案生成
- 知识检索：similarity(query, document) -> top-k chunks
- 知识集成：output = Generator(query, retrieved_context)

## Applications
- 问答系统（单跳/多跳/长篇QA）
- 信息提取（实体链接/关系提取）
- 文本理解与生成（分类/摘要）
- BI数据分析（如DataLab平台）

## Relationships
- [[Transformer]] -- RAG底层依赖Transformer架构的LLM
- [[MoE]] -- Agentic RAG中的多代理协作与MoE思路相通
- [[KVCache]] -- Memory RAG中的显式记忆采用键值缓存形式
- [[FlashAttention]] -- 密集检索和注意力计算需要优化

## Sources
- [[rag-knowledge-survey]] -- RAG综述，覆盖基本原理到高级方法
- [[datalab-llm-bi-platform]] -- DataLab中RAG在BI场景的应用
