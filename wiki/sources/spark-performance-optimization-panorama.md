---
title: "Spark性能优化全景图"
type: source
tags: [big-data, spark, performance]
date: 2026-04-10
source_file: raw/杂记/spark性能优化1：性能优化全景图.md
last_updated: 2026-05-18
---

## Summary
Spark性能优化的全景式指南，覆盖资源配置与并行度、内存管理与OOM、Shuffle过程优化、代码与算子优化、数据序列化与格式、JVM与GC调优七大方向。文章提供了完整的排查路线图：从Spark Web UI诊断到参数调整再到代码重构的渐进式优化策略。

## Key Claims
- Spark性能问题可归为七大类：资源配置、内存管理、Shuffle瓶颈、代码效率、序列化/格式、JVM/GC、数据倾斜
- 并行度推荐设为集群总CPU核数的2-3倍，spark.sql.shuffle.partitions默认200对大数据集往往不够
- 优先调整参数后修改代码，参数调整成本低、见效快
- Kryo序列化比Java默认序列化性能提升约10倍
- G1GC是大多数Spark工作负载的最佳GC算法选择
- 数据倾斜是许多性能问题的"万恶之源"，应优先解决

## Key Quotes
> "面对一个Spark性能问题，首先打开Spark Web UI，从Jobs -> Stages下找到耗时的Stage，深入查看其Tasks的分布（是否有数据倾斜）、Shuffle Read/Write量、GC时间等，从而定位根本原因。"

> "优化往往需要权衡。例如，增加并行度可能提高并发，但也增加调度开销；增大缓冲区可能减少I/O，但也增加内存压力。"

## Connections
- [[SparkPerformance]] -- 本文是Spark性能优化全景图的核心来源
- [[DataSkew]] -- 数据倾斜是Spark性能的头号杀手
- [[ShuffleOptimization]] -- Shuffle优化是性能提升的关键环节
- [[ColumnarStorage]] -- 推荐使用Parquet/ORC列式存储格式

## Contradictions
