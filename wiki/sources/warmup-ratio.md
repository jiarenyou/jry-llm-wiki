---
title: "warmup_ratio（预热比例）"
type: source
tags: [ai, training, hyperparameter]
date: 2026-04-10
source_file: raw/杂记/warmup_ratio (预热比例).md
last_updated: 2026-05-18
---

## Summary
解释大模型微调训练中warmup_ratio（预热比例）参数的含义、作用和取值策略。预热比例控制学习率从0逐渐增加到目标值的阶段占整个训练过程的比例，本质是让学习率在梯度最不稳定的初始阶段"温柔发力"，既避免被大梯度带崩（防爆炸），又避免被小梯度拖慢（防消失）。

## Key Claims
- warmup_ratio控制学习率预热阶段占整个训练的比例，一般取值0.01~0.2
- 预热应对三个问题：初始梯度不可靠、间接降低梯度爆炸风险、避免梯度消失时的参数停滞
- 较大warmup_ratio适合难训练模型，训练前期更稳定但初期进展慢
- 学习率是"控制梯度作用的开关"，warmup控制"开关的开启速度"
- 类比开车：刚启动时慢踩油门（小学习率），车速稳定后再加到正常速度（目标学习率）

## Key Quotes
> "梯度消失/爆炸是'梯度本身的问题'，而学习率是'控制梯度作用的开关'。warmup_ratio通过控制'开关的开启速度'，让学习率在梯度最不稳定的初始阶段'温柔发力'" -- warmup的本质

> "就像开车：刚启动时慢踩油门，就能避免急刹或失控；等车速稳定，再加到正常速度" -- warmup的直觉类比

## Connections
- [[TrainingPipeline]] -- warmup是训练管线中学习率调度的一部分
- [[FineTuning]] -- warmup在微调训练中尤其重要
- [[LoRA]] -- LoRA微调同样需要配置warmup参数
- [[Transformer]] -- Transformer训练中warmup是标准做法

## Contradictions
