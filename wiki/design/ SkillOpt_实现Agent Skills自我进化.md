---
type: index
description: "小红书笔记 · 2026-06-20 抓取（mega batch #2）"
timestamp: 2026-06-20
---
# 🔧 SkillOpt：实现Agent Skills自我进化

> 小红书笔记 · 2026-06-20 抓取（批量 #2）
> Raw：[raw/小红书/ SkillOpt_实现Agent Skills自我进化_6a1476c60000000008026716.md](../../raw/小红书/ SkillOpt_实现Agent Skills自我进化_6a1476c60000000008026716.md)
> 作者 ID：`6707bd58000000000d025614`（未登录态无昵称）
> 数据：299 赞 / 447 收藏 / 8 评论 / 7 图
> 分类：AI Agent 开发

> ⚠️ **可读性说明**：原图为英文内容（GitHub README / arXiv 论文截图），OCR 保留英文原文。如需中文理解，请结合 desc 摘要。

---

## 摘要

❓ Skill该怎么写
写一段好的 skill prompt 往往比调模型还重要。但现在常见的做法（手写、LLM一次生成、或者让模型自己改）都不太靠谱，核心问题是缺乏具体的「优化规则」：训模型的时候，有 batch、有学习率，但改 prompt 呢？基本还是凭感觉。
-
💡 文本空间优化
SkillOpt的思路是把skill当成模型的外部参数，像训神经网络一样训它：
- rollout batch：用当前 skill 跑一批任务，收集成功/失败轨迹；
- edit budget → 学习率：每次只允许做有限次 add/delete/replace 编辑，编辑太多容易过拟合；
- held-out validation gate → 验证集：候选 skill 必须在 unseen 数据上优于当前版本，不然直接拒绝；
- rejected-edit buffer → 负反馈：被拒绝的编辑存起来，提醒优化器下次别犯同样的错误；
- epoch-wise slow/meta update → 动量：每隔一段时间做一次全局复盘，保护长期有用但短期看不出效果的模式。
-
📊 实验结果
在 6 个 benchmark、7 个模型、3 种执行方式（direct chat、Codex、Claude Code）的 52 个配置中，SkillOpt 全部最优或并列最优。
实验还发现，优化一整轮实际上只需要 1-4 次 accepted edits，说明大部分候选编辑其实都是无效的；优化后的skill在不同模型、环境、benchmark上依然维持较好的效果。
-
🌟 研究总结
这篇论文最有价值的地方在于证明了一件事：「文本空间」的优化可以和「参数空间」的优化一样，有全套的训练纪律。
因为Prompt调优的过程本质上是在做手动梯度下降，SkillOpt相当于直接把这个过程自动化了，而且整体的部署产物只是一个小文件 best_skill.md（300-2000 tokens），不需要改模型权重，不需要推理时多调任何模型。所以以后做 agent evaluation 的时候，与其一遍遍手工改 prompt，不如跑一次 SkillOpt 循环。
#Skill[话题]# #agent[话题]# #llm[话题]# #大模型[话题]# #算法[话题]# #nlp[话题]# #论文分享[话题]# #人工智能[话题]# #智能体[话题]# #微软[话题]#

## 关键要点

_见 raw 文档 OCR 全文_

## 与本 Wiki 的关联

- [[AI Agent 开发]]

---

*版本：v1.0 · 抓取日期 2026-06-20 · 标签 `#AI Agent 开发`*
