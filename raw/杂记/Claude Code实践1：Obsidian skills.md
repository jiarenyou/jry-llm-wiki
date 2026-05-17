---
title: Claude Code实践1：Obsidian skills
draft: false
tags:
  - AI
---

![image.png](https://jry-img-file.oss-cn-beijing.aliyuncs.com/my_picture_file/202601090745508.png)

最近， Obsidian CEO (Kepano/Steph Ango) 开源的一个项目：[ **obsidian-skills**](https://github.com/kepano/obsidian-skills) 是，它的核心定位是 **“让 AI（特指 Claude Code 等编程/Agent 工具）真正学会如何操作 Obsidian”**。![image.png](https://jry-img-file.oss-cn-beijing.aliyuncs.com/my_picture_file/202601090750485.png)
我认为这更加方便了个人知识管理，obsidian存储的一般都是高质量、结构化清晰的知识，但由于我们使用时间越长，文件管理的混乱程度也就越大，耗费了我们大量的时间去管理，而现在obsidian skills的出现，连通了obsdian与claude code，能够像管理项目，整理代码等工作可以交给AI来做，做的比我们效率更高，质量更好。就相当于把知识管理很大一部分重复性、没有创造性的工作外包给了AI，能够把精力时间放到创意、决策上。

下面了解下obsidian skills项目

简单来说，这是一个专门为 AI Agent 准备的“技能包”或“说明书”，旨在让 AI 能够像 Obsidian 专家一样读写你的笔记和文件。
# Obsidian skills
## 1. 它的核心作用是什么？

这个仓库包含了一组 **MCP (Model Context Protocol) 技能** 或提示词规则，专门用于教导 AI（主要是 Claude Code）理解和生成符合 Obsidian 标准的文件格式。

它主要赋予了 AI 三项核心能力（Skills）：

- **Obsidian Markdown**: 让 AI 学会写 Obsidian 风格的 Markdown（例如使用双链 `[[Link]]` 而不是标准链接，正确使用 Callouts `[!note]`，正确处理 Frontmatter 属性）。
    
- **Obsidian Bases**: 让 AI 能够创建和编辑 `.base` 文件（这通常涉及 Obsidian 的数据库类视图、过滤器、公式等高级配置）。
    
- **JSON Canvas**: 让 AI 能够理解并生成 `.canvas` 无限画布文件（通过代码生成节点、连线和分组）。
    

## 2. 它解决了什么痛点？

在使用通用 AI（如 ChatGPT、Claude 网页版）辅助 Obsidian 笔记时，用户通常会遇到以下几个非常割裂的痛点，而这个项目就是为了解决它们：

- **痛点一：AI 不懂“Obsidian 方言” (语法格式错误)**
    
    - **问题**: 通用 AI 默认输出标准 Markdown。当你让它“整理笔记”时，它会给你 `[链接](URL)` 格式，而不是 Obsidian 核心的 `[[双向链接]]`。它可能不懂 Obsidian 的 Callouts 语法，或者生成的 Mermaid 图表很难看。
        
    - **解决**: 这个技能包“教会”了 AI 必须使用 `[[wikilinks]]`，如何正确配置 YAML Frontmatter（元数据），以及如何使用 Obsidian 特有的语法糖。
        
- **痛点二：复杂文件无法手写 (自动化生成 Canvas/数据库)**
    
    - **问题**: `.canvas` (画布) 和 `.base` (数据库视图) 的底层是复杂的 JSON 或 YAML 数据。人类几乎不可能手动编写这些代码，通用 AI 也因为缺乏训练数据而经常写错结构。
        
    - **解决**: 该项目提供了精确的 Schema 定义。你可以直接对 AI 说：“帮我把这篇长文整理成一个逻辑清晰的 Canvas 导图”，AI 就能直接生成一个可以在 Obsidian 里完美打开的 `.canvas` 文件，包含节点和连线。
        
- **痛点三：配置高级功能门槛高 (省去折腾时间)**
    
    - **问题**: 如果你想在 Obsidian 里配置一个“阅读清单”数据库，可能需要学习复杂的插件语法、编写过滤公式。
        
    - **解决**: 有了这个技能包，你可以直接用自然语言告诉 AI：“建一个追踪我看过电影的数据库视图，按年份筛选”，AI 就能自动生成带有正确过滤器和公式的配置文件。
        


**Obsidian Skills** 是打通 **AI 编程助手** 与 **Obsidian 本地笔记库** 的一座桥梁。

它让 AI 从一个“只会写普通文本的外部工具”，变成了一个“懂 Obsidian 内部结构、能帮你画图、建库、整理双链的**原生助手**”。对于希望通过 AI 深度自动化管理 Obsidian 库的高级用户来说，这是一个非常重要的基础设施。

# 实践
登录到claude后，直接告诉它帮我安装obsidian skills，即可自动安装，直至能够使用，

![image.png](https://jry-img-file.oss-cn-beijing.aliyuncs.com/my_picture_file/202601101631925.png)


我们知道claude skills采用的是**渐进式披露**， 在我输入指令中有canvas后，自动识别到canvas，启动json-canvas技能
![image.png](https://jry-img-file.oss-cn-beijing.aliyuncs.com/my_picture_file/202601101635265.png)

此图是经过json-canvas处理后的画板，如果我手动画这么一张图耗费的功夫太长，可能我还没有它排版设计的好
![image.png](https://jry-img-file.oss-cn-beijing.aliyuncs.com/my_picture_file/202601101650928.png)

## 相关笔记
- 续篇参见[[Claude Code实践2：《The complete claude code tutoria》阅读心得]]，深入探讨了Claude Code的高效使用方法论
