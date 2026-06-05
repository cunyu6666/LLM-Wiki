---
id: "7412019721924513221"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499355&idx=1&sn=17377960dcfc3d276608d7ceebc78094&chksm=cfe629cd7ac42dce9f53c65061cd0405bb789cb57ebde605352bf34384ebbd391c417e3c0bb0&mpshare=1&scene=1&srcid=0115IVhiKc0Lg2POpAFN0Dw8&sharer_shareinfo=6716e8fc6b11d077c23c083000bb555b&sharer_shareinfo_first=6716e8fc6b11d077c23c083000bb555b
author: "有新 有新Newin"
collected: 2026-01-17
tags: []
---

# Claude Cowork 前脚刚发布，Eigent 后脚就被推上了台面

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499355&idx=1) · 有新 有新Newin


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHfpLmI5MibCVKPa7bw396N24PpDAAOOtc3VBhhHzkZI3cYXTefB8ThIIibMvjQj9WT321nz6IYym3qg%2F640%3Fwx_fmt%3Dother%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHc53LPCRfxmtjPPicOibpicR793VFTG3TBzZBMmXUnU8f4qvricdsFtBdE9yoBTczzZK4lO4f6XYtuMgA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHfpLmI5MibCVKPa7bw396N24gBz2qTSicrwzRYAvvwsU9Agh6QzwKffAxiaf0f67iaicXic0gu39TFeIEsA%2F640%3Fwx_fmt%3Dpng%23imgIndex%3D2)

![](https://image.cubox.pro/cardImg/5xbo8i461slx307hutrhuyfzwykc6r5mmw5g2erh4bp87vvvyu?imageMogr2/quality/90/ignore-error/1)

**有新Newin**

探索新科技，聚焦新价值。

827篇原创内容

<br />

公众号  

，

在 Claude 推出 Cowork 功能后，一个明显的信号 ------ Agent 不仅仅是辅助工具，而是一种可以被设计、被组织、被反复调用的协作单元。

几乎在同一时间，一条创始人的推文在 X 上流传开来，内容很直接：**如果你想要一个 Cowork，但不想被绑在云端、不想被模型和权限限制，其实已经有一个开源替代方案存在** 。这条推文很快拿到了 8**000+ 点赞、超 150 万次浏览** ，讨论点也逐渐收敛到同一个名字------Eigent。

搜了一下，发现 Eigent 不是凭空出现的产品，其背后团队先前开发的 CAMEL 项目本身就是当前多智能体领域里被反复引用的一套基础框架，也是**最早系统性提出并实现多 Agent 协作范式的开源项目之一** 。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHc53LPCRfxmtjPPicOibpicR79fjrMvbfSXzQ71bRM03SoBT0W8hggqYeHv4Ey5Qr092GAXmr60Pr0VA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

围绕 CAMEL，该团队先后开源了多个多智能体相关项目，包括 CAMEL、OWL 和 OASIS，在 GitHub 上累计获得了数万级别的 stars，被广泛用于研究、实验和实际系统搭建中。

Eigent 更像是一层开放的执行基础设施，以开源的方式呈现任务拆解、调度与执行机制，使其能够被复用、扩展和二次开发；既可以作为一个即用型工具运行，也构成了一套可以被接入不同系统、持续生长的开源生态基础。

▍Eigent 的开源契机

最早围绕 Eigent 的讨论，并不友好。Claude 公布 Cowork 之后，很多人的第一反应是：**这类多 Agent 协作工具的窗口期已经关上了** 。大厂掌握模型、产品入口和分发能力，独立项目很难在同一条线上正面竞争，尤其是在"协作"这种高度平台化的方向上。

事情的转折，来自创始人的一条推文，可以说 Claude Cowork 的发布推动了团队全面开源 Eigent 这款产品：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHcY7cMN7Wkzibe2jdmfuEUGF5jFHVq8BJ7wWIMZyTwFdQvl6L9SicGpsaZicwORvxP95VxVnk5AXlicBg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

**这条推文意外引发了大规模转发，在极短时间内拿到数千点赞和百万级浏览** ，也把 Eigent 这个名字推到了更大的视野里。讨论的重点开始从"会不会被覆盖"，转向"为什么它和 Cowork 看起来不太一样"。

随之而来的，是一系列非常明确、甚至有些激进的动作。域名被迅速买下，项目定位被重新表述，**License 被直接改成 Apache 2.0** ，提交记录里没有长篇解释，甚至有点随意，但态度已经很明确了 ------ 以开源的形式，将选择权交给使用者和开发者。

大家也慢慢意识到，Eigent 的诞生源自 CAMEL 这套多智能体体系里，产品的设计思路也很清晰：先把事情拆解，再多个 Agent 分工推进，用并行的方式把问题解决，而不是依赖一个全能的 Agent。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHc53LPCRfxmtjPPicOibpicR79YqvETt5oSHq2dP9S7G8xFvqHZEicWCmBSDmjhMCWrBhaTnCcUMEp8TA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

这套思路很快被外部节点注意到，包括 Google Gemini 对其"下一代 Agent"方向的公开提及，也包括来自 xAI、Hugging Face 等社区核心人物的互动。

就在 5 天前，团队发布了一个围绕 **terminal agents 的执行环境扩展（scaling environments for terminal agents）** 的新项目，继续向"Agent 如何接管真实执行环境"这一问题推进,这一发布很快在技术圈内获得反馈，包括来自 Andrej Karpathy、John Schulman 等人的互动。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHc53LPCRfxmtjPPicOibpicR7944nZ8S5eY4L8iaMRDTfEyU0Z5PYv3Gc4Jobn5icAhxIpKhLj5Tkp1UBg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

于是，"会不会被杀死"已经不再是讨论的中心，反而是进入到了一个必须认真对待的阶段。团队开始公开招人，目标也变得更明确------不再只是做一个概念验证，而是全力推进一个从模型、工具到桌面形态都完全开源的本地 Agent 系统。  

▍Agent 开始在电脑上帮你把事做完

和大量停留在浏览器或聊天窗口里的 Agent 产品不同，Eigent 从一开始就被做成一个 **多智能体工作流的桌面应用程序** ，目标是将复杂流程直接变成可执行任务。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

这种取向首先体现在它对执行环境的选择上。Eigent 并不要求用户做复杂配置，也不强制绑定云端模型，而是支持 **本地部署、开源运行和自定义模型接入。**

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

在实际使用中，Agent 可以**同时操控浏览器、Terminal 以及本地文件系统；在任务层面，Eigent 的设计逻辑接近真实团队协作。**

**Eigent 会将一个目标动态拆解成多个子任务，并激活不同类型的智能体并行推进：** **开发智能体负责代码和终端命令，搜索智能体负责网页检索和内容提取，文档智能体整理输出结果，多模态智能体处理图像和音频** 。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHc53LPCRfxmtjPPicOibpicR79B2SvaiahLlCkLRjialwZfH1GCahR0EDWK79iaQ01xoiaWnPibLsPcyDkH4Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)

