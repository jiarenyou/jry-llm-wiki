---
title: "性能优化三层框架"
type: source
tags: [big-data, spark, performance, sql]
date: 2026-04-10
source_file: raw/杂记/性能优化.md
last_updated: 2026-05-18
---

## Summary
性能优化的三层系统框架：数据源头层（文件格式、压缩、分区、分桶）、SQL语句层（过滤逻辑、连接逻辑、聚合操作）、计算引擎层（内存管理、并行度调优、AQE）。三层环环相扣，数据源层的存储组织方式直接影响SQL执行效率和引擎资源配置。文章详细介绍了列式存储的谓词下推、分区裁剪、分桶避免Shuffle、广播连接、排序合并连接、两阶段聚合、加盐打散等核心技术。

## Key Claims
- 三层优化环环相扣：数据源组织方式决定SQL执行效率，SQL写法影响引擎资源需求
- 列式存储（Parquet/ORC）通过谓词下推实现高效I/O，只读取需要的列
- 分区裁剪（Partition Pruning）实现零I/O，查询性能提升是指数级的
- 分桶（Bucketing）预先按Join Key分好数据，可完全避免Shuffle
- 小表关联大表用Broadcast Join（Map-Side Join），大表关联大表用Sort-Merge Join
- 大表Join数据倾斜：随机化大表Key（加盐打散）+ 复制小表数据（Replicate）
- GROUP BY数据倾斜：两阶段聚合（局部聚合+全局聚合），类比"地方选举计票"
- Spark 3.0+ AQE可利用直方图统计信息自动识别和处理数据倾斜

## Key Quotes
> "性能调优是一个环环相扣的综合过程。如果数据源没有存储好，还是调不到一个更优的性能。"

> "从手动优化聊到了自动优化，底层的原理都是相通的，就是识别倾斜 -> 打散倾斜。"

## Connections
- [[SparkPerformance]] -- 三层框架是Spark性能优化的系统方法论
- [[DataSkew]] -- Join和GROUP BY的数据倾斜解决方案是本文重点
- [[ColumnarStorage]] -- 列式存储是数据源头层优化的核心
- [[DataWarehouse]] -- 分区分桶是数仓建模的物理实现手段

## Contradictions
