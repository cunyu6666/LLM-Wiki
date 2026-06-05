---
id: "7449835777116078910"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI1NzUxOTUzMA==&mid=2247486518&idx=1&sn=9a3186998bbbef48051f5ac15244c0d4&chksm=ebfe31acf1ed0b786a7973f6a856881b0377e63552c970acedd8c561c8290890348c40a8b79b&mpshare=1&scene=1&srcid=05017vqfG9cNSg85CiHKOQeV&sharer_shareinfo=8bdf813459ad5e5d80d7dc2ad172c491&sharer_shareinfo_first=8bdf813459ad5e5d80d7dc2ad172c491
author: "teacher李 由由学习吧"
collected: 2026-05-01
tags: []
---

# 用不具备tools的弱模型实现tools能力

# 用不具备tools的弱模型实现tools能力

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1NzUxOTUzMA==&mid=2247486518&idx=1&sn=9a3186998bbbef48051f5ac15244c0d4&chksm=ebfe31acf1ed0b786a7973f6a856881b0377e63552c970acedd8c561c8290890348c40a8b79b&mpshare=1&scene=1&srcid=05017vqfG9cNSg85CiHKOQeV&sharer_shareinfo=8bdf813459ad5e5d80d7dc2ad172c491&sharer_shareinfo_first=8bdf813459ad5e5d80d7dc2ad172c491)teacher李 由由学习吧

像**OpenClaw / OpenDevin / CodeLlama 执行命令的本质的** 最小可运行结构：

*
  模型输出 JSON
*
  你写一段 Python/JS 解析 JSON
*
  调用 subprocess 执行
*
  把结果返回模型

这里使用的模型都是经过专门训练的

## 能做 "外部执行" 的模型，必须具备的能力

*
  JSON
*
  FunctionCall
*
  ToolCall
*
  ACP（OpenClaw 自己的协议）
* 

我们这里只是谈怎么能使用不具备tools的弱模型，比如一些7b以下的对话模型怎么实现具备执行外部工具的能力呢？

这里我采取的方案是：普通模型 + 提示词 + 正则 + 容错

流程就是：

1.
   模型随便输出（带废话、带解释、带 JSON）
2.
   你用正则把 { ... } 抠出来
3.
   尝试 json.loads()
4.
   能解析 → 执行；不能解析 → 重试 / 报错

**简单任务：90% 能用。**

## 那专门训练过的模型，到底多了什么？

不是更聪明，是**输出结构被锁死了** ：

*
  输出**只有** 工具调用格式，没有废话
*
  引号、括号、逗号**永远正确**
*
  知道**什么时候必须调用工具**
*
  知道**下一步要继续执行**

它是**从生成源头就保证格式合法** ，而不是**靠后期抢救** 。

示例代码：

    import jsonimport reimport subprocessfrom typing import Optional, Dict, Any# ------------------------------------------------------------------------------# 1. 模拟你的模型调用（换成你自己的模型：OpenAI、本地Llama、Qwen等都行）# ------------------------------------------------------------------------------def call_llm(prompt: str) -> str:    """    替换成你真实的模型接口：本地llama.cpp / Ollama / API 都行    这里只是模拟返回一段带废话+JSON的输出    """    # 模拟模型输出：前面废话 + 中间JSON + 后面废话    return """    好的，我帮你执行命令：    {        'tool': 'shell',        'command': 'dir'  # 注意我故意用了单引号，测试容错    }    执行完成后我会告诉你结果。    """# ------------------------------------------------------------------------------# 2. 正则提取 {...}，支持多行# ------------------------------------------------------------------------------def extract_json(text: str) -> Optional[str]:    # 匹配第一个 { ... }，非贪婪，支持多行    pattern = r"\{[\s\S]*?\}"    match = re.search(pattern, text)    if not match:        return None    return match.group(0)# ------------------------------------------------------------------------------# 3. 容错JSON解析：修单引号、去注释、容错解析# ------------------------------------------------------------------------------def safe_json_loads(json_str: str) -> Optional[Dict[str, Any]]:    try:        # 1. 单引号 -> 双引号        json_str = json_str.replace("'", '"')                # 2. 简单去掉 // 注释（只处理单行注释）        json_str = re.sub(r"//.*", "", json_str)                # 3. 解析        return json.loads(json_str)    except Exception:        return None# ------------------------------------------------------------------------------# 4. 安全执行命令（Windows / Linux 通用）# ------------------------------------------------------------------------------def run_command(cmd: str, timeout=10) -> dict:    try:        result = subprocess.run(            cmd,            shell=True,            capture_output=True,            text=True,            timeout=timeout        )        return {            "success": result.returncode == 0,            "stdout": result.stdout,            "stderr": result.stderr        }    except subprocess.TimeoutExpired:        return {"success": False, "error": "timeout"}    except Exception as e:        return {"success": False, "error": str(e)}# ------------------------------------------------------------------------------# 5. 主流程：提问 → 取JSON → 执行 → 输出# ------------------------------------------------------------------------------def agent_execute(user_query: str):    # === 强提示词：逼模型输出JSON ===    prompt = f"""你是一个命令执行助手。用户需求：{user_query}你必须只输出一个JSON，不要任何多余文字、解释、对话。格式严格如下：{{    "tool": "shell",    "command": "你的命令"}}""".strip()    print("=== 发送给模型的提示词 ===")    print(prompt)    print("=" * 50)    # 1. 调用模型    llm_output = call_llm(prompt)    print("=== 模型原始输出 ===")    print(llm_output)    print("=" * 50)    # 2. 正则提取JSON    json_str = extract_json(llm_output)    if not json_str:        print("❌ 未提取到JSON")        return    print("=== 正则提取到的JSON ===")    print(json_str)    print("=" * 50)    # 3. 容错解析    tool_call = safe_json_loads(json_str)    if not tool_call:        print("❌ JSON解析失败")    print("=== 解析后工具调用 ===")    print(tool_call)    print("=" * 50)    # 4. 只允许shell工具，做安全限制    if tool_call.get("tool") != "shell":        print("❌ 不支持的工具")        return    cmd = tool_call.get("command")    if not cmd:        print("❌ 无命令")        return    # 5. 执行    print(f"▶️ 执行命令: {cmd}")    result = run_command(cmd)    print("=" * 50)    print("=== 执行结果 ===")    print(json.dumps(result, indent=2, ensure_ascii=False))# ------------------------------------------------------------------------------# 运行# ------------------------------------------------------------------------------if __name__ == "__main__":    agent_execute("查看当前目录")


