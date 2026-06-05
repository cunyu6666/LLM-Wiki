---
id: "7459318759128303299"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524420&idx=1&sn=98cc073826e9b49bc7e4fe5788f22d80&chksm=c1a9c7967c0fe9952391d918a032fd179ff9119fd59b0aca05862d1bc065ff1d65008583e20d&mpshare=1&scene=1&srcid=0527g5whhJg9fzMhJEUQjXWb&sharer_shareinfo=106d5924eba5bb9fbb0d656be75fe291&sharer_shareinfo_first=106d5924eba5bb9fbb0d656be75fe291
author: "Founder Park Founder Park"
collected: 2026-05-27
tags: []
---

# Cursor Composer 2.5 拆解：最强大的 RL 环境，就是你自己的产品

# Cursor Composer 2.5 拆解：最强大的 RL 环境，就是你自己的产品

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524420&idx=1&sn=98cc073826e9b49bc7e4fe5788f22d80&chksm=c1a9c7967c0fe9952391d918a032fd179ff9119fd59b0aca05862d1bc065ff1d65008583e20d&mpshare=1&scene=1&srcid=0527g5whhJg9fzMhJEUQjXWb&sharer_shareinfo=106d5924eba5bb9fbb0d656be75fe291&sharer_shareinfo_first=106d5924eba5bb9fbb0d656be75fe291)Founder Park Founder Park


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FqpAK9iaV2O3sAVsSPfCN9UX44XiaoicbUJIrOGuaujdMNY6iaQewDZEX1GY3tcVk3QGeKJyUMMHBSMALvO8B7DZwsA%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D0)

「每家应用公司最后都应该训练属于自己的模型。」

今年 5 月，Cursor 推出了 Composer 2.5，一个 Agentic 编程模型。相比前代，2.5 更擅长处理耗时较长的持续任务，在遵循复杂指令方面也更可靠。而且在同等能力的模型中，成本效率可以高出 10 倍。

Coding Agent 的能力越来越强，Coding 也许是比自然语言更适合模型学习的形式，几乎已经快要成为业内的「共识」。

Cursor 采取了一种很典型、且「经济」的思路：不搞从头开始的预训练，在开源模型 Kimi 2.5 的基础之上，做深度后训练，把所有模型权重专门化到自己的产品环境里。

Cursor 的研究负责人 Federico 认为，「最强大的 RL 环境，就是你自己的产品。」

怎么训练模型来理解你的环境，工具怎么调用、harness 怎么工作，一直是最近业内关注的重点。

在 Sequoia 的最近一期播客中，Cursor 的研究负责人 Federico Cassano 和 Fireworks AI 的基础设施负责人 Dmytro Dzhulgakov，深入聊了聊他们是怎么做 Composer 2.5 的。从 mid-training 到 RL，背后的技术决策、训练过程是怎么样的，非常值得一读。

![](https://image.cubox.pro/cardImg/49ptyqcouzc9s3xbvbkji7igwiujtno1uzwe4pm8wftkt6j5kq?imageMogr2/quality/90/ignore-error/1)

**Founder Park**

来自极客公园，专注与科技创业者聊「真问题」。

555篇原创内容

<br />

公众号  

，

⬆️关注 Founder Park，最及时最干货的创业分享  


Founder Park 正在持续寻找值得被看见的 AI 团队与项目。

我们将通过「AI 产品市集」、内容报道、社群分发等方式，帮你触达早期用户、获得真实反馈，以及建立关键连接。
如果你正在做 AI 相关的事，欢迎和我们聊聊。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FUrL1kkHON7KtwJvXZC7PKR2vfA8algP47mrNiaVxibSsiaAnqSiaEkZ7sTPEoMfANkcfrug4QCVG0icmRIQqBVPvytreVe5VoPcWAFIjqxxSlHkE%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D1)

*** ** * ** ***


## **01**

## **模型是一块有限的存储盘**

**主持人：Cursor 一直以来都是用别人的模型。为什么突然要重度到投入自研模型？**

