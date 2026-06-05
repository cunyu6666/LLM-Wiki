---
id: "7440813761952220407"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzYzMzc3NTcyOQ==&mid=2247484349&idx=1&sn=97614f01cf74c8459a2c4713cba39217&chksm=f1c31ea2f6f04d903eb4609e6601dcaa37830c7e7eb02c224bf7cc39a5341dbb21ed5369d5e4&mpshare=1&scene=1&srcid=04063qifZQT3jJsffflItgSM&sharer_shareinfo=9eb3ba867f8a95656d6d98a126784b63&sharer_shareinfo_first=9eb3ba867f8a95656d6d98a126784b63
author: "ranranStar 一个算法er的日常"
collected: 2026-04-06
tags: []
---

# 技能内化！SKILL0让Agent告别检索，推理Token暴降5倍

# 技能内化！SKILL0让Agent告别检索，推理Token暴降5倍

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYzMzc3NTcyOQ==&mid=2247484349&idx=1&sn=97614f01cf74c8459a2c4713cba39217&chksm=f1c31ea2f6f04d903eb4609e6601dcaa37830c7e7eb02c224bf7cc39a5341dbb21ed5369d5e4&mpshare=1&scene=1&srcid=04063qifZQT3jJsffflItgSM&sharer_shareinfo=9eb3ba867f8a95656d6d98a126784b63&sharer_shareinfo_first=9eb3ba867f8a95656d6d98a126784b63)ranranStar 一个算法er的日常


*SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization*

现在的 Agent 都在搞"外挂大脑"------遇到不会的任务，就去 Skill Bank 里检索一堆操作指南塞进 Context。这套打法确实管用，但代价惨重：检索噪声干扰判断、Context 越来越长导致推理贵得离谱，最要命的是，模型永远在"照着说明书操作"，一旦拔掉网线（去掉 Skill 提示），瞬间变回智障。

这篇论文直接掀桌子：能不能别老想着怎么检索，而是把技能直接训练进模型参数里？推理时完全零依赖，不仅省钱，性能还更强。

这就是 **SKILL0** ，一个让 Agent 真正"学会"技能，而不是"背诵"技能的强化学习框架。

## 1. 为什么"检索增强"走不远？

在 Agent 领域，Inference-time Skill Augmentation（推理时技能增强）几乎是标配。它的逻辑很简单：把历史成功经验抽象成 Skill 文件，推理时检索相关的 Skill 注入 Prompt。

但这条路有三个致命伤：

1. **检索噪声** ：检索回来的 Skill 未必精准，错误的引导比没有引导更可怕，直接带偏 Agent 的决策。

2. **Token 开销** ：多轮交互中，Skill 内容叠加历史轨迹，Context 长度指数级膨胀。推理成本居高不下，延迟感人。

3. **模型不学习** ：这是最本质的问题。模型只是在执行 Prompt 里的指令，能力存在于 Context 中，而非模型参数里。这叫"执行技能"，不叫"掌握技能"。

人类学习骑车是这样的：开始有辅助轮（显式指导），慢慢拆掉辅助轮（内化平衡感），最后完全独立骑行。而现在的 Agent 永远带着辅助轮在跑。

SKILL0 的核心思想就是模拟这个过程：**训练时给 Skill，推理时零 Skill** 。通过强化学习，逼迫模型把外部知识内化为内在策略。

## 2. 核心方法：像教小孩一样训练 Agent

SKILL0 的全称是 In-Context Agentic Reinforcement Learning for Skill Internalization。它的设计非常巧妙，主要包含三个关键机制。

### 2.1 范式转移：从 Augmentation 到 Internalization

先看一张对比图，直观感受两种范式的差异。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fcv2qnxtPoV9FqyRDXprI2ZJYKN8QGiajicnwib0dgP0NRzs40gPT8mibrjF571DvAic9tJ7QP0Ux8vEXdynAfBN1TSf2uJ7sBANdiaQEtibIWdLeib4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

图1： 技能增强与技能内化范式对比：上部依赖检索，下部实现零样本推理。

