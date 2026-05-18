---
title: "数据压缩"
type: source
tags: [big-data, storage]
date: 2026-04-10
source_file: raw/杂记/数据压缩.md
last_updated: 2026-05-18
---

## Summary
以IoT场景（每日2TB压缩到400GB，压缩率1:5）为例，深入解析大数据压缩的原理。核心是列式存储（Parquet/ORC）与多种压缩编码（字典编码、增量编码、RLE、位打包、帧偏移编码）的组合。列式存储将同类型高相似性数据物理聚集，再通过针对性编码和通用压缩算法层层"瘦身"。

## Key Claims
- 列式存储是高压缩比的基础：同列数据类型一致、重复性高、规律性强
- 字典编码将字符串替换为短整数，是压缩device_id等列的主力
- 增量编码存储相邻值的差值，是压缩timestamp等单调递增列的核心
- 编码是压缩比的核心功臣，通用压缩（Snappy/Zstd）是锦上添花
- 列式格式避免了行式格式中每条记录的结构信息冗余
- IoT数据特性（设备ID重复、时间戳递增、传感器值缓变）是高压缩比的内因

## Key Quotes
> "列式存储是基础，编码是关键，通用压缩是最后一步。"

> "从2TB原始数据压缩到400GB的HDFS存储，正是列式存储（Parquet/ORC等）巧妙地利用了IoT数据的强规律性和重复性，通过一系列针对性的编码和高效的通用压缩算法，层层'瘦身'后的必然结果。"

## Connections
- [[ColumnarStorage]] -- 列式存储是数据压缩效率的基础
- [[DataCompression]] -- 本文是数据压缩概念的核心来源
- [[SparkPerformance]] -- 压缩选择影响Spark的I/O和内存效率

## Contradictions
