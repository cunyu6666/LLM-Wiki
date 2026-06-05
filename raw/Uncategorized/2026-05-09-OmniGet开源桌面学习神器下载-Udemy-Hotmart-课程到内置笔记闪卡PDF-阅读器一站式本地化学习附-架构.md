---
id: "7452657886167043298"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg4MjcyOTc3MA==&mid=2247483810&idx=1&sn=a12f8880871e0a6c632d35e5ddb1cd88&chksm=ce32a652cc1c54d4a35041d4e0f89364f51b629f89be4273fe317e999feb42bcd6a35e97bf41&mpshare=1&scene=1&srcid=0509bLqqgpllQmJiTfA1pTtj&sharer_shareinfo=5c70f3f26b9c2e0e8e2eed99e1962a9b&sharer_shareinfo_first=5c70f3f26b9c2e0e8e2eed99e1962a9b
author: "Star探 开源hub-lab"
collected: 2026-05-09
tags: []
---

# OmniGet：开源桌面学习神器——下载 Udemy Hotmart 课程到内置笔记·闪卡·PDF 阅读器，一站式本地化学习（附 架构解析与完整安装指南）

# OmniGet：开源桌面学习神器------下载 Udemy Hotmart 课程到内置笔记·闪卡·PDF 阅读器，一站式本地化学习（附 架构解析与完整安装指南）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg4MjcyOTc3MA==&mid=2247483810&idx=1&sn=a12f8880871e0a6c632d35e5ddb1cd88&chksm=ce32a652cc1c54d4a35041d4e0f89364f51b629f89be4273fe317e999feb42bcd6a35e97bf41&mpshare=1&scene=1&srcid=0509bLqqgpllQmJiTfA1pTtj&sharer_shareinfo=5c70f3f26b9c2e0e8e2eed99e1962a9b&sharer_shareinfo_first=5c70f3f26b9c2e0e8e2eed99e1962a9b)Star探 开源hub-lab


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FQibQ5Tfib83wncAQXBxgftnCpysnKAOmldiauk4xRxR0mFvL8FP7EWxIpAe4pL0TfyJN06Mib62t6Ja7sJJpTdHsN8ZDnGCrNd4pylZGibfgAxQ4%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**开源hub-lab**

前沿科技信息，热门开源项目等

22篇原创内容

<br />

公众号  

，

想象一下：花重金买了 Udemy 或 Hotmart 的在线课程，结果每次学习都要打开浏览器、登录账号、忍受广告和网络卡顿，笔记散落在 Notion、浏览器书签里，进度无法同步......更别提 PDF/EPUB 书籍还需要额外工具才能高亮标注。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FQibQ5Tfib83wmy7dtMRsbxearPAfNibq0icZFCtfl98P91icZTNp5X6k6FoyghvQejTbHicHdYaW6Xz1QxJaBL3x46U9LzHjZ3K7I7ibRvNaftFnYg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

**OmniGet（tonhowtf/omniget）彻底终结了这种#碎片化#痛点** 。完全开源、免费的跨平台桌面应用（Windows 便携版、macOS dmg、Linux Flatpak），核心理念："**先下载一次，文件归你所有，然后就在 App 内完成全部#学习闭环** "。不仅支持 Hotmart、Udemy、Kiwify 等主流课程平台下载，还内置专业级视频播放器（带时间戳笔记、自动续播、附件预览）和 PDF/EPUB/CBZ 阅读器（高亮、书签、专注模式），同时集成 Anki 风格的间隔重复闪卡、Pomodoro 专注计时器、进度仪表盘、FFmpeg 转换、Telegram 聊天浏览器，甚至 P2P 4 词码文件互传和全局热键。

项目采用 **Tauri 2.0（Rust 后端 + Svelte 5 前端）** 架构，轻量高效、无 Electron 臃肿，全部数据本地 SQLite 存储，零云端上传。最新版本已达 0.5.0，支持 8 种语言、14 种主题（含 Catppuccin、e-ink 仿真）。

### 一、核心功能全景：不止下载，更是"学习操作系统"

OmniGet 设计哲学是"下载只是入口，学习才是核心"。将下载器、视频播放器、书籍阅读器、知识管理工具无缝融合，所有功能围绕**本地文件** 展开，课程/书籍文件夹保持原始结构，可随时用 VLC 或其他工具打开。

#### 1. 在线课程下载与内置视频学习器

支持平台包括：Hotmart、Udemy、Kiwify、Gumroad、Teachable、Kajabi、Skool、Wondrium、Thinkific、Rocketseat，以及 yt-dlp 支持的近千个站点（YouTube、Instagram、TikTok、Twitter/X、Reddit、Twitch、Pinterest、Vimeo、Bluesky、Bilibili、Douyin、Xiaohongshu 等亚洲平台）。

**下载流程** ：复制链接 → 粘贴到 Omnibox 或全局热键（Ctrl+Shift+D）→ 预览质量/格式选项 → 一键下载（后台运行，支持队列、恢复、Cookie 注入、SponsorBlock 跳广告、章节分割）。

