---
id: "7440412204647582081"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzY0MDY5MDA4MQ==&mid=2247484434&idx=1&sn=6dcc2b85ec03798c677e053a62366369&chksm=f011cbf6d1af9f9e4fa8842c4e42af37d8cdbffcbfff01ad01c2a7fe294a71542cb60f355d06&mpshare=1&scene=1&srcid=0405ZDeqbU9EBbchXgEKTHej&sharer_shareinfo=8107701fb6fef23716271d0d4eba4cf0&sharer_shareinfo_first=8107701fb6fef23716271d0d4eba4cf0
author: "ITADN技术社区 ITADN技术社区"
collected: 2026-04-05
tags: []
---

# 别给你的agent用chrome了——加载快十倍、内存少九倍，AI原生的浏览器本该如此！

# 别给你的agent用chrome了------加载快十倍、内存少九倍，AI原生的浏览器本该如此！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY0MDY5MDA4MQ==&mid=2247484434&idx=1&sn=6dcc2b85ec03798c677e053a62366369&chksm=f011cbf6d1af9f9e4fa8842c4e42af37d8cdbffcbfff01ad01c2a7fe294a71542cb60f355d06&mpshare=1&scene=1&srcid=0405ZDeqbU9EBbchXgEKTHej&sharer_shareinfo=8107701fb6fef23716271d0d4eba4cf0&sharer_shareinfo_first=8107701fb6fef23716271d0d4eba4cf0)ITADN技术社区 ITADN技术社区


> 当你的 AI Agent 在云服务器上跑 100 个 Chrome 实例时，账单会让你怀疑人生------207MB × 100 = 20GB 内存，每月云费用几万块。如果有人告诉你，有个浏览器能做到**11 倍快、9 倍省内存、即时启动** ，而且**完全开源、兼容你现有的 Puppeteer/Playwright 代码** ------你会不会觉得这是在做梦？


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FFGl2atX1iaibrazkJH6EfnsvSmgUG9Oj47zlicxFNRicwiaHUicmf1ibGzBiaNeC4dHKmXq4NK635jL2pyEVzc7IG0mjDwUjlv8IOO2mgyuT1xFa8c0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