如上图所示，传统的 Skill Augmentation（上部分）是一个闭环：Agent Policy 依赖 SkillBank，通过 Similarity 检索技能，甚至还要 Skill Evolve 来更新技能库。这导致推理时始终背负着检索和注入的开销。

而 SKILL0 的 Skill Internalization（下部分）则完全不同。训练时，它利用 On-Policy Helpfulness 来筛选技能；但到了推理阶段（Zero-shot Inference），完全不需要检索，Agent Policy 直接输出动作。这意味着技能已经"长"在模型参数里了。

### 2.2 视觉压缩：把文本历史变成图片

为了进一步降低 Token 开销，SKILL0 引入了 **Context Rendering** 机制。它不直接把文本历史塞给模型，而是把交互历史（Observations 和 Actions）渲染成一张紧凑的 RGB 图片。

通过 Vision Encoder 压缩，原本几千 Token 的文本历史被压缩成几百个 Visual Token。更绝的是，模型可以自己决定压缩率 cₜ。如果当前步骤很简单，模型就输出一个高压缩率，进一步省钱。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fcv2qnxtPoV8qmtqiaq2ayWMSOhzLEmqrUF3UGCNHeYQoEdOr5HoUHYpVm14DFu35D22l39Geo8kR0iars4yv8YkBJrpjCnNib80fibZykR3ibOL0%2F640%3Ffrom%3Dappmsg%23imgIndex%3D1)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fcv2qnxtPoVibhhQwvZq99ayRMI180eA3s4pdAicaUvBBR1MODOibqxZZbGIQEvCianXibf66PQvVGIdhAR4cAPfGXKicjvV8u8ba6TB9vDIYvIwBg%2F640%3Ffrom%3Dappmsg%23imgIndex%3D2)

### 2.3 动态课程学习：慢慢拆掉"辅助轮"

这是 SKILL0 的灵魂。如果一开始就不给 Skill，模型学不会；如果一直给 Skill，模型学不进去。所以需要一套**动态课程学习（Dynamic Curriculum）** 机制。

SKILL0 定义了一个技能预算 M(s)，随着训练阶段 s 的推进，预算线性衰减：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fcv2qnxtPoV9sIxPPXl94fptfaibUhpl7aj8POCdU6xq3XP6DdumvwXMj1T2uhEP8CBYLngmWwgRX6qohyJe03YaHnXhF3hcZub0vPsBR0MwE%2F640%3Ffrom%3Dappmsg%23imgIndex%3D3)

其中 N 是总技能数，N_S 是总阶段数。预算越来越少，直到最后 M(N_S) = 0，完全零技能。

但在每个阶段，具体保留哪些技能？不是随机的，而是基于 **Helpfulness（有用性）** 。作者定义了一个指标 Δₖ：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fcv2qnxtPoVicyHoXsGEwm8blQpMEG00WnCw6ovianOncaxfjpW7qpAxOXuicxuB6mWAgNRn3JcuVMYPziaP1CDOpKQVFt9lTSxAYd83fXx2elrc%2F640%3Ffrom%3Dappmsg%23imgIndex%3D4)

即在验证集子任务 Tₖ 上，有技能 Sₖ 和无技能的准确率差值。只有 Δₖ \> 0 的技能才会被保留，并且按 Δₖ 排序，取 Top-M。这确保了模型只依赖那些它还没学会的技能，学会的技能会被果断抛弃。

### 2.4 奖励设计：既要成功，又要压缩

为了激励模型内化技能并压缩 Context，SKILL0 设计了复合奖励：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fcv2qnxtPoVibvzwj8uGeFsXuhvoJaNv3ZOl1atdsSQiauVILibRGstALicw1lK5x0t6UYl8qRLU8Hu7YibysX8r3wTKzGWUcGk394pUekqz38nQs%2F640%3Ffrom%3Dappmsg%23imgIndex%3D5)

其中 r\^(comp)ₜ = (cₜ)。如果任务成功，奖励包含对数压缩率，鼓励模型用更少的 Token 完成任务；如果失败，压缩奖励为 0，防止模型为了省钱而胡乱压缩导致任务失败。

## 3. 实验结果：性能更强，成本更低

作者在 **ALFWorld** （具身智能文本游戏）和 **Search-QA** （搜索增强问答）上进行了全面评估。

