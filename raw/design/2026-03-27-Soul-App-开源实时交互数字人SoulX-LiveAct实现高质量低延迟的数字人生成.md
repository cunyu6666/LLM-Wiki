---
id: "7437067086838370294"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODkyOTkwOQ==&mid=2247497944&idx=1&sn=7071139c633003de08bed106c5499087&chksm=c1559a03cff8c2b834030030e7ccf7e6fd5323fa5ff418235f711bd0b79e55ac6d14737ea4d1&mpshare=1&scene=1&srcid=0327Sg9Q3EaiMst8BaaPQEuK&sharer_shareinfo=01a868fb1f305cd418cf41ea1a5bbe0b&sharer_shareinfo_first=01a868fb1f305cd418cf41ea1a5bbe0b
author: "鳗鱼 AIGitHub"
collected: 2026-03-27
tags: []
---

# Soul App 开源实时交互数字人！SoulX-LiveAct：实现高质量、低延迟的数字人生成。

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg5ODkyOTkwOQ==&mid=2247497944&idx=1) · 鳗鱼 AIGitHub


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZdrSHaq5Gr1uXuaAG1Jgibd5DC6ibtVhrX4ff5eQib3ZApns6BEqpPxkBUXQ2PHQMsO6E9djzk54CbcU4MPx8Zibicg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26randomid%3Du1uwjimf%23imgIndex%3D0)

SoulX-LiveAct是Soul App AI Lab开源的一款实时数字人生成框架，它系统性地解决了自回归（AR）扩散模型在流式生成场景中长期存在的稳定性难题。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9Qib8Ek8cFpj39h0QQmmrm1sibFx0Gou2yw3ASRA5vWSPWicPvmqoab8M3kCPRKtrpoPybxZeZnIOt8rRLEliaFicBqtVdlmsyjPpTY4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D17)

传统扩散模型在生成视频时采用逐帧生成方式，但在实时应用（如直播、视频通话）中，这种模式会导致严重的画面抖动、人物变形、身份漂移和细节不一致等问题。

SoulX-LiveAct通过一系列创新技术，实现了高质量、高稳定性、低延迟的实时数字人视频生成。

以下视频来源于

Soul社交

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

##### **功能特点**


**实时流式推理能力**

在双卡H100/H200配置下，SoulX-LiveAct能够在720×416或512×512分辨率下实现20 FPS的实时生成速度，端到端延迟仅0.94秒。这一性能指标使其能够满足直播、实时对话等对延迟敏感的应用需求。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9Qibte6jHZx3q5ALvFNPJPIIEzSCBV19MIibrFrXvO340d4pokJblnA6JoicVueGDCRHesntklJc25bJCDGqc4pUWBb4qfOx9Mp3T0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D18)

**长时视频生成**

框架支持小时级甚至理论上的无限时长视频生成，突破了传统视频生成模型随时长增加显存占用线性增长的技术瓶颈。实测表明，系统能够在长时间运行中保持稳定的性能表现。

**精准的口型与表情同步**

集成chinese-wav2vec2-base音频编码器，能够根据输入的音频信号实时生成高度匹配的口型动作和面部表情。在技术报告中，其口型同步准确率（Sync-C）达到9.40，显著优于同类方案。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

**多分辨率支持与设备适配**

除了服务器级H100/H200配置外，框架还针对消费级显卡进行了优化。在RTX 4090/5090上，通过启用FP8 KV Cache和块卸载等技术，仍能实现24 FPS的生成速度，大大降低了使用门槛。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

**动作与表情编辑控制**

支持通过JSON配置文件对数字人的动作和表情进行精细控制，为内容创作提供了更大的灵活性和创造性空间。

性能表现

根据技术报告的对比实验数据，SoulX-LiveAct在多个关键指标上均表现出显著优势：

**口型同步质量**   

