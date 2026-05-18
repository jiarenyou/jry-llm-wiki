---
title: "Swift框架中swift_output输出的是什么"
type: source
tags: [ai, llm, finetuning, lora, tools]
date: 2026-04-10
source_file: raw/杂记/swift框架中swift_output输出的是什么.md
last_updated: 2026-05-18
---

## Summary
解释SWIFT微调框架中swift_output文件夹的内容本质：它存储的是轻量级适配器（Adapter）或增量权重，而非完整模型。通过"百科全书原著+附录"的比喻说明适配器与基础模型的关系，并详细解释合并（Merge）的两大目的：部署推理（简化流程+提升性能）和后续处理分发。总结"训练时分离，部署时合并"的PEFT标准实践流程。

## Key Claims
- swift_output存储的是LoRA适配器/增量权重（几十到几百MB），不是完整模型（几十GB）
- 微调时冻结99.9%基础模型参数，只训练0.1%的增量参数
- 适配器无法独立工作，必须与基础模型结合使用
- 合并的两种方式：加载时合并（推理时动态结合）和物理合并（预先合并为完整模型）
- 合并目的：简化部署流程、提升推理性能、方便模型共享、作为新基础模型进行二次微调
- "训练时分离，部署时合并"是PEFT方法的标准实践

## Key Quotes
> "基础模型就像百科全书原著，适配器就像附录/勘误表，附录里的内容只有结合原著才有意义" -- 适配器的本质

> "训练时分离，部署时合并是使用LoRA等PEFT方法进行大模型微调的一个标准且高效的实践流程" -- PEFT标准范式

## Connections
- [[LoRA]] -- swift_output中的适配器就是LoRA低秩适配权重
- [[QLoRA]] -- QLoRA适配器同样是增量权重
- [[FineTuning]] -- 适配器是PEFT微调方法的核心产物
- [[ModelQuantization]] -- 量化与适配器是互补的优化方向

## Contradictions