![](https://image.cubox.pro/cardImg/2sxwz6jvjrcoywkh56kbjuphy4mmm3dkezdk1faj4q2ii63348?imageMogr2/quality/90/ignore-error/1)

**ITADN技术社区**

技术社区拥有300多万用户 ，1.6亿程序源码、高质量博客文章。

60篇原创内容

<br />

公众号  

，

*** ** * ** ***

## 一、Chrome正在"杀死"你的自动化预算？

### 1.1 一个真实的成本账

假设你是一家做 AI Agent 的公司，每天需要爬取 100 万个网页。你的架构师告诉你：
> "用 Headless Chrome 吧，成熟稳定。"

然后你发现：

|   指标   |   Chrome   |         你的云账单         |
|--------|------------|-----------------------|
| 单实例内存  | **207 MB** | 100 实例 = 20 GB RAM    |
| 启动时间   | **2-3 秒**  | 等待时间 × 100 = 5 分钟白白浪费 |
| CPU 峰值 | **高**      | 需要更多 vCPU             |
| 并发瓶颈   | **有限**     | 得加服务器                 |


**一个月后，你的 AWS 账单是 5 位数。**

### 1.2 Chrome的"原罪"

Chrome 从来不是为服务器设计的------它是为人类设计的：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FFGl2atX1iaibqBDUgZMDVr3BKkL1ficiceMIR1rZo4t86J6ibh6PibkFgckPMzBwh7p2L53lX3JcHbjlL1icm6TlXlkdZT2UJic58HSaMmEzbSnrgvM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

**问题根源：** 你在用"给人类用的浏览器"来跑"机器的任务"------这就像开卡车去买菜，能买，但太奢侈了。

*** ** * ** ***

## 二、Lightpanda：第一个"为机器而生"的浏览器

### 2.1 这个项目什么来头？


|    硬指标    |                  数据                   |
|-----------|---------------------------------------|
| 📦 GitHub | **lightpanda-io/browser**             |
| 🔤 开发语言   | **Zig 0.15.2** (低级系统语言)               |
| 🧠 JS 引擎  | **V8 14.0.365.4**                     |
| 📜 许可证    | **AGPL-3.0** (开源免费)                   |
| 🔗 兼容性    | **Playwright / Puppeteer / chromedp** |
| 🐳 部署     | **Docker 一行命令**                       |


**Lightpanda 的核心理念：**
> **浏览器不应该有 GUI------如果用户是 AI，为什么需要渲染像素？**

### 2.2 性能数据说话


|    指标     |  Chrome  | Lightpanda |     提升     |
|-----------|----------|------------|------------|
| **执行时间**  | 25.2 秒   | 2.3 秒      | **11x 更快** |
| **内存峰值**  | 207 MB   | 24 MB      | **9x 更省**  |
| **启动时间**  | 2-3 秒    | 毫秒级        | **即时**     |
| **二进制大小** | \~500 MB | \~30 MB    | **16x 更小** |


<br />


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FFGl2atX1iaiboqXjjGxkHfabxVZtJpkMbKlT5vKLehyAq5liaYmGEDCXLrfqLsVwRh7e6jWSnVibVCwrTDoESibhIfBq0LMaeeFwuJpjuusvibUNg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

**这意味着什么？**

*
  原来需要 10 台服务器的负载，现在 1 台就能扛
*
  原来每月 5 万的云费用，现在 5 千就够
*
  原来启动 100 个实例要等 5 分钟，现在秒级

*** ** * ** ***

## 三、它是怎么做到的？源码深度拆解

### 3.1 架构全景：从零开始的设计

Lightpanda 不是 Chrome 的 fork------它是**从零开始写的浏览器** ：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FFGl2atX1iaibricbXjj7ibMwIwtUJ15SgUDbX627rAAscN5bJfnpRQiabKQNUJicdMdmVWDvzxE8dEubSaZdobLRuH98G2O0ueUeibbL826EBJygmc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

### 3.2 核心模块详解

从源码 browser/src/ 目录结构看：

|      模块      |        职责         |   技术选型    |
|--------------|-------------------|-----------|
| main.zig     | 程序入口              | Zig       |
| Server.zig   | CDP WebSocket 服务器 | 原生 Socket |
| Browser.zig  | 浏览器实例管理           | Zig + V8  |
| Page.zig     | 页面/DOM/事件         | Zig       |
| js/          | V8 绑定层            | Zig + C++ |
| webapi/      | Web API 实现        | Zig       |
| cdp/domains/ | CDP 协议域           | Zig       |


### 3.3 为什么选 Zig？

    // 这不是 Python，这是 Zig ------ 系统级编程语言
    const std = @import("std");

    pub fn main() !void {
        // Arena Allocator: 页面生命周期结束后一次性释放所有内存
        var arena = std.heap.ArenaAllocator.init(std.heap.c_allocator);
        defer arena.deinit();  // 编译期确定的生命周期管理

        // 零开销抽象，无 GC 停顿
        const page = try Page.init(arena.allocator(), url);
    }

**Zig 的三大优势：**

1.
   **无 GC** ：垃圾回收会导致 unpredictable latency，Zig 的确定性内存管理对高并发场景至关重要
2.
   **编译期优化** ：大量工作在编译期完成，运行时零开销
3.
   **与 C 无缝互操作** ：直接调用 V8 的 C++ API，无需 FFI 桥接

### 3.4 执行流程：一个页面请求的生命周期


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FFGl2atX1iaibqu977kmormTmSYpTTIIpqP9o7GEAeXwXLyP5Z9iaTSK3TIclOIGv29LNKJ45pd2iaC3lWKerdJ6hcq1H0NVHUB6biacGXQtPXejw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

### 3.5 CDP 协议实现：兼容性的秘密

从 cdp.zig 源码看，Lightpanda 实现了完整的 CDP 域分发：

    // 高效的字符串匹配 ------ 编译期优化
    fn dispatchCommand(command: anytype, method: []const u8) !void {
        const domain = method[0..std.mem.indexOfScalar(u8, method, '.')];

        switch (domain.len) {
            3 => switch (@as(u24, @bitCast(domain[0..3].*))) {
                asUint(u24, "DOM") => return dom.processMessage(command),
                asUint(u24, "Log") => return log.processMessage(command),
                asUint(u24, "CSS") => return css.processMessage(command),
            },
            4 => switch (@as(u32, @bitCast(domain[0..4].*))) {
                asUint(u32, "Page") => return page.processMessage(command),
            },
            7 => switch (@as(u56, @bitCast(domain[0..7].*))) {
                asUint(u56, "Runtime") => return runtime.processMessage(command),
                asUint(u56, "Network") => return network.processMessage(command),
            },
            // ... 更多域
        }
    }

**支持的 CDP 域：**

|    域    |       功能       | 状态 |
|---------|----------------|----|
| Page    | 页面导航、截图        | ✅  |
| DOM     | DOM 树操作        | ✅  |
| Runtime | JS 执行          | ✅  |
| Network | 请求拦截           | ✅  |
| Input   | 点击、输入          | ✅  |
| Target  | 多上下文           | ✅  |
| Fetch   | 请求修改           | ✅  |
| Storage | Cookie/Storage | ✅  |


*** ** * ** ***

## 四、实际场景：谁需要 Lightpanda？

### 4.1 AI Agent 开发者


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FFGl2atX1iaibpnUFdInlnicx6dBWXopRicHEUd5EyDBXEYibt3vOicj9rGgIjudW6UTHGApgMn7ItvE6hu6DFCoeD3wavZlIibOq5j4G15NHriagn44%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

**真实案例：** 某 AI 客服公司，100 个并发 Agent 处理用户请求。从 Chrome 切换到 Lightpanda 后，云成本从每月 3 万降到 3 千。

### 4.2 大规模网页采集

    // 你的 Puppeteer 代码几乎不用改
    import puppeteer from 'puppeteer-core';

    // 只需要改这一行 ------ 从 launch 改成 connect
    const browser = await puppeteer.connect({
        browserWSEndpoint: "ws://127.0.0.1:9222",  // Lightpanda CDP 地址
    });

    // 后面完全一样
    const page = await browser.newPage();
    await page.goto('https://example.com');
    const title = await page.title();
    console.log(title);

### 4.3 LLM 训练数据收集


|    场景     |   Chrome   | Lightpanda |
|-----------|------------|------------|
| 采集 100 万页 | 需要 10 台服务器 | 1 台搞定      |
| 内存峰值      | 2 TB       | 200 GB     |
| 完成时间      | 24 小时      | 2 小时       |


### 4.4 自动化测试

    # 一行命令启动 CDP 服务器
    docker run -d -p 9222:9222 lightpanda/browser:nightly

    # 然后用你熟悉的 Playwright 测试直接跑
    npx playwright test --project=chromium

*** ** * ** ***

## 五、与竞品对比：为什么不是它们？


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FFGl2atX1iaibreCvCkujhJjYqosF741nxic69EwOLRXtRpGxTeiaQuEXpOJX47iaY1GznEnfIQicB7AxMJhB1o7MkqjuewsXgtNCnLUoCuf1ssegE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

|       维度       | Chrome | Playwright | Puppeteer | **Lightpanda** |
|----------------|--------|------------|-----------|----------------|
| **内存占用**       | 207 MB | \~200 MB   | \~200 MB  | **24 MB**      |
| **启动时间**       | 2-3 s  | 1-2 s      | 1-2 s     | **毫秒级**        |
| **兼容性**        | 100%   | 100%       | 100%      | **95%+**       |
| **Web API 覆盖** | 完整     | 完整         | 完整        | **持续增加**       |
| **分布式友好**      | 一般     | 一般         | 一般        | **极佳**         |
| **开源**         | ✅      | ✅          | ✅         | **✅**          |
| **无 GUI**      | 需配置    | 内置         | 内置        | **天生无 GUI**    |


*** ** * ** ***

## 六、5 分钟跑起来

### 方式一：Docker（推荐）

    # 一行命令，启动 CDP 服务器
    docker run -d --name lightpanda -p 9222:9222 lightpanda/browser:nightly

### 方式二：直接下载二进制

    # Linux x86_64
    curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux
    chmod a+x ./lightpanda

    # 启动 CDP 服务器
    ./lightpanda serve --host 0.0.0.0 --port 9222

### 方式三：命令行直接抓取

    # 不需要写代码，直接抓取页面 DOM
    ./lightpanda fetch --obey_robots https://example.com

### 连接测试

    // test.mjs
    import puppeteer from 'puppeteer-core';

    const browser = await puppeteer.connect({
        browserWSEndpoint: "ws://localhost:9222"
    });

    const page = await browser.newPage();
    await page.goto('https://example.com');
    console.log(await page.title());
    await browser.disconnect();

    console.log("🎉 Lightpanda 连接成功！");

*** ** * ** ***

## 七、当前状态与 Roadmap

### 7.1 已实现功能


|       功能        | 状态 |
|-----------------|----|
| HTTP/HTTPS 加载   | ✅  |
| HTML5 解析        | ✅  |
| DOM 树构建         | ✅  |
| JavaScript (V8) | ✅  |
| Fetch / XHR     | ✅  |
| CDP WebSocket   | ✅  |
| 点击 / 输入         | ✅  |
| Cookies         | ✅  |
| 代理支持            | ✅  |
| 网络拦截            | ✅  |
| robots.txt 遵守   | ✅  |


### 7.2 开发中

*
  更多 Web API 覆盖
*
  WebGL 支持（部分）
*
  音视频处理
*
  更多 CDP 域

*** ** * ** ***

## 八、Lightpanda 的核心竞争力

### 8.1 技术护城河


|   维度   |      优势       |
|--------|---------------|
| **架构** | 从零设计，无历史包袱    |
| **语言** | Zig 带来的零开销抽象  |
| **引擎** | V8 的完整 JS 能力  |
| **协议** | 完整 CDP 兼容     |
| **部署** | 单二进制 / Docker |


### 8.2 商业价值

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FFGl2atX1iaibrNTMg8gLgk8xQLs5h2snopK0ASQ38ibsMuywTajjs0ib9Qbpfvef70icCVg76jI0zEMeicjWNDW7A0cdFLG4ObicpnC9XWJIMll6PY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

### 8.3 适用人群


|        人群        |   使用场景    |
|------------------|-----------|
| **AI Agent 开发者** | 高并发浏览器自动化 |
| **数据工程师**        | 大规模网页采集   |
| **LLM 训练者**      | 数据收集预处理   |
| **测试工程师**        | 快速 E2E 测试 |
| **创业公司**         | 低成本启动     |


*** ** * ** ***

## 九、谁暂时不适合用 Lightpanda？

公平起见，Lightpanda 还在 Beta 阶段：

*
  **需要 100% Chrome 兼容** ：复杂 SPA、WebGL 游戏暂时可能有问题
*
  **需要截图/PDF** ：目前不支持渲染输出
*
  **需要音视频** ：还在开发中
*
  **极度保守的企业** ：等 1.0 正式版

但如果你是------

*
  做 AI Agent / LLM 应用
*
  需要大规模网页采集
*
  想降低云成本
*
  愿意尝试新技术

**Lightpanda 值得你花 5 分钟试一试。**

*** ** * ** ***

## 十、结语：浏览器的"AI 原生"时代

### 10.1 历史的回响


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FFGl2atX1iaibpZUeTjo41th6GS6bibZhQmkz2YXibib1F4Uvd8aHicoSSdQTJYAbJsWcZvotTjwbjs7pAR8zF524MfAFv9SdDl4ceTHdbV4A7zNT4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

### 10.2 为什么说"AI 原生浏览器"时代已来？

当 AI Agent 开始成为互联网的主要"用户"，浏览器的设计逻辑必须改变：

| 传统浏览器  | AI 原生浏览器 |
|--------|----------|
| 给人看    | 给机器用     |
| 需要 GUI | 不需要渲染    |
| 单实例    | 高并发      |
| 启动慢    | 即时启动     |
| 内存大    | 极致省内存    |


**Lightpanda 是第一个真正为 AI 设计的浏览器。**

它不是 Chrome 的优化版，不是 Chromium 的 fork------它是**从第一行代码开始就为机器设计的全新物种** 。

*** ** * ** ***

## 快速链接


|       资源       |                    地址                    |
|----------------|------------------------------------------|
| 📦 **GitHub**  | https://github.com/lightpanda-io/browser |
| 🌐 **官网**      | https://lightpanda.io                    |
| 🐳 **Docker**  | docker pull lightpanda/browser:nightly   |
| 📖 **文档**      | https://lightpanda.io/docs               |
| 🐦 **Twitter** | @lightpanda_io                           |


*** ** * ** ***

> 💡 *如果你的 AI Agent 还在用 Chrome 一个个爬网页，云账单一个月比工资还高------是时候看看 Lightpanda 了。*
>
> *11 倍快，9 倍省内存，一行代码切换。*
>
> *毕竟，AI 不需要看到像素------它只需要 DOM。*

*** ** * ** ***

*关注公众号，每天带你发现一个高质量开源项目。*

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY0MDY5MDA4MQ==&mid=2247484434&idx=1&sn=6dcc2b85ec03798c677e053a62366369&chksm=f011cbf6d1af9f9e4fa8842c4e42af37d8cdbffcbfff01ad01c2a7fe294a71542cb60f355d06&mpshare=1&scene=1&srcid=0405ZDeqbU9EBbchXgEKTHej&sharer_shareinfo=8107701fb6fef23716271d0d4eba4cf0&sharer_shareinfo_first=8107701fb6fef23716271d0d4eba4cf0)

