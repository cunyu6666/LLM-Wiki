---
id: "7315978967247227235"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MjM5ODIzNDQ3Mw==&mid=2649970759&idx=1&sn=7000610d26f68d82024d6f6cd6ecce64&chksm=bf46e81f1f6b3d8fa05797a769a4e69755a610cc0aeea25360cc7053595be96fbaebb0df4f0e&mpshare=1&scene=1&srcid=0427Kwj1pVCOC9j1zoNsHmqI&sharer_shareinfo=aaa621e0fb3d58adefa8686cb288f371&sharer_shareinfo_first=aaa621e0fb3d58adefa8686cb288f371
author: "我是张成 待字闺中"
collected: 2025-04-27
tags: []
---

# 详解A2A(Agent2Agent)协议

# 详解A2A(Agent2Agent)协议

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODIzNDQ3Mw==&mid=2649970759&idx=1&sn=7000610d26f68d82024d6f6cd6ecce64&chksm=bf46e81f1f6b3d8fa05797a769a4e69755a610cc0aeea25360cc7053595be96fbaebb0df4f0e&mpshare=1&scene=1&srcid=0427Kwj1pVCOC9j1zoNsHmqI&sharer_shareinfo=aaa621e0fb3d58adefa8686cb288f371&sharer_shareinfo_first=aaa621e0fb3d58adefa8686cb288f371)我是张成 待字闺中


## 什么是 A2A 协议

A2A（Agent2Agent）协议 是由 Google Cloud 推出的一个开放协议，旨在促进不同 AI 代理之间的互操作性。其主要目标是允许这些代理在动态的、多代理的生态系统中进行有效的通信和协作，无论它们是由不同的供应商构建的还是使用不同的技术框架。

### A2A 的设计原则总结

A2A（Agent2Agent）协议的设计原则旨在提升代理之间的协作能力，确保灵活性、安全性和与现有系统的兼容性。以下是这些原则的综合总结：

1. 1. **拥抱代理能力**

   * • 允许代理在其自然、非结构化的模式下进行协作，无需共享内存、工具或上下文，从而实现真实的多代理场景。

2. 2. **基于现有标准构建**

   * • 协议建立在广泛接受的技术标准之上，如 HTTP、SSE 和 JSON-RPC，便于与企业现有的 IT 堆栈集成。

3. 3. **默认安全**

   * • 设计支持企业级身份验证和授权，确保只有经过授权的用户和系统可以访问代理，增强了系统的安全性。

4. 4. **支持长时间运行的任务**

   * • 灵活支持从快速任务到复杂研究的多种场景，能够在任务执行过程中提供实时反馈、通知和状态更新。

5. 5. **模态无关**

   * • 支持多种交互形式，包括文本、音频和视频流、form 、 iframe 等，增强了代理的交互能力和适应性。

整体看下来，协议在开放性、安全性、灵活性上考虑得比较多。这些点都是 MCP 有所不足的。和 MCP 的对比我们放在最后。先说正题------详解A2A

## A2A 的参与者

A2A 协议有三个参与者：

* • 用户（User）：使用代理系统完成任务的用户（人类或服务）

* • 客户端（Client）：代表用户向不透明代理（服务、代理、应用程序）请求操作的实体。

* • 服务端（Server）：不透明（黑盒）的远程代理，即 A2A 服务器。

参考如下的图

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FuVhqWvaiaiaPPibzcKOSmFfib3TVvFDZVE4HD1J4NiaicQgVpAry6jMymPsQo49rctbUgHr0DTy2dwD4F3oRNicEiaBDyw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)

通过上面的图，我们可以清晰地看到三个参与者的位置，对比之前 MCP 参与者，缺少一个 Host 的参与者。这个是设计思路上的不同，是要开放实现，还是规范一个机制，在 A2A 的实现中，安全等因素，已经通过别的方式实现，但确实User 如何发现需要的 Agent，是一个遗留的问题。

## A2A 核心概念

### AgentCard

AgentCard 是一个 JSON 文件，描述了 Agent 提供了什么样的功能，官方建议托管在**https:// base url /.well-known/agent.json**。  
这样就可以直接通过 HTTP GET 获取 AgentCard，得到有关 Agent 的描述。

