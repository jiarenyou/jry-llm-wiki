---
title: "从零搭建Transformer架构"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/04-模型代码实现.md
last_updated: 2026-05-18
---

## Summary
本课从底层组件出发，逐步搭建完整的Transformer架构代码实现。内容涵盖FeedForward前馈网络、单头注意力与多头注意力机制、TransformerBlock的组装，以及正弦位置编码、残差连接和层归一化等关键技术细节。课程最后以交叉熵损失函数收尾，完成从输入到输出的完整前向传播链路。

## Key Claims
- FeedForward网络由两个线性层夹一个激活函数组成，本质是对每个位置独立做非线性变换
- 单头注意力的核心计算为 softmax(QK^T/√d_k)V，缩放因子√d_k防止点积过大导致softmax梯度消失
- 多头注意力将Q、K、V分别投影到h个子空间并行计算注意力再拼接，让模型关注不同子模式
- 正弦位置编码利用三角函数的周期性为每个位置生成唯一编码，且相对位置关系可被线性表示
- 残差连接（Add）缓解深层网络的梯度消失问题，层归一化（Norm）稳定每层输出的数值范围
- 交叉熵损失衡量模型预测分布与真实token分布的差异，是语言模型训练的标准目标函数

## Key Quotes
> "多头注意力就像是让模型戴着不同颜色的眼镜看同一句话——每副眼镜关注不同的东西。" -- 形象化解释多头机制

> "残差连接的意思是：别怕，就算这一层学坏了，至少还有上一层的输出兜底。" -- 解释残差连接的意义

> "缩放因子√d_k不是随便加的，它是对点积结果的'温度调节'。" -- 说明注意力缩放的作用

## Connections
- [[Transformer]] — 本课核心主题，从零实现Transformer架构
- [[MultiHeadAttention]] — 多头注意力机制的完整代码实现
- [[PositionalEncoding]] — 正弦位置编码的原理与实现

## Contradictions