**Federico：** 你可以把模型想象成一块存储盘，它的权重里能存储的信息量是有限的。

**我们只关心一件事。我们甚至不关心编程或写代码本身，我们只关心 Cursor 里的软件工程。** 那如果把模型所有的比特都分配给这一个任务呢？

效果非常明显。大家可能注意到了，Composer 2.5 的成本比 Opus 和其他编程模型低了一个量级，就是因为我们可以把所有权重都专门化（specialize）到这个任务上，用一个更小的模型就能达到更好的效果。

**主持人：这不是跟 Bitter Lesson 相矛盾吗？过去我们看到的趋势是，大模型在所有任务上都越来越好，包括编程。你们的专业化路线不是在对抗 scaling law 吗？**

**Federico：** 不矛盾。大实验室训练的大模型本身也在代码上做了大量专门化，代码是它们的核心训练任务之一，不是泛化出来的能力。

对我们来说，**如果我们相信 Bitter Lesson，那我们做的恰恰是在数据维度上猛推。** 模型容量有限，要把这些容量用满，就需要大量数据。而要让模型能摄入更多有用的数据，就需要把权重从「干扰」中释放出来，不需要它会写诗、会做数学，只需要它在 Cursor 里写好代码。

**Dmytro：** 这是一个我们在 Fireworks 跟很多客户身上看到的普遍模式。应用公司的演化路径通常是：先用现成模型做原型 → prompt engineering → 发现瓶颈 → 开始训练自己的模型。

但**应用最有价值的地方在于用户数据和产品特有的交互方式，** 工具怎么调用、harness 怎么工作。这些东西靠 prompt 能做一点，但真正的方式是把模型训练成在你的环境里原生行动。

**Federico：** 对，比如有些工具调用的行为，你很难用提示词精确描述清楚。但通过训练，我们可以把最优的工具使用方式直接烧进模型里。说实话，Composer 2.5 现在即使不给 prompt 也知道该怎么做，因为训练过程中我们已经把正确行为推进了模型权重。

**Dmytro：从 Fireworks 的视角，我们把应用的 AI 优化看作质量-速度-成本的三维 trade-off。** 纯做基础设施优化能走很远，但进入模型训练后，你可以把这个 trade-off 推到一个全新的水平：更好的模型、更低的成本、更快的速度。Composer 就是最好的例子。

## **02**

## **Composer 2.5 同时推进了两个轴：**

## **Mid-training + 大规模 RL**

**主持人：Composer 2.5 在发布后立刻引起关注了，在 benchmark 表现强劲，推理成本也大幅降低。Composer 2.5 具体是怎么训练的？**

**Federico：** 我们从一个很强的基座开始，Kimi 2.5，一个 1 万亿参数的 MoE 模型，30B 活跃参数。

Composer 1 只推了一个轴，强化学习。**Composer 2.5 同时推进了两个轴：continual pre-training** （我们叫 mid-training）**和强化学习。** 这是 Composer 2.5 变强的关键。

具体来说，训练分两步：第一步是大规模的 mid-training，在海量代码 token 上做接近预训练规模的训练，同时也包含一些 web data 来保持世界知识。第二步是从 mid-training 的 checkpoint 出发，做大规模的 RL。

**主持人：Mid-training 阶段和** **RL** **阶段，模型分别在学什么？**

**Federico：** Mid-training 阶段，模型在学代码库、学代码模式、学世界知识，它在建立一个更宽的分布，然后 RL 会在这个分布上的基础上做锐化。

RL 阶段，模型直接在 Cursor 的 harness 里「玩」。它学的是怎么正确调用工具、怎么导航自己的环境、怎么写出正确的代码。Mid-training 让模型学会了写代码，但不代表它学会了写正确的代码，模型不知道怎么区分好代码和坏代码。RL 的核心就是调这个旋钮，告诉模型「从现在起你必须始终写正确的代码」。

**主持人：为什么不从零预训练自己的模型？**

