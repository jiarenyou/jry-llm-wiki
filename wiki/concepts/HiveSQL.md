---
title: "HiveSQL"
type: concept
tags: [big-data, sql, hive]
sources:
  - hive-sql-syntax-guide
  - data-warehouse-modeling-core
  - data-warehouse-modeling-methodology
last_updated: 2026-05-18
---

# HiveSQL

## Definition
Hive SQL（HiveQL）是Apache Hive提供的类SQL查询语言，用于在大数据平台（Hadoop生态）上进行数据查询和分析。它是数据仓库开发的基础工具，将SQL语句翻译为MapReduce/Tez/Spark作业执行。

## Core Capabilities
- **DDL**：数据库/表的创建、删除、修改（支持内部表、外部表、分区表、分桶表）
- **DML**：数据加载（LOAD DATA、INSERT SELECT）、数据导出
- **DQL**：SELECT查询、JOIN连接、GROUP BY聚合、UNION联合
- **数据类型**：原始类型（INT/BIGINT/STRING/TIMESTAMP等）+ 复杂类型（ARRAY/MAP/STRUCT）

## Key Features
- **分区表**：通过PARTITIONED BY实现分区裁剪，大幅减少扫描数据量
- **分桶表**：通过CLUSTERED BY实现，支持Bucket-Map Join避免Shuffle
- **外部表**：EXTERIAL TABLE，删除时不删HDFS数据
- **虚拟列**：INPUT__FILE__NAME、BLOCK__OFFSET__INSIDE__FILE等，用于数据追踪
- **Sampling**：TABLESAMPLE支持随机桶抽取和数据块抽取

## Built-in Functions
- 数值函数：round、rand、abs
- 集合函数：size、array_contains、map_keys、map_values
- 类型转换：cast、binary
- 日期函数：current_timestamp、year/month/day、datediff、date_add

## Complex Types
| Type | Definition | Access | Functions |
|------|-----------|--------|-----------|
| ARRAY | array<type> | array[index] | size, array_contains, sort_array |
| MAP | map<keyType, valueType> | map[key] | size, map_keys, map_values |
| STRUCT | struct<col1 type, col2 type> | struct.colName | - |

## ETL Pattern
```sql
-- Load data
LOAD DATA INPATH '/path' INTO TABLE target PARTITION(dt='2024-01-01');
-- Transform and insert
INSERT OVERWRITE TABLE dwd_table PARTITION(dt)
SELECT *, clean_logic(col) FROM ods_table WHERE conditions;
```

## Related Concepts
- [[DataWarehouse]] -- Hive SQL是数仓ETL开发的核心语言
- [[DataSkew]] -- Hive SQL中GROUP BY/JOIN同样面临数据倾斜问题
- [[SparkPerformance]] -- Spark SQL与Hive SQL的性能优化策略相通
