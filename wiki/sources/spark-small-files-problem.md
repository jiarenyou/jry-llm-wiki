---
title: "Spark小文件问题"
type: source
tags: [big-data, spark, performance]
date: 2026-04-10
source_file: raw/杂记/spark性能优化3：小文件问题.md
last_updated: 2026-05-18
---

## Summary
系统分析Spark中小文件问题的成因、危害和解决方案。小文件（远小于HDFS块大小128MB/256MB）会带来NameNode内存压力、任务调度效率低下、存储浪费和网络I/O开销。解决方案涵盖源头预防（DISTRIBUTE BY、调整并行度）、写入阶段自动合并、事后合并（repartition/coalesce）以及Spark 3.0+ AQE自适应优化。

## Key Claims
- 小文件导致四大危害：NameNode内存压力、任务调度低效、存储浪费、网络I/O增大
- 成因包括：过度动态分区、Task/Reduce数量过多、Spark Streaming微批处理、频繁INSERT OVERWRITE
- spark.sql.mergeSmallFiles.enabled=true可在写入时自动合并小文件
- Spark 3.0+的AQE可运行时动态调整Shuffle分区数并自动合并过小分区
- 优先使用Parquet/ORC列式格式搭配Snappy/Zstd压缩

## Key Quotes
> "每个小文件在Spark中通常对应一个Task。启动Task、分配资源、执行短任务等操作本身就有开销。任务启动与调度时间远超实际计算时间。"

## Connections
- [[SparkPerformance]] -- 小文件问题是Spark性能优化的重要子课题
- [[DataCompression]] -- 压缩后文件更小可能加剧小文件问题
- [[DataWarehouse]] -- 数仓中的动态分区写入是小文件的主要来源之一

## Contradictions
