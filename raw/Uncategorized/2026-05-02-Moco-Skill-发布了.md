---
id: "7450253694727095201"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg4ODYwNDkwMQ==&mid=2247484302&idx=1&sn=4d6b458eef3009d7b4d1d227b7177db4&chksm=cea7c8dbba63a12b8630cfea607aa15b5ffa877e0bfcd25d78d86607b1118c35c9cbe72415ab&mpshare=1&scene=1&srcid=0502V1QWniF7lgQbMZjCT4LC&sharer_shareinfo=7da6f69062373aeac7c7d68eb5d55c00&sharer_shareinfo_first=7da6f69062373aeac7c7d68eb5d55c00
author: "郑晔 郑大晔校"
collected: 2026-05-02
tags: []
---

# Moco Skill 发布了

# Moco Skill 发布了

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg4ODYwNDkwMQ==&mid=2247484302&idx=1&sn=4d6b458eef3009d7b4d1d227b7177db4&chksm=cea7c8dbba63a12b8630cfea607aa15b5ffa877e0bfcd25d78d86607b1118c35c9cbe72415ab&mpshare=1&scene=1&srcid=0502V1QWniF7lgQbMZjCT4LC&sharer_shareinfo=7da6f69062373aeac7c7d68eb5d55c00&sharer_shareinfo_first=7da6f69062373aeac7c7d68eb5d55c00)郑晔 郑大晔校


我很高兴地宣布，Moco Skill 正式发布了。

## Moco Skill 是什么？

Moco^\[1\]^ 是一个可以轻松搭建模拟服务器的框架/工具/程序库。Moco Skill^\[2\]^ 是一个面向 AI 工具的 skill，帮助其更好地理解和使用 Moco。

随着 AI 开发工具的兴起，越来越多的开发者开始在日常工作中使用 AI 开发工具编写代码，其中也包括测试代码。Moco Skill 让 AI 开发工具能够准确掌握 Moco 的 API，生成符合当前版本的代码，避免出现过时的 API 或编造不存在的功能。

## 主要能力

Moco Skill 为 AI 开发工具提供了完整的 Moco API 参考：

*
  **核心概念速查** ：请求匹配、响应定义、操作符、模板变量等核心用法的 Java/JSON 对照表
*
  **Java API 参考** ：服务器创建、请求匹配器、响应处理器、模板、事件、验证等
*
  **JSON 配置参考** ：完整的 JSON 配置语法，包括请求匹配、响应定义、模板、录制回放等
*
  **协议支持** ：HTTP/HTTPS、REST、WebSocket、SSE、Socket 等全部协议的 API 参考
*
  **工具链集成** ：CLI 用法、JUnit 5 集成

## 安装

以 Claude Code^\[3\]^ 为例，将 Moco Skill 克隆到 Claude Code 的 skills 目录即可：

    git clone https://github.com/dreamhead/moco-skill ~/.claude/skills/moco

安装完成后，Claude Code 会在遇到 Moco 相关问题时自动加载这个技能。

更新时，进入 skill 目录执行 git pull 即可更新到最新版本：

    cd ~/.claude/skills/moco && git pull

## 使用

安装后无需额外配置，在 Claude Code 中直接提问即可：
> 帮我写一个 Moco 的 JSON 配置，GET /api/users 返回一个 JSON 数组

Claude Code 会根据 Skill 中的 API 参考生成准确的代码。

### JSON 配置示例

当你需要生成 JSON 配置时：
> 我需要一个 Moco 的 JSON 配置：POST /api/login，请求体匹配 JSON，返回 200 和 cookie

Claude Code 会生成：

    [
      {
        "request": {
          "method": "post",
          "uri": "/api/login",
          "json": {
            "username": "admin",
            "password": "secret"
          }
        },
        "response": {
          "status": 200,
          "cookies": {
            "token": "abc123"
          },
          "json": {
            "status": "ok"
          }
        }
      }
    ]

### Java API 示例

当你需要编写 Java 测试代码时：
> 用 Moco Java API 写一个测试：匹配 POST /api/login，返回 JSON 和 cookie

Claude Code 会生成：

    import static com.github.dreamhead.moco.Moco.*;
    import static com.github.dreamhead.moco.Runner.*;

    HttpServer server = httpServer(12306);
    server.post(and(by(uri("/api/login")), by(json(text("{\"user\":\"admin\"}")))))
          .response(json(new Response("ok")), status(200), cookie("token", "abc123"));

### SSE 流式响应

当你需要模拟 LLM 风格的流式输出时：
> 帮我创建一个 SSE mock 的 Java 版，模拟逐字输出 Hello World

Claude Code 会生成：

    import static com.github.dreamhead.moco.MocoSse.*;

    HttpServer server = httpServer(12306);
    server.request(by(uri("/sse")))
            .response(sse(
                       event("message", "H"),
                       event("message", "e"),
                       event("message", "l"),
                       event("message", "l"),
                       event("message", "o"),
                       event("message", " "),
                       event("message", "W"),
                       event("message", "o"),
                       event("message", "r"),
                       event("message", "l"),
                       event("message", "d")
                   ).delay(100));

### REST API

当你需要构建 RESTful 服务时：
> 用 Moco Java API 创建一个 REST 服务，资源名 tasks，支持 GET 和 POST

Claude Code 会生成：

    RestServer server = restServer(12306);
    server.resource("tasks",
        get().response(json(taskList)),
        post().response(status(201), header("Location", "/tasks/123"))
    );

**欢迎使用 Moco Skill，让 AI 开发工具更好地辅助你使用 Moco！**

参考资料

\[1\]

Moco: *https://github.com/dreamhead/moco*
\[2\]

Moco Skill: *https://github.com/dreamhead/moco-skill*
\[3\]

Claude Code: *https://docs.anthropic.com/en/docs/claude-code*


[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg4ODYwNDkwMQ==&mid=2247484302&idx=1&sn=4d6b458eef3009d7b4d1d227b7177db4&chksm=cea7c8dbba63a12b8630cfea607aa15b5ffa877e0bfcd25d78d86607b1118c35c9cbe72415ab&mpshare=1&scene=1&srcid=0502V1QWniF7lgQbMZjCT4LC&sharer_shareinfo=7da6f69062373aeac7c7d68eb5d55c00&sharer_shareinfo_first=7da6f69062373aeac7c7d68eb5d55c00)

