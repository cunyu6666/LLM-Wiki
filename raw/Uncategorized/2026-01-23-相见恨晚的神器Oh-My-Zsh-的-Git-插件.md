---
id: "7414254861547472217"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzU5NTc3ODk5Ng==&mid=2247483833&idx=1&sn=ec638bccdf6477d76800ab193ca9a26b&chksm=ffb4b8c5d1add067753833aa7886c87236dd711131816b0c4a3362aec0aa184ded21c40ddfa5&mpshare=1&scene=1&srcid=0123KWeiprU7Am6lUQNieOI9&sharer_shareinfo=0f7f9a79991fb224bcf57f3b2a890bcf&sharer_shareinfo_first=0f7f9a79991fb224bcf57f3b2a890bcf
author: "马蜂1024 小马向前走"
collected: 2026-01-23
tags: []
---

# 相见恨晚的神器：Oh My Zsh 的 Git 插件

# 相见恨晚的神器：Oh My Zsh 的 Git 插件

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU5NTc3ODk5Ng==&mid=2247483833&idx=1&sn=ec638bccdf6477d76800ab193ca9a26b&chksm=ffb4b8c5d1add067753833aa7886c87236dd711131816b0c4a3362aec0aa184ded21c40ddfa5&mpshare=1&scene=1&srcid=0123KWeiprU7Am6lUQNieOI9&sharer_shareinfo=0f7f9a79991fb224bcf57f3b2a890bcf&sharer_shareinfo_first=0f7f9a79991fb224bcf57f3b2a890bcf)马蜂1024 小马向前走


1. 引言：Git 命令行里的小烦恼

大多数人使用 Git，都是在 IDE 里完成的，而我偏偏喜欢在命令行里敲命令，通过命令行可以更深刻地理解 Git 的操作逻辑，但随着时间久了，我也不得不承认：Git 的命令和参数实在太多、太难记。每次切分支、合并、提交都要手动输入一长串命令。

所以我一直在寻找，看看有没有一种方式，既保留命令行的纯粹，又能简化 Git 命令的繁琐。一个偶然的机会，我发现了一个恰到好处的插件------Oh My Zsh 的 Git 插件。那一刻的感觉，简直就是相见恨晚。

2. Zsh 的隐藏宝藏：你不知道的效率神器

用过 Mac 的朋友都知道，系统默认的shell是 zsh，而 Oh My Zsh 是一个让 zsh 更强大的配置框架。它内置了很多高效插件，其中最让我惊喜的就是------git 插件。启用后，原本冗长的 Git 命令，立刻变得简洁、优雅、高效。

更妙的是，这个插件是 Oh My Zsh 自带的，无需额外安装。你只需要在 .zshrc 文件中添加一行配置即可启用：

     plugins=(... git)


3. 一行命令的魔法：别名让 Git 更顺手

Oh My Zsh 的 Git 插件，其实是一个集合了上百条别名（alias）的配置。它把常见的 Git 命令浓缩成简短易记的缩写，让命令行使用变得轻盈又顺手。

github地址：https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fv5BjKnicZLric9Ss5bh8c2R6nLbudYy5BRlWupox3Yqu1zx29q1ScN4XxOsJpvL8iabWDwEPoYL8F75zljOb7vFOQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

下面是我最常用的一些命令缩写：

| 常用别名  |      等价命令       |   功能说明    |
|-------|-----------------|-----------|
| g     | git             | git       |
| gst   | git status      | 查看仓库状态    |
| ga    | git add         | 添加变更      |
| gco   | git checkout    | 切换分支      |
| gcb   | git checkout -b | 创建并切换分支   |
| gb    | git branch      | 分支操作      |
| gcmsg | git commit -m   | 提交信息      |
| gp    | git push        | 推送代码      |
| gf    | git fetch       | 拉取更新(不合并) |
| gl    | git pull        | 拉取更新      |
| gm    | git merge       | 合并        |


4. 写在最后：简单就在身边
回想起来，我曾经在各种效率工具、终端主题之间反复折腾，想找到那个能让我"更高效"的完美方案。结果发现，好用的工具其实就在身边，而我却一直在寻找！Oh My Zsh 的 Git 插件就像那个被忽略的老朋友，安静地待在 plugins 目录里，直到有一天我真正启用了它，蓦然回首感慨万千。其实没必要挑来挑去，用好身边的工具，先把事干起来，才是正道。

如果你用 Mac、用 zsh、也用 Git，那我真心建议你试试这个插件！

*** ** * ** ***


欢迎大家关注我的公众号

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fv5BjKnicZLr8bQ2R8LcvRpdnO369lKT6aTpgBVsb3myQwUwwp6TQ2UYNXjIy7fyYmjTmsatBOa4dkPLbmuL9qUA%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**小马向前走**

技术分享

16篇原创内容

<br />

公众号  

，

电脑端的朋友也可查看我的博客，博客中的内容更深入，适合沉浸式阅读。

https://mankou.github.io

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU5NTc3ODk5Ng==&mid=2247483833&idx=1&sn=ec638bccdf6477d76800ab193ca9a26b&chksm=ffb4b8c5d1add067753833aa7886c87236dd711131816b0c4a3362aec0aa184ded21c40ddfa5&mpshare=1&scene=1&srcid=0123KWeiprU7Am6lUQNieOI9&sharer_shareinfo=0f7f9a79991fb224bcf57f3b2a890bcf&sharer_shareinfo_first=0f7f9a79991fb224bcf57f3b2a890bcf)