### 3.1 主实验对比


|         Method         | ALFWorld Avg↑ | ALFWorld Cost↓ | Search-QA Avg↑ | Search-QA Cost↓ |
|------------------------|---------------|----------------|----------------|-----------------|
| Qwen2.5-VL-3B-Instruct |               |                |                |                 |
| Zero-Shot              | 15.2          | 1.21           | 15.9           | 0.48            |
| Few-Shot               | 29.3          | 2.30           | 17.9           | 0.86            |
| AgentOCR               | 78.2          | 0.38           | 34.2           | 0.26            |
| SkillRL                | 82.4          | 2.21           | 38.9           | 0.87            |
| **SKILL0**             | **87.9**      | **0.38**       | **40.8**       | **0.18**        |
| Qwen2.5-VL-7B-Instruct |               |                |                |                 |
| AgentOCR               | 81.2          | 0.43           | 40.1           | 0.36            |
| SkillRL                | 89.9          | -              | 47.1           | -               |
| **SKILL0**             | **89.8**      | **0.41**       | **44.4**       | **0.34**        |


> **解读** ：  
> - **性能碾压** ：在 3B 模型上，SKILL0 在 ALFWorld 上达到 87.9%，比强基线 AgentOCR 高出近 10 个点；在 Search-QA 上也提升了 6.6%。7B 模型同样保持领先。  
> - **零技能推理** ：注意 SKILL0 的推理是 Zero-shot（无技能注入），而 SkillRL 是 Few-Shot（有技能注入）。SKILL0 在没有任何外部提示的情况下，干掉了需要检索技能的对手。  
> - **Token 成本暴降** ：这是最惊人的。SkillRL 的推理成本高达 2.21k Token/step，而 SKILL0 只有 0.38k。**成本降低了近 6 倍** ，而且性能更好。这证明了技能内化不仅可行，而且极其高效。

### 3.2 训练动态：内化过程的可视化

SKILL0 是否真的在"内化"技能？训练过程中的准确率变化给出了答案。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fcv2qnxtPoV8dHDzl8OSnuqq80Dvl0fJwff3bwRdE07IEmRMZjT7YIPyePNEqpffCecxibDRBOTCBvcHoPchaNVO3rryQ1xqWFRonJyrM7Vew%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

图2： 训练动态对比：SKILL0在有无技能增强下的验证性能及与其他基线的对比。

上面这张图包含三个子图，信息量巨大。

子图 (a) 展示了 SKILL0 在训练过程中，"有技能"和"无技能"验证准确率的变化。可以看到，初期"有技能"的曲线远高于"无技能"，说明模型还依赖外部指导。但随着训练进行，"无技能"曲线快速上升，最终在 120 步左右追上甚至超过"有技能"曲线。这就是**技能内化** 的直接证据：模型不再需要 Skill 提示，自己就能做得一样好。

子图 (b) 和 (c) 则是在推理时完全不给技能的公平对比。SKILL0 不仅超越了 AgentOCR，而且在训练后期持续上升，没有像 GRPO 和 SkillRL 那样过早 plateau。这说明动态课程学习有效地避免了模型陷入局部最优，逼出了更高的性能上限。

### 3.3 技能预算消融：多少辅助轮合适？

技能预算 M 的衰减策略至关重要。作者对比了不同的预算设置。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fcv2qnxtPoV9duQsY5IcfcUo9YZgCqfibJWNyqCBgbElicsUmSGj2Ve42pM0qqSR6v63s8hsYxibBSb18YGom2QK7uHJhOLLlVnsLd4rAtw6nd4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

图3： 技能预算消融实验：不同预算设置下有无技能的推理性能对比。

该柱状图对比了五种预算策略。最左侧的 **\[6,3,0\]** 是 SKILL0 的默认设置（线性衰减到 0），它不仅在有技能时表现好，在去掉技能后（绿色柱子）反而提升了 1.6%。这反直觉的结果说明，**适度的技能依赖有助于模型探索，但最终必须彻底断奶** 。

