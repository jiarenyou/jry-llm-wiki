---
title: "数据服务与API层"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/数据服务与API层.md
last_updated: 2026-05-19
---

## Summary
介绍工厂数据平台中数据服务层的设计，包括指标API分层（实时指标API和历史指标API）、RESTful设计规范、指标注册中心、报表服务（日报/周报/月报的自动生成与分发）、看板技术选型（Grafana/Superset/自研）、数据服务治理（RBAC权限控制、限流熔断、版本管理、监控日志），以及四阶段实施路径。

## Key Claims
- API层的核心价值是解耦数据生产与消费、统一数据口径，避免各部门"各自计算、数字打架"
- 指标API按时效性分两类：实时API（<500ms，WebSocket推送）和历史API（<2s）
- 看板推荐组合：Grafana（车间操作看板）+ 自研React/ECharts（管理驾驶舱）+ Superset（数据分析平台）
- 权限模型采用RBAC，角色定义参考ISA-95的组织层级
- 服务治理包括限流策略、熔断机制、超时设置、版本管理和调用监控

## Connections
- [[工厂数据平台总体架构]] — API层是数据平台的"门面"，连接数据与业务应用
- [[工厂数据仓库建模]] — ADS层数据通过API层对外暴露
- [[实时数据流水线]] — 实时指标API的数据来自实时流水线的产出
- [[工厂主数据管理]] — 维度权限与主数据关联
- [[ISA-95参考架构]] — 权限模型参考ISA-95组织层级