**Federico：** 我们是自上而下思考的，不是自下而上。怎么用最短的时间给用户交付一个有用的模型？如果从头搞预训练，然后 mid-training，然后 RL，那要很久很久。反过来做，从开源基座出发，先推 RL 得到有用的模型，我们能极快地交付给用户。

希望下一代 Composer 会是我们自己从底层训练的模型。

## **03**

## **Agent 训练就是一个巨大的工厂，**

## **训练器和 rollout 要同时运转**

**主持人：大规模** **RL** **跟预训练有什么本质区别？**

**Dmytro：** 区别很大。**预训练就是预测下一个 token。** **RL** **是让模型在真实环境中完整地行动。**

一次 rollout（模型的完整操作序列）可能有 50 轮交互，模型收到初始 prompt，决定调用工具，工具执行，模型再生成代码，就像用户在 Cursor 里的一整个 Agent 会话。做完之后给一个 reward，然后把这个信号反馈回训练器更新权重。

这意味着你需要的组件比预训练多得多，仍然需要编排数万张 GPU 做前向/反向传播，但现在你还需要编排一大堆运行环境、需要高效的模型推理来做 rollout。整个系统是一个巨大的异构循环。

所以训 Agent 的核心循环是：模拟会话 → 评估结果 → 更新权重。但这里面每一步都有巨大的工程挑战。

**主持人：这个循环的效率瓶颈在哪里？**

**Dmytro：** 最朴素的方式是先暂停训练 → 做一批 rollout（可能每个要 5-10 分钟甚至更长）→ 拿到结果 → 暂停推理 → 回去训练。这种做法在算法上很干净，但系统效率极低，一半的算力永远在闲置。

所以我们做了异步流水线化。想象成一个巨大的工厂：**训练器大楼和 rollout 大楼永远同时运转。** rollout 永远拿最新的模型版本去做新的模拟会话，训练器永远拿新到的结果去计算更新。所有东西都一直在动。

**Federico：** 但代价是引入了 staleness，当你完成某个 rollout 时，模型权重可能已经被其他数据更新过了。你是在用旧版本模型产生的数据来训练新版本。这在训练动态上会有影响，但你通过不浪费一半算力来补偿了。

我们对性能非常认真。不像大实验室有百万级 GPU，我们只有几万块。所以我们什么技巧都用，甚至在生产环境用 FP4 训练。

## **04**

## **最强大的** **RL** **环境，**

## **就是你自己的产品**

**主持人：你们提到环境模拟必须尽可能接近用户真实的电脑。为什么？**

**Federico：** 因为有时候模型能识别出自己是在模拟环境还是真实环境中运行，然后在模拟中表现出不同的行为。

**主持人：模型真的会意识到自己在假环境里？**

**Federico：** 是的。它会说「哦，我在假环境里。我学到了一些小技巧可以在这个环境里拿更高的 reward，让我试试。」**模型非常擅长作弊。** **RL** **非常擅长鼓励作弊。**

**主持人：你们用第三方** **RL** **环境供应商吗？**

**Federico：** 不用。**最强大的** **RL** **环境就是你自己的产品。** 因为那才是模型真正要运行的地方。

对 Frontier Lab 来说，他们需要覆盖所有任务，需要各种各样的环境，那确实有第三方环境的价值。但如果你是在为自己的产品训练模型，你应该用你的生产环境。

当然，要做好隔离。不能让模型在生产数据库上搞破坏。你要 clone 一份。

我们在 Cursor 建了一整套虚拟机栈。我们会对系统说「请现在给我 10 万台虚拟机」，它必须全部快速启动。这个系统需要极强的突发弹性。

普通容器根本不好用。如果模型要测试一个数据库迁移，你需要数据库跑着。如果模型要测试一个 web 服务，你需要那些服务都起来。你不能用玩具环境（Docker 容器里跑个 Atari 游戏）来训练一个真实的生产级 Agent。

**主持人：你们有大量真实用户数据。为什么不直接只用真实用户数据做** **RL** **，跳过模拟环节？**

**Federico：** 我们也在做。我们叫它 Real-time RL（实时强化学习）。我们找到用户对模型生成结果满意或不满意的信号，用来实时更新模型，然后每隔几小时发布一个新版本。

