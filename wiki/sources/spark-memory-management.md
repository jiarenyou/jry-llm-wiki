---
title: "Spark内存管理"
type: source
tags: [big-data, spark, performance]
date: 2026-04-10
source_file: raw/杂记/spark性能优化6：内存管理.md
last_updated: 2026-05-18
---

## Summary
深度解析Spark Executor JVM的内存模型：Reserved Memory、User Memory、Spark Memory（Execution+Storage）和Off-Heap Memory。详解统一内存管理的动态借用机制（Execution优先于Storage）、核心参数调优（memory.fraction、storageFraction、offHeap）、代码层面的序列化优化和缓存策略，以及OOM诊断方法。

## Key Claims
- Executor内存分为四区域：Reserved（约300MB不可用）、User（用户代码对象）、Spark Memory（执行+存储）、Off-Heap（Tungsten堆外）
- 统一内存管理核心：Execution Memory可借用Storage Memory空闲部分，Execution优先级高于Storage
- Kryo序列化比Java默认序列化速度提升10倍，数据体积减少
- reduceByKey替代groupByKey实现Map端预聚合，大幅减少Shuffle数据量
- MEMORY_AND_DISK是推荐的缓存级别，兼顾性能与安全
- GC Time占Task总时间10%以上需优化内存分配或代码

## Key Quotes
> "Spark的内存管理是一个动态平衡的过程。它需要在减少溢写/磁盘I/O（需要更多内存）和减少GC压力（需要更少对象、更少内存）之间找到最佳平衡点。"

## Connections
- [[SparkPerformance]] -- 内存管理是Spark性能优化的核心战场
- [[DataCompression]] -- 内存优化与数据压缩策略密切相关
- [[DataSkew]] -- 数据倾斜导致单个Task内存暴增是OOM的常见原因

## Contradictions