**视频学习器亮点** （远超普通播放器）：

●播放速度 0.5x--2x、键盘快捷键、全屏/PiP/剧院模式、自动下一课（5 秒倒计时可取消）。

●**自动续播** ：精确到秒记住上次停止位置。

●**时间戳笔记** ：Markdown 支持，点击笔记自动跳转视频时间点。

●**附件面板** ：课程自带 PDF、图片、代码文件实时并排预览。

●**字幕支持** （.vtt 自动加载）。

●**课程库管理** ：多根目录扫描、标签/合集、状态过滤（未开始/进行中/完成）、搜索、健康检查（零字节文件、孤儿附件）。

●首页"继续观看"卡片 + 进度仪表盘（GitHub 式热力图、每日目标、连击计数）。

#### 2. 书籍阅读器（PDF/EPUB/CBZ/TXT/HTML 一体机）

无需 Calibre 或 Adobe，直接拖入文件夹扫描即可自动提取封面、ISBN 元数据查询（自动补全作者/出版社/高清封面）。

**阅读器功能** ：

●两种模式：翻页（书本感）/滚动（网页感）。

●大纲/目录跳转、单键书签、彩色高亮 + 笔记（Markdown）。

●全文搜索、PDF DPI 缩放（比简单缩放更锐利）、EPUB 字体/大小自定义。

●**多主题** ：白/米黄/暗黑 + e-ink 纸张滤镜。

●**光标行引导** （辅助阅读长句、 dyslexia 友好）。

●**专注模式** ：隐藏所有界面，仅留页面，全键盘导航。

●**阅读进度 + 会话计时器** ：自动记录每日阅读时长。

●Manga 模式（CBZ 右到左翻页）。

所有标注/笔记存入本地 SQLite，随文件备份迁移。

#### 3. 学习增强工具（真正实现"闭环"）

●**间隔重复闪卡** ：内置 SM2 算法（Anki 同款），支持 .apkg 导入 + AnkiWeb 同步。

●**Pomodoro 专注计时器** ：可联动视频暂停。

●**笔记 App** ：双向链接、每日日记、知识图谱、模板。

●**FFmpeg 本地转换** ：无需网络，快速转码视频/音频。

●**Telegram 聊天浏览器** ：读取本地账号，保存任意聊天中的媒体/文件。

●**浏览器扩展** （Chrome/Firefox）：一键把当前页面交给 OmniGet。

●**P2P 文件互传** ：4 个单词口令实现两台电脑直传（无需服务器）。

●**Torrents \& Magnet** ：内置 librqbit 会话，支持种子下载。

●**全局热键 + 剪贴板监听** ：随时下载。

●**多语言 \& 主题** ：8 种语言（含简/繁中、日语）、14 种主题（Catppuccin 全系列、Dracula、e-ink 等）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FQibQ5Tfib83wnLuzgoAHFgBxaOiaibCeiaiaTR2FxSsE6a2k13xCTOAnsiaO5ialTtSnZAMovloZDGsAu0tbYyGchR8ibVjPHiajoUo3OwSIfFrYsvJlk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

### 二、安装方法

**推荐方式（普通用户）** ：

1.前往 GitHub Releases 最新版（https://github.com/tonhowtf/omniget/releases/latest）。

2.Windows：下载 portable .exe（双击即用，无需安装）。

3.macOS：下载 .dmg，拖入 Applications。

4.Linux：下载 Flatpak（flatpak install）或 AppImage。

5.首次运行自动检查更新，后台静默更新。

**注意** ：Windows SmartScreen/macOS Gatekeeper 首次可能提示，点击"更多信息→仍要运行"或终端执行 xattr -cr+ codesign即可。

**从源码安装（开发者/极致自定义）** ：

```
●●●bashgit clone https://github.com/tonhowtf/omniget.git
cd omniget
pnpm install
pnpm tauri dev   # 开发模式热重载
```

生产构建：pnpm tauri build。

**Linux 依赖** （仅一次）：

```
●●●bashsudo apt-get install -y libwebkit2gtk-4.1-dev build-essential curl wget file libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev patchelf
```

**前提** ：Rust（rustup）、Node.js 18+、pnpm。

便携模式：在 exe 同目录创建 portable.txt或 .portable文件，数据自动存入 ./data。

### 三、使用方法：3 分钟上手 + 进阶技巧

1.**添加课程/书籍库** ：设置 → Library → 添加文件夹路径 → 扫描（自动生成封面、元数据）。

2.**下载课程** ：复制平台链接 → Omnibox 或热键 → 选择质量 → 下载（支持 Cookie 导入浏览器登录态）。

3.**学习视频** ：打开课程 → 选课时 → 播放器自动加载笔记/附件。

4.**阅读书籍** ：打开书籍 → 切换模式/主题 → 高亮标注 → 专注模式。

5.**闪卡/笔记** ：侧边栏打开对应面板，导入 Anki 或新建。

