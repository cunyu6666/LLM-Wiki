---
id: "7361362727249380548"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247505670&idx=1&sn=84d614828a4aabc721e2abdc7f3d5354&chksm=e94b2dcd3d38c6d0756d6713f0cee505918a8be2e82768db264d5daf16053784dcd9a6f1020c&mpshare=1&scene=1&srcid=08307zfgVOs02QRcLCVDCCYd&sharer_shareinfo=786c42a80f8b8041d8dbf953d6b4c7ac&sharer_shareinfo_first=786c42a80f8b8041d8dbf953d6b4c7ac
author: "ByteNote 字节笔记本"
collected: 2025-08-30
tags: [IDE]
---

# Claude Code 也来梦幻联动 Zed了！

# Claude Code 也来梦幻联动 Zed了！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247505670&idx=1&sn=84d614828a4aabc721e2abdc7f3d5354&chksm=e94b2dcd3d38c6d0756d6713f0cee505918a8be2e82768db264d5daf16053784dcd9a6f1020c&mpshare=1&scene=1&srcid=08307zfgVOs02QRcLCVDCCYd&sharer_shareinfo=786c42a80f8b8041d8dbf953d6b4c7ac&sharer_shareinfo_first=786c42a80f8b8041d8dbf953d6b4c7ac)ByteNote 字节笔记本

上午发了Gemini和Zed的梦幻联动后，[太爽了！我最喜欢的两个编码工具梦幻联动了！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247505641&idx=1&sn=dc2511abee98ce84cd0f14f37746ece0&scene=21#wechat_redirect)下午Claude Code和Zed的联动也来了来了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F4HWyricuhgQcfhUD7QNnrcvUu69AQibrwpoib5bM8OTNJJexBoYSibA5V9a1qINg9KxqNcHfsWKDx3m0TZsPxaiboBA%2F640%3Fwx_fmt%3Dpng%26watermark%3D1)

不过这回并不是官方的，是能用轻量级桥接器让Claude Code 通过 Agent Client Protocol (ACP) 与 Zed 编辑器无缝集成。

Agent Client Protocol (ACP)是一个用于"编辑器前端"与"AI 后端"之间双向通信的开放协议。

定位等价于 LSP（Language Server Protocol）之于语言服务，但面向 AI 驱动的代码生成、重构与工具调用场景。当前由社区主导、Rust/TypeScript 双参考实现，已被 Zed、Cursor、Neovim 等编辑器纳入官方或第三方支持路线。

如果把本地的环境都安装好了，安装过程很简单

    npm install -g acp-claude-code   # 或 pnpm add -g acp-claude-code


配置 Zed，打开如下路径的配置文件

`~/.config/zed/settings.json`

追加以下的内容即可：

       {
         "agent_servers": {
           "claude-code": {
             "command": "npx",
             "args": ["acp-claude-code"],
             "env": {
               "ACP_PERMISSION_MODE": "acceptEdits"   // 自动接受文件编辑
             }
           }
         }
       }


启动并使用，如果首次启动 Claude Code 可能需要认证一下才行：

    claude setup-token


在 Zed 里打开 Agent Panel → 选择 `claude-code`，即可开始对话、生成/修改代码。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F4HWyricuhgQcfhUD7QNnrcvUu69AQibrwp9QtxGxyd5pvicpM3fsIuhbOxU29ohRxd19Qh0JXOAgcGaU9gZ5Cb4QA%2F640%3Fwx_fmt%3Dpng%26watermark%3D1)

如需调试，在 `env` 里加 `"ACP_DEBUG": "true"`。

Claude Code 还依赖 ⁠bun，系统找不到它的话需要使用下面的命令来安装一下：

    curl -fsSL https://bun.sh/install | bash
    source ~/.bashrc   # 或 ~/.zshrc

    # 确认 bun 已加入 PATH
    which bun         # macOS / Linux
    where bun         # Windows


重启 Zed 或终端即可。完成后，Zed 就能像原生一样调用 Claude Code，实现实时对话、文件编辑与工具调用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F4HWyricuhgQcfhUD7QNnrcvUu69AQibrwpLLwgicQTw82AIvfvyeXJoR6h7zk0bbe1X76KNoukFib4VP0V9MhHwLyw%2F640%3Fwx_fmt%3Dpng%26watermark%3D1)

不需要再重新开一个命令行窗口了，直接实现会话保持、流式输出、工具调用、权限管理、跨平台即装即用，把 Claude 变成 Zed 的原生 AI 代理，零配置即可对话、生成、改代码。

Claude Code交流群，可以免费领取Claude Code 体验日卡：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F4HWyricuhgQcfhUD7QNnrcvUu69AQibrwpZbjEX32FLDl4qCWbUkBiaL2kicExSgRJ0YmIaxr1KvDFO0tiaGRugnlsA%2F640%3Fwx_fmt%3Djpeg%26watermark%3D1)

![](https://image.cubox.pro/cardImg/4lb2ds2m4duzs3iawd3zcomh4295lpfw5o214rp4go7j9nj3y5?imageMogr2/quality/90/ignore-error/1)

**字节笔记本**

专注于AIGC, AI编程经验和案例分享以及全栈开发

870篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247505670&idx=1&sn=84d614828a4aabc721e2abdc7f3d5354&chksm=e94b2dcd3d38c6d0756d6713f0cee505918a8be2e82768db264d5daf16053784dcd9a6f1020c&mpshare=1&scene=1&srcid=08307zfgVOs02QRcLCVDCCYd&sharer_shareinfo=786c42a80f8b8041d8dbf953d6b4c7ac&sharer_shareinfo_first=786c42a80f8b8041d8dbf953d6b4c7ac)

