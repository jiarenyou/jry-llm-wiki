---
title: "DecodingStrategy"
type: concept
tags:
  - decoding
  - inference
  - text-generation
sources:
  - llm-lesson-02-decoding-strategy
last_updated: 2026-05-18
---

## Overview

解码策略决定了语言模型在生成文本时如何从概率分布中选取下一个 token。不同的解码策略在生成质量、多样性和计算效率之间做出不同权衡。从确定性的 Greedy Search 到随机采样的 Top-K/Top-P，再到调节分布形态的 Temperature，每种策略都有其适用场景。

## Key Ideas

- **Greedy Search**：每步选择概率最大的 token（argmax），速度快但容易产生重复和退化文本
- **Beam Search**：同时维护多个候选序列（beam width），在多路径中探索最优解，平衡质量与多样性
- **Top-K 采样**：从概率最高的 K 个候选中随机采样，K 为固定值，候选池大小不随分布变化
- **Top-P（Nucleus Sampling）**：选取累积概率达到 P 的最小候选集，候选池大小随分布动态调整
- **Temperature**：通过调节 logits 的缩放系数控制分布的"尖锐度"，T 越高分布越平坦（更多样），T 越低分布越集中（更确定）

## Related Concepts
- [[TrainingPipeline]] — 训练阶段与解码策略的选择密切相关
- [[Transformer]] — Transformer 的解码器输出 logits 用于解码策略
