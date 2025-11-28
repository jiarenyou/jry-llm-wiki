---
title: Xtuner：大模型微调快速上手
draft: false
tags:
  - AI
  - 微调
---
 
### 一、XTuner是什么？

简单来说，**XTuner 是一个轻量级、易于使用的、为大语言模型（LLM）设计的微调工具库**。

它由上海人工智能实验室（OpenMMLab）开发，是其强大AI工具生态（MMCV, MMEngine等）的一部分。它的核心设计理念是“**用一个配置文件搞定一切**”，让开发者和研究人员可以极大地简化微调流程。


### 二、为什么选择XTuner？（核心优势）

1.  **轻量且用户友好**：
    *   **命令行驱动**：你不需要编写复杂的训练脚本，大部分操作通过简单的命令行 `xtuner train ...` 就能完成。
    *   **配置驱动**：所有的训练设置（模型、数据集、优化器、学习率等）都集中在一个配置文件中，清晰明了，易于修改和复用。

2.  **丰富的算法和模型支持**：
    *   **微调算法**：支持全量参数微调（Full Fine-tuning）、LoRA、QLoRA（目前最流行的高效微调方法）等多种算法。
    *   **模型支持**：支持市面上几乎所有主流的开源大模型，如 InternLM、Llama 系列、Mistral、Qwen（通义千问）、ChatGLM、Baichuan 等。

3.  **高性能**：
    *   集成了 FlashAttention、Triton Kernels 等业界领先的优化技术，显著提升训练速度、降低显存占用。
    *   与 DeepSpeed 深度集成，轻松实现分布式训练。

4.  **生态联动**：
    *   **无缝衔接**：微调完成后，可以无缝对接到 **LMDeploy** 进行高性能推理部署，以及使用 **OpenCompass** 进行全面的模型评测。形成“**微调-评测-部署**”的全流程解决方案。

5.  **支持自定义**：
    *   虽然提供了大量预置的配置文件，但如果你想使用自己的数据集，XTuner 也支持多种格式（如JSONL），只需简单修改配置即可，非常灵活。

### 三、核心概念：配置文件（Config File）

这是理解XTuner的**钥匙**。一个典型的XTuner配置文件（以 `.py` 结尾）包含了微调所需的所有信息，它像一份“配方单”。

一个配置文件通常包含以下几个部分：

*   `model`: 定义你要微调的基础模型和微调方法（如LoRA）。
*   `dataset`: 定义你要使用的数据集、数据格式和预处理方式。
*   `optimizer` 和 `param_scheduler`: 定义优化器（如AdamW）和学习率策略。
*   `train_dataloader`, `val_dataloader`: 定义数据加载的方式。
*   `runner`: 运行时的设置，如训练轮次（epochs）、日志记录、模型保存等。

XTuner最棒的一点是，它内置了**大量预设好的配置文件**，覆盖了“不同模型 + 不同算法 + 不同数据集”的各种组合。你几乎总能找到一个与你需求相近的配置作为起点。

---

### 四、快速上手实战：用QLoRA微调InternLM2-1.8B模型

这个例子将带你用最少的资源（一张消费级显卡，如RTX 3060 12GB即可）微调一个模型，并与它对话。

#### 第0步：环境准备

确保你有Python环境（推荐3.10+）和支持CUDA的PyTorch。

```bash
# 确保PyTorch已安装，且与你的CUDA版本匹配
# 访问 PyTorch官网 获取正确的安装命令: https://pytorch.org/
```

#### 第1步：安装XTuner