在HDTF数据集上，Sync-C指标达到9.40（越高越好），Sync-D指标降至6.76（越低越好），明显优于OmniAvatar（5.13/10.19）、InfiniteTalk（7.12/8.01）和Live-Avatar（7.68/8.38）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9Q8WV0bVVnLLibuoC0j8OSIe8gpX0za2jckG90w5zYqHXyJukOpz233AzjyZoOyXct0ur2s2xic4kdmt3kSF0GNYQJlTAejD7jc6k%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D19)

**人工评估分数**   

在VBench评估中，时序质量达到97.6，图像质量63.0，人类逼真度99.9，在所有对比方法中位列第一。

**视频质量指标**   

FID（弗雷歇起始距离）仅为10.05，远低于其他对比方法（15.85-27.90），表明生成视频与真实视频的分布最为接近。FVD（弗雷歇视频距离）为69.43，同样大幅领先。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

推理效率对比  

仅需2张GPU即可实现20 FPS吞吐和0.94秒延迟，每帧计算量（TFLOPs）仅为27.2。相比之下，InfiniteTalk需要8张GPU、3.20秒延迟和50.2 TFLOPs/帧；Live-Avatar需要5张GPU、2.89秒延迟和39.1 TFLOPs/帧。

**长时稳定性验证**   

在长时间生成测试中，基线方法普遍出现身份漂移、细节丢失、口型失配、配饰忽隐忽现等问题，而SoulX-LiveAct能在更长时间窗口内保持身份一致性与关键细节稳定。

应用场景

**播客与对话场景**   

适用于双人对谈、访谈节目、脱口秀等需要自然交互的场景。系统能够根据对话内容实时生成匹配的面部表情、眼神交流和口型动作，创造沉浸式的观看体验。

**音乐表演与歌唱**   

支持需要强表情管理和情感表达的音乐表演场景。数字人能够根据歌曲的节奏、旋律和情感变化，生成相应的面部表情和身体语言，为虚拟歌手、音乐教学等应用提供技术支持。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

**视频通话与远程交互**   

模拟真实的FaceTime体验，可用于虚拟客服、在线教育、远程医疗、企业培训等B端场景。低延迟特性确保了交互的实时性和自然性。

**内容创作与媒体制作**   

为视频创作者、广告制作、游戏开发等提供高效的数字人生成工具。支持动作和表情编辑的功能，为创意表达提供了更多可能性。


    GitHub：https://github.com/Soul-AILab/SoulX-LiveAct


**【招募兼职 AI 文案作者】**

招募熟悉 AI 领域、有写作经验的兼职作者，负责AI相关文章创作。

按篇结算，稿费从优，要求对 AI 工具、AI 应用、行业动态有一定了解，文笔通顺、逻辑清晰。

有意者可添加VX：wenhuaijun94

**欢迎扫码加入社群**

**一起交流AI前沿技术！**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FTJPc1U4E9Qib4EVHWYFQBkV4ia45Ox8XIg4sJibv8V9pBvhfAllW7zP1sq8BhTQoRpARaMtBJbe49pVRM5bWhEfK9asgoEdSocwMXETaaYZ7zA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D16)

**小编免费共享AI开源项目知识库，**

****实现大家的AI资讯自由！****

****直接扫码或点击链接即可查看！****

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FZdrSHaq5Gr2icoAqL9FLIibAkebXyIt25G4z0EOJ8nVNrIQA45Bpnbotv000NOyLBQW92us6z977xIo5Qs1zsCTg%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%26randomid%3Dhvcwn0ta%23imgIndex%3D12)

AI开源项目知识库：https://qyxznlkmwx.feishu.cn/wiki/BwWIwsCOuiMWGmkUzNHcKLvPnPh

点击下方名片「**关注我们**」第一时间收到推送

![](https://image.cubox.pro/cardImg/2kd0hamq06wa0f9wise0vv84nwn30e119ohhfwoiz5w5cjx42x?imageMogr2/quality/90/ignore-error/1)

**AIGitHub**

专注GitHub开源AI项目、AI前沿资讯、最新AI工具分享推荐

465篇原创内容

<br />

公众号  

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg5ODkyOTkwOQ==&mid=2247497944&idx=1)
