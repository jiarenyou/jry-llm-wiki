---
title: pytorch初级
draft: false
tags:
  - AI
---
 


本文章是本人通过读[《Pytorch实用教程》第二版](https://github.com/TingsongYu/PyTorch-Tutorial-2nd)做的学习笔记，深度学习的核心部分：数据准备 ➡️ 模型构建 ➡️ 模型训练 ➡️ 模型评估与应用。根据上面的思路，我们分为几个部分：
- **第一部分：PyTorch 基础** - 涵盖了从基本概念（如 Tensor）到数据加载、模型搭建和训练的所有核心知识。
    
- **第二部分：PyTorch 实战** - 提供了一些非常棒的案例，让你把学到的知识应用到真实世界的问题中，比如图像分类和自然语言处理。
    
- **第三部分：PyTorch 模型部署** - 教你如何将训练好的模型应用到生产环境中。

# 一 PyTorch 基础
## 1.1 Tensor

>[!question] 先提一个问题，Tensor和Numpy中的array相比，最关键的区别是什么？

Tensor 与 NumPy 数组最根本的区别是Tensor能够给深度学习提供GPU计算和自动求梯度的能力：
- **GPU 加速计算：** 利用 GPU 大规模并行计算的能力，极大缩短训练时间，是深度学习能够发展到今天的关键。
- **自动求梯度 (Automatic Differentiation)：** 通过记录计算图。我们只需要搭建好模型（前向传播），PyTorch 就能自动计算出所有参数的梯度，然后我们就可以用这些梯度来更新模型（反向传播），让模型变得越来越好。

### 创建Tensor
我们了解了Tensor能做什么后，来看下如何创建Tensor，创建Tensor的方式很多，我们只说两种，其他方式可移步[pytorch官方文档](https://docs.pytorch.org/docs/stable/index.html)
- `torch.tensor(numpy_array)`: 会创建一个 Tensor，并**复制**一份 NumPy 数组的数据。之后修改原来的 NumPy 数组，**不会**影响到这个新的 Tensor。是最常用、最直接的方法，尤其适合将 Python 的列表 (list) 或元组 (tuple) 转换成 Tensor。
- `torch.from_numpy(numpy_array)`: 创建的 Tensor 和原来的 NumPy 数组会**共享内存**。这意味着，如果你修改其中一个，另一个**也会跟着改变**。

通过下面的例子了解下：
```python
import torch
import numpy as np

# 使用 torch.from_numpy() (共享内存)
numpy_arr = np.array([1, 2, 3, 4])
tensor_shared = torch.from_numpy(numpy_arr)

print(f"修改前，NumPy 数组是: {numpy_arr}")
print(f"修改前，Tensor 是: {tensor_shared}")

# 我们只修改 NumPy 数组
numpy_arr[0] = 99 

print("---------------------------")
print(f"修改后，NumPy 数组是: {numpy_arr}")
print(f"修改后，Tensor 也跟着变了: {tensor_shared}") # 注意这里的变化

```

在什么场景下使用 `torch.from_numpy()` 会比 `torch.tensor()` 更有优势？
在进行前向传播 (forward pass) 的时候，我们经常需要把来自不同来源（比如用 OpenCV 或其他库处理过的图像数据）的 NumPy 数组送入 PyTorch 模型。

这时候，如果数据量非常大（比如成千上万张高清图片），使用 `torch.tensor()` 就会遇到一个问题：**内存占用会翻倍**。因为它需要额外申请一块内存来存放复制过来的数据。

而使用 `torch.from_numpy()` 就优雅地解决了这个问题。它非常高效，因为它避免了不必要的数据复制，直接利用已经存在于内存中的 NumPy 数据。这在处理大规模数据集时，能**节省大量的内存空间和数据复制的时间**。
- **`torch.tensor()`**：更安全，因为数据是独立的。适合一般情况。
- **`torch.from_numpy()`**：更高效，因为共享内存。适合处理大型数据集，特别是作为模型输入时。

### “全 1”或“全 0” Tensor
“全 1”或“全 0” Tensor的用途
- 参数初始化，比如，神经网络中，经常把“偏置”参数全部初始化为0
- 作为掩码，假设你有一个 Tensor，但你只想保留其中一部分的数据，把另一部分数据“屏蔽”掉（比如变成 0）。这时你就可以创建一个由 0 和 1 组成的“掩码” Tensor，然后把它和你的原始 Tensor 相乘。任何数字乘以 0 都会变成 0，乘以 1 则保持不变。这样就实现了精确的“屏蔽”效果，这在很多高级应用（比如 NLP 里的注意力机制）中非常有用。
主要的函数是torch.ones()和tensor.zeros()

### Tensor的属性
主要用于检查Tensor的属性，比如其尺寸（形状）、包含的数字类型（dtype）以及存储位置
- **`.shape`**：张量的大小和尺寸。📏
- **`.dtype`**：存储在里面的数字的数据类型（如小数的 `float32` 或整数的 `int64`）。
- **`.device`**：Tensor 的物理存储位置—— **在 CPU** 或 **GPU** （`cuda`） 上。

```python
import torch

# Our sample tensor
my_tensor = torch.tensor([[1, 2, 3], 
                          [4, 5, 6]], dtype=torch.float32)

# Checking its attributes
print(f"Shape: {my_tensor.shape}")
print(f"Data Type: {my_tensor.dtype}")
print(f"Device: {my_tensor.device}")

# 输出结果
Shape: torch.Size([2, 3]) 
Data Type: torch.float32 
Device: cpu

```

### Tensor的计算
Tensor计算，最常用的，也是最重要的就是矩阵乘法，主要函数是`torch.matmul()`，作为一个方便快捷方式，可以使用`@`符号
```python
import torch

# Create a 2x3 tensor
tensor_A = torch.randn(2, 3)

# Create a 3x2 tensor
tensor_B = torch.randn(3, 2)

# Perform matrix multiplication using the @ operator
result = tensor_A @ tensor_B

print(f"Shape of A: {tensor_A.shape}")
print(f"Shape of B: {tensor_B.shape}")
print(f"Shape of the result: {result.shape}")

# 输出
Shape of A: torch.Size([2, 3]) 
Shape of B: torch.Size([3, 2]) 
Shape of the result: torch.Size([2, 2])
```

以上是非常简单的Tensor操作，如果想了解更深，可以去[官网](https://docs.pytorch.org/docs/stable/tensors.html)查看更多API

## 1.2 数据加载
数据加载主要介绍Dataset和DateLoader
- **`Dataset` 📖**: 这就像**食谱** 。它知道所有单独的数据点（“食谱”）是什么以及在哪里可以找到它们。它的主要工作是定义数据点的总数以及如何在询问时获取单个数据点。
- **`DataLoader` 👨‍🍳**：这就像**厨师** 。厨师获取食谱（ `数据集` ）并有效地准备模型的数据。厨师负责打乱食谱，将它们分组（例如，一次提供 8 道菜），甚至可以使用多个厨房助手（多处理）来加快速度。

### Dataset
在PyTorch中，任何我们想要自定义的数据集，都必须遵循一个固定的“格式”，要求我们实现最核心的两个“功能”：
- `__len__(self)`: 这个函数用来告诉 PyTorch，我们的数据集中**一共有多少个样本**。就像是食谱的目录，告诉厨师一共有多少道菜。
- `__getitem__(self, idx)`: 这个函数用来**获取单个样本**。当我们给它一个索引号 `idx` (比如 5)，它就要能准确地把第 5 个样本（比如第 5 张图片和它对应的标签）拿出来。`__getitem__` 函数负责返回一对：`（image_tensor， label）。`
只要我们定义好了这两个函数，PyTorch的DataLoader就知道该如何与数据进行交互了。

以下是一个自定义数据集`CatDogDataset`的骨架。
```python
from torch.utils.data import Dataset
# We'll probably need libraries to handle file paths and open images
import os
from PIL import Image 

class CatDogDataset(Dataset):
    def __init__(self, image_dir, transform=None):
        # 1. Get a list of all our image file names from the directory.
        self.image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir)]
        self.transform = transform

    def __len__(self):
        # 2. The total number of samples is just the number of image files.
        return len(self.image_paths)

    def __getitem__(self, idx):
        # 3. Get the full file path for the requested index `idx`.
        image_path = self.image_paths[idx]
        
        # 4. Load the image using its path.
        image = Image.open(image_path)

        # 5. Determine the label from the file name.
        if 'cat' in image_path:
            label = 0
        else: # 'dog'
            label = 1
        
        # 6. (Optional but important) Apply any transformations (like resizing).
        if self.transform:
            image = self.transform(image)
        
        # 7. Return the image and its label.
        return image, label
```

### DataLoader
DataLoader采用我们的Dataset（食谱）并处理准备训练数据的工作，其主要工作是：
- 批处理：将单个数据点分组为批次，我们可以一次向模型提供一批32或64张图像，而不是一次向模型提供一张图像。这对GPU来说效率要高得多。
- Shuffle：在每个训练周期（epoch）开始随机洗牌数据
- 并行处理：使用多个后台工作线程同时加载数据，这样模型不必等待

以下是我们为刚刚定义的 `CatDogDataset` 创建 `DataLoader` 的方法：
```python
from torch.utils.data import DataLoader

# 1. First, we create an instance of our "cookbook".
# (Assuming we have a folder named 'data/cats_and_dogs')
cat_dog_dataset = CatDogDataset(image_dir='data/cats_and_dogs')

# 2. Now, we give the cookbook to our "chef".
# We'll ask for batches of size 32 and to shuffle the data.
data_loader = DataLoader(dataset=cat_dog_dataset, batch_size=32, shuffle=True)

# 3. Now we can iterate over the data_loader to get our batches.
for image_batch, label_batch in data_loader:
    # In each loop, we get a batch of 32 images and their 32 labels.
    # We can then feed these batches directly to our model.
    pass
```

可以看到DataLoader中shuffle是True，通过打乱数据，确保模型看到的每一批都是整个数据集的随机混合样本。这迫使模型学习真正的区别特征（如尖耳朵或胡须），使最终模型更加**稳健** ，并且能够更好地推广到新的、看不见的数据

>[!summary] 小结
>我们现在已经构建了一个完整的数据管道。我们有：
>1. 基本数据块 （**Tensor**）。
>2. 知道在哪里可以找到数据（ **数据集** ）的“食谱”。
>3. 准备训练的“厨师”（**DataLoader**）。
> 
> 数据准备好，下一步我们就要构建模型


## 1.3 模型搭建和训练
### 模型搭建
在 PyTorch 中，所有的神经网络模型都应该继承一个叫做 `nn.Module` 的“基类”。

可以把 `nn.Module` 想象成一个乐高积木的“底板” ⚫。它本身提供了一些非常重要的基础功能（比如追踪模型的所有参数），而我们则需要往这块底板上添加我们自己的“积木块”（也就是神经网络的各种层，比如线性层、卷积层等）。

搭建一个模型，通常也需要实现两个核心部分：

1. `__init__(self)`: 这是模型的“构造函数”。我们在这里**定义**模型需要用到的所有“积木块”（神经网络层）。
    
2. `forward(self, x)`: 这里是“前向传播”的核心。我们在这里**连接** `__init__` 中定义的积木块，明确规定数据 `x` 应该如何一步步流过这些层，最终得到输出。

**简单来说：`__init__` 负责“买零件”，`forward` 负责“组装”**。

下面我们来看一个简单的例子，构建一个模型，可以查看手写数字的图片（来自著名的 MNIST 数据集）并对它是哪个数字进行分类（0 到 9）。

MNIST 图像是 28x28 像素的灰度图片。为了将其输入到一个简单的模型中，我们首先将其展平为一条 784 像素的单行 （28 * 28 = 784）。

以下是此任务的基本模型在 PyTorch 中的样子：
```python
import torch.nn as nn

class SimpleClassifier(nn.Module):
    def __init__(self):
        # First, we must call the __init__ of the parent class (nn.Module)
        super().__init__()
        
        # "Buying the parts": We need one 'linear' layer.
        # It will take the 784 pixels as input and must output 10 numbers,
        # one score for each possible digit (0-9).
        self.layer1 = nn.Linear(in_features=784, out_features=10)

    def forward(self, flattened_image):
        # "Assembling the parts": We define how the data flows.
        # The flattened image data simply goes through our one layer.
        output = self.layer1(flattened_image)
        return output
```

784是将28 * 28的图片展平为一条784像素的单行，10是此目标分类个数是10

上面的模型非常简单，只是一个线性层，。为了学习手写之类的复杂模式，我们需要在层之间引入一个“秘密成分”： **非线性激活函数**。最常见的激活函数之一是ReLU，让我们加入激活函数。
```python
import torch.nn as nn
import torch.nn.functional as F

class SimpleClassifierWithReLU(nn.Module):
    def __init__(self):
        super().__init__()
        # "Buying the parts"
        self.layer1 = nn.Linear(784, 128)  # Hidden layer
        self.layer2 = nn.Linear(128, 10)   # Output layer

    def forward(self, x):
        # "Assembling the parts"
        # Pass through the first layer
        x = self.layer1(x)
        # Apply the ReLU activation function
        x = F.relu(x)
        # Pass through the output layer
        output = self.layer2(x)
        return output
```

### 模型训练
训练模型本质上是一个循环，在这个循环里，不断地根据训练的模型结果，进行“微调”，这个过程需要三个关键组件：
1. 损失函数(Loss Function): 用来衡量模型预测结果和真实答案之间的差距。差距越大，损失值就越高。
2. 优化器(Optimizer): 根据损失函数计算出的梯度，来更新模型的权重参数，目标是让损失值越来越小。
3. 训练循环(Training Loop): 把所有步骤（获取数据 -> 前向传播 -> 计算损失 -> 反向传播 -> 更新权重）串起来，并重复执行

#### 损失函数
损失函数可以看做是记分员，他的工作室两件事：
1. 模型的预测结果
2. 实际的正确答案，即标签

来衡量预测结果和正确答案的差距，即损失。
- 如果模型的预测偏离很大，就给出高分
- 如果模型预测偏离小，就给出低分
训练的最终目标是将这个分数最小化

有很多介绍损失函数的文章，详细资料可网上去搜

#### 优化器
损失函数是“记分员”， 优化器就像是“教练”。
教练会根据记分员给出的分数（损失值），以及每个参数对这个分数的影响程度（梯度），来制定一个“训练计划”，告诉模型的每一个参数（权重）应该如何微调——是该调高一点，还是该调低一点，以及调整的幅度应该多大。

最常用的优化器之一叫做 **Adam**。现在我们只需要知道，它的工作就是根据 `backward()` 计算出的梯度，来智能地更新模型的权重，从而让损失值越来越小。

下面我们了解下优化器的发展，可以看做是分三步走：
1. SGD（随机梯度下降）：这是最基础、最经典的优化器，就像是优化器中的“老爷车”，理解它就能理解了所有优化器的出发点
2. Momentum（动量）：这是对SGD的一个重要改进，给“老爷车”加了一个“惯性系统”，让它跑的更稳，更快
3. Adam：这是目前最流行、最常用的优化器之一，非常智能，自适应不同的情况，就像一辆“现代跑车”

关于优化器的最常见比喻是，寻优过程就像是蒙眼下山。
- SGD
	可以把它想象成一个**蒙着眼睛**、想要走到山谷最低点的**下山者** 👨‍🦯。
	他看不见整个山谷的全貌，所以他只能采取一个最简单的策略：
	1. 在当前位置，伸脚向**四周**探一探，感受哪个方向是**下坡最陡**的。（这就是**计算梯度**）
	2. 然后，朝着这个最陡峭的方向，迈出**一小步**。（这就是**更新权重**）
	3. 重复这个过程，一步一步地往下走。
	
	在简单的蒙眼下山策略中，有个潜在问题，如果徒步者走入山坡上的小凹陷，从他们的位置来看，每个方向似乎要么是平坦的，要么是略微上坡的，导致进入“局部最优解”，无法到达真正的谷底（全局最优解），SGD的最大弱点之一：很容易被局部最优解或鞍点困住
	
- Monentum
	上面的问题，就是Monentum要解决的，Monentum是“动量”、“惯性”的意思，在优化器里Monentum算法会积累过去几个步骤的梯度（就像是累计“质量”和“速度”），形成一个“动量”，当遇到梯度变小（比如平坦区域或局部小坑）的时候，下山者也能通过这个“动量”冲过去，不会像SGD那样被卡主
	
- Adam (Adaptive Moment Estimation)
	Adam 是目前最受欢迎的优化器之一，我们可以把它看作一辆**智能的现代跑车** 🏎️。它不仅吸收了 Momentum 的“惯性”优点，还增加了一个更强大的功能：**自适应学习率 (Adaptive Learning Rates)**。
	拿下山的例子，在下山的时候，步子大一点，能快速接近谷底；快到谷底的时候，步子变小，有利于找到最底的谷底
	这里的“**一小步**”的大小，在深度学习里被称为“**学习率 (Learning Rate)**”。
	如果步子（学习率）**太大**，他可能会一步迈过头，直接跨到对面山坡上，导致永远在谷底附近来回震荡，到不了最低点。
    如果步子（学习率）**太小**，他下山的速度会非常非常慢

#### 训练循环
**训练循环 (Training Loop)** 就是整个过程的核心，它把我们之前讨论的所有部件——数据、模型、损失函数和优化器——全部串联起来，协同工作。

标准的训练循环就像一个固定的“仪式”，每一步都有明确的目的：
1. **清零梯度 (`optimizer.zero_grad()`)**: 准备开始新一轮的计算。
2. **前向传播 (`model(inputs)`)**: 让模型根据输入数据进行预测。
3. **计算损失 (`loss_fn(outputs, labels)`)**: 评估模型的预测有多糟糕。
4. **反向传播 (`loss.backward()`)**: 根据损失，计算出每个参数应该如何调整（即计算梯度）。
5. **更新权重 (`optimizer.step()`)**: “教练”正式出手，根据梯度更新模型的参数。
这五个步骤会一遍又一遍地重复，每一次重复，模型都会变得比上一次更“聪明”一点。

>[!tip] 为什么要先进行梯度清零
> PyTorch 在设计 `backward()` 函数时，就是让它把新计算出的梯度**累加**到已有的 `.grad` 属性上，而不是覆盖掉。
> 这么设计其实是有意为之的，因为它在一些高级应用（比如循环神经网络 RNN 的某些变种）中非常有用。
> 但对于我们现在正在做的、最常见的训练任务来说，每一轮的梯度计算都应该是一个全新的开始，完全独立于上一轮。我们只关心当前批次数据所产生的梯度。
> 所以，如果我们不在每一轮循环开始时手动“清零”，那么旧的梯度就会像“幽灵”一样一直影响着新的梯度，导致“教练”（优化器）拿到完全错误的信息，最终模型也就无法被正确地训练了。


# 二 PyTorch实践
下面我们来进行代码实战，我们的目标是编写一个完整的 Python 脚本

1. 加载 MNIST 手写数字数据集。
2. 构建 `SimpleClassifierWithReLU` 模型。
3. 使用我们讨论的损失函数和优化器训练模型。
4. 评估训练模型的性能。

## 2.1 准备数据集
我们可以逐步构建脚本。任何 Python 文件的第一步始终是**导入必要的库** 。
```python
import torch
from torch import nn # nn 包含了模型层 (nn.Module, nn.Linear) 和损失函数 (nn.CrossEntropyLoss)
from torch.utils.data import DataLoader
from torchvision import datasets # 这是一个方便的库，已经帮我们打包好了 MNIST 等常用数据集
from torchvision.transforms import ToTensor # 这是一个工具，可以把图片转换成 Tensor
import torch.optim as optim # 这里面有我们需要的各种优化器，比如 Adam
```
在 PyTorch 里，准备数据的代码通常非常简洁，因为 `torchvision` 库已经为我们处理了大部分繁琐的工作，比如下载数据集和进行基础的转换。

这是加载 MNIST 训练数据的标准代码：
```python
# --- 1. 数据准备 ---
training_data = datasets.MNIST(
    root="data",       # 指定数据下载后存放的目录
    train=True,        # 明确指出这是训练集
    download=True,     # 如果 'data' 目录里没有，就自动下载
    transform=ToTensor() # 把图片数据转换成 PyTorch Tensor
)

# 我们可以用 DataLoader 来打包数据
train_dataloader = DataLoader(training_data, batch_size=64)
```

>[!question] 为什么使用ToTensor
>- **更改格式：** 它获取图像（通常是来自 Pillow （PIL） 等库的数据结构），并将其转换为 PyTorch 张量。
>- **缩放像素值：** 这是关键部分。图像像素通常是从 0（黑色）到 255（白色）的整数。`ToTensor（）` 将它们转换为 **0.0 到 1.0** 之间的浮点数。

这种缩放是规范化的一种形式，对于帮助神经网络高效训练非常重要

## 2.2 构建 `SimpleClassifierWithReLU` 模型。
1. 构建模型
```python
	# --- 2. Model Definition ---
class SimpleClassifierWithReLU(nn.Module):
    def __init__(self):
        super().__init__()
        # "Buying the parts"
        self.layer1 = nn.Linear(28*28, 128) # Input is 784, hidden layer is 128
        self.layer2 = nn.Linear(128, 10)    # Output is 10 classes

    def forward(self, x):
        # "Assembling the parts"
        # This is the flattening step we talked about!
        # It reshapes the (1, 28, 28) image into a (784) vector.
        x = x.view(x.size(0), -1)
        
        # Now the data flows through the layers
        x = self.layer1(x)
        x = nn.functional.relu(x) # Apply ReLU activation
        output = self.layer2(x)
        return output
	```
## 2.3 损失函数
```python
# --- 3. Loss Function and Optimizer ---
loss_fn = nn.CrossEntropyLoss()
```
## 2.4 优化器
```python
# (在模型定义和损失函数之后)

# 首先，我们需要创建模型的一个实例
model = SimpleClassifierWithReLU()

# 然后，我们创建优化器，并把模型的参数告诉它
optimizer = optim.Adam(model.parameters(), lr=1e-3) # lr 是学习率
```

## 2.5 清零梯度
```python
# --- 4. The Full Training Loop ---

# First, create an instance of our model
model = SimpleClassifierWithReLU()

# Create our loss function and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# We'll train for 5 "epochs" (5 full passes over the dataset)
epochs = 5

for epoch in range(epochs):
    print(f"Epoch {epoch+1}\n-------------------------------")
    # Loop over the data loader
    for batch, (X, y) in enumerate(train_dataloader):
        
        # 1. ZERO GRADIENTS
        optimizer.zero_grad()
        
        # 2. FORWARD PASS
        pred = model(X)
        
        # 3. COMPUTE LOSS
        loss = loss_fn(pred, y)
        
        # 4. BACKWARD PASS
        loss.backward()
        
        # 5. UPDATE WEIGHTS
        optimizer.step()
        
        # Optional: Print progress
        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{len(train_dataloader.dataset):>5d}]")

print("Done Training!")
```

## 2.6 模型评估
```python
# (Assuming we have a test_dataloader prepared just like our train_dataloader)
size = len(test_dataloader.dataset)
num_batches = len(test_dataloader)
model.eval() # Set the model to evaluation mode
test_loss, correct = 0, 0

with torch.no_grad(): # We don't need gradients for testing
    for X, y in test_dataloader:
        pred = model(X)
        test_loss += loss_fn(pred, y).item()
        # Find the index of the highest score, which is the model's prediction
        correct += (pred.argmax(1) == y).type(torch.float).sum().item()

test_loss /= num_batches
correct /= size
print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
```


# 三 部署应用
部署的目标是采用我们训练好的PyTorch模型并将其转换为以下格式：
1. Fast：针对纯预测速度（推理）进行优化，而不是训练
2. Portable：能够在不同的环境中运行，例如 Web 服务器、手机或边缘设备，这些设备甚至可能没有安装 Python 或 PyTorch
主要侧重将两项关键技术：ONNX和TensorRT
让我们打个比方：

- **我们的 PyTorch 模型** ：它就像一个复杂的定制引擎⚙️，在我们的车间（Python 环境）中设计。它功能强大，但需要我们所有的专用工具才能运行。
    
- **ONNX**：这就像为我们的引擎创建通用**技术蓝图** 📜。这是一种标准格式，准确描述了引擎的工作原理。任何能阅读此标准蓝图的人都可以构建我们引擎的副本，即使他们没有我们原创的创意工坊工具。这解决了**便携性**问题。
    
- **TensorRT：** 这是英伟达打造的高性能工厂🏭。它采用蓝图（ONNX 文件）并使用先进的优化技术来构建我们引擎的极快生产级版本，专门针对在 NVIDIA GPU 上运行进行了调整。这解决了**速度**问题。
    
因此，典型的工作流程是：**PyTorch 模型 -> ONNX 蓝图 -> 优化的 TensorRT 引擎** 。

## 3.1 ONNX
ONNX（开放神经网络交换）是通用**蓝图** 。从我们的 PyTorch 模型创建此蓝图的过程称为**导出** 。
这个函数以一种巧妙的方式工作。它不仅保存模型的架构，还**跟踪**模型。这意味着我们需要：

1. 创建一段虚假的输入数据（“虚拟输入”）。
2. 通过我们的模型传递此虚拟输入。
3. 当数据流过时，`torch.onnx.export（）` 会记录发生的每一个作。
4. 然后，它将此记录的作序列保存到 `.onnx` 文件中。

以下是我们一直在使用的 `SimpleClassifierWithReLU` 模型的执行此作：
```python
import torch

# (Assume the SimpleClassifierWithReLU class is defined above)

# 1. Create an instance of our model
model = SimpleClassifierWithReLU()
# IMPORTANT: Before exporting, you would typically load your saved trained weights
# and put the model in evaluation mode.
# model.load_state_dict(torch.load("path_to_weights.pth"))
model.eval()

# 2. Create a dummy input tensor with the correct shape.
# Our model expects a flattened image, but the original input is (batch_size, channels, height, width)
# So let's create a dummy 28x28 image.
# We'll use a batch size of 1.
dummy_input = torch.randn(1, 1, 28, 28) 

# 3. Export the model
torch.onnx.export(
    model,                          # The model to export
    dummy_input,                    # A sample input to trace the model
    "mnist_classifier.onnx",        # The name of the output file
    input_names=["input_image"],    # A name for the input node
    output_names=["output_scores"]  # A name for the output node
)

print("Model successfully exported to mnist_classifier.onnx")
```

>[!question] 这个过程最独特的部分是需要 `dummy_input`。为什么我们需要向导出功能提供这些虚假数据吗？
>答案是为了追踪，举个例子，写下你的朋友从椅子这里走到前门那，这个过程中你的朋友走的每一步你都记录了下来。这个过程中，你的朋友就是`dummy_input`; 穿过房间的每一步就是前向传递；你记录的文件就是`.onnx`文件


如何使用这个文件_在_**未安装 PyTorch** 的环境中进行预测（例如，在简单的 Web 服务器上）？

我们有`.onnx` 文件，但现在我们需要一个“阅读器”或“引擎”来理解并执行它。该引擎称为 **ONNX Runtime**

可以这样想：
- 要打开 `.pdf` 文件，您需要一个像 Adobe Reader 这样的程序。
- 若要运行 `.onnx` 模型，需要像 **ONNX Runtime** 这样的库。

runtime是安装在部署环境中的单独轻量级库。它根本不需要 PyTorch。它唯一的工作是加载 `.onnx` 文件并非常非常快地执行预测（推理）。

下面介绍如何使用 Python 中的 `onnxruntime` 库来运行导出的模型：
```python
import onnxruntime as ort
import numpy as np

# 1. Create an "inference session" by loading the .onnx file
session = ort.InferenceSession("mnist_classifier.onnx")

# 2. Get the name of the input layer (we named it "input_image" during export)
input_name = session.get_inputs()[0].name

# 3. Prepare a sample input. ONNX Runtime works well with NumPy arrays.
# The shape must match what the model expects: (1, 1, 28, 28)
sample_input = np.random.rand(1, 1, 28, 28).astype(np.float32)

# 4. Run the prediction
# The result is a list containing the output arrays
results = session.run(None, {input_name: sample_input})

# 5. Interpret the result
output_scores = results[0]
predicted_digit = np.argmax(output_scores)

print(f"The ONNX Runtime produced output scores: \n{output_scores}")
print(f"The predicted digit is: {predicted_digit}")
```


## 3.2 TensorRT
将其视为一个高度专业化的工厂🏭，它获取模型的蓝图（`.onnx` 文件）并重新构建它，使其在特定的 NVIDIA GPU 上尽可能快地进行物理处理。

这不仅仅是运行模型;它正在**积极优化**它。TensorRT 使用几种巧妙的技术来做到这一点，但我们可以专注于三个主要想法：

1. **精密校准（量化）：** 它巧妙地使用不太精确的数字来更快地进行数学运算，例如使用 `1.5` 而不是 `1.5000001`。
2. **图层融合** ：它将模型的多个步骤组合成一个超级高效的步骤。
3. **内核自动调整** ：它为您的特定 GPU 硬件上的每个作找到绝对最快的代码。

### 精准校准（量化）
一种更广泛地称为**量化**的技术。核心思想出奇地简单。想象一下你正在测量一些东西。
- 您可以使用一个非常精确的数字，例如 **`3.14159265`**
- 或者，对于大多数实际目的，您可以只使用 **`3.14`**。
第二个数字不太精确，但它更短且更容易使用。电脑也有同样的感觉！
默认情况下，神经网络使用高精度 32 位数字（称为 `FP32`）进行训练。TensorRT 分析模型并找出它可以在哪些方面安全地使用较低精度的数字，例如 16 位 （`FP16`） 甚至 8 位整数 （`INT8`），而不会对最终结果造成太大损害。
由于这些数字较小，GPU 可以更快地处理它们并将更多数字放入内存中。
不过，这不仅仅是盲舍入。“校准”部分意味着 TensorRT 使用实际数据的一小部分样本来智能地找出将数字转换为较低精度的最佳方法，同时将信息丢失降至最低。这里的主要好处是速度的巨大提升。

但如果操作太“粗糙”，累积的误差就会越来越大，最终导致模型的**准确率下降**。 TensorRT 的“校准”（Calibration）步骤就显得至关重要。它会非常智能地分析模型，只在那些对最终结果影响不大的地方使用低精度计算，而在关键部分仍然保持高精度。这是一个在**速度**和**精度**之间的权衡。

### 图层融合
图层融合，概念也很直观，这个概念也很直观。想象一下在工厂的流水线上组装一个玩具：
- **步骤1：** 工人A拿起玩具的身体。
- **步骤2：** 工人A把身体递给工人B。
- **步骤3：** 工人B给玩具装上头部。
- **步骤4：** 工人B把玩具递给工人C。
- **步骤5：** 工人C给头部画上眼睛。

现在，如果我们把这三个步骤**融合**成一个，让工人A一个人完成“拿起身体 -> 装上头部 -> 画上眼睛”这整套动作，会发生什么？整个流水线的效率会有什么变化？

答案是效率直线上升，什么原因导致的呢？
有两个主要原因：

1. **减少开销：** 消除了工作线程之间的“切换”时间。GPU 不必启动新任务，从内存中读取数据，然后将其写回，只是为了发生下一个小步骤。
2. **节省内存** ：在融合发生时，数据可以保留在 GPU 内核的本地内存（缓存）中，而不是在每一步之间发送回主 GPU 内存。

因此，TensorRT 会查看模型的蓝图，并自动找到可以合法有效地融合到单个自定义作中的层序列。

### 内核自动调整
想象一下，你是一位顶级赛车工程师 👨‍🔧，正在为一场特定的比赛调校赛车。对于赛车上的**每一个螺丝**，你手上都有一整套工具箱，里面有几十种看似相同但实际有细微差别的扳手。

为了追求极致的速度，你会不厌其烦地用**每一种扳手**去试着拧紧那个螺丝，直到找到那一把能让你用最快、最完美的方式完成工作的扳手。

在 GPU 的世界里：

- **“核心” (Kernel)** 就是一个为特定任务（比如一次卷积计算）编写的高度优化的底层代码，就像是那把“扳手”。
- 对于同一个任务，NVIDIA 的工程师们已经准备好了很多种不同的“核心”实现。
- **”自动调整” (Auto-Tuning)** 就是 TensorRT 在构建模型时，会像那位工程师一样，为模型中的每一个操作，在你的**特定 GPU** 上实际运行和测试多种不同的”核心”，然后选择那个表现最快的。

## 相关笔记
- [[第4课 手写 Model.py 大模型代码逻辑]]：从PyTorch基础到Transformer模型的完整实现
- [[第5课 手写 Train.py 大模型代码逻辑]]：训练脚本的完整实现，包含数据加载、训练循环和优化器配置
