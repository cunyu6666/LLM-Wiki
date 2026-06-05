---
id: "7420001431140174506"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247867508&idx=1&sn=01e810d49e693b961a1503ef3a690257&chksm=e91ba2c894ead487715e0fcb6ab617445b3b51e70171e4e339bd72bc64e92c7897626cbf2305&mpshare=1&scene=1&srcid=0208BWx9uuEMzvH0bkDbt4i2&sharer_shareinfo=00305bc5f4fa1eced41723009cdfaffd&sharer_shareinfo_first=00305bc5f4fa1eced41723009cdfaffd
author: "关注前沿科技 量子位"
collected: 2026-02-08
tags: []
---

# AI编程节省95% token，工具调用上限狂飙20倍，开源记忆系统登顶GitHub热榜

# AI编程节省95% token，工具调用上限狂飙20倍，开源记忆系统登顶GitHub热榜

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247867508&idx=1&sn=01e810d49e693b961a1503ef3a690257&chksm=e91ba2c894ead487715e0fcb6ab617445b3b51e70171e4e339bd72bc64e92c7897626cbf2305&mpshare=1&scene=1&srcid=0208BWx9uuEMzvH0bkDbt4i2&sharer_shareinfo=00305bc5f4fa1eced41723009cdfaffd&sharer_shareinfo_first=00305bc5f4fa1eced41723009cdfaffd)关注前沿科技 量子位

##### 梦晨 发自 凹非寺
量子位 \| 公众号 QbitAI

用Claude Code写代码的人，终于不用每次开新会话都从头解释项目背景了。

顶GitHub开源热榜的一款持久化记忆系统Claude-Mem，直击AI编程助手最致命的痛点：跨会话失忆。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGHoP2rOaN0SHHJiczzUdX0o6HiartkymNeoEtMejkXaM26mt2T7NYJBRjOZk9HgJXb6kxIl3EPLleUCHmQx26sGkA5Jqh2NND9q4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

Claude-Mem本身100%免费，还能帮你省token钱。

它通过"三层渐进式披露"的检索架构，常规使用下能节省90% Token，测试阶段的"无尽模式"更是能把Token消耗砍掉95%，工具调用次数上限直接拉高20倍。

## 给Claude Code装上"长期记忆"

传统AI编程助手有个绕不开的问题，每次新会话都是一张白纸。

昨天刚聊完的架构设计、上周敲定的编码规范、刚刚那些踩过的坑，AI统统不记得。开发者只能一遍遍重复解释，时间和Token都在这种"复读"中白白流失。

Claude-Mem的解法是在本地环境搭建一套完整的记忆系统。

它采用事件驱动架构，通过五个生命周期钩子*（SessionStart、UserPromptSubmit、PostToolUse、Stop、SessionEnd）* 在后台静默运行。

每当Claude Code执行文件读写、代码编辑、命令执行这类工具调用，系统都会自动把这些操作捕获下来，存成"观察记录"。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGENx1FCAk8iaEN8Wp7bro5RFgicq5JzcicnibOGAVz9e3r06nuUOcicZ42YUhPjHZqddTtnVP1mYaaSEgDjiaPB2MYbzCfSzPOqJ5C3o%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

存储方案走的是混合路线：SQLite配合FTS5负责全文检索，Chroma向量数据库则用来做语义搜索。

所有数据都躺在用户本地的目录里，隐私方面不用担心。

会话结束时系统会调用Claude Agent SDK，把整个会话期间那些冗长的原始工具使用记录，压缩成结构化的精炼摘要。

包含调查内容、学习成果、已完成工作、后续步骤这几个关键模块。

下次开新会话时，系统自动查库、检索、注入上下文，无缝衔接上回的工作。

## 三层检索省下10倍Token

Claude-Mem最大的亮点是一套"渐进式披露"检索工作流。

传统记忆系统做法把所有历史记录一股脑塞进上下文窗口，简单粗暴但极其烧钱。

Claude-Mem反其道而行，把检索拆成三层：

第一层是索引层，用search工具拉一个只包含ID、标题和类型的紧凑列表，每条结果大约只吃50到100个Token；

第二层是时间线层，用timeline工具获取某条感兴趣记录前后的时序上下文；

第三层才是完整细节，用get_observations根据筛选出的具体ID批量获取详情，单条成本在500到1000 Token之间。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGE6R8QUCRXV45fUZAgCvXD4Z9yls2J7u69v8htbHukiaBJXujmKjShxbx9F2fEQbzibE4gZoicGoJ0uSZQafOCuL01Ll2A5ejALcQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

这套分层策略作用下，一个原本需要20000 Token才能完整加载的上下文，经过筛选后可能只需要3000 Token就能拿到所有必要信息，而且相关度是100%。

处于测试阶段的无尽模式（Endless Mode）则更激进，它把工具输出实时压缩成大约500 Token的观察记录，Token节省率直接拉到95%。

由于上下文窗口占用率大幅下降，工具调用次数上限也跟着水涨船高，提升了约20倍，处理那些又长又复杂的任务也不用担心不够用了。

## 两条命令完成安装

功能之外，Claude-Mem在用户体验上也下了功夫。

它内置了mem-search技能，支持自然语言查询项目历史。想知道"上周修复了哪些bug"直接问就行。

系统还提供了一个本地Web界面，可以实时查看记忆流、会话摘要，也能在稳定版和Beta版之间切换配置。

隐私控制方面，用户可以用标签阻止敏感信息被记录，新版本还引入了双标签系统，控制粒度更细。

安装流程走的是Claude Code插件市场，两条命令加一次重启就能搞定，不需要折腾复杂的环境配置。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FA6fTew8FFGGCvjC122u7PRibNWCKDdPrlug4J6nWMNwAz9LMnRfBE82SKEAzLBUpNicuXv6ymaJicG4oZU0UibTo3XD7xRsPicPY9xJDib764ld5s%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

GitHub

https://github.com/thedotmack/claude-mem

--- **欢迎AI产品从业者共建** ---

📚「AI产品知识库」是量子位智库基于长期产品库追踪和用户行为数据推出的飞书知识库，旨在成为AI行业从业者、投资者、研究者的核心信息枢纽与决策支持平台。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FYicUhk5aAGtCCtgppOPb34icXInEib3PpbKbw7iaKqUwxVI7icDUaaVHL2pkmddUdeKibHSwYrurt5pjnPUCJmpB7ialg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

**一键关注 👇 点亮星标**

**科技前沿进展每日见**

![](https://image.cubox.pro/cardImg/14z8gf5kbumqt19jevpu5db2zudnou01s2jjqjv5of2bi3c0k8?imageMogr2/quality/90/ignore-error/1)

**量子位**

追踪人工智能新趋势，关注科技行业新突破

3668篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247867508&idx=1&sn=01e810d49e693b961a1503ef3a690257&chksm=e91ba2c894ead487715e0fcb6ab617445b3b51e70171e4e339bd72bc64e92c7897626cbf2305&mpshare=1&scene=1&srcid=0208BWx9uuEMzvH0bkDbt4i2&sharer_shareinfo=00305bc5f4fa1eced41723009cdfaffd&sharer_shareinfo_first=00305bc5f4fa1eced41723009cdfaffd)