6.**进阶** ：设置 → 启用浏览器扩展 + 全局热键；下载设置中开启 SponsorBlock、章节分割、自动字幕翻译；P2P 发送时生成 4 词码分享给朋友。

全部操作本地完成，隐私零泄露。

### 四、技术原理、架构与实现方式

OmniGet 采用**现代 2025-2026 设计原则** ：极简目的性、即时反馈、WCAG 2.2 AA 无障碍优先。**核心架构** 为 Tauri 2.0 单体应用：

●**前端** ：SvelteKit 2 + Svelte 5（Runes：$state、$derived、$effect、$props） + TypeScript strict。文件路由（routes/+page.svelte）、组件按领域组织（buttons/、dialog/、omnibox/ 等）。**无 Tailwind** ，全部 Scoped CSS + CSS 自定义属性主题系统（--primary、--accent 等 20+ tokens，支持 light/dark + 14 种预设）。设计系统强调系统字体、IBM Plex Mono 代码字体、11px 基础圆角、12px 基础间距。

●**后端** ：Rust + Tauri 插件生态（single-instance、updater、global-shortcut、deep-link、clipboard、fs、store、notification 等）。使用 tokio 异步运行时、reqwest HTTP、serde 序列化、sqlx SQLite（本地库、笔记、进度、闪卡全存这里）、chromiumoxide（可能用于扩展自动化）。

●**状态管理** ：AppState（Arc\>）管理 active_downloads、download_queue、PlatformRegistry、torrent_session（librqbit）、active_p2p_sends 等。

●**下载核心** ：**Trait-based 可扩展插件系统** （platforms/ 目录）。PlatformRegistry统一注册各平台 Downloader（Instagram、YouTube、Bilibili、Magnet、P2P、GenericYtdlpDownloader 等）。每个平台实现 PlatformDownloadertrait（解析链接、获取元数据、下载逻辑）。通用 yt-dlp 桥接（core/ytdlp.rs）：通过环境变量/设置注入 Cookie（浏览器扩展 native host 读取）、referer、SponsorBlock、章节分割、自动字幕翻译等。下载队列支持并发（默认 2）、取消令牌（CancellationToken）、进度日志实时 emit 到前端。

●**P2P \& Torrent** ：librqbit Session + 自定义 4 词码机制（P2pDownloader）。

●**IPC 通信** ：Tauri commands（commands/ 目录）实现 Rust ↔ Svelte 双向调用（下载、库扫描、设置读写、热键等）。

●**存储与持久化** ：sqlx + tauri_plugin_store。课程文件夹磁盘不变，注解独立 DB，保证可迁移。

●**其他原生集成** ：全局热键（tauri_plugin_global_shortcut）、托盘（tray.rs）、便携模式检测（portable.txt）、FFmpeg（shell 插件调用）、Telegram（可能通过插件或浏览器自动化）、浏览器扩展 native host（native_host.rs，实现主机通信）。

●**插件系统** ：plugin_loader.rs 支持动态插件加载（未来扩展）。

●**构建与跨平台** ：Cargo + Vite，打包后体积小、启动快。Linux 特殊 WEBKIT 环境变量处理。

**源码亮点** ：

●main.rs处理便携模式、Python 环境（yt-dlp）、native host 分支。

●AppState集中管理所有共享资源，支持单实例 deep-link（外部 URL 自动处理）。

●设计系统完全基于 CSS vars + 自定义控件（Toggle、Switcher、Dialog 使用原生+\<dialog\> + ARIA），确保可访问性与一致性。

●扩展性极高：新增平台只需实现 trait 并注册到 registry。

这种架构让 OmniGet 既轻量（远优于 Electron）又强大（Rust 性能 + Web 现代 UI），完美平衡了下载引擎的复杂性和学习界面的流畅性。

OmniGet是**个人知识管理操作系统** 。让你真正"拥有"学习内容，而不是租用浏览器会话。项目完全 GPL-3.0 开源。

立即行动：去 Releases 下载体验，或 clone 源码编译。 Udemy 课程、Hotmart 专栏、PDF 书库，从此只属于你自己。

**关注公众号** ，持续分享更多开源工具与深度技术！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FQibQ5Tfib83wncAQXBxgftnCpysnKAOmldiauk4xRxR0mFvL8FP7EWxIpAe4pL0TfyJN06Mib62t6Ja7sJJpTdHsN8ZDnGCrNd4pylZGibfgAxQ4%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**开源hub-lab**

前沿科技信息，热门开源项目等

22篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg4MjcyOTc3MA==&mid=2247483810&idx=1&sn=a12f8880871e0a6c632d35e5ddb1cd88&chksm=ce32a652cc1c54d4a35041d4e0f89364f51b629f89be4273fe317e999feb42bcd6a35e97bf41&mpshare=1&scene=1&srcid=0509bLqqgpllQmJiTfA1pTtj&sharer_shareinfo=5c70f3f26b9c2e0e8e2eed99e1962a9b&sharer_shareinfo_first=5c70f3f26b9c2e0e8e2eed99e1962a9b)

