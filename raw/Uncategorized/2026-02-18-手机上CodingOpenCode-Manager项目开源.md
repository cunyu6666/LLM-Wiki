---
id: "7423478911264098942"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461158535&idx=1&sn=11e5938a4edb72e4166cfd31bc4b029d&chksm=867235c42d153014fdf2729caf2d0202d3596aa7aff259794bf62db11eb38d5c5b7e0a24f685&mpshare=1&scene=1&srcid=0218QasvnKnKbXfQszlmflIb&sharer_shareinfo=5ce0a673522d48993c559671ebc46b10&sharer_shareinfo_first=5ce0a673522d48993c559671ebc46b10
author: "winkrun AI工程化"
collected: 2026-02-18
tags: []
---

# 手机上Coding？OpenCode Manager项目开源

# 手机上Coding？OpenCode Manager项目开源

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461158535&idx=1&sn=11e5938a4edb72e4166cfd31bc4b029d&chksm=867235c42d153014fdf2729caf2d0202d3596aa7aff259794bf62db11eb38d5c5b7e0a24f685&mpshare=1&scene=1&srcid=0218QasvnKnKbXfQszlmflIb&sharer_shareinfo=5ce0a673522d48993c559671ebc46b10&sharer_shareinfo_first=5ce0a673522d48993c559671ebc46b10)winkrun AI工程化

马年大吉，要是想在旅途也过过vibecoding的瘾怎么办？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FrY5icXvTTrJ9Vd6qibTSicOWNzuYYmzichJMjvuEI6w4FytKjOfKwHqibSDNIlXIVqaSJKfbC9RiaZNUW4R3Qp8omwMtXfrwSlhrzeWLtTDnR7WicQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

有开发者开源了一个名为OpenCode Manager的项目，这是一个专为移动设备设计的Web界面，用于管理OpenCode AI代理。项目采用Docker容器化部署，支持Git集成、文件浏览器、语音转文本、文本转语音、推送通知等功能。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FrY5icXvTTrJib2cncZcxkT1uCvERiaGrSS1707ib1JkeibMWafHiarqKJicJyWZweunjqrymzVwIptI6CPwa2sBEAcEe6zVKI0ibJ4pbbqesWe1Jic5M%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D1)
移动优先的设计理念

OpenCode Manager最大的特点是移动优先的响应式设计。用户可以在手机、平板或桌面上管理多个OpenCode AI代理，进行代码编写和控制。界面采用PWA（渐进式Web应用）技术，提供类似原生应用的体验。

## 实际界面体验

**移动端聊天界面**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FrY5icXvTTrJicqZZGL3vzCcE0QVQGCWq2gzDQQBQPn6Um5KkqknBnRIaYgSvVq73lat82sWicSQa7l8bHJ0gf8PWAewedduxj4r8e4qiaXOUOT8%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D2)

**移动端文件管理**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FrY5icXvTTrJibu86fYMEqVAiaclKRaj6cexeiaRBFP44CWSLoV5stxibU1YV1vLAJ5j0eRgPu7qbSnSxf2ictRbnAjVoI5aeXLEjCbibtsHt3bdOPk%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D3)

**内联差异对比视图**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FrY5icXvTTrJ8RzKod9xstWnL96K1RAiaS6XF33oP14c7B5KePpVtEBXicERVfhnKehNIDJAiclG3yTvQqUTyicKZvmu1hzN9TmXxI1geoApZIOaA%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D4)

从这些实际演示可以看出，界面确实针对移动设备做了优化，触摸操作流畅，文件管理和代码差异对比在小屏幕上也能清晰显示。

## 核心功能一览

*
  **Git集成**：多仓库支持，SSH密钥认证，Git工作树管理
*
  **文件管理**：完整的文件浏览器，支持文件上传、下载和编辑
*
  **实时聊天**：与AI代理进行实时对话交流，支持斜杠命令
*
  **语音功能**：支持语音转文本和文本转语音
*
  **推送通知**：重要事件实时推送提醒
*
  **多设备同步**：在任何设备上都能保持工作状态同步

## 技术架构

项目采用前后端分离架构，后端使用Node.js，前端基于React构建。数据库使用SQLite，支持Docker Compose一键部署。代码结构清晰，包含backend、frontend、shared等模块。

## 部署简单

通过Docker部署只需几个命令：

    git clone https://github.com/chriswritescode-dev/opencode-manager.git
    cd opencode-manager
    docker-compose up -d
    # 访问 http://localhost:5003

对于经常需要在移动设备上处理代码的开发者来说，这个工具提供了一个不错的解决方案。特别是结合AI编程助手的使用场景，让代码编写和项目管理更加便捷。

说不定2026年主题就是"碎片化编程"！

**项目地址**：https://github.com/chriswritescode-dev/opencode-manager


![](https://image.cubox.pro/cardImg/65nmox3xvl5vpnhfd64wky7tseu9o855a6d84pn0cc66o0wzdc?imageMogr2/quality/90/ignore-error/1)

**AI工程化**

专注于AI领域（大模型、MLOPS/LLMOPS 、AI应用开发、AI infra）前沿产品技术信息和实践经验分享。

730篇原创内容

<br />

公众号  

，

关注公众号回复"进群"入群讨论。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461158535&idx=1&sn=11e5938a4edb72e4166cfd31bc4b029d&chksm=867235c42d153014fdf2729caf2d0202d3596aa7aff259794bf62db11eb38d5c5b7e0a24f685&mpshare=1&scene=1&srcid=0218QasvnKnKbXfQszlmflIb&sharer_shareinfo=5ce0a673522d48993c559671ebc46b10&sharer_shareinfo_first=5ce0a673522d48993c559671ebc46b10)

