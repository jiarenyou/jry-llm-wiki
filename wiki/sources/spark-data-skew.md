---
title: "Spark数据倾斜"
type: source
tags: [big-data, spark, performance]
date: 2026-04-10
source_file: raw/杂记/spark性能优化4：数据倾斜.md
last_updated: 2026-05-18
---

## Summary
数据倾斜是Spark作业性能的头号杀手，本质是Shuffle过程中数据在分区/任务间分布不均。文章提供了从定位（Spark Web UI诊断）、到解决（提高并行度、处理倾斜Key、优化Join策略、AQE自动处理）的完整决策树。核心方法包括：两阶段聚合（加盐+去盐）、Broadcast Join避免Shuffle、Spark 3.0+ AQE自动拆分倾斜Partition。

## Key Claims
- 数据倾斜发生在Shuffle过程中，某个Key数据量异常大导致对应Task成为瓶颈
- 表现为两类：Task执行极慢（少数Task耗时数小时）或Task频繁OOM
- 解决优先级：提高并行度（简单优先） -> 处理倾斜Key -> 优化Join策略 -> AQE自动处理
- 两阶段聚合：局部聚合加盐打散 -> 全局聚合去盐合并，适用于groupByKey/reduceByKey
- AQE在运行时自动识别倾斜Partition并拆分为多个子Partition并行处理
- Broadcast Join将小表广播到所有Executor，完全避免Shuffle

## Key Quotes
> "数据倾斜是Spark作业性能的头号杀手，但并非不可战胜。其核心是数据分布不均，主要发生在Shuffle过程。"

> "Execution Memory的优先级高于Storage Memory。计算任务是'实时'的，必须保证其内存需求；而缓存的数据可以被驱逐到磁盘。"

## Connections
- [[DataSkew]] -- 本文是数据倾斜概念的核心来源
- [[SparkPerformance]] -- 数据倾斜是Spark性能优化的核心挑战
- [[HiveSQL]] -- Hive SQL中GROUP BY/JOIN同样面临数据倾斜问题

## Contradictions
