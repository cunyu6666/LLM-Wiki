---
type: index
description: "小红书笔记 · 2026-06-20 抓取（批量）"
timestamp: 2026-06-20
---
# Loop Engineering 是什么｜8 张图讲透

> 小红书笔记 · 2026-06-20 抓取（批量）
> Raw：[raw/小红书/Loop Engineering 是什么｜8 张图讲透_6a2bdb14000000001503dc0e.md](../../raw/小红书/Loop Engineering 是什么｜8 张图讲透_6a2bdb14000000001503dc0e.md)
> 作者 ID：`5652a49e62a60c290444c4ba`（未登录态无昵称）
> 数据：197 赞 / 311 收藏 /  评论 / 8 图
> 分类：AI Agent 开发

---

## 摘要

这两周 timeline 全在聊 Loop Engineering，我把它整明白了，顺手做成了 8 张图。
说白了就一句话：别再一句句手写 prompt，改成设计一个会自己派活、检查、记录、再接着干的闭环，让这套系统去 prompt agent，而不是你盯着键盘一轮一轮敲。Claude Code 负责人 Boris Cherny 原话——"写 loop 才是现在的工作"。
为什么是现在不是去年？不是模型突然变强，是搭这种闭环要的零件——定时触发、隔离分支、skills、连接器、子代理，再加一个外部记忆——现在全内建进 Codex 和 Claude Code 了；去年你还得自己写一堆 bash 自己维护。
但别上头。它有三件事解决不了，而且 loop 越顺反而越要命：验证还是你的责任、你对代码的理解会越欠越多、最舒服的那个"啥都不想直接收货"最危险。所以我最喜欢它的收尾——build the loop, stay the engineer，搭你的循环，但继续当那个工程师。
图里从"是什么"一路拆到"怎么落地"。觉得有用先收藏～下一篇拆怎么从 0 搭你自己的第一个 loop。
#LoopEngineering[话题]# #循环工程[话题]# #ClaudeCode[话题]# #Codex[话题]# #AI编程[话题]# #AIagent[话题]# #提示词工程[话题]# #程序员[话题]# #AI工具[话题]# #vibecoding[话题]#

## 关键要点

_见 raw 文档 OCR 全文_

## 与本 Wiki 的关联

- [[AI Agent 开发]]

---

*版本：v1.0 · 抓取日期 2026-06-20 · 标签 `#AI Agent 开发`*
