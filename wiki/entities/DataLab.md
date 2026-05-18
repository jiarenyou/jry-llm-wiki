---
title: "DataLab"
type: entity
tags: [ai, bi, platform, tencent]
sources: [datalab-llm-bi-platform]
last_updated: 2026-05-18
---

## Overview
DataLab是腾讯提出的一站式LLM-based BI平台，将BI工作流与Agent框架和Jupyter Notebook界面集成统一。论文地址：https://arxiv.org/abs/2412.02205

## Architecture
- **LLM-based Agent Framework**：多个Agent + 数据工具（Python沙箱、Vega-Lite可视化）
- **Computational Notebook Interface**：增强版JupyterLab，支持SQL/Python/Markdown/Chart多语言单元格

## Three Key Modules
1. **领域知识整合**：知识自动生成（LLM Map-Reduce）-> 知识图谱组织 -> 查询重写+检索+DSL翻译
2. **代理间通信**：FSM建模 + 共享信息缓冲区 + 结构化信息单元
3. **基于单元格的上下文管理**：DAG依赖图 + 自适应检索，减少token消耗

## Performance
- NL2SQL和NL2VIS任务准确率显著高于基线
- 上下文管理后时间和token消耗明显下降

## Relationships
- [[RAG]] -- DataLab领域知识整合采用RAG思路
- [[Transformer]] -- 底层依赖Transformer架构的LLM
- [[MoE]] -- 多Agent协作与MoE多专家路由思路相似

## Sources
- [[datalab-llm-bi-platform]] -- DataLab平台详细解读
