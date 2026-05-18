---
title: "Hive SQL语法大全"
type: source
tags: [big-data, sql, hive]
date: 2026-04-10
source_file: raw/杂记/Hive-SQL语法大全.md
last_updated: 2026-05-18
---

## Summary
Hive SQL的完整语法参考手册，覆盖数据库操作（CREATE/DROP/ALTER）、表操作（内外部表、分区、分桶）、数据类型（原始类型+ARRAY/MAP/STRUCT复杂类型）、数据加载与导出、查询语法（RLIKE正则、UNION联合、Sampling采样、虚拟列）以及各类内置函数（数值、集合、转换、日期）。包含社交案例的完整ETL实践。

## Key Claims
- Hive支持内部表和外部表（EXTERNAL），外部表删除时不删除HDFS数据
- 分区表通过PARTITIONED BY实现，分区裁剪可大幅减少扫描数据量
- 分桶表通过CLUSTERED BY实现，需要设置hive.enforce.bucketing=true
- LOAD DATA用于加载文件到表，INSERT SELECT用于从其他表导入数据
- Hive虚拟列可查看数据行的文件位置和偏移量
- 复杂类型：array支持索引访问和size/array_contains函数，map支持key-value操作

## Key Quotes
> "分桶表无法使用LOAD DATA进行数据加载，必须使用INSERT SELECT并指定CLUSTER BY。"

## Connections
- [[HiveSQL]] -- 本文是HiveSQL概念的核心参考资料
- [[DataWarehouse]] -- Hive SQL是数仓开发的基础工具
- [[DataSkew]] -- Hive中GROUP BY/JOIN同样面临数据倾斜问题

## Contradictions