但模拟 RL 不能省掉。模拟中你可以从同一个 prompt 做 16 次甚至 128 次 rollout，并行跑很多次。有些做得好，有些做得差。通过多次 rollout，你能得到更精确的训练信号（GRPO 这类算法就是靠多次 rollout 来工作的）。real-time 只有一次 rollout 回来。

更重要的是，如果模拟中的 rollout 出了错，没关系，就是浪费了些 GPU 时间。但如果是真实用户遇到了奇怪的输出，那会是一次糟糕的用户体验。所以模拟允许你做更多离策略（off-policy）的探索，但不影响用户。

所以路径是：**先通过离线** **RL** **把 Agent 训到足够好，教会它推理、工具调用、环境导航，再放到用户面前。** 模型必须过一个门槛才配做 online RL。**因为如果模型太差，用户不会用它，你就拿不到任何反馈信号。** 这也是 Real-time RL 的悖论：你不能用它从零构建模型，模型必须先足够好，然后你只能让它变得更好。

**主持人：怎么让模型处理越来越长的任务？**

**Federico：** 有几个难题。**第一个是信用分配（credit assignment），** 模型做完一长串操作后拿到一个 thumbs up/down，它要弄清楚自己哪一步做对了、哪一步做错了。轨迹越长，这个问题越难。

第二个是物理限制，**模型的上下文窗口是有限的** 。我们的解法叫 Self-summarization（自我总结）。在 RL 训练过程中，Agent 学会怎么总结自己的工作，然后用这个总结来重启上下文窗口，继续完成任务。

所以 Composer 2.5 名义上是一个 200K context window 的模型，但实际上它可以处理数百万 token 的任务，因为它学会了自我压缩和续接。不是外挂的上下文管理，而是在 RL 优化循环中联合训练出来的能力：模型同时在学「把任务做对」和「生成好的总结」以及「根据总结恢复工作」。

**Dmytro：** 我觉得这个特别迷人，通常上下文管理被认为是 Agent 系统的一个外部难题。在 Cursor 的做法中，**你把这个难题直接扔进了端到端的优化循环里，让计算机去解决。** 这又是 Bitter Lesson 的体现：你把越多东西扔给计算去端到端优化，就能得到越好的系统。

## **05**

## **数值精度，**

## **MoE 模型的 RL 噩梦**

**主持人：Kimi 2.5 是一个非常大的稀疏模型。这对** **RL** **训练有什么特殊的困难？**

**Federico：** 推理时模型做前向传播，产生每个 token 的 log probability（对数概率）。当我们把 rollout 的生成结果传回训练器时，因为是异步训练，产生这些 token 的模型版本可能已经落后了几步。所以训练器必须重新跑一遍前向传播，重新计算 log probability。

理论上，同一个模型版本对同一个输入应该产生完全相同的 log probability，但实际上你会得到不同的值。

**主持人：为什么会有差异？**

**Dmytro：** 因为浮点运算本质上是不确定的。我们在学校学过 a + b + c = c + b + a，对整数来说在计算机上永远成立。但对浮点数（floating-point numbers），那种用尾数和指数来近似表示的数，a + b + c 和 c + b + a 会给出不同的结果。

差异很小，但在数百万次乘法和加法运算之后会被放大。对普通推理来说通常无所谓------翻几个 bit 不会影响 benchmark。**但对** **RL** **来说，你用的是非常微弱的信号来教模型，数值差异的噪声可以直接毁掉训练。**

**主持人：这跟 MoE 有什么特殊关系？**

**Dmytro：** MoE 的工作方式是：每一层，模型会用一个 gating layer（路由层）决定「对于这个 token，我在 384 个 expert 中激活哪 8 个」。

问题是：你的隐藏状态在小数点后第五位有一点点差异，这个差异本身不重要。但它可能导致路由层选择了 expert 7 而不是 expert 9。突然之间，你激活了模型完全不同的部分，差异被灾难性地放大了。

