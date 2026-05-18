---
title: "XTuner"
type: entity
tags: [ai, tools, finetuning]
sources: [xtuner-quickstart]
last_updated: 2026-05-18
---

## Overview
XTuner是由上海人工智能实验室（OpenMMLab）开发的大语言模型微调工具库。核心设计理念是"用一个配置文件搞定一切"，通过命令行驱动和配置驱动简化微调流程。

## Key Features
- **配置文件驱动**：所有训练设置集中在.py配置文件中，清晰可复用
- **丰富算法支持**：全量微调、LoRA、QLoRA
- **广泛模型支持**：InternLM、Llama、Mistral、Qwen、ChatGLM、Baichuan等
- **高性能**：集成FlashAttention、Triton Kernels、DeepSpeed
- **生态联动**：与LMDeploy（部署）、OpenCompass（评测）无缝衔接

## Core Commands
- `xtuner list-cfg` -- 列出所有内置配置
- `xtuner copy-cfg` -- 复制配置文件
- `xtuner train` -- 启动微调训练
- `xtuner convert pth_to_hf` -- 适配器格式转换
- `xtuner convert merge` -- 合并适配器与基础模型
- `xtuner chat` -- 与模型对话

## Resources
- GitHub: https://github.com/InternLM/xtuner
- Docs: https://xtuner.readthedocs.io/zh-cn/latest/

## Relationships
- [[FineTuning]] -- XTuner是微调工具库
- [[LoRA]] -- XTuner支持LoRA适配方法
- [[QLoRA]] -- XTuner支持QLoRA量化适配方法
- [[FlashAttention]] -- XTuner集成FlashAttention优化
- [[PyTorch]] -- XTuner基于PyTorch生态

## Sources
- [[xtuner-quickstart]] -- XTuner快速上手指南
