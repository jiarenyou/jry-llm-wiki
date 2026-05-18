---
title: "DataSkew"
type: concept
tags: [big-data, spark, performance]
sources:
  - spark-data-skew
  - performance-optimization-three-layers
  - spark-performance-optimization-panorama
last_updated: 2026-05-18
---

# DataSkew (数据倾斜)

## Definition
数据倾斜（Data Skew）是分布式计算中数据在各分区/任务间分布不均衡的现象。最直接的后果是：大部分Task迅速完成，但少数Task处理的数据量异常巨大，执行时间极长甚至OOM失败，像木桶的短板决定了整体容量。

## Root Cause
数据倾斜本质上发生在**Shuffle过程**中。当某个Key的数据量远超其他Key时，哈希分区策略会将该Key的所有数据分配到同一个分区，由同一个Task处理，该Task成为瓶颈。

## Typical Symptoms
1. **Task执行极慢**：99%的Task在数秒/分钟内完成，1-3个Task执行数小时
2. **Task频繁OOM**：倾斜Task所需内存超过Executor容量

## Solution Hierarchy (Simple First)
1. **提高Shuffle并行度**（最简单，调spark.sql.shuffle.partitions）
2. **过滤异常Key**（如NULL、-1等无意义值，有损但立竿见影）
3. **两阶段聚合**（局部聚合加盐 -> 全局聚合去盐，适用于GROUP BY）
4. **Broadcast Join**（小表广播避免Shuffle，适用于大小表Join）
5. **随机前缀+扩容**（打散倾斜Key，适用于大表Join大表）
6. **AQE自动处理**（Spark 3.0+，运行时自动检测并拆分倾斜Partition）

## Two-Stage Aggregation Example
```
// Stage 1: Local aggregation with random salt
saltedRdd = rdd.map(key => (randomPrefix + "_" + key, 1)).reduceByKey(_ + _)
// Stage 2: Global aggregation, remove salt
aggregatedRdd = saltedRdd.map(removePrefix).reduceByKey(_ + _)
```

## Salting for Join
- Large table: randomize skewed Key to N variants (-1_0 to -1_99)
- Small table: replicate that row N times with matching keys
- Each task now handles ~1/N of the skewed data

## Related Concepts
- [[SparkPerformance]] -- 数据倾斜是Spark性能的头号杀手
- [[DataWarehouse]] -- 数仓中的动态分区和大数据表是数据倾斜的高发场景
- [[HiveSQL]] -- Hive中GROUP BY/JOIN同样面临数据倾斜