一个自然的引申是：需要注册表，无论是公开的、还是隐私的。这样方便查找 Agent 。

但另一个方面，注册表也可以是去中心化的。我们想象这样一个场景：每一个网站都有一个**https:// base url /.well-known/agent.json**，描述了自己可以做什么，然后在一个 P2P 的网络中，不断的广播自己的 AgentCard ------甚至这些 AgentCard，可以放在 IPFS 、或者以太坊上，这样 Agent 的协作关系，就构成了一个自组织的 Agent 网络。

回到 A2A，一个 AgentCard 的定义如下：

    // An AgentCard conveys key information:
    // - Overall details (version, name, description, uses)
    // - Skills: A set of capabilities the agent can perform
    // - Default modalities/content types supported by the agent.
    // - Authentication requirements
    interface AgentCard {
      // Human readable name of the agent.
      // (e.g. "Recipe Agent")
      name: string;
      // A human-readable description of the agent. Used to assist users and
      // other agents in understanding what the agent can do.
      // (e.g. "Agent that helps users with recipes and cooking.")
      description: string;
      // A URL to the address the agent is hosted at.
      url: string;
      // The service provider of the agent
      provider?: {
        organization: string;
        url: string;
      };
      // The version of the agent - format is up to the provider. (e.g. "1.0.0")
      version: string;
      // A URL to documentation for the agent.
      documentationUrl?: string;
      // Optional capabilities supported by the agent.
      capabilities: {
        streaming?: boolean; // true if the agent supports SSE
        pushNotifications?: boolean; // true if the agent can notify updates to client
        stateTransitionHistory?: boolean; //true if the agent exposes status change history for tasks
      };
      // Authentication requirements for the agent.
      // Intended to match OpenAPI authentication structure.
      authentication: {
        schemes: string[]; // e.g. Basic, Bearer
        credentials?: string; //credentials a client should use for private cards
      };
      // The set of interaction modes that the agent
      // supports across all skills. This can be overridden per-skill.
      defaultInputModes: string[]; // supported mime types for input
      defaultOutputModes: string[]; // supported mime types for output
      // Skills are a unit of capability that an agent can perform.
      skills: {
        id: string; // unique identifier for the agent's skill
        name: string; //human readable name of the skill
        // description of the skill - will be used by the client or a human
        // as a hint to understand what the skill does.
        description: string;
        // Set of tagwords describing classes of capabilities for this specific
        // skill (e.g. "cooking", "customer support", "billing")
        tags: string[];
        // The set of example scenarios that the skill can perform.
        // Will be used by the client as a hint to understand how the skill can be
        // used. (e.g. "I need a recipe for bread")
        examples?: string[]; // example prompts for tasks
        // The set of interaction modes that the skill supports
        // (if different than the default)
        inputModes?: string[]; // supported mime types for input
        outputModes?: string[]; // supported mime types for output
      }[];
    }

内容很长，但是比较简单，我们用下图来表示：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FuVhqWvaiaiaPPibzcKOSmFfib3TVvFDZVE4HFYtkCeFsiaJncgoq9NBM68jxiayicIBQsxpD00nR5Cq8jLYfnqBXQuSnQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

完整的定义可以参考这里：**https://github.com/sing1ee/a2a-agent-coder/blob/main/src/schema.ts**

### Task（任务）

任务是一个有状态的实体，允许客户端与远程代理协作以达成特定的结果并生成相应的输出。在任务内，客户端与远程代理之间会交换消息，远程代理则生成工件作为结果（代理即是 Agent）。

任务始终由客户端创建，而其状态则由远程代理决定。如果客户端需要，多个任务可以归属于同一个会话（通过可选的 sessionId 表示）。在创建任务时，客户端可以设置这个可选的 sessionId。

代理收到请求之后，可以采取以下几种行动：

* • 立即满足请求

* • 安排稍后执行的工作

* • 拒绝请求

* • 协商不同的执行方式

* • 向客户端索要更多信息

* • 委派给其他代理或系统

即使在完成目标后，客户端仍然可以请求更多信息或在同一任务的上下文中进行更改。例如，客户端可以请求："画一只兔子的图片"，代理回应："\<图片\>"，随后客户端又可以要求："把它画成红色"。