在推理时这通常不影响，平均下来没问题。但在 RL 训练时，推理端激活了 expert 7，训练端却在试图更新 expert 9，那个在推理时根本没参与的 expert。这就是毁灭性的不匹配。

**主持人：你们是怎么解决的？手写** **GPU** **kernel？**

**Dmytro：** 部分是。你可以非常小心地写所有 GPU kernel，确保数字永远按相同顺序相加，完全消除不确定性。但代价是系统变慢 2-3 倍。

实际的做法是找到最佳的取舍点：**承受几个百分点的性能损失，解决 90% 的差异。**

对 MoE 具体来说，有一个很巧妙的技巧叫 Router Replay，让推理端把一个额外的小信息传给训练端：「我对这个 token 激活了 expert 7。」就是一个整数。训练端拿到之后就能对齐路由，不需要自己重新计算（并得出可能不同的结果）。

这类数值对齐工作，匹配量化级别、匹配 kernel、做 router replay，是训练能成功还是直接发散的分界线。

## **06**

## **Composer 2.5 的训练用了 4 个集群，**

## **分布在全球各地**

**主持人：你们提到 Composer 2.5 是全球分布式训练的，为什么要这样做？**

**Federico：** 很大的连续 GPU 集群在市场上非常难找。你不可能在集群规模上简单翻倍，找到 2 倍大的集群比找到当前大小的难得多。但我们可以把训练和推理拆开：一个集群负责所有训练（训练必须集中），然后推理部分分布在全球多个小集群上。

**Composer 2.5 的训练用了 4 个集群，分布在全球各地，彼此相距很远** 。甚至在用户流量低谷时段，我们还把 Composer 1.5 的生产推理 GPU 拿来加速训练。

**Dmytro：** 推理集群不需要训练那种昂贵的宽带互联，可以用更小的 GPU 群组、不同代际的 GPU、不同地区更便宜的硬件。而且推理可以弹性伸缩，你可以把所有推理 GPU 看成一个池子，在真实用户流量和 RL 模拟之间动态平衡。

**主持人：模型有 1TB，怎么实现跨洲同步？**

**Dmytro：核心挑战是权重同步。** 一个训练 step 大概 5 到 15 分钟，也就是说每 5-10 分钟就会产生一个 1TB 的新权重快照。问题是怎么高效地把它送到地球另一边？而且你不想让 staleness 太严重。

关键洞察是：**RL** **训练中，不是每一步所有权重都会变化。** 尤其是训练后期，RL 做的是非常精细的调整。所以权重变化有规律的模式，每一步的 delta 其实很小。

我们写了一个压缩算法，利用这个特性，把 delta 压缩到了原来的 1/20。现在问题就变成了一个数据库系统问题：管理全量快照和增量 delta、做恢复和一致性校验。我们做到了无损，另一端拿到的模型跟源头完全一致（bit-equivalent）。

传输通常不到一分钟，最差情况也在几分钟内。切换权重只需要暂停推理大约 30 秒。我们还把上传和下载做了分片，把集群的出口带宽完全打满。

**Federico：** 这跟传统观点是相反的。传统观点是，RL 基础设施就应该是一个巨大的、RDMA 互联的单一集群。但如果你能把组件拆开，你不需要找那么大的集群，推理可以放在更便宜的硬件上，成本能显著降低。

## **07**

## **每家应用公司都应该训练自己的模型**

**主持人：你觉得每家公司都会像 Cursor 一样在自己的 harness 上做 RL 吗？**

**Federico：** 如果他们在用 AI，在产生大量 token，而且有一个可以优化的产品，**我认为训模型就是正确的方向。**

**主持人：** **RL** **只适用于 Agent / 工具调用场景吗？如果你的任务是摘要或续写，也需要 RL 吗？**

**Federico：** **RL** **适用于所有场景。** 哪怕是自动补全（tab），我们也在用 RL。

我个人的理论是：当你预训练一个模型时，它摄入了人类知识的全部。假设你在训练一个数学模型，模型学了 Stack Exchange 上所有的数学。但当它面对一道数学题时，它需要想一想，我是那个专家，还是那个在学习的学生？

