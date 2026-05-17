---
title: "LinearTransformation"
type: concept
tags:
  - linear-algebra
  - transformer
  - math-foundation
sources:
  - llm-lesson-01-linear-transformation
last_updated: 2026-05-18
---

## Overview

线性变换是向量空间之间保持加法和标量乘法运算的映射，是理解 Transformer 架构的数学基础。在几何直观上，线性变换表现为旋转、拉伸、剪切等操作，任何线性变换都可以用矩阵乘法来表示。Transformer 中的 WQ、WK、WV 权重矩阵本质上就是对输入向量进行线性变换，将其投影到不同的表示空间。

## Key Ideas

- 线性变换满足两条核心性质：T(u+v) = T(u) + T(v)（可加性）和 T(cu) = cT(u)（齐次性）
- 几何直观：旋转（保持长度和角度）、拉伸（缩放各轴）、剪切（平行位移）是最典型的三种线性变换
- 矩阵乘法是线性变换的标准表示方式，矩阵的列向量就是基向量变换后的位置
- Transformer 中的 WQ、WK、WV 三个权重矩阵分别将输入映射到查询（Query）、键（Key）、值（Value）空间

## Related Concepts
- [[Transformer]] — Transformer 架构中大量使用线性变换作为核心操作
- [[MultiHeadAttention]] — 多头注意力中的 QKV 投影就是线性变换
- [[RoPE]] — 旋转位置编码本质上是特殊的线性变换（旋转变换）