任务不仅用于传递工件（结果）和消息（思考、指令等），还维护着任务的状态及其可选的历史记录，包括状态变化和消息记录。

这些特性非常重要，尤其是同一个任务的上下文，可以进行多轮的对话，这些状态，还有历史记录，都有保存，这个非常匹配现在以 Chat 形式为主的AI 交互。

任务的定义如下：

    interface Task {
      id: string; // unique identifier for the task
      sessionId: string; // client-generated id for the session holding the task.
      status: TaskStatus; // current status of the task
      history?: Message[];
      artifacts?: Artifact[]; // collection of artifacts created by the agent.
      metadata?: Record<string, any>; // extension metadata
    }
    // TaskState and accompanying message.
    interface TaskStatus {
      state: TaskState;
      message?: Message; //additional status updates for client
      timestamp?: string; // ISO datetime value
    }
    // sent by server during sendSubscribe or subscribe requests
    interface TaskStatusUpdateEvent {
      id: string;
      status: TaskStatus;
      final: boolean; //indicates the end of the event stream
      metadata?: Record<string, any>;
    }
    // sent by server during sendSubscribe or subscribe requests
    interface TaskArtifactUpdateEvent {
      id: string;
      artifact: Artifact;
      metadata?: Record<string, any>;
    }
    // Sent by the client to the agent to create, continue, or restart a task.
    interface TaskSendParams {
      id: string;
      sessionId?: string; //server creates a new sessionId for new tasks if not set
      message: Message;
      historyLength?: number; //number of recent messages to be retrieved
      // where the server should send notifications when disconnected.
      pushNotification?: PushNotificationConfig;
      metadata?: Record<string, any>; // extension metadata
    }
    type TaskState =
      | "submitted"
      | "working"
      | "input-required"
      | "completed"
      | "canceled"
      | "failed"
      | "unknown";

### Artifact(工件)

工件是代理作为任务最终结果生成的输出。工件具有不可变性，可以被命名，并且可以包含多个部分。通过流式响应，可以将新部分附加到现有的工件中。

一个任务可以生成多个工件。例如，当执行"创建一个网页"时，可能会产生单独的 HTML 工件和图像工件。

不得不说 A2A 出现的时机很准确，现在 AI 的一些主要的应用的形式，在协议定义上都包括了。Artifact就是很火的一个形式。

具体的定义：

    interface Artifact {
      name?: string;
      description?: string;
      parts: Part[];
      metadata?: Record<string, any>;
      index: number;
      append?: boolean;
      lastChunk?: boolean;
    }

### Message(消息)

消息是包含任何非工件内容的实体。这些内容可以包括代理的思考、用户的上下文、指令、错误信息、状态更新或元数据。

所有来自客户端的内容均以消息的形式发送。代理通过消息来传达状态或提供指令，而生成的结果则以工件的形式发送。

消息可以包含多个Part(片段)，以表示不同类型的内容。例如，一个用户请求可能包括用户的文本描述以及多个用于上下文的文件。

定义如下：

    interface Message {
      role: "user" | "agent";
      parts: Part[];
      metadata?: Record<string, any>;
    }

### Part(片段)

Part是客户端与远程代理之间作为消息或工件一部分交换的完整内容。每个Part都有其独特的内容类型和元数据。

以下是不同类型部分的接口定义：

#### 文本部分（TextPart）

    interface TextPart {
    type: "text";
    text: string;
    }

#### 文件部分（FilePart）

    interface FilePart {
    type: "file";
    file: {
      name?: string;
      mimeType?: string;
      // 可能的内容
      // oneof {
      bytes?: string; // base64 编码的内容
      uri?: string;
      //}
    };
    }

#### 数据部分（DataPart）

    interface DataPart {
    type: "data";
    data: Record<string, any>;
    }

#### 综合类型

    type Part = (TextPart | FilePart | DataPart) & {
    metadata: Record<string, any>;
    };

更多的消息的细节，参考链接：**https://a2aprotocol.ai/blog/a2a-sample-methods-and-json-responses**

## 通信机制与异步支持

A2A 支持以下的通信机制：