*
  模型输出**带废话** → 正则干掉
*
  模型用**单引号** → 自动修复
*
  模型加 \*\*// 注释 \*\* → 自动删除
*
  执行**超时、报错、崩溃** → 全捕获
*
  只执行**shell** ，可加白名单


如果你想在 ReAct 框架中增加多轮循环能力（将每轮执行结果反馈给大模型），同时为命令执行添加白名单机制和路径访问限制，以此提升安全性和可控性可以参考下面示例。

    import subprocessimport osfrom typing import List, Dict, Optionalclass SafeReActExecutor:    def __init__(        self,        command_whitelist: List[str],        allowed_paths: List[str],        max_rounds: int = 5  # 限制最大循环轮数，防止无限执行    ):        # 初始化核心配置        self.command_whitelist = set(command_whitelist)  # 命令白名单（如ls, pwd, cat）        self.allowed_paths = [os.path.abspath(p) for p in allowed_paths]  # 允许访问的路径        self.max_rounds = max_rounds        self.conversation_history = []  # 存储多轮交互历史    def _is_path_allowed(self, path: str) -> bool:        """检查路径是否在允许范围内"""        abs_path = os.path.abspath(path)        for allowed in self.allowed_paths:            if abs_path.startswith(allowed):                return True        return False    def _sanitize_command(self, command: List[str]) -> Optional[List[str]]:        """        命令安全校验：        1. 检查主命令是否在白名单        2. 检查路径参数是否合规        """        if not command:            return None
            # 第一步：校验主命令        main_cmd = command[0]        if main_cmd not in self.command_whitelist:            print(f"❌ 命令 {main_cmd} 不在白名单中，禁止执行")            return None
            # 第二步：校验路径参数（针对涉及文件操作的命令）        path_related_cmds = {"cat", "ls", "rm", "cp", "mv"}        if main_cmd in path_related_cmds and len(command) > 1:            for arg in command[1:]:                if os.path.exists(arg) and not self._is_path_allowed(arg):                    print(f"❌ 路径 {arg} 不在允许范围内，禁止访问")                    return None
            return command    def execute_command(self, command_str: str) -> str:        """执行命令（带安全校验），返回执行结果"""        # 拆分命令（简单拆分，实际场景可使用shlex.split）        command = command_str.strip().split()        if not command:            return "⚠️ 空命令，无执行结果"
            # 安全校验        sanitized_cmd = self._sanitize_command(command)        if not sanitized_cmd:            return "❌ 命令校验失败，禁止执行"
            # 执行命令        try:            result = subprocess.run(                sanitized_cmd,                capture_output=True,                text=True,                timeout=10,  # 超时限制                cwd=self.allowed_paths[0] if self.allowed_paths else os.getcwd()  # 限制工作目录            )            # 拼接输出结果            output = f"✅ 执行成功:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"        except subprocess.TimeoutExpired:            output = "❌ 命令执行超时"        except Exception as e:            output = f"❌ 命令执行异常: {str(e)}"
            return output    def react_loop(self, initial_prompt: str, llm_predict_func):        """        多轮 ReAct 循环核心逻辑        :param initial_prompt: 初始提示词        :param llm_predict_func: 大模型预测函数（输入prompt返回思考+命令）        """        current_prompt = initial_prompt        self.conversation_history.append(f"初始提示: {initial_prompt}")        # 多轮循环        for round_num in range(1, self.max_rounds + 1):            print(f"\n===== ReAct 循环第 {round_num} 轮 =====")
                # 1. 大模型思考并生成命令（核心ReAct步骤）            llm_response = llm_predict_func(current_prompt)            print(f"🤖 模型输出: {llm_response}")            self.conversation_history.append(f"第{round_num}轮模型输出: {llm_response}")            # 2. 提取命令（简化版，实际需解析模型输出中的命令）            # 假设模型输出格式："思考：需要查看文件... 执行：cat test.txt"            command_str = None            if "执行：" in llm_response:                command_str = llm_response.split("执行：")[-1].strip()
                if not command_str:                print("⚠️ 未提取到有效命令，结束本轮循环")                break            # 3. 执行命令并获取结果            exec_result = self.execute_command(command_str)            print(f"🖥️  命令执行结果: {exec_result}")            self.conversation_history.append(f"第{round_num}轮执行结果: {exec_result}")            # 4. 构建新一轮prompt（将执行结果反馈给模型）            current_prompt = f"""            历史交互：{self.conversation_history}            上一轮命令执行结果：{exec_result}            请基于上述结果继续思考，若任务完成则回复"任务完成"，否则生成下一条执行命令（格式：思考：xxx 执行：xxx）            """            # 5. 检查是否结束循环            if "任务完成" in llm_response or round_num == self.max_rounds:                print(f"\n📌 ReAct 循环结束（{'任务完成' if '任务完成' in llm_response else '达到最大轮数'}）")                break        return self.conversation_history# ------------------- 测试示例 -------------------def mock_llm_predict(prompt: str) -> str:    """模拟大模型预测函数（实际替换为真实LLM调用）"""    # 模拟多轮思考逻辑    if "test.txt" in prompt and "第1轮" not in prompt:        return "思考：需要查看test.txt内容 执行：cat test.txt"    elif "执行结果" in prompt and "STDOUT" in prompt:        return "思考：已成功查看文件内容，任务完成 执行：任务完成"    else:        return "思考：先查看当前目录文件 执行：ls"if __name__ == "__main__":    # 初始化执行器：白名单+路径限制+最大5轮循环    executor = SafeReActExecutor(        command_whitelist=["ls", "cat", "pwd"],  # 仅允许这3个命令        allowed_paths=[os.path.abspath("./safe_dir")],  # 仅允许访问safe_dir目录        max_rounds=5    )    # 创建测试目录（确保路径存在）    os.makedirs("./safe_dir", exist_ok=True)    with open("./safe_dir/test.txt", "w") as f:        f.write("测试内容：Hello ReAct!")    # 启动多轮ReAct循环    initial_prompt = "请查看safe_dir目录下的test.txt文件内容"    history = executor.react_loop(initial_prompt, mock_llm_predict)    # 输出最终交互历史    print("\n===== 最终交互历史 =====")    for item in history:        print(item)


#### 1. 多轮 ReAct 循环

* **循环机制**
  ：通过 react_loop 函数实现固定轮数（可配置）的循环，每轮包含「模型思考→提取命令→执行命令→结果反馈」完整流程
* **结果反馈**
  ：将每轮命令执行结果拼接进新一轮 prompt，让模型基于历史结果继续决策
* **终止条件**
  ：支持两种终止方式 ------ 模型回复「任务完成」或达到最大轮数，防止无限循环

#### 2. 命令白名单

* **核心逻辑**
  ：_sanitize_command 函数首先校验主命令是否在白名单（如仅允许 ls/cat/pwd）
* **配置方式**
  ：初始化时通过 command_whitelist 参数指定允许执行的命令列表，不在列表中的命令直接禁止
* **示例**
  ：如果模型生成 rm test.txt，因 rm 不在白名单，会直接返回校验失败

#### 3. 路径限制

* **路径校验**
  ：_is_path_allowed 函数检查命令中的路径参数是否在允许范围内（通过绝对路径前缀匹配）
* **工作目录限制**
  ：执行命令时强制指定工作目录为允许路径，防止访问其他目录
* **示例**
  ：若允许路径为 ./safe_dir，则 cat ../other.txt 会因路径越权被禁止

这就是解决用不具备tools的弱模型实现tools能力的基本逻辑

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1NzUxOTUzMA==&mid=2247486518&idx=1&sn=9a3186998bbbef48051f5ac15244c0d4&chksm=ebfe31acf1ed0b786a7973f6a856881b0377e63552c970acedd8c561c8290890348c40a8b79b&mpshare=1&scene=1&srcid=05017vqfG9cNSg85CiHKOQeV&sharer_shareinfo=8bdf813459ad5e5d80d7dc2ad172c491&sharer_shareinfo_first=8bdf813459ad5e5d80d7dc2ad172c491)

