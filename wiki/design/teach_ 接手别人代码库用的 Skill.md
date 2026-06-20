---
type: index
description: "小红书笔记 · 2026-06-20 抓取（mega batch #2）"
timestamp: 2026-06-20
---
# /teach: 接手别人代码库用的 Skill

> 小红书笔记 · 2026-06-20 抓取（批量 #2）
> Raw：[raw/小红书/teach_ 接手别人代码库用的 Skill_6a23ae570000000015024862.md](../../raw/小红书/teach_ 接手别人代码库用的 Skill_6a23ae570000000015024862.md)
> 作者 ID：`6527b906000000002a035523`（未登录态无昵称）
> 数据：362 赞 / 630 收藏 / 3 评论 / 1 图
> 分类：AI编程与Vibe Coding

> ⚠️ **可读性说明**：原图包含中英文混合内容，OCR 已尽量按视觉顺序重建，少量 Vision API 识别错误已手工修正。

---

## 摘要

有人问Matt：我正在接手别人的代码库，需要一个快速理解代码的方式。你有对应的Skill吗？
	
Matt回复：
/teach me about this codebase
It’s in the in-progress folder.
	
意思是：Matt的skills repo里有一个还在开发中的 Skill，叫/teach，使用这个Skill让它教你即可。
	
[拔草R] 根据Github描述打开方式大概是这样：
	
先在repo根目录跑 /teach，提示词写成：teach me about this codebase，建立学习地图。
	
知道大概结构后，跑/zoom-out，让它从系统层解释某个陌生模块。README里对/zoom-out 的描述就是让agent对陌生代码区域给更高层视角。
	
这两步是know-how，可以大胆询问，但是接下来涉及行动记得备份代码库。
	
然后它应该先问你mission。你可以这样回答：
	
我的目标是快速接手这个repo。你要教我看懂项目结构、核心模块、运行方式、测试方式、数据流、危险区域，并知道下一步该用 /grill-with-docs、/review、/improve-codebase-architecture 还是 /tdd。
	
之后它会把这个目标写进MISSION.md。接着它会建立术语表，比如repo里的核心概念、模块名、业务实体、测试名词。再把高信任资源写进 RESOURCES.md，这里可能包括项目 README、CLAUDE.md、CONTEXT.md、docs/adr、package.json scripts、测试文件、关键源码路径。
	
最后，它会逐步生成学习记录，比如用户已理解worktree与branch的区别、用户已理解该项目入口文件和构建命令、用户已理解某个核心模块的边界。这些学习记录后面会继续影响Claude Code怎么教你。
	
所有的Skill都是Matt自己的，我有一篇笔记叫《人类满分程序员Skill Repo导览》，程序员必须掌握 engineering 这个文件夹的内容，辅助素材在Matt 的AIhero.dev，有视频详解，记得订阅。
	
另外，/teach是一个开发中的Skill，意味着不完善或会被迭代和替换。记得在评论区分享这个用后感，或者来我直播间聊一聊你还有什么场景是需要一个Skill 解决的。

## 关键要点

_见 raw 文档 OCR 全文_

## 与本 Wiki 的关联

- [[AI编程与Vibe Coding]]

---

*版本：v1.0 · 抓取日期 2026-06-20 · 标签 `#AI编程与Vibe Coding`*