* • A2A 支持安全的推送通知机制，允许代理在不连接的情况下向客户端发送更新。

* • 客户端和服务器可以使用标准请求/响应模式，也可以通过 SSE 进行流式更新。

  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FuVhqWvaiaiaPPibzcKOSmFfib3TVvFDZVE4HZ4F8GHyYBIOxEE24SImHWC5NK5NrKNUK9U0ptZdZmTp8hd1Km1qicibg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在推送通知时，代理需要验证通知服务的身份，并使用受信任的凭证进行身份验证，以确保通知的安全性。  
基于以上的通信机制，A2A 支持客户端在处理长时间运行的任务时进行轮询，代理也可以通过 SSE 向客户端推送状态更新。

这里，最重要的是异步的支持，client 可以通过类似注册一个 webhook，异步的获取长时间运行任务的结果------就是PushNotification 相关的实现。目前大家在使用 LLMs API 的时候，都会遇到一个问题，就是输出太慢了，而且输出的过程中，并不能做别的事情。如果有了异步的回调，或者轮询、重新订阅，那么就可以在 client 的开发上，更加灵活，可以给用户带来更好的体验。

以下是推送的定义：

    interface PushNotificationConfig {
      url: string;
      token?: string; // token unique to this task/session
      authentication?: {
        schemes: string[];
        credentials?: string;
      };
    }
    interface TaskPushNotificationConfig {
      id: string; //task id
      pushNotificationConfig: PushNotificationConfig;
    }

## 错误处理（Error Handling）

### 错误消息格式

以下是服务器在处理客户端请求时遇到错误时响应客户端的 `ErrorMessage` 格式：

    interface ErrorMessage {
    code: number;
    message: string;
    data?: any;
    }

### 标准 JSON-RPC 错误代码

以下为服务器在错误场景中可以响应的标准 JSON-RPC 错误代码：

|       错误代码       |                信息                |        描述        |
|------------------|----------------------------------|------------------|
| -32700           | JSON parse error                 | 无效的 JSON 被发送     |
| -32600           | Invalid Request                  | 请求负载验证错误         |
| -32601           | Method not found                 | 非法方法             |
| -32602           | Invalid params                   | 无效的方法参数          |
| -32603           | Internal error                   | 内部 JSON-RPC 错误   |
| -32000 to -32099 | Server error                     | 保留供实现特定错误代码使用    |
| -32001           | Task not found                   | 找不到提供的 ID 的任务    |
| -32002           | Task cannot be canceled          | 无法由远程代理取消任务      |
| -32003           | Push notifications not supported | 推送通知由代理不支持       |
| -32004           | Unsupported operation            | 操作不支持            |
| -32005           | Incompatible content types       | 客户端与代理之间的内容类型不兼容 |


## 动手实践

我把官方的 ts 的示例进行了修改，支持了 OpenRouter，主要是改动了兼容 OpenAI 的 API 形式。代码在这里：**https://github.com/sing1ee/a2a-agent-coder**

我是在 Mac 环境下进行的，打开你最爱的终端：

1. 1. 安装 Bun

    brew install oven-sh/bun/bun # 针对 macOS 和 Linux

1. 2. 克隆仓库

    git clone git@github.com:sing1ee/a2a-agent-coder.git

1. 3. 安装依赖

    cd a2a-agent-coder
    bun i

1. 4. 配置环境变量  
   参考\*\*\*.env.example**创建一个**.env\*\*\*文件，内容如下：

    OPENAI_API_KEY=sk-or-v1-xxxxxxx
    OPENAI_BASE_URL=https://openrouter.ai/api/v1
    OPENAI_MODEL=anthropic/claude-3.5-haiku

我用的是 OpenRouter，支付方便，模型众多。大家尝试的话，可以注册一个 OpenRouter，即使没有充值，可以有每天 50 次免费模型的额度，例如**deepseek/deepseek-chat-v3-0324:free**  
让环境变量生效

    export $(cat .env | xargs)

1. 5. 运行 A2A Server

    bun run agents:coder

1. 6. 再打开一个新的终端，运行 A2A Client，这里不需要配置 env

    bun run a2a:cli