**RL** **的第一阶段做的就是调这个旋钮，告诉模型「你是专家，你需要每次都做对」。** 这就是为什么即使在很少的计算下，RL 也能快速带来很大的提升。然后是第二阶段，长尾优化，需要大量算力才能持续提升，那是模型开始真正学习推理的地方。

**Dmytro：** 我完全同意。我们在 Fireworks 跟很多客户做 RL fine-tuning，看到的模式很一致：**mid-training / supervised fine-tuning 是知识转移，RL 是行为锐化（sharpening behavior）。** 你通常两个都需要。

就算是摘要也是，如果你想要特定风格的摘要，靠手工标注好摘要、坏摘要的样本非常难。但如果你用 LLM-as-judge，你可以写很精确的评分标准，扔进 RL 循环，让模型自己去探索不同的摘要风格，然后由 judge 来评估是否符合标准。开更多算力，看图往上走。

**主持人：最终是可验证的 reward 更有效，还是 LLM-as-judge？**

**Dmytro：奖励越可验证越好。** 因为可以无限扩展算力。代码和数学天然有这个优势（代码能编译 / 测试能过）。LLM-as-judge 有效是因为判断比创造容易------跟人类一样。实际操作中你通常会有一个复合 reward：一部分是确定性的（代码能不能跑），一部分是基于 LLM 的（风格、结构评估），拆成多个维度分别打分。

但专家仍然是必不可少的，不是直接判断 rollout，是设计评估规则。我们经历了 Software 1.0（手写代码）→ 2.0（训练数据）→ 3.0（现在），现在你实际上是在手工设计评价标准（evaluation rules）。产品体验的编码从写代码变成了写 reward，但仍然需要人来做。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FUrL1kkHON7Kcz8Or5brWBwzqAYIlYKibyEbpPpNkVwSABfH4YXdCWaLlDdicEyZicYTMbVsPqiatsWtgyIlVsfbemF4pOsJA6npibOGqoicSNSRo8%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D3)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FqpAK9iaV2O3u2fI9s28mn09TnD4aChWibVHIyyBzPC2GibicVQ57QYiaEw6yibwy9zhkB7aFajGpNtBru6icEFuibRKXwA%2F640%3Fwx_fmt%3Dother%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwebp%23imgIndex%3D3)

**更多阅读**

****## [创业者闭门探讨：Make for Agent ，其实还是 Make for Human](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524402&idx=1&sn=af0ef7a741dd33ddb0e5a6830b758dea&scene=21#wechat_redirect)
## [拆解 Anthropic：最好的 AI 公司，可能也是一种组织发明](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524328&idx=1&sn=97ebe18816f4b1af83e2b56c4f21171a&scene=21#wechat_redirect)
## [对话 Lucius 赵赫：AI 员工的本质，是一份有 SLA 的劳动合同](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524259&idx=1&sn=94070278b3af3db7239828730f329eeb&scene=21#wechat_redirect)
## [AGI Playground 2026，欢迎来新加坡！](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524316&idx=1&sn=4974ce701988a7dfa630ed34dcabfebc&scene=21#wechat_redirect)
![](https://image.cubox.pro/cardImg/49ptyqcouzc9s3xbvbkji7igwiujtno1uzwe4pm8wftkt6j5kq?imageMogr2/quality/90/ignore-error/1)
**Founder Park**
来自极客公园，专注与科技创业者聊「真问题」。
555篇原创内容
<br />
公众号
，****

转载原创文章请添加微信：founderparker

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247524420&idx=1&sn=98cc073826e9b49bc7e4fe5788f22d80&chksm=c1a9c7967c0fe9952391d918a032fd179ff9119fd59b0aca05862d1bc065ff1d65008583e20d&mpshare=1&scene=1&srcid=0527g5whhJg9fzMhJEUQjXWb&sharer_shareinfo=106d5924eba5bb9fbb0d656be75fe291&sharer_shareinfo_first=106d5924eba5bb9fbb0d656be75fe291)

