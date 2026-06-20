---
id: "6a2a20c7000000000e031400"
source: 小红书
author_id: "61d67d89000000001000c76b"
url: https://www.xiaohongshu.com/explore/6a2a20c7000000000e031400?xsec_token=ABusxZOWM2_Ki3cid9xDlz_fnO7ZbFHO7Mv3tNxrTMgjA=&xsec_source=pc_collect
tags: ["AI Agent 开发", "AI", "批量入库"]
liked: 75
collected: 70
comments: 1
images: 7
ocr_engine: macOS Vision API (VNRecognizeTextRequest, accurate, zh-Hans + en)
captured: 2026-06-20
batch: "xhs mega batch #1 (10 notes)"
---

# Anthropic Deep Research: 多智能体架构

> 抓取日期：2026-06-20
> 数据：75 赞 / 70 收藏 / 1 评论 / 7 图
> 作者 ID：`61d67d89000000001000c76b`（未登录态无昵称）
> OCR：macOS Vision API

---

## 原文摘录

> 为什么 Multi-Agent 能赢？Anthropic 给了一个很反直觉、却很核心的结论：
	
Multi-agent systems work mainly because they help spend enough tokens to solve the problem. （Multi-Agent 之所以有效，主要是因为它们能花掉足够多的 token 来解决问题。）
	
#大模型[话题]#  #ai[话题]# #aiagent[话题]# #AI编程[话题]# #mle[话题]# #aicoding[话题]# #ai学习[话题]# #机器学习[话题]# #编程[话题]# #程序员[话题]#

---

## OCR 全文（7 张图）

### 第 1 张图

![[imgs/6a2a20c7000000000e031400/1.jpg]]

Anthropic发布了一篇很好的工程博客，讲他们如何用 Multi-Agent 架构来构建 Deep
Research 功能。这是一个非常典型的 Multi-Agent架构，有很多有价值的创新和实践经验，值得 Al Engineer 学习。
原文：How we built our multi-agent research system
一、为什么要用Multi-Agent？
Anthropic 给 Deep Research 的定义：开放式（open-ended）的问题，很难提前预测需要哪些步骤。你没法为探索复杂主题写死一条固定路径，因为这个过程本身是动态的、路径依赖
（path-dependent）的—随着调查展开，需要灵活地转向或追查旁支线索。
正因为这种开放性，Multi-Agent 架构很合适，原因：
1. 并行探索：多个 subagents 同时进行，各目币独立的 context window，探索问题的不同
侧面。
2. 关注点分离 （separation of concerns）：每个 subagent 有自己独立的工具、prompt 和
探索轨迹，这降低了路径依赖，让每条调查更深入、更独立。
3.突破单 context 上限：研究要处理的信息常常超出 Single-Agent 的 context window，多
个 Agent 分摊就能装下更多。
效果有多好？Anthropic 给了一个数字：用 Claude Opus 4 当 lead agent, Claude Sonnet 4
当 subagents 的 Multi-Agent 系统，在内部研究评测上比 Single-Agent（用 Opus 4）高出
90.2%。
一个经典例子：找出 S&P 500里所有IT 公司的董事会成员。这种需要广度优先、同时铺开多
条搜索的任务，Single-Agent 顺序搜索会失败；多个 subagents 并行分工就能搞定。

### 第 2 张图

![[imgs/6a2a20c7000000000e031400/2.jpg]]

二、架构：Orchestrator-Worker 模式
核心是一个 指挥官-工人（Orchestrator-Worker）模式：
•Lead Agent： 分析问题、制定策略、把计划存到外部记忆（memory，防止 context 溢
出），然后派出多个 subagents。
•Subagents：每个拿到一个具体任务，独立去搜索，用 interleaved thinking评估结果，再把过滤后的发现返回给lead。Subagent 的角色就像一个"智能过滤器"。
•CitationAgent：最后专门负责给结论标注引用来源。
下面这张图是系统的整体结构—一个 Le32Fi保协调，多个 Subagents 在下层并行干活：
用户提问
Lead Agent（指挥官）
存入计划..context 溢出后取回计划过滤后的发现过滤后的发现过滤后的发现
Memory 外部记忆Subagent 1Subagent 2Subagent 3CitationAgent 标注引用
并行调用工具/搜索并行调用工具/搜索并行调用工具/搜索带引用的最终答案

### 第 3 张图

![[imgs/6a2a20c7000000000e031400/3.jpg]]

如果按时间顺序看，整个流程是这样的，注意Lead 汇总后可以回头补充研究，形成一个循
环：
① 用户提问
② Lead 思考+制定计划
存入 memory
③ 并行派出3-5个
Subagents
④ 每个 Subagent 并行调用需亞外予
3+工具搜索
⑤ Lead 汇总结果
判断是否需要补充研究
已经足够
⑥ CitationAgent 标注引用
⑦ 返回带引用的最终答案
关键在于并行：Lead 一次起3-5个 subagents，每个 subagent 又并行调用多个工具。对复
杂问题，研究时间最多能减少 90%。

### 第 4 张图

![[imgs/6a2a20c7000000000e031400/4.jpg]]

三、并行的代价：Token 经济学
天下没有免费的午餐。并行很快，但很烧 token：
• 普通 chat：基准
• Single-Agent： 约 4倍 token
• Multi-Agent： 约15倍 token
所以一条重要原则：只有当任务价值足够高，能覆盖这个成本时，才值得用 Multi-Agent。
为什么 Multi-Agent 能赢？Anthropic 给了一个很反直觉、却很核心的结论：
Multi-agent systems work mainly because they help spend enough tokens to solve theproblem.（Multi-Agent 之所以有效，主要是因为它们能花掉足够多的token来解决问
题。）
数据也支持这点：在 BrowseComp评测上，token 用量、工具调用次数、模型选择这三个因素一起能解释 95% 的性能差异，其中仅 token用量一项就解释了80%。换句话说，给任
务"喂"足够多的token 去探索，本身就是性能的主要来源—而 Multi-Agent 正是一种把 token
用量扩展到 Single-Agent装不下的程度的方式。

