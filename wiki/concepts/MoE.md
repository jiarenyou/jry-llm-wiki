---
title: "MoE"
type: concept
tags: [ai, moe, architecture, scaling]
sources: [transformer-vs-moe]
last_updated: 2026-05-18
---

## Definition
MoE（Mixture of Experts，混合专家模型）是一种将模型拆分为多个独立"专家网络"并通过门控机制动态选择激活专家的架构。MoE实现了"条件计算"（Conditional Computation），使模型总参数量可大幅增加而计算成本仅线性增长。

## Core Formula
$$y = \sum_{i=1}^{k} G(x)_i \cdot E_i(x)$$

- E_i(x): 第i个专家网络的输出（每个专家可能是FFN或小型Transformer）
- G(x): 门控网络，输出稀疏权重（通常只激活Top-1或Top-2专家）

## Key Components
- **专家网络（Experts）**：独立的FFN或小型Transformer，参数量远小于全量模型
- **门控网络（Gating Network）**：轻量级线性层+Softmax，G(x) = Softmax(W_g * x + b_g)
- **负载均衡（Load Balancing）**：辅助损失函数防止专家被过度激活或闲置

## Advantages
- 计算高效：参数量大幅增加（万亿级），计算成本仅线性增长
- 任务适应性：不同专家隐式学习不同领域知识

## Challenges
- 训练不稳定：专家间"马太效应"（强者恒强）
- 通信开销：分布式训练中跨设备路由

## Notable Implementations
- **Switch Transformer**（Google, 2021）：1.6万亿参数，每输入仅激活约1000亿
- **GShard**（Google, 2020）：机器翻译中部署MoE，专家分布于不同GPU

## Relationships
- [[Transformer]] -- MoE通常替换Transformer中的FFN层
- [[MultiHeadAttention]] -- MoE与多头注意力共享"条件计算"设计理念
- [[SparseAttention]] -- 稀疏注意力与MoE共享"稀疏激活"思想
- [[RAG]] -- Agentic RAG中的多代理协作与MoE思路相通

## Sources
- [[transformer-vs-moe]] -- Transformer与MoE架构对比分析