这种结构，使得很多原本需要人工反复切换工具的工作，可以被压缩成一次指令。例如，从本地 CSV 文件生成财务报告、清理下载目录中的重复文件，甚至直接在本地完成 PDF 签名和文档整理。Agent 不再只是给建议，而是**直接在用户机器上完成操作本身** 。

在这个意义上，Eigent 选择以开源方式推进协作能力的演进，而 Claude Cowork 则沿着闭源产品体系持续完善。

▍Agent 各司其职，关键在调度和执行

如果只从表面看，多智能体产品很容易被理解成"同时开了几个 Agent"。但在 Eigent 的设计里，关键并不在数量，而在于 **任务是如何被系统性拆解、调度，并在同一时间推进的** 。

当一个复杂目标被提交时，Eigent 并不会让单个 Agent 从头做到尾，而是先拆任务、再分角色，让不同能力的 Worker 并行推进。规划、执行和结果整合被拆开，**没有任何一个 Agent 需要独自承担全部复杂度** 。这种机制有没有意义，只有放进真实工作里才看得出来。

**1）高频、低价值、却极费精力的日常工作**

这也是 Claude Cowork 最早被大量转发和讨论的能力之一：整理桌面和各类文件夹。场景极其普通------几十个下载项、上百张截屏、命名混乱的文档、重复文件散落在不同位置。平时看起来问题不大，但一旦需要查找、归档或复用，就会不断打断注意力。

传统工具更多是提醒：哪些文件重复了、哪些该改名了，真正的整理仍然要靠人一点点完成。Eigent 则把这类事情当成一个**需要被执行完的工作流** 。Agent 会并行扫描桌面和文件夹，识别重复或相似文件，完成分类、整理和归档，把原本零散的操作一次性跑完：

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