### 第 5 张图

![[imgs/6a2a20c7000000000e031400/5.jpg]]

四、Prompt Engineering 的关键经验
每个 Agent都由一段prompt 来驱动，所以正如原文所说：“prompt engineering是我们改
进这些行为的主要杠杆（primary lever）。“ Anthropic 总结了8条原则：
1. Think like your agents（像你的 Agent一样思考）：一步步观察 Agent 的行为，才能看
清失败模式（派了太多 subagents、query 太啰嗦、用错工具）。
2. Teach the orchestrator how to delegate（教指挥官如何分工）：派任务时必须写清楚
—目标、输出格式、用什么工具、边界在哪。
3. Scale effort to query complexity（让投入匹配问题复杂度）：在 prompt 里写明规则。简单事实=1个 agent/3-10次调用；对比类 =2-4个 subagents；复杂研究=10+个
subagents 分工。
4. Tool design and selection are criti a） 157设计与选择至关重要）：把工具接口当成
UX来设计。Agent选错工具几乎必败，每个工具要有清晰、互不重叠的描述。
5. Let agents improve themselves（让 Agent 自我改进）：Claude 4能自己诊断失败、
改进 prompt。一个"工具测试 Agent"重写工具描述后，让后续 Agent 的任务完成时间減少了 40%。
6. Start wide, then narrow down（先宽后窄）：先用简短、宽泛的 query，看看有什么，
再逐步收窄—这模仿了人类专家的研究方式。
7. Guide the thinking process（引导思考过程）：用 extended thinking 当"可控的草稿
纸"。Lead 用它来规划；Subagents 在每次工具调用后用 interleaved thinking 评估质量、
找差距、优化下一步。
8. Parallel tool calling transforms speed（并行调用工具，大幅提速）：Lead 并行起
subagents，subagent 又并行调工具，把复杂研究的时间最多压缩 90％。

### 第 6 张图

![[imgs/6a2a20c7000000000e031400/6.jpg]]

五、评估（Evaluation）
•从小处开始：用约 20个真实场景的 query 就够了，早期迭代的影响巨大（成功率能从
30%提到 80%）。
•LLM-as-judge：用一个 prompt 给 0.0-1.0的分数，按多个维度打分：事实准确性、引用准确性、完整性、来源质量、工具效率。
•人工评估不可省：人能发现LLM 评委漏掉的问题，比如 Agent偏爱 SEO 内容农场，而不是权威的学术 PDF。
六、生产环境的挑战
把 Agent 放到生产环境，会遇到普通软件没有的难题：
•状态与错误累积：Agent 长时间运行并保持状态，一个小错误会层层放大。对策：用可持久化的执行、checkpoint 续跑、让 Agent优雅地应对工具失败。
•非确定性调试：同样的 prompt，每次运行决策都可能不同。对策：做完整的 productiontracing，监控决策模式。
•部署协调：更新时 Agent 可能正跑到一半。对策：用 rainbow deployment，新旧日版本同时在线，逐步切流量。

### 第 7 张图

![[imgs/6a2a20c7000000000e031400/7.jpg]]

六、生产环境的挑战
把 Agent放到生产环境，会遇到普通软件没有的难题：
•状态与错误累积：Agent 长时间运行并保持状态，一个小错误会层层放大。对策：用可持久
化的执行、checkpoint 续跑、让 Agent优雅地应对工具失败。
•非确定性调试：同样的prompt，每次运行决策都可能不同。对策：做完整的 production
tracing，监控决策模式。
•部署协调：更新时 Agent 可能正跑到一半。对策：用 rainbow deployment，新旧版本同时
在线，逐步切流量。
要点速记
•Why：研究任务不可预测、信息超出 Single-Agent context、可并行 Multi-Agent。
•架构：Orchestrator-Worker,Lead 分工 + Subagents 并行 + CitationAgent 引用。
•数字：比 Single-Agent 高 90.2%；时间省 90%；但token 是 chat 的15倍；token 一项
就解释 80%（三因素共 95%）的性能差异。
•核心结论：Multi-Agent 有效，主要是因为它能"花掉足够多的 token 来解决问题"。• Prompt:prompt engineering 是主要杠杆—分工要具体、投入匹配复杂度、工具设计即
UX、先宽后窄、让 Agent 自我改进、善用并行。
一句话：Multi-Agent 适合高价值、可并行、信息量超过单个 context 的任务；但要靠精细的
prompt engineering、好的工具设计、扎实的评估，以及能扛住长时间运行的生产系统。

---

## 抓取与 OCR 说明

- 抓取方式：`curl` + iPhone Safari UA + Referer（无需登录）
- HTML 提取：`__INITIAL_STATE__` 中 `undefined` 替换为 `null`，括号状态机解析
- 图片下载：curl 直连 `sns-webpic-qc.xhscdn.com`
- OCR：macOS Vision API（`VNRecognizeTextRequest`，accurate 级别，zh-Hans + en）
- 阅读顺序：按视觉坐标 `y` 降序 + `x` 升序重建

## 元数据

- 抓取日期：2026-06-20
- 点赞/收藏/评论：75 / 70 / 1
- 图片数：7 张（已存档 `imgs/6a2a20c7000000000e031400/1.jpg` ~ `7.jpg`）
- 作者 ID：`61d67d89000000001000c76b`（未登录态无法解析昵称）

[[Anthropic Deep Research: 多智能体架构|wiki 索引版]]