以下是我之前运行的结果：

    bun run a2a:cli

    # result
    $ bun x tsx src/cli.ts
    A2A Terminal Client
    Agent URL: http://localhost:41241
    Attempting to fetch agent card from: http://localhost:41241/.well-known/agent.json
    ✓ Agent Card Found:
      Name:        Coder Agent
      Description: An agent that generates code based on natural language instructions and streams file outputs.
      Version:     0.0.1
    Starting Task ID: a1a608b3-3015-4404-a83f-6ccc05083761
    Enter messages, or use '/new' to start a new task.
    Coder Agent > You: implement binary search
    Sending...

    Coder Agent \[4:28:00 PM\]: ⏳ Status: working
      Part 1: 📝 Text: Generating code...

    Coder Agent \[4:28:02 PM\]: ⏳ Status: working
      Part 1: 📄 File: Name: src/algorithms/binary_search.py, Source: """
    Implementation of the binary search algorithm in Python.
    """

    def binary_search(arr, target):
        """
        Performs a binary search on a sorted array to find the index of a target value.

        Args:
            arr (list): A sorted list of elements.
            target: The value to search for in the array.

        Returns:
            int: The index of the target value if found, otherwise -1.
        """
        low = 0
        high = len(arr) - 1

        while low \<= high:
            mid = (low + high) // 2  # Integer division to find the middle index

            if arr\[mid\] == target:
                return mid  # Target found at index mid
            elif arr\[mid\] \< target:
                low = mid + 1  # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half

        return -1  # Target not found in the array

    Coder Agent \[4:28:02 PM\]: ✅ Status: completed
    SSE stream finished for method tasks/sendSubscribe.
    --- End of response for this input ---
    Coder Agent \> You:
    Exiting terminal client. Goodbye!

运行过程的流程图如下：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FuVhqWvaiaiaPPibzcKOSmFfib3TVvFDZVE4Ho468btMAaNcr7HxUY1tHEZz1CZL3V0nV51vwzv662ZExe5Zq98YPaA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

目前非程序员用户想体验，还需要耐心等待，也可以借助 Cursor 等试一试。

## A2A 与 MCP 比较

这个问题，很多人关心，我大概做了一个总结：

|  特性   |          A2A           |                  MCP                   |
|-------|------------------------|----------------------------------------|
| 主要用途  | 代理间通信和协作               | 为模型提供工具和上下文，连接外部资源                     |
| 核心架构  | 客户端-服务器（代理-代理）         | 客户端-主机-服务器（应用-LLM-外部资源）                |
| 标准接口  | JSON 规范、代理卡、任务、消息、工件   | JSON-RPC 2.0、资源、工具、记忆、提示               |
| 关键特性  | 多模态、动态协作、安全性、任务管理、能力发现 | 模块化、安全边界、可重用连接器、SDK、工具发现               |
| 通信协议  | HTTP, JSON-RPC, SSE    | JSON-RPC 2.0 over stdio, HTTP with SSE |
| 性能重点  | 异步通信，处理负载              | 高效上下文管理、并行处理、缓存以提高吞吐量                  |
| 采用与社区 | 初期行业支持良好，新兴生态系统        | 行业广泛采用，社区快速增长                          |


同时，我也在做一些思考，

* • 我们要如何区分 Agent 和 Tools？真的有绝对的边界么？

* • 目前从技术上看，A2A 适应的场景更多，包括了 MCP 的场景

* • 如果未来 Agent 很多，以及 MCP server 很多，会构成一个什么样的网络呢？前者更倾向于去中心化的，后者更倾向于中心化的。前者更倾向于分散自治，后者是集中的管理。

都在思考中，需要更多的实践。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODIzNDQ3Mw==&mid=2649970759&idx=1&sn=7000610d26f68d82024d6f6cd6ecce64&chksm=bf46e81f1f6b3d8fa05797a769a4e69755a610cc0aeea25360cc7053595be96fbaebb0df4f0e&mpshare=1&scene=1&srcid=0427Kwj1pVCOC9j1zoNsHmqI&sharer_shareinfo=aaa621e0fb3d58adefa8686cb288f371&sharer_shareinfo_first=aaa621e0fb3d58adefa8686cb288f371)

