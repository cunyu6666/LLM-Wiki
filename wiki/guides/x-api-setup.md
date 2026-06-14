# X (Twitter) API 调通指南

> 记录从 0 到 1 调通 twitter-cli 的完整流程，包括代理配置、Cookie 导出、环境变量设置。

## 问题背景

macOS 环境下使用 `twitter-cli` 搜索推文时遇到以下问题：

1. **网络超时**：直接访问 x.com 被墙，连接超时
2. **未登录**：`twitter doctor` 显示 `env_auth_token_set: false`，无法使用搜索等需要认证的功能
3. **代理不生效**：系统有代理（ClashX Pro），但 twitter-cli 不走代理

## 环境要求

- macOS（本指南基于 macOS 13.7）
- ClashX Pro 或其他代理工具（端口 7890）
- twitter-cli v0.7.0+（`pipx install twitter-cli`）
- 已登录的 X 账号

## 步骤 1：导出 X 登录 Cookie

### 方法 A：浏览器扩展（推荐）

1. 安装浏览器扩展 **"Get cookies.txt LOCALLY"**
   - Chrome: https://chromewebstore.google.com/detail/ccleffnvagkjblgbojedbhgfnchogbco
   - Edge: 同上

2. 在浏览器登录 **x.com**

3. 点击扩展图标 → 导出 cookies.txt → 保存到本地（如 `~/Downloads/x.com_cookies.txt`）

4. 从文件中提取两个关键值：
   ```bash
   grep -E "auth_token|ct0" ~/Downloads/x.com_cookies.txt
   ```
   
   输出类似：
   ```
   .x.com  TRUE  /  TRUE  1812980385  auth_token  25fd0f7a964251416e2573ab922720a50d73e1f1
   .x.com  TRUE  /  TRUE  1816004386  ct0         61dfe1ddd8eb82258e189a643587b378...
   ```

5. 复制 `auth_token` 和 `ct0` 的值

### 方法 B：浏览器 DevTools

1. 打开 x.com → F12 → Application → Cookies → https://x.com
2. 找到 `auth_token` 和 `ct0`，复制值

### 方法 C：Cookie-Editor 扩展

1. 安装 Cookie-Editor 扩展
2. 登录 x.com → 点击扩展 → 找到 `auth_token` 和 `ct0` → 复制

## 步骤 2：配置代理

### 检查系统代理

```bash
# 查看 macOS 系统代理设置
networksetup -getwebproxy Wi-Fi
networksetup -getsecurewebproxy Wi-Fi

# 检查代理端口是否开放
for port in 1080 1087 7890 7891 8080 8118 9090 10808 10809; do
  (echo >/dev/tcp/127.0.0.1/$port) 2>/dev/null && echo "Port $port is OPEN"
done

# 检查代理进程
ps aux | grep -iE "surge|clash|v2ray|shadowsock|trojan|proxy" | grep -v grep
```

### 常见代理端口

| 工具 | 默认端口 |
|------|----------|
| ClashX Pro | 7890 |
| Surge | 6152 / 6153 |
| V2Ray | 10808 / 10809 |
| Shadowsocks | 1080 |

## 步骤 3：设置环境变量

编辑 `~/.zshrc`（或 `~/.bashrc`），添加：

```bash
# ===== 代理配置 =====
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
# 如果需要排除本地地址：
# export no_proxy=localhost,127.0.0.1,localaddress,.localdomain.com

# ===== Twitter/X API =====
export TWITTER_AUTH_TOKEN="你的auth_token值"
export TWITTER_CT0="你的ct0值"
```

刷新环境变量：

```bash
source ~/.zshrc
```

## 步骤 4：验证配置

### 验证代理

```bash
# 测试代理是否生效
curl -s -o /dev/null -w "%{http_code}" --proxy http://127.0.0.1:7890 https://x.com
# 应该返回 200
```

### 验证 Twitter 登录

```bash
twitter doctor
```

应该显示：
```
ok: true
env_auth_token_set: true
env_ct0_set: true
screen_name: '你的用户名'   # 如果有值说明登录成功
```

### 测试搜索

```bash
# 简单搜索测试
twitter search "designer" -n 5 --yaml
```

## 步骤 5：常用命令

```bash
# 搜索推文（按热度）
twitter search "designer vibe coding" --min-likes 50 -n 20 --since 2025-01-01 --yaml

# 搜索推文（按时间）
twitter search "AI agent" -n 20 --type Latest --yaml

# 查看用户时间线
twitter user-posts @ryolu_ -n 20 --yaml

# 查看单条推文
twitter tweet https://x.com/username/status/1234567890 --yaml

# 首页时间线
twitter feed -n 20 --yaml
```

## 常见问题

### Q: twitter search 返回 404 或超时

**原因**：Twitter 频繁修改 GraphQL API 端点

**解决**：
```bash
pipx upgrade twitter-cli
```

### Q: 代理设置了但还是超时

**排查**：
1. 确认代理进程在运行：`ps aux | grep clash`
2. 确认端口开放：`lsof -i :7890`
3. 手动测试：`curl -x http://127.0.0.1:7890 https://x.com`
4. 检查 ClashX Pro 是否开启了"系统代理"

### Q: twitter doctor 显示 screen_name 为空

**原因**：Cookie 可能过期或无效

**解决**：重新导出 Cookie，更新环境变量

### Q: 不想每次手动设置代理

**方案 A**：写入 `~/.zshrc`（本指南方案）

**方案 B**：在 ClashX Pro 设置中开启"设置为系统代理"，大部分工具会自动走系统代理

**方案 C**：使用 proxychains（更高级）
```bash
brew install proxychains-ng
# 编辑 /usr/local/etc/proxychains.conf
# 最后一行改为：socks5 127.0.0.1 7890
# 使用：proxychains4 twitter search "query"
```

## 完整配置模板

```bash
# ~/.zshrc 追加内容

# ===== 代理 =====
# ClashX Pro 默认端口 7890
# 如果不用代理，注释掉下面两行即可
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890

# ===== Twitter/X =====
# 从浏览器 Cookie 导出，过期后需要重新获取
export TWITTER_AUTH_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWITTER_CT0="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## 相关链接

- twitter-cli 文档：https://github.com/Panniantong/agent-reach（agent-reach 内置）
- agent-reach skill 路由：`~/.agents/skills/agent-reach/references/social.md`
- X API 限制：搜索 API 可能随时被 Twitter 修改，需要保持 twitter-cli 更新

---

*最后更新：2026-06-14*
*环境：macOS 13.7 + ClashX Pro + twitter-cli 0.7.0*
