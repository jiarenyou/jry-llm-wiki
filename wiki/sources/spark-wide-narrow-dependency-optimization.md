---
title: "Spark宽窄依赖优化"
type: source
tags: [big-data, spark, performance]
date: 2026-04-10
source_file: raw/杂记/spark性能优化2：宽窄依赖优化.md
last_updated: 2026-05-18
---

## Summary
通过将宽依赖（触发Shuffle）和窄依赖（流水线执行）操作分别集中处理，可显著减少Shuffle次数并提升Spark作业性能。实践案例表明，仅通过操作顺序重组，任务执行时间从42分钟减少到23分钟，提升约45%。结合Spark 3.x的AQE和广播连接可进一步优化。

## Key Claims
- 宽窄依赖交替执行会导致不必要的Shuffle开销、Stage划分过多、内存压力增大
- 将窄依赖优先集中形成流水线执行，宽依赖批量处理减少Shuffle次数
- 广播连接可将宽依赖Join转为窄依赖，彻底避免Shuffle
- 操作重组必须在不改变业务逻辑正确性的前提下进行
- 实际案例：10个操作（7宽3窄）重组后Shuffle次数从3次减少到2次，性能提升45%

## Key Quotes
> "按照业务逻辑顺序组织的转换操作，在执行时却效率低下。问题在于，当我们交替执行宽依赖和窄依赖操作时，Spark不得不频繁地进行Stage划分和数据Shuffle。"

> "性能优化永无止境，而宽窄依赖的合理利用为我们提供了一个简单却有效的切入点。"

## Connections
- [[SparkPerformance]] -- 宽窄依赖优化是Spark性能优化的关键策略之一
- [[ShuffleOptimization]] -- 减少Shuffle次数是宽窄依赖优化的核心目标
- [[DataSkew]] -- 广播连接可同时解决数据倾斜和宽依赖问题

## Contradictions