反观 **\[6,6,6\]** （始终保持满技能），一旦去掉技能，性能暴跌 13.3%。这证明如果训练时一直给技能，模型会产生严重的路径依赖，根本学不到东西。**Fixed Full** 设置同样惨烈，下降 12.3%。这再次印证了"辅助轮必须拆"的道理。

### 3.4 子任务细粒度分析

SKILL0 在不同类型的子任务上表现如何？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fcv2qnxtPoV9oiaZuKbnxsNPFVNJ4CdV4feiarIQ4t1OtvhDMF6ewdsyXBZdwoXVHJ16hctxP0hmV69BFFvwH6llEknl7fPJjSkBR9gPfRz2SQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

图4： ALFWorld各子任务训练动态：SKILL0在六个具身操作任务上的技能内化过程。

从上面这组折线图可以看出，无论是"Look At Obj"还是"Pick And Place"，所有子任务都呈现出一致的"内化"趋势：初期 w/ skill 领先，后期 w/o skill 追上。特别是在"Pick Heat"这种复杂任务上，内化过程虽然缓慢但非常稳健，最终无技能推理准确率接近 0.8。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fcv2qnxtPoVickPxtc5Sszzq5gj9g6SicZAfMxqcyeicKoHAEvcl8djpnqobxtLwAF5bHEgl5sk64U3vRHyu9e7DrXNJFUtDiaDGM9aBJtdxOLUQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9)

图5： SearchQA子任务训练动态：SKILL0在四个搜索问答子任务上的准确率变化。

在 Search-QA 任务上，趋势同样明显。"Direct Retrieval"和"Multi Hop Reasoning"等子任务中，w/o skill 曲线都成功追平了 w/ skill。这证明 SKILL0 的内化能力具有泛化性，不仅适用于具身操作，也适用于复杂的搜索推理。

## 4. Vicky 的个人视角

### 4.1 真正的贡献是什么？

SKILL0 最大的贡献不在于刷榜，而在于**提出了"Skill Internalization"这一新范式** 。过去两年，大家都在卷 Skill Retrieval、Skill Evolution，默认 Skill 必须是外部知识库。SKILL0 证明了：Skill 可以是训练数据，而不是推理上下文。这为 Agent 的轻量化部署打开了一扇新门。

### 4.2 业内人士的潜台词

作者没明说，但懂行的人都能看出来：**Skill Bank 可能会逐渐消亡** 。如果模型能把技能内化，为什么还要维护一个庞大的外部技能库？未来的 Agent 架构可能会变成：离线蒸馏技能 -\> 在线强化学习内化 -\> 零技能推理。这不仅省钱，还更安全（没有检索注入攻击的风险）。

### 4.3 局限与未来方向

当然，SKILL0 也有局限。它依赖初始 SkillBank 的质量，如果初始技能很烂，内化出来的策略也会跑偏。此外，离线相关性分组在跨域时需要重新划分，灵活性有待提高。

接下来的方向很明显：

1. **自动化技能生成** ：能不能让模型自己生成初始 Skill，然后自己内化？形成完全自动的闭环。

2. **多模态技能内化** ：现在的 Skill 主要是文本，未来能否内化视觉操作技能、音频交互技能？

3. **终身学习** ：内化后的技能如何更新？当环境变化时，模型能否快速"遗忘"旧技能，"内化"新技能？

SKILL0 只是一个开始，但它指出的方向------**让 Agent 真正学会，而不是永远依赖外挂** ------绝对是正确的。

❤️❤️❤️如果这篇内容对你有帮助，欢迎点个赞、点个在看，也欢迎转发给更多有需要的朋友。你的每一次互动，都是我持续更新的动力。❤️❤️❤️

*** ** * ** ***

> 论文原文: https://arxiv.org/abs/2604.02268

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYzMzc3NTcyOQ==&mid=2247484349&idx=1&sn=97614f01cf74c8459a2c4713cba39217&chksm=f1c31ea2f6f04d903eb4609e6601dcaa37830c7e7eb02c224bf7cc39a5341dbb21ed5369d5e4&mpshare=1&scene=1&srcid=04063qifZQT3jJsffflItgSM&sharer_shareinfo=9eb3ba867f8a95656d6d98a126784b63&sharer_shareinfo_first=9eb3ba867f8a95656d6d98a126784b63)

