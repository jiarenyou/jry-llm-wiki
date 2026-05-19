---
title: "Visual Quality Inspection"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/视觉质检.md
last_updated: 2026-05-19
---

## Summary

Visual quality inspection (Automated Visual Inspection) uses computer vision to automatically detect surface defects, dimensional deviations, and assembly errors, replacing or augmenting human inspection. The technology has evolved from rule-based traditional CV through deep learning (YOLO/ResNet) to large vision foundation models (SAM/GPT-4V), with each stage trading off flexibility, annotation requirements, and inference cost. The end-to-end pipeline covers data acquisition (industrial cameras, structured lighting), annotation, model training, edge deployment (TensorRT/ONNX), and MES/QMS integration.

## Key Claims

- Defect sample scarcity (normal products exceed 99%) and long-tail distribution are the primary data challenges, addressed via data augmentation, GANs, few-shot learning, and tiered detection strategies.
- Edge deployment demands inference latency under 100ms per image, requiring model quantization and optimized runtimes on industrial PCs or Jetson devices.
- Detection results feed back into MES and QMS systems, and aggregate into the data warehouse for trend analysis and yield optimization.

## Connections

- [[DataWarehouse]] -- inspection results are aggregated into the warehouse for cross-batch defect trend analysis
- [[RAG]] -- vision-language models could use RAG to match detected defects against historical corrective actions
- [[DataSkew]] -- the severe class imbalance in defect vs. normal samples is analogous to data skew in distributed computing
