---
title: "Transformer深入理解：从编解码到注意力机制"
type: source
tags: [ai, transformer, nlp, attention]
date: 2026-04-10
source_file: raw/杂记/Transformer.md
last_updated: 2026-05-18
---

## Summary
从编解码结构、潜空间、词嵌入、注意力机制四个层面深入拆解Transformer架构。文章将Transformer置于RNN/CNN的演进脉络中，通过"码"（语义编码）、矩阵空间变换、Word2Vec、QKV注意力计算等核心概念的串联，揭示Transformer为什么优于RNN和CNN。核心论点是注意力机制的本质是"通过上下文关联修正词典中的客观语义，赋予词向量主观语义"。

## Key Claims
- Transformer保留了RNN的编解码结构，但完全基于注意力机制，舍弃了循环结构，实现了并行计算
- 词向量编码是将token通过one-hot降维投射到潜空间（词嵌入），潜空间的连续性使AI能处理训练中未见过的表达
- Word2Vec（CBOW/Skip-gram）训练出体现客观语义的嵌入矩阵，但不包含上下文主观语义
- 注意力机制中Q与K分离（而非单矩阵）引入了二次型的非线性表达能力，使模型能区分"设定语义"和"表达语义"
- Q x K转置计算的是词向量间的内积投影（相关性强弱），softmax归一化后与V相乘，相当于用上下文关联系数修正客观语义
- 绝对位置编码使用正弦/余弦函数（类似傅里叶级数），相对位置编码在注意力得分矩阵上修饰
- 多头注意力本质类似CNN的卷积核，按维度分组后跨通道融合

## Key Quotes
> "理解Transformer的关键地方是编码和解码的结构，注意力机制是在这整个框架下为了满足某种特定的任务而产生的" -- 编解码是骨架，注意力是特定优化

> "Q是'问'，K是'标签'，V是'答案'；先问再查，最后加权汇总信息" -- QKV直觉理解

> "注意力机制需要搞定的就是要识别出因上下文关联，而对词典中原本客观的语义进行调整和改变的幅度" -- 注意力机制的语义修正功能

> "Word2Vec训练出的潜空间的词义是不依赖作者的主观意图的，是一种客观的表达" -- Word2Vec提供基础语义，Transformer的注意力负责主观语义

## Connections
- [[Transformer]] -- Transformer架构概念页，本文是深度解读
- [[MultiHeadAttention]] -- 多头注意力机制详解
- [[LinearTransformation]] -- 矩阵空间变换是理解Transformer的基础
- [[LoRA]] -- 低秩适配与本文中矩阵分解思路相通
- [[PositionalEncoding]] -- 位置编码方案详解
- [[PyTorch]] -- PyTorch框架是实现Transformer的基础工具
- [[RAG]] -- Transformer是RAG系统的底层模型架构
- [[MoE]] -- MoE在Transformer基础上引入稀疏激活

## Contradictions