```bash
# 安装基础版XTuner
pip install -U xtuner

# 为了使用QLoRA和FlashAttention等高级功能，安装所有依赖
# 如果遇到网络问题，可以去掉 -i ... 部分
pip install -U 'xtuner[all]' -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 第2步：准备模型和数据集

XTuner会自动从HuggingFace Hub下载所需的模型和数据集，你无需手动下载。这个例子我们将使用 `internlm/internlm2-chat-1_8b` 模型和 `oasst1` 数据集。

#### 第3步：选择并准备配置文件

1.  **查看所有可用的配置文件**：
    XTuner提供了一个方便的命令来列出所有内置的配置。

    ```bash
    xtuner list-cfg
    ```
    你会看到一个很长的列表，比如 `internlm2_chat_1_8b_qlora_oasst1_e3`，这个名字的含义是：
    *   `internlm2_chat_1_8b`: 基础模型是 InternLM2-Chat-1.8B
    *   `qlora`: 微调算法是 QLoRA
    *   `oasst1`: 数据集是 oasst1
    *   `e3`: 训练3个epoch

2.  **复制一份配置文件到当前目录**：
    这是一个好习惯，不要直接修改库里的文件。我们选择 `internlm2_chat_1_8b_qlora_oasst1_e3` 这个配置。

    ```bash
    xtuner copy-cfg internlm2_chat_1_8b_qlora_oasst1_e3 .
    ```
    执行后，当前目录下会多出一个 `internlm2_chat_1_8b_qlora_oasst1_e3_copy.py` 文件。你可以打开它看看里面的内容，但对于快速上手，我们暂时不需要修改它。

#### 第4步：启动微调

现在，最激动人心的一步来了！用一行命令启动微调。

```bash
# --work-dir 指定了训练日志和模型权重保存的目录
xtuner train ./internlm2_chat_1_8b_qlora_oasst1_e3_copy.py --work-dir ./my_finetuned_model
```

XTuner会自动开始下载模型和数据集，然后你会看到训练进度条和日志信息。根据你的显卡性能，这个过程可能需要几十分钟到几个小时。

训练完成后，`./my_finetuned_model` 目录下会生成一个 `.pth` 文件，这就是我们微调得到的**适配器（Adapter）**权重。

> **注意**：QLoRA等方法并不会生成一个完整的模型，而是生成一个轻量的“补丁”（适配器）。我们需要将它与原模型合并才能使用。

#### 第5步：合并适配器权重

将微调后的适配器权重合并到原始的基础模型中，生成一个完整的、可以直接使用的模型。

```bash
# 定义变量，方便复用
export MNT_DIR=${YOUR_MNT_DIR:-/path/to/your/data} # 你想存放HF模型缓存的地方
export SRC_MODEL_PATH=${MNT_DIR}/internlm/internlm2-chat-1_8b # 原始模型路径
export FT_MODEL_PATH=./my_finetuned_model # 微调输出路径
export DST_MODEL_PATH=${FT_MODEL_PATH}/merged_model # 合并后模型的存放路径

# 1. 将 .pth 格式的适配器转换为HuggingFace格式
xtuner convert pth_to_hf ${FT_MODEL_PATH}/iter_555.pth ${FT_MODEL_PATH}/hf_adapter

# 2. 将HuggingFace格式的适配器与原始模型合并
xtuner convert merge ${SRC_MODEL_PATH} ${FT_MODEL_PATH}/hf_adapter ${DST_MODEL_PATH}
```

执行完毕后，`./my_finetuned_model/merged_model` 目录里就是一个全新的、经过微调的完整模型了！

#### 第6步：与你的模型对话

现在，来检验一下我们的微调成果吧！

```bash
# --prompt-template 指定对话模板，这对于聊天模型很重要
xtuner chat ./my_finetuned_model/merged_model --prompt-template internlm2_chat
```

启动后，你就可以在终端里输入问题，和自己微调过的模型进行对话了！

```
user: 你好，介绍一下你自己
assistant: 你好！我是一个由上海人工智能实验室训练的语言模型，InternLM2。我...（模型会给出它的回答）
user: 给我讲一个关于太空旅行的笑话
assistant: ...
```
输入 `exit` 即可退出对话。

---

### 五、接下来可以做什么？

1.  **使用你自己的数据集**：
    *   将你的数据整理成 [JSONL 格式](https://jsonlines.org/)。
    *   修改配置文件的 `dataset` 部分，将 `data_files` 指向你的数据文件路径。
    *   重新运行 `xtuner train` 命令。

2.  **尝试不同的微调方法**：
    *   在 `xtuner list-cfg` 中寻找其他配置，比如全量参数微调的配置（文件名里通常没有 `qlora` 或 `lora`）。
    *   复制配置，然后开始训练。

3.  **部署与评测**：
    *   使用 **LMDeploy** 工具，可以让你合并后的模型以极高的效率运行，提供类似OpenAI的API服务。
    *   使用 **OpenCompass** 工具，可以在各种标准学术榜单上全面评估你的模型性能。

### 总结

XTuner通过**“配置文件驱动”**和**“命令行工具”**，将复杂的大模型微调流程变得标准化和简单化。你只需要：
1.  **选配置** (`xtuner list-cfg`, `xtuner copy-cfg`)
2.  **跑训练** (`xtuner train`)
3.  **转模型** (`xtuner convert`)
4.  **去聊天** (`xtuner chat`)

希望这份指南能帮助你顺利迈出大模型微调的第一步！

**官方资源：**
*   **GitHub仓库**：[https://github.com/InternLM/xtuner](https://github.com/InternLM/xtuner)
*   **官方文档**：[https://xtuner.readthedocs.io/zh-cn/latest/](https://xtuner.readthedocs.io/zh-cn/latest/)