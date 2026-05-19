---
title: "Industrial Data Security"
type: source
tags: [smart-manufacturing]
date: 2026-05-18
source_file: raw/智能制造/工业数据安全.md
last_updated: 2026-05-19
---

## Summary

Industrial data security addresses the challenges arising from OT/IT network convergence in smart manufacturing, where previously air-gapped industrial control systems (PLC, DCS, SCADA) are now exposed to cyber threats. Security revolves around three core principles -- confidentiality, integrity, and availability -- with availability and integrity prioritized over confidentiality in industrial settings. The defense-in-depth strategy follows ISA-95 and IEC 62443 standards with layered protection from field devices through control, execution, management, and cloud levels. Compliance with China's Level Protection 2.0 (Grade 3) is standard for manufacturing enterprises.

## Key Claims

- OT/IT convergence introduces risks: attackers penetrating from IT to OT networks to control PLCs, ransomware encrypting MES databases, competitors stealing process parameters, and insider threats accessing sensitive production data.
- Data masking strategies differ by type: numerical noise for process parameters, name masking for employee data, code substitution for supplier information, and range fuzzing for equipment parameters, with static masking for dev/test and dynamic masking for API layers.
- Access control follows ISA-95 organizational hierarchy with role-based permissions, factory-workshop-line data scope restrictions, fine-grained functional permissions, and time-limited temporary access, all backed by comprehensive audit logging with 180-day retention.

## Connections

- [[DataWarehouse]] -- security policies govern warehouse access, with dynamic masking at the API layer protecting sensitive production data
- [[DataGovernance]] -- security is a core pillar of data governance, covering access policies, audit trails, and compliance requirements
- [[RAG]] -- security-aware RAG systems must respect access control boundaries when retrieving sensitive manufacturing data
