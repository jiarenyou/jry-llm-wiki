---
title: "Spark资源配置与并行度优化"
type: source
tags: [big-data, spark, performance]
date: 2026-04-10
source_file: raw/杂记/spark性能优化5：资源配置与并行度优化.md
last_updated: 2026-05-18
---

## Summary
详解Spark Executor资源配置（数量、核数、内存）与并行度参数（spark.default.parallelism、spark.sql.shuffle.partitions）的调优方法。提供中小规模和大规模场景的spark-submit命令示例，以及静态分配vs动态分配的选择策略。核心原则：并行度设为总CPU核数的2-3倍，每个Task目标处理数据量128MB-256MB。

## Key Claims
- Executor推荐配置：2-5核、6-10GB内存，总数10-100个
- spark.default.parallelism用于RDD操作，spark.sql.shuffle.partitions用于SQL/Shuffle操作（默认200）
- 动态分配（spark.dynamicAllocation.enabled=true）适合多租户、资源波动大的集群
- 并行度公式：min(总数据量/每个Task目标数据量, 总Executor核心数*2-3)
- 小数据集spark.sql.shuffle.partitions可设100-200，大数据集TB级应设500-1000+
- spark.memory.fraction默认0.6，Shuffle/Join重时可调至0.7-0.8

## Key Quotes
> "没有'银弹'配置。最优配置取决于你的数据量、计算复杂度、集群资源和具体作业特性。务必通过监控和实验来找到最佳平衡点。"

## Connections
- [[SparkPerformance]] -- 资源配置是Spark性能优化的基础
- [[DataSkew]] -- 大规模数据倾斜场景需要特殊资源配置策略
- [[DataWarehouse]] -- 数仓ETL作业是Spark资源配置的典型应用场景

## Contradictions