**2）在浏览器里跑完业务流程**

在常见的销售场景里，真正消耗时间的是在浏览器里反复点击页面。以 Salesforce 为例，推进一笔交易往往要来回跳转：改阶段、确认状态、查看联系人、再回到机会页填写下一步。这些操作本身并不难，但高频重复，很容易漏一步、填错字段。

在 Eigent 里，这类流程不再需要人一页一页点。Agent 会直接在浏览器中完成整套操作：定位到 "200 Widgets" 这笔交易，更新阶段，进入联系人页面读取姓名和电话，再返回机会页把 "Next Step" 一次性填好。**整个过程发生在真实网页里，就像有人在替你操作浏览器** 。

以下视频来源于

CAMEL AI

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

解决的其实是一个更普遍的问题：有多少工作，本质上只是发生在浏览器和本地环境里的重复操作。当这些流程能够被稳定执行，人就可以把精力从反复点击中抽离出来，用在判断、沟通和推进关系上。

把这些场景放在一起看，会发现它们有一个共同点：一边是整理桌面、清理文件夹这类高频、低价值却持续消耗注意力的工作，另一边是在浏览器中反复推进业务流程、填写字段、切换页面的连续操作。它们并不复杂，却占据了大量真实工作的时间。

随着 Claude 推出 Cowork，这类协作型 Agent 的价值开始被更广泛地理解，多 Agent 参与执行流程也逐渐成为共识。

在这一背景下，Eigent 选择沿着同一条执行路径继续向下展开，将协作进一步延伸到本地、浏览器和 Terminal 等真实执行环境中，并从一开始就以开源生态为核心推进。围绕这些执行能力，相关实现、代码、文档和实践示例持续沉淀在官网和 GitHub 上，逐步形成一个面向开发者、可以参与共建的开源生态。

GitHub：**https://github.com/eigent-ai/eigent**

**官网：****https://www.eigent.ai/******

根据最新消息，Eigent 在今天登顶了 GitHub Trending 榜单 NO.1，成为当天最受关注的项目之一：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHcY7cMN7Wkzibe2jdmfuEUGFmlk232Y9S4G9WibGH98jic2IyibicUOLd7mzZLxfQWpoICnvLlP1Hup95Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D8)

**✦** **最新活动** **✦**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FwqO5B9doEHeoEiaIkf48L6h81oks0gzFJlmlia1TiboCGVAQ4cbgC5bqYH5LSYoAfSaRcyFABJ0okescWn8lxRttA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D9)

**✦** **精选内容** **✦**

**[Workus AI：不只是销售自动化，还想重新定义"全球商业关系"](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499327&idx=1&sn=00a28716722c21996ce79d3502616ea3&scene=21#wechat_redirect)**

**[AllScale：为全球"超级个体"打造的数字银行](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499304&idx=1&sn=cb9ce1a1f844d520f389f6dd7b3a004d&scene=21#wechat_redirect)**

**[不只是出图工具，Lovart 正在让设计告别返工](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499287&idx=1&sn=864e707d49abaf74a758ee3d08d0cb61&scene=21#wechat_redirect)**

**[豆包大模型日均 tokens 使用量超 50 万亿！同比去年增长超十倍](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499266&idx=1&sn=49b3de5059ee0380688ed012ce7355de&scene=21#wechat_redirect)**

**[Seko2.0 让长线创作不再是奢侈品](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499219&idx=1&sn=0a8b91b9a13dfdb932ee84c8ebe01ddf&scene=21#wechat_redirect)**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHfpLmI5MibCVKPa7bw396N24za67FmrIFnk3Ye6HDGMwp7Sf4oNIdWTsUugRnQ3WSKwticba27xZ88Q%2F640%3Fwx_fmt%3Dpng%23imgIndex%3D10)

![](https://image.cubox.pro/cardImg/5xbo8i461slx307hutrhuyfzwykc6r5mmw5g2erh4bp87vvvyu?imageMogr2/quality/90/ignore-error/1)

**有新Newin**

探索新科技，聚焦新价值。

827篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwqO5B9doEHfpLmI5MibCVKPa7bw396N24V1YrxWz29QrkAUrO7QILtUGHwUoBhxhxyZGbdvpaNg067cUpVAksibw%2F640%3Fwx_fmt%3Dpng%23imgIndex%3D11)

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247499355&idx=1)
