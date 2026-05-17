---
title: "解码策略：从贪心到采样"
type: source
tags: [llm-course]
date: 2026-04-09
source_file: raw/领域/LLM张老师/02-解码策略.md
last_updated: 2026-05-18
---

## Summary
本课系统讲解了大语言模型的解码策略，从最基础的贪心解码到Beam Search，再到引入随机性的Top-K和Top-P采样，以及温度参数对生成分布的调控作用。课程通过HuggingFace Transformers库和GPT-2模型进行实战演示，直观展示不同策略对生成文本多样性与连贯性的影响。核心观点是没有万能的最优解码策略，选择取决于具体应用场景。

## Key Claims
- 贪心解码（Greedy Decoding）每步选概率最高的token，容易产生重复且缺乏多样性
- Beam Search维护k个候选序列，比贪心更优但仍偏向高频表达，适合翻译等确定性任务
- Top-K采样从概率最高的K个token中随机采样，K值过小退化为贪心、过大则引入噪声
- Top-P（核采样）动态选择累积概率达到P的最小token集合，比Top-K更自适应
- 温度（Temperature）控制softmax分布的尖锐程度，高温更随机、低温更确定
- 创意写作适合高温度+Top-P，代码生成适合低温度+贪心或Beam Search

## Key Quotes
> "贪心搜索就像一个人永远只选最安全的路走——走出来的路很稳，但风景很单调。" -- 解释贪心解码的局限性

> "温度参数就像是给模型的'创意旋钮'——往左拧更保守，往右拧更疯狂。" -- 比喻温度参数的作用

> "没有免费的午餐：多样性和确定性是一对永恒的矛盾。" -- 总结解码策略的核心权衡

## Connections
- [[DecodingStrategy]] — 本课核心主题，多种解码策略的对比与选择
- [[Transformer]] — 解码策略应用于Transformer的解码器输出

## Contradictions
