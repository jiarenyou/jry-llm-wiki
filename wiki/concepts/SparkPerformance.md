---
title: "SparkPerformance"
type: concept
tags: [big-data, spark, performance]
sources:
  - spark-performance-optimization-panorama
  - spark-wide-narrow-dependency-optimization
  - spark-small-files-problem
  - spark-data-skew
  - spark-resource-parallelism-optimization
  - spark-memory-management
  - performance-optimization-three-layers
last_updated: 2026-05-18
---

# SparkPerformance (Spark性能优化)

## Definition
Spark性能优化是一套系统化的方法论和实践技术，旨在提升Apache Spark作业的执行效率、稳定性和资源利用率。覆盖资源配置、内存管理、Shuffle优化、代码与算子优化、数据序列化与格式、JVM/GC调优七大方向。

## Key Dimensions
- **资源配置与并行度**：Executor数量/核数/内存配置，spark.default.parallelism和spark.sql.shuffle.partitions调优
- **内存管理**：Reserved/User/Spark Memory三区域，统一内存管理动态借用机制，堆外内存利用
- **Shuffle优化**：宽窄依赖集中处理减少Shuffle次数，缓冲区调优，文件合并
- **数据倾斜处理**：两阶段聚合、Broadcast Join、随机前缀打散、AQE自动处理
- **小文件问题**：源头预防、写入自动合并、事后repartition/coalesce合并
- **序列化与格式**：Kryo序列化（性能提升10倍）、Parquet/ORC列式存储

## Optimization Roadmap
1. 打开Spark Web UI诊断瓶颈（慢Stage、数据倾斜、GC时间）
2. 优先调整参数（成本低见效快）
3. 优化代码与算子（reduceByKey替代groupByKey等）
4. 处理数据倾斜（简单优先，渐进式优化）

## Related Concepts
- [[DataSkew]] -- 数据倾斜是Spark性能的头号杀手
- [[ColumnarStorage]] -- 列式存储格式影响I/O效率
- [[DataCompression]] -- 压缩选择影响存储和计算效率
- [[HiveSQL]] -- Spark SQL与Hive SQL的性能优化有共通之处
