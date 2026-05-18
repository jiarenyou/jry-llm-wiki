---
title: "PyTorch初级：从Tensor到部署"
type: source
tags: [ai, pytorch, deeplearning, tutorial]
date: 2026-04-10
source_file: raw/杂记/pytorch初级.md
last_updated: 2026-05-18
---

## Summary
基于《Pytorch实用教程》第二版的学习笔记，系统覆盖PyTorch三大模块：基础（Tensor、数据加载、模型搭建与训练）、实战（MNIST手写数字分类完整代码）、部署（ONNX导出+TensorRT优化）。文章从Tensor与NumPy数组的区别（GPU加速+自动求梯度）讲起，到Dataset/DataLoader数据管道、nn.Module模型搭建、损失函数/优化器/训练循环，最后到ONNX蓝图导出和TensorRT三重优化（量化/图层融合/内核自动调整）。

## Key Claims
- Tensor相比NumPy数组的核心优势：GPU加速计算 + 自动求梯度（Autograd）
- torch.from_numpy()共享内存高效处理大数据，torch.tensor()复制数据更安全
- PyTorch数据管道：Dataset定义数据（__len__ + __getitem__），DataLoader处理批次/洗牌/并行加载
- 模型搭建：继承nn.Module，__init__定义层，forward定义数据流；"__init__负责买零件，forward负责组装"
- 训练循环五步：zero_grad -> forward -> loss -> backward -> step
- 优化器演进路线：SGD（蒙眼下坡） -> Momentum（惯性冲过局部最优） -> Adam（自适应学习率）
- 部署路径：PyTorch模型 -> ONNX通用蓝图 -> TensorRT优化引擎
- TensorRT三大优化：精确校准（量化FP32->FP16/INT8）、图层融合（减少GPU核间切换）、内核自动调整（针对特定GPU选最快实现）

## Key Quotes
> "Tensor与NumPy数组最根本的区别是Tensor能够给深度学习提供GPU计算和自动求梯度的能力" -- Tensor核心价值

> "__init__负责'买零件'，forward负责'组装'" -- PyTorch模型搭建范式

> "PyTorch模型 -> ONNX蓝图 -> 优化的TensorRT引擎" -- 部署工作流

## Connections
- [[PyTorch]] -- PyTorch框架概念页
- [[TrainingPipeline]] -- 训练管线概念页
- [[LinearTransformation]] -- 神经网络层的本质是线性变换+激活函数
- [[ModelQuantization]] -- TensorRT量化部署与模型量化概念相关
- [[Transformer]] -- PyTorch是实现Transformer的基础工具
- [[FineTuning]] -- PyTorch训练循环是微调的基础

## Contradictions
