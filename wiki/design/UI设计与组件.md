---
title: "UI设计与组件"
summary: "Bento UI 流行、拟物化回归、AI 时代交互模式定义"
tags: [UI设计, 组件, Bento UI, 拟物化]
created: 2026-06-07
updated: 2026-06-07
---
# UI设计与组件

## Overview

UI 设计正在经历一场"风格回归"与"AI 重塑"的双重变革。一方面，Bento UI（便当盒式布局）从 2024 年开始持续流行，苹果 Widget、Windows Phone Metro 都是其灵感源头；Airbnb 的改版宣告"扁平化已死"，拟物化设计迎来第三次文艺复兴。另一方面，AI 正在改变界面设计的生产方式——Google 搜索引擎全程 AI 加持、ChatGPT 界面大更新卷入应用战场、AI 排版工具 Kami 获得 46K Star。

对设计师而言，UI 设计的核心能力正在从"画好看的界面"转向"定义 AI 时代的交互模式"。8 个 AI 时代产品设计模式被总结出来，IXDC 专访中朱宁（有赞创始人）深度讨论了"AI 取代界面设计，设计师该突围还是转型"。传统组件库（ElementUI、Ant Design）的使用率在下降，Tailwind/shadcn 等新范式在崛起。

## UI 趋势与风格

- [[2024-08-28-1分钟带你了解Bento-box设计趋势.md|1分钟带你了解Bento box设计趋势]] ([1分钟带你了解Bento box设计趋势](../../raw/design/2024-08-28-1分钟带你了解Bento-box设计趋势.md))

> Bento box设计风格或Bento UI作为一种设计趋势正在被验证，它近期频繁的出现在大众视野。本文中我们将讨论Bento box设计趋势的起源和发展，并结合设计应用案例，让大家感受它的魅力，望此后的应用中，为设计师朋友带来更多灵感和启发。
> 大家对便当盒(Bento box)应该很熟悉，印象最深的是日式便当盒，看上去既精致又有食欲，格子用来区分食物，极其讲究组合的美感。Bento UI就是用户界面如同便当盒的结构，有清晰的区块划分，整齐又整体的将内容排布。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/cibketMByvrZfIStjict8QIeJWNibHT386UxPtj8kbPGltm27iaUjZnZqQWZraMyhNqTic6TnHk13K65sfVuFsTyXBg/640?wx_fmt=png&from=appmsg)

- [[2024-09-24-Bento-UI真的是百看不厌啊除了用在产品界面里还可以怎么玩.md|Bento UI真的是百看不厌啊除了用在产品界面里还可以怎么玩]] ([Bento UI真的是百看不厌啊除了用在产品界面里还可以怎么玩](../../raw/design/2024-09-24-Bento-UI真的是百看不厌啊除了用在产品界面里还可以怎么玩.md))

> 之前提过Bento UI在很多网页和移动端上得以应用，但说起更大的获益者，应该是一些非功能性的展示类排版。设计师们常常用一些优雅的Bento box来展示一组设计方案中的细节点，达到丰富但不杂乱的效果。
> 个人认为，用于功能图或者VI设计展示，是Bento UI最好的归宿。以下是外网非常火的一种UI展现方式，用一个个小便当盒来展现一个设计系统里的不同亮点组件，是一个很不错的汇报展示形式。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/9cCKqSU1AUiaiadm40xjKhovZhPA5l1UibicIYBOt1kdy3JgC34HdhFuypTdVf56wfAMCHksXVIxP6IsyH6wSK83icA/640?wx_fmt=png&from=appmsg)

- [[2024-11-28-设计总监秘籍5步搞定弥散渐变卡片.md|设计总监秘籍5步搞定弥散渐变卡片]] ([设计总监秘籍5步搞定弥散渐变卡片](../../raw/design/2024-11-28-设计总监秘籍5步搞定弥散渐变卡片.md))

> figma也能搞定弥散渐变啦！
![](https://sns-webpic-qc.xhscdn.com/202411281109/073a151ea5855821cd0e731fee9d4146/spectrum/1040g34o31ab2ha6d6o0g5p8kbpep2mq71bfvhg0!nd_dft_wlteh_webp_3)

- [[2025-03-24-5种方法教会你如何打造高级感产品造型.md|5种方法教会你如何打造高级感产品造型]] ([5种方法教会你如何打造高级感产品造型](../../raw/design/2025-03-24-5种方法教会你如何打造高级感产品造型.md))

> Rope Trick灯罩以黑色为主，搭配白色内壁，形成鲜明对比，增添视觉层次。灯罩与灯臂通过巧妙的穿插造型连接，线条流畅，富有艺术感。整体造型既实用又具有装饰性
> SONEX Sound-X Series 1是一款设计独特的扬声器。其穿插造型设计，使两个部分相互交错，形成一种视觉上的流动感。这种设计不仅美观，还有助于声音的扩散和环绕效果。外观以橙色点缀，增添了一丝科技感和未来感。
![](https://mmbiz.qpic.cn/mmbiz_gif/hnYmdfhqDe3VX2icuCNt0bHPQ1NAo8QUkfyNEm5IJAwiajfSibVibPC7ZZ9jXPwJfdYr5meTdsJb7n2Yal4hOE3uCw/640?wx_fmt=gif)

- [[2025-03-28-白色系-UI-居然能做出如此的高级感.md|白色系 UI 居然能做出如此的高级感]] ([白色系 UI 居然能做出如此的高级感](../../raw/design/2025-03-28-白色系-UI-居然能做出如此的高级感.md))

> > 白色系UI之所以能带来如此强烈的视觉冲击力，关键在于其对色彩搭配的精妙运用。设计师Tran Mau Tri Tam ✪为UI8所作的设计案例便是一个极好的例子。他选择了浅灰色作为底色，与纯白形成对比，增加了界面的层次感。同时，通过引入少量高亮色彩作为点缀，使得整个设计看起来更加生动有趣。此外，渐变流光效果的应用更是锦上添花，赋予了作品流动的生命力。
![](https://mmbiz.qpic.cn/mmbiz_gif/lxibAV50VDZKE8QsNbncuOH69aXNoryPa17AzlcekEYTsiasUupgYjgwCP0ecMiaqsWg0Y9o0EwtaKAPHcHzKItYg/640?wx_fmt=gif)

- [[2025-04-09-优秀作品这个科技感很强的可视化界面值得一看.md|优秀作品这个科技感很强的可视化界面值得一看]] ([优秀作品这个科技感很强的可视化界面值得一看](../../raw/design/2025-04-09-优秀作品这个科技感很强的可视化界面值得一看.md))

> 分享一个视觉效果很强的作品，这是一个可视化科技产品的项目，界面设计感十足，一起来看看吧：
> 通过黑色与橙色的大胆对比，不仅突出了品牌的独特性，也让内容层次更加清晰。在配色、布局以及品牌形象塑造等各个方面都很专业，呈现出强烈的科技感与创新感。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rxq4ibnuic59dZka45JOIp31GuFKYbuXXGdIegy2F8sSmV2kMY36O6m6ZNKibciaQhPolXr9PHpxMd1ROv43JHGia6w/640?wx_fmt=jpeg&from=appmsg)

- [[2025-05-20-扁平化已死从Airbnb改版看拟物化设计的第3次文艺复兴.md|扁平化已死从Airbnb改版看拟物化设计的第3次文艺复兴]] ([扁平化已死从Airbnb改版看拟物化设计的第3次文艺复兴](../../raw/design/2025-05-20-扁平化已死从Airbnb改版看拟物化设计的第3次文艺复兴.md))

> 从2013年iOS 7推出以来，苹果引领了界面设计的巨大转变，告别了繁琐的拟物化设计，进入了扁平化设计时代。扁平化设计以其简洁、信息突出、迭代更迅速的优势深受欢迎。然而，时至今日，经过12年的发展，曾经经典的设计风格似乎已不再那么新鲜。很多人开始对扁平化设计产生审美疲劳，似乎在呼唤一种新的变化。
> 近年来确实出现了一些新的设计风格，比如微软的 Fluent Design 亚克力毛玻璃风格、Figma 采用的新粗野主义（Neo-Brutalism）、以及在 Dribbble 上流行的新拟态（New Skeuomorphism）等。不过这些风格都如昙花一现，并没有掀起什么大风浪。
![](https://mmbiz.qpic.cn/mmbiz_png/QTQ5tw73f0qy1XaqzkvV272jN92CQ0lBjfGozibT8sMITsDDFAxePZHdzV6IBJVpcRm9icoWTzoJ7G5d0epQUgew/640?wx_fmt=png&from=appmsg)

## UI 组件与工具

Siteinspire 等网站为设计师提供灵感库。值得注意的是，传统企业级组件库（ElementUI、Ant Design）的使用率正在下降，Tailwind CSS 原子化方案和 shadcn/ui 的组合成为新主流。

- [[2025-04-22-The-Best-Websites-Page-3-Siteinspire.md|The Best Websites Page 3 Siteinspire]] ([The Best Websites Page 3 Siteinspire](../../raw/design/2025-04-22-The-Best-Websites-Page-3-Siteinspire.md))

## 界面设计案例

- [[2024-09-20-不愧是做系统的vivo设计师把弹窗设计摸得很透.md|不愧是做系统的vivo设计师把弹窗设计摸得很透]] ([不愧是做系统的vivo设计师把弹窗设计摸得很透](../../raw/design/2024-09-20-不愧是做系统的vivo设计师把弹窗设计摸得很透.md))

> 中国每年有50万的设计毕业生，相比之下，能够进入大厂的寥若晨星。但所有投身于设计的设计师，都有一颗渴望成长的心。《体验设计师入门实战课程》是vivo VMIC UED 为新入职设计师量身打造的专业成长课程，是UED全体讲师的结晶。现在，我们将这套课程整理成文章发表出来，希望给选择并从事设计行业的你一点成长的力量。~
> 随着互联网应用的不断发展，弹窗组件已经成为了界面设计中不可或缺的一部分。弹窗组件可以帮助我们更好地展示信息，提供更多的交互方式，以及增强用户体验。但是，设计一个好的弹窗组件并不是一件容易的事情。需要考虑的因素很多，比如弹窗的类型、场景、功能、样式等等。同时，弹窗是一把双刃剑，用的好能使用户行为更加聚焦从而提效，如果使用的不恰当，可能会使用户产生负面情绪甚至击退潜在用户。
![](https://mmbiz.qpic.cn/mmbiz_png/cNxKibZm70g68gY5sOCjPhuiaa3kGPWKhJUpeymOcp6oWPeBYEXA5QOfavUXjm3XdRGibRPON4AAkmqotg8JTdUVA/640?wx_fmt=png&from=appmsg)

- [[2024-09-25-谷歌的一个不错的代码界面.md|谷歌的一个不错的代码界面]] ([谷歌的一个不错的代码界面](../../raw/design/2024-09-25-谷歌的一个不错的代码界面.md))
- [[2024-10-06-ChatGPT界面大更新开始卷应用了这次想灭谁.md|ChatGPT界面大更新开始卷应用了这次想灭谁]] ([ChatGPT界面大更新开始卷应用了这次想灭谁](../../raw/design/2024-10-06-ChatGPT界面大更新开始卷应用了这次想灭谁.md))

> 就在OpenAI宣布获得史上最大规模66亿美元融资的第二天，又推出了自ChatGPT问世两年来的首次重大界面更新"canvas（画布）"。
> canvas是一个全新设计的交互界面，专为写作和编程任务设计。不再局限于传统的聊天模式，而是通过在标准对话框旁开启的独立窗口，提供一个用户与ChatGPT的深度协作空间，共同创建和优化项目。
![](https://mmbiz.qpic.cn/mmbiz_png/jopKOlhibRBIT8QiaibicM2ul8xRib6SzLu58I9SpYVibz7YpsMHuWEickrMsIYuAc5l3c6npUpHkwEIZchsCGibQy7gSA/640?wx_fmt=png&from=appmsg)

- [[2024-10-12-系统弹窗UI平平无奇来看看这些有没有眼前一亮.md|系统弹窗UI平平无奇来看看这些有没有眼前一亮]] ([系统弹窗UI平平无奇来看看这些有没有眼前一亮](../../raw/design/2024-10-12-系统弹窗UI平平无奇来看看这些有没有眼前一亮.md))

> 系统弹窗要好看，首先需要简洁明了。弹窗中只呈现关键信息，避免过多繁杂内容干扰用户。
> 其次，具有视觉吸引力。在色彩和图形设计上用心，与整体界面风格协调又突出。可能用明亮但不刺眼的颜色吸引注意，或搭配简洁的图标辅助说明。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/9cCKqSU1AUia6PEyMYgQ9cb6g1zWoldUFibA0QJjNN6lUjbQR3Foe0870yFSgSicIicwKI1ibkFrZPqogrUMgF7T5lg/640?wx_fmt=png&from=appmsg)

- [[2024-12-05-淘宝运营设计能整这么多交互思路真会啊.md|淘宝运营设计能整这么多交互思路真会啊]] ([淘宝运营设计能整这么多交互思路真会啊](../../raw/design/2024-12-05-淘宝运营设计能整这么多交互思路真会啊.md))

> 「淘宝秒杀」致力于为用户打造高性价比的购物体验阵地，伴随发展过程，我们需要解决逐渐多样的运营内容手段，让用户选购体验简单明了，所以围绕以"品"为核心+价差直给的设计思考，对秒杀频道持续进行体验优化，形成"快看、速买"的购物体验。
> 淘宝秒杀价格直降，不需凑单领券。前台导购通过直降箭头表达价差语义，同时优化商品决策因子强弱。经过元素级的定量对比测试，沉淀出导购效率最优解，定义秒杀价格力的高效率体验标准。
![](https://mmbiz.qpic.cn/mmbiz_png/wmHsWeibDlwO41vMw32VbRibxp1JaP1K3q0vfTKiceGQvRH9a3Gls7lFRpUjBVcvlDDQsa1soSqPMeNYjJBLFNHSg/640?wx_fmt=png&from=appmsg)

- [[2024-12-09-这种设计多来些吧盒马用一个小卡片颠覆了传统零售行业.md|这种设计多来些吧盒马用一个小卡片颠覆了传统零售行业]] ([这种设计多来些吧盒马用一个小卡片颠覆了传统零售行业](../../raw/design/2024-12-09-这种设计多来些吧盒马用一个小卡片颠覆了传统零售行业.md))

> 你知道吗，盒马ReX AIoT团队自研的 全彩营销价签 荣获了美国IDEA 2024 FEATURED FINALIST大奖 。今天我们来讲讲这个可能是世界上最先进的电子价签背后的故事，看我们如何让货架上的商品重获关注。
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Nk2qAQpCJzicicZIR4x88Qkk3vd0ECIlHDqvZsTeh5gzx0ulJksChCB6eefFgPAOFtffmyzMWrcrMnibN4iaRQAhsw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- [[2025-08-10-IXDC专访-有赞科技创始人兼CEO朱宁深度谈AI取代界面设计设计师该突围还是转型.md|IXDC专访 有赞科技创始人兼CEO朱宁深度谈AI取代界面设计设计师该突围还是转型]] ([IXDC专访 有赞科技创始人兼CEO朱宁深度谈AI取代界面设计设计师该突围还是转型](../../raw/design/2025-08-10-IXDC专访-有赞科技创始人兼CEO朱宁深度谈AI取代界面设计设计师该突围还是转型.md))

> 随着AI技术的快速发展，许多重复性的设计工作，如图形用户界面设计和用户交互设计，正逐渐被自动化工具所取代。这一变革对于设计师而言，既是机遇也是挑战。
> IXDC有幸采访到有赞科技创始人兼CEO朱宁（白鸦）先生，他就如何在没有GUI界面的情况下提供易于理解的用户体验，以及如何在AI主导的设计流程中保持界面的独特性和创新性等话题，进行深入的探讨和分享。
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/G9CRsoNKowiam8TWe3aSzicTDmQ8ouToqc73GKEOhkqmeVpaeOwKVuSVsLvRicNh00epQ8numudzkYOWUwHWaOCHw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

## 其他

AI 正在重新定义"界面"本身。Google 搜索引擎的 AI 重新设计展示了搜索界面的未来形态；文心一言改名"文小言"后 app 变化很大，反映了国内 AI 产品的界面迭代速度；AI 排版工具 Kami（46K Star）让 AI 生成的文档也能精致好看；"8 个 AI 时代产品设计模式"则试图总结 AI 产品的界面设计规律。

- [[2024-08-27-谷歌重新设计搜索引擎全程AI加持从AI概览到自动分类.md|谷歌重新设计搜索引擎全程AI加持从AI概览到自动分类]] ([谷歌重新设计搜索引擎全程AI加持从AI概览到自动分类](../../raw/design/2024-08-27-谷歌重新设计搜索引擎全程AI加持从AI概览到自动分类.md))

> 提出多部分问题并得到单一答案------这就是 AI 搜索的工作原理。图片：谷歌
> 一年前，谷歌表示相信人工智能是搜索的未来。这个未来显然已经到来：谷歌开始向美国用户推出"人工智能概览"，以前称为搜索生成体验（SGE），很快将在全球推出。很快，数十亿谷歌用户将在许多搜索结果的顶部看到人工智能生成的摘要。而这只是人工智能改变搜索的开始。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a8VwFo6liafUl7uicDTplP5tDLFpGiceFXqibckFpnCiaicMlMu4qicXXAP5OUpHnUlepPNpn1XDKL6lkpWVRdGjyicUibg/640?wx_fmt=jpeg&from=appmsg)

- [[2024-09-10-设计很有特色的AI语音笔记工具.md|设计很有特色的AI语音笔记工具]] ([设计很有特色的AI语音笔记工具](../../raw/design/2024-09-10-设计很有特色的AI语音笔记工具.md))

> "Magical Dream Journal"旨在帮助用户记录和回顾他们的梦境。应用程序具有语音记录、日历回顾、个性化定制、简约设计和隐私保护等特点，由两位热爱设计和自然的用户Dennis和Lorant开发。
> 产品特点: 应用具有语音记录功能，允许用户快速记录梦境；日历功能让用户可以回顾旧梦；黑白设计保护视力；个性化设置满足用户偏好。 隐私保护: 用户的梦境记录是安全且私密的，只有用户自己可以查看。 使用便捷: 应用设计简洁直观，用户可以通过语音或打字轻松添加梦境记录。 开发团队: 由Dennis和Lorant两位开发者组成，他们热爱设计、创造和户外活动，对花生酱和辣椒有特别的喜爱。
![](https://sns-webpic-qc.xhscdn.com/202409100017/eec2a663646ef053306157a799661358/1040g2sg31704upiak6705p9h7vgamtrjfmuilcg!nd_prv_wlteh_webp_3)

- [[2024-09-11-UI丨UNICARE-健康管理.md|UI丨UNICARE 健康管理]] ([UI丨UNICARE 健康管理](../../raw/design/2024-09-11-UI丨UNICARE-健康管理.md))

> 标签：健康管理、医疗保健服务平台提
![](https://mmbiz.qpic.cn/mmbiz_gif/iaPZmgH52FZkVyrj1uc87TDbm0SnUAgoqAUCrTtYyoRjHg1xA1Bd9mbQB9Bl04wJE6yib8iabDfVyibDrHsFoN5kGw/640?wx_fmt=gif&from=appmsg)

- [[2024-09-20-文心一言改名文小言后app变化很大.md|文心一言改名文小言后app变化很大]] ([文心一言改名文小言后app变化很大](../../raw/design/2024-09-20-文心一言改名文小言后app变化很大.md))

> 之前写AI相关的文章，总结觉得文心一言这名字又长又拗口，又不知道怎么缩写。直到9月4日百度宣布将其改名为文小言，一下子接地气多了。
> 这波不只是改个名字，app也做了大改版。现在跟国内其它同类app相比，更有"大厂的专业感"了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/UzDNI6O6hCHcqRLxKh2mFO6lQib8sibBSGAJsg5MGVnvRPS60MAm47ap8QKeUvFfyKKIGaNJticTGqmn9rhkd2nIw/640?wx_fmt=png&from=appmsg)

- [[2024-10-09-人工智能编辑器官网太绝了.md|人工智能编辑器官网太绝了]] ([人工智能编辑器官网太绝了](../../raw/design/2024-10-09-人工智能编辑器官网太绝了.md))

![](https://sns-webpic-qc.xhscdn.com/202410091323/9d68cc2f4bb45c695c639f3cd73f1ee5/1040g008318miukkqkc005oicvd741r3r4idf7ho!nd_dft_wlteh_webp_3)

- [[2025-05-11-设计分享-Ai-chat-做不出差异看这里---小红书.md|设计分享 Ai chat 做不出差异看这里   小红书]] ([设计分享 Ai chat 做不出差异看这里   小红书](../../raw/design/2025-05-11-设计分享-Ai-chat-做不出差异看这里---小红书.md))

> 同质化严重的 chat ui 如何在不影响已养成的习惯性下，拉开差异，从每一处细节出发！来自 dribbble Mohamad Shahrestani

- [[2026-05-01-给AI装个排版系统文档好看了.md|给AI装个排版系统文档好看了]] ([给AI装个排版系统文档好看了](../../raw/design/2026-05-01-给AI装个排版系统文档好看了.md))
- [[2026-05-07-斩获46Kstar的开源AI排版项目Kami让AI生成的文档也能精致又好看.md|斩获46Kstar的开源AI排版项目Kami让AI生成的文档也能精致又好看]] ([斩获46Kstar的开源AI排版项目Kami让AI生成的文档也能精致又好看](../../raw/design/2026-05-07-斩获46Kstar的开源AI排版项目Kami让AI生成的文档也能精致又好看.md))

> 很多人用 Claude 等 AI 写研究报告或文档，但默认输出往往是纯白背景、默认黑字、排版随意且每次风格都不一致，内容再好也让人不想读。
> 于是开源作者 tw93就开源了Kami，这是一套专为 AI Agent 设计的文档设计系统与排版约束语言，在GitHub上已经斩获了4.6Kstar！
![](https://mmbiz.qpic.cn/mmbiz_png/ZdrSHaq5Gr1uXuaAG1Jgibd5DC6ibtVhrX4ff5eQib3ZApns6BEqpPxkBUXQ2PHQMsO6E9djzk54CbcU4MPx8Zibicg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&randomid=u1uwjimf#imgIndex=0)

- [[2026-05-22-值得收藏关注的8个AI时代产品设计模式.md|值得收藏关注的8个AI时代产品设计模式]] ([值得收藏关注的8个AI时代产品设计模式](../../raw/design/2026-05-22-值得收藏关注的8个AI时代产品设计模式.md))

> 这篇分享在国外网站收集到的AI时代的产品设计模式。> 由于AI可以在明确的需求下，独立完成端到端的多步骤的工作流程。所以这种需要一步步操作的表单设计需要简化，像下图这种中间需要填用户信息，公司信息等任务很多都来自CRM，而AI可以直接通过MCP, API等方式获取到这些。在AI能了解到上下文的情况下，可以考虑简化设计。
![](https://mmbiz.qpic.cn/mmbiz_png/3JU60Y16iaoZRsetkPOoXtENKJVvicGE2LHpYc5CyZrXachKurswpMVNrYMXVOKZdicV3vodJz9WAr31m45ZxbicpeB8eMbwm5icEJicjvuPB0sZk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

- [[2024-08-28-lattics-让人爱上写作的可视化笔记软件.md|lattics-让人爱上写作的可视化笔记软件]] ([lattics-让人爱上写作的可视化笔记软件](../../raw/有趣的产品/2024-08-28-lattics-让人爱上写作的可视化笔记软件.md))

> 说到笔记写作工具的时候，你会想到什么？是笔记工具还是写作工具？
> 在市场高度成熟的今天，笔记和写作软件都已经进化出相对完整的两种形态：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hhcZYRw6oyfVQ3micXR0j2sURweMjQOYFpaOlmIYFrtjAjbBygaqb4UlHd6Yibycyya4sN6BglRAWEDl2e6Eia2A/640)

- [[2024-10-29-DOCUMENTS-让气味可视化.md|DOCUMENTS-让气味可视化]] ([DOCUMENTS-让气味可视化](../../raw/有趣的产品/2024-10-29-DOCUMENTS-让气味可视化.md))

> DOCUMENTS意为「记录与文献」，取其谐音，寓意「值得被记住的气味与馈赠」，「闻献DOCUMENTS」由此而生。
> 品牌有意择取与记录、文献相关的文化元素，在深挖其历史后，将它们在视觉、设计、概念等方向进行运用，从而形成与「闻献DOCUMENTS」强关联的品牌基因。
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/oSxy99diagQiaz3zkAicRGrW12wibyicw3LrOVH1LFYkgKNXHHlKdRzLpNu7EqUpmfKr2r23x6xvf0eZmSYldnP7VbQ/640?wx_fmt=gif&from=appmsg)

- [[2024-09-04-从零开始我用-AI-做了一个图文卡片小工具.md|从零开始我用-AI-做了一个图文卡片小工具]] ([从零开始我用-AI-做了一个图文卡片小工具](../../raw/AI实操/2024-09-04-从零开始我用-AI-做了一个图文卡片小工具.md))

> 编注 ：我们会不定期挑选 Matrix 的优质文章，展示来自用户的最真实的体验和观点。文章代表作者个人观点，少数派仅对标题和排版略作修改。
> AI 的热潮正逐渐渗透到各行各业，那么普通人能够借助AI做些什么呢？作为设计师的我，在 AI 的助力之下，成功地把自己的想法开发落地，并且完成了产品上线。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oylw20gGnRhswnRv0tJeklfoMbU4MPYibHibkwyEfFMkicLlbF5ECDlFDF2jlNp5ORtcvic5zGuv6iaEARIsibaeeLZA/640?wx_fmt=png)

- [[2025-03-10-低饱和配色肉感机械娘简直是柔与钢的完美碰撞-DROCK.md|低饱和配色肉感机械娘简直是柔与钢的完美碰撞-DROCK]] ([低饱和配色肉感机械娘简直是柔与钢的完美碰撞-DROCK](../../raw/Uncategorized/2025-03-10-低饱和配色肉感机械娘简直是柔与钢的完美碰撞-DROCK.md))

> 来自南韩的艺术家Henu Caulfield Joo，目前是一位自由职业者。他的作品风格和运用到的元素都让人眼前一亮，特别擅长角色与人物设计。
> 笔下的女性角色娇憨可爱，因为擅长运用体块感的组合，所以人物也不失力量感。
![](https://mmbiz.qpic.cn/mmbiz_jpg/R0WXlemZXicTWImpbgY9mPT8eEFFDxWDQpicg2ChRMW7EDvgyg5ZBQSiaicTkkIqibNKMbuAIfgZl0gF4SqNmtlAdLA/640?wx_fmt=jpeg)

- [[2025-08-28-一款高颜值现代化的-Git-可视化管理神器.md|一款高颜值现代化的-Git-可视化管理神器]] ([一款高颜值现代化的-Git-可视化管理神器](../../raw/Uncategorized/2025-08-28-一款高颜值现代化的-Git-可视化管理神器.md))

> 想象一下：你正在紧急修复线上 bug，突然产品经理要求你立即审查另一个功能的代码，接着又有同事紧急请求你帮忙调试一段脚本。在传统的 Git 工作流中，这意味着反复的 git stash、git checkout 和分支切换，上下文切换成本高昂。
> GitButler 是一款开源的 Git 客户端，它引入了 虚拟分支（Virtual Branches） 的概念，允许开发者同时工作在多个功能分支上而无需物理切换分支。它像是一个智能的版本控制协调员，底层基于标准 Git，但通过抽象层提供了突破性的工作流体验。
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aEPult10iakLziaibxXyFgUVRQGju2ymUaQtvVafOt6kJ0eDZNrEwY73cd4rfE5ndBpuJsfhoMcvoYP3Q3xBRibluQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=qjrbcg1c&tp=webp)

- [[2025-11-12-Z-ProductProduct-Hunt最佳产品915-21一站式数据爬虫和可视化AI工具登顶.md|Z-ProductProduct-Hunt最佳产品915-21一站式数据爬虫和可视化AI工具登顶]] ([Z-ProductProduct-Hunt最佳产品915-21一站式数据爬虫和可视化AI工具登顶](../../raw/Uncategorized/2025-11-12-Z-ProductProduct-Hunt最佳产品915-21一站式数据爬虫和可视化AI工具登顶.md))

> 一句话描述： Capalyze是一款结合网页实时抓取与AI辅助分析，支持交互数据可视化和导出的无代码智能数据平台。
![](https://image.cubox.pro/cardImg/27zbwi1d1jlsvwa2t0p5loxkjoy5hpdzd3ovvbzx1zcpkcxcm4?imageMogr2/quality/90/ignore-error/1)

- [[2026-01-09-Z-ProductSuno在用的客户调研AgentDialogue-AI重构千亿美元的市场研究产业VC正在押注理解的速度.md|Z-ProductSuno在用的客户调研AgentDialogue-AI重构千亿美元的市场研究产业VC正在押注理解的速度]] ([Z-ProductSuno在用的客户调研AgentDialogue-AI重构千亿美元的市场研究产业VC正在押注理解的速度](../../raw/Uncategorized/2026-01-09-Z-ProductSuno在用的客户调研AgentDialogue-AI重构千亿美元的市场研究产业VC正在押注理解的速度.md))

> * 在传统企业中，市场调研往往是决策最慢的一环，从问卷设计到洞察输出要花上数周。Dialogue AI试图用AI自动化整个研究流程，让洞察生成的速度与产品迭代保持同步。它的出现不仅是效率的革新，更是企业理解用户方式的范式转变------让研究从被动响应变为实时驱动。
> * Dialogue AI打造了一个端到端平台，从研究设计、参与者招募、AI主持访谈到即时洞察，几乎全由AI驱动。它的目标是让研究人员与非研究人员都能轻松、快速地获得可执行的市场反馈。通过将"定性深度"与"自动化规模"结合，Dialogue AI正在为传统市场研究行业注入新的技术灵魂。
![](https://image.cubox.pro/cardImg/27zbwi1d1jlsvwa2t0p5loxkjoy5hpdzd3ovvbzx1zcpkcxcm4?imageMogr2/quality/90/ignore-error/1)

## 月维周刊资源合集（#7–#23）

> 整合自 [Moonvy 月维](https://moonvy.com)「设计素材周刊」共 8 个条目分发到本分类，覆盖 2 个原版块。
> 排序按周报期数倒序（最新在前），同一版块内按原文顺序。
> 原始描述文本与图片链接保留；图片采用外部 URL（`moonvy.com/blog/_assets/...`）。
### Figma 技巧

### 01. 快捷创建样式文件夹

> 来源：周刊 #007 · 2022/04/05 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/007/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/007/)
之前只知道用 / 创建文件夹层级，但是这样的操作重复度高也不够直观。现在我发现可以在「属性面板」中对它们进行分组，这样创建就简单多了。

选中要分组的样式，并按`cmd`+`G`进行分组，或者在选中的样式上右键菜单「添加新文件夹」，然后命名。还可以在文件夹内和文件夹之间对样式进行排序和拖动，空的样式文件夹会自动删除。

![在属性面板中排序和移动样式](https://moonvy.com/blog/_assets/14594644af263e03.gif)在属性面板中排序和移动样式
### 02.快速自动宽度文本

> 来源：周刊 #007 · 2022/04/05 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/007/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/007/)
想要将文本设置为自动宽度？简单！只需**双击文本框**。完毕（太开心了，这样好方便）

![双击文本框可快速更改为自动宽度](https://moonvy.com/blog/_assets/1624148bb64f6ed3.gif)双击文本框可快速更改为自动宽度
### 03. 将图像填充设为样式

> 来源：周刊 #007 · 2022/04/05 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/007/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/007/)
可以像保存颜色样式一样保存图像。可以将图像填充任何形状，包括有填充的文本。

![图像可以像任何其他样式一样保存和使用](https://moonvy.com/blog/_assets/78be1a9b1cecade.png)图像可以像任何其他样式一样保存和使用
---

### Figma 插件

### Find Page，在 Figma 里搜索查找设计图

> 来源：周刊 #023 · 2022/07/23 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/)
支持跨 Page 搜索 Frame 和 原始组件名称，搜索结果可以定位，推荐 👍

[https://www.figma.com/community/plugin/1110553741323547165](https://www.figma.com/community/plugin/1110553741323547165)

![](https://moonvy.com/blog/_assets/a80aa86e7ad673b4.png)
### 导出应用程序需要的图标格式 icns、ico

> 来源：周刊 #023 · 2022/07/23 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/)
Figma 插件，将图标导出为适合应用程序使用的图标格式， `.ico (Windows)` 和或 `.icns (Mac)`文件。

[https://www.figma.com/community/plugin/742318143106037364](https://www.figma.com/community/plugin/742318143106037364)

![](https://moonvy.com/blog/_assets/c2c465bc71b9eb28.png)
另外还有个在线工具可以将 PNG 转为 icns 格式 [https://cloudconvert.com/png-to-icns](https://cloudconvert.com/png-to-icns)

### Figma 插件，Ruri，几何渐变生成工具

> 来源：周刊 #023 · 2022/07/23 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/)
上周推荐的在线几何背景工具上线了 Figma 插件社区，在 Figma 里使用效率就更高了

[https://www.figma.com/community/plugin/1130394960851487602](https://www.figma.com/community/plugin/1130394960851487602)

![](https://moonvy.com/blog/_assets/89ae0944ff861cc6.png)
### Figma 插件，Splines 生成渐变曲线路径

> 来源：周刊 #023 · 2022/07/23 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/)
在插件里绘制路径，模拟 Illustrator 里的混合工具生成有立体感的渐变线条

[https://www.figma.com/community/plugin/1094343067414782306](https://www.figma.com/community/plugin/1094343067414782306)

![](https://moonvy.com/blog/_assets/7c0a289e4edf45d0.png)
### ClipDrop，Figma 自动抠图插件

> 来源：周刊 #023 · 2022/07/23 · [https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/](https://moonvy.com/blog/post/%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90%E5%91%A8%E5%88%8A/023/)
智能抠图的同时将内容分图层保留，并且将背景也自动去掉元素修补好

[https://www.figma.com/community/plugin/1123355421740529204](https://www.figma.com/community/plugin/1123355421740529204)

![](https://moonvy.com/blog/_assets/497c58c46d7ad3a5.png)

![](https://moonvy.com/blog/_assets/249405fcd33b4ebd.gif)
## B端 UI 设计规范（来自抖音系列）

> 以下内容综合自梁17、xg、曲sir 等 B 端设计系列视频，覆盖表格、表单、弹窗、导航、图标等核心组件的设计方法论。

### B端产品拆解心法

所有 B 端产品都可以用"**管人、管事、管资源**"三条线拆解核心功能。以智慧工厂系统为例：管资源 = 物料管理、设备管理；管事 = 生产管理、质量管理；管人 = 员工管理。设计师在接到需求时，先用这三条线梳理业务，再进入具体组件设计。

- ![[一条心法拆解所有的B端产品 学浪计划  B端设计  UI设计  产业互联网_7031847407046511886.gif]]
[[一条心法拆解所有的B端产品 学浪计划  B端设计  UI设计  产业互联网_7031847407046511886.md|一条心法拆解B端产品]]

### 表格设计要点

**高度公式**：表格文字字号 14px，行高 = 字号 x 1.5，上下间距 = 字号 x 1.2。**表格高度 = 文字行高 + 上下间距**。

**三个优化要点**：
1. **冻结阴影**：当表格数据项过多需要冻结首行首列时，给被冻结的列加阴影效果，让用户快速感知内容区可滑动
2. **无衬线字体**：表格中不使用衬线字体，避免视觉干扰，易读性才是关键
3. **悬停操作**：默认隐藏操作按钮，鼠标悬停时才显示，保持表格整洁

**数字对比**：B 端表格中数字列应使用**等宽字体**（Monospace），而非比例字体。比例字体的字符宽度随字形变化，会导致小数点与千分位错位，不利于数据直观对比。

**超长数据处理**：设计前一定要问清数据最大值以确定列宽。超出列宽时：不重要信息用省略号；重要信息换行完整展示；公告信息用轮播循环展示；大数值用"万""亿"作计量单位。

**操作按钮过多**（20+按钮场景）：
1. 全局操作**置顶**（新增、上传等） -- 置于页面顶部
2. 批量操作**紧贴**（导出、复制等） -- 置于表格上方或选择数据后覆盖表头
3. 单行操作**断后**（详情、编辑、删除） -- 置于行尾
4. 深度操作**内收**（通过、驳回等需谨慎处理的操作） -- 内置于详情页/编辑页
5. 高频核心操作前置，支持**原位编辑**

### 表单设计规则

**间距美学**：强相关元素亲密、弱相关元素靠近、不相关元素远离 -- 保持秩序感；同时给彼此呼吸空间，避免过于拥挤。

**标签对齐五种方式**：
1. **顶对齐**：标签在输入区上方左对齐，亲密性强，横向空间充裕，标签长时友好
2. **左对齐**：字段左对齐，易于浏览，垂直空间占用少，但标签与输入框距离不固定会打断视觉动线
3. **右对齐（冒号对齐）**：字段右对齐，标签与输入区距离固定，亲密度高，阅读效率高
4. **内联式**：标签在输入区内（类似 placeholder），填写时消失，适合单行场景如搜索
5. **浮动标签**：输入前类似 placeholder，点击后标签上移并缩小，节约空间但增加开发难度

**主按钮位置**：
- 放**左侧**：提升操作效率 -- 适用于跟随按钮、表底按钮（顺延用户操作路径）
- 放**右侧**：提升操作准确率 -- 适用于顶部与底部按钮（让用户先了解所有操作项再行动）

**必填项符号**：标记必填项让用户快速预估工作量，避免不知情提交带来的挫败感。登录注册等低错误率表单可舍弃。标签右对齐时符号放左侧，标签左对齐或顶对齐时放右侧。

**步骤条使用**：步骤 < 3 时无需展示步骤条。横向步骤条适合步骤少的场景；纵向适合步骤多或动态变化的场景；迷你步骤条适合移动端或模块内使用；指向步骤条适合严格线性操作。

### 弹窗尺寸规范

宽度采用系统最小间距的倍数（最小间距为 4 时）：320 / 560 / 720 / 960。
高度范围 200-560px（基于 1024x768 最小可视面，减去顶部菜单栏和底部工具栏，留安全距离）。在区间内根据内容量定义。

- ![[B端设计之弹窗尺寸规范学浪计划 B端设计 UI设计 产业互联网_6995117610819915045.gif]]
[[B端设计之弹窗尺寸规范学浪计划 B端设计 UI设计 产业互联网_6995117610819915045.md|弹窗尺寸规范]]

### 面包屑导航

用于页面层级过多时显示当前层级位置。1 级子站点直接用"返回"；超过 5 级时只保留第一级和最后两级，中间用省略号代替，悬停或点击可展开全部。返回键需区分：**层级返回**（从当前层级返回上一层级）和**任务流返回**（从当前任务返回同层级上一个任务），根据场景决定是否保留。

- ![[最容易被忽略的面包屑导航细节学浪计划 B端设计 UI设计 产业互联网_7013286672464923911.gif]]
[[最容易被忽略的面包屑导航细节学浪计划 B端设计 UI设计 产业互联网_7013286672464923911.md|面包屑导航细节]]

### B端设计稿尺寸

- 用户在公司办公、配 1920 显示器 -> 以 **1920x1080** 为设计尺寸
- 用户经常外勤、用小尺寸笔记本 -> 以 **375x812**（移动端）和 **1280x720** 为设计尺寸
- SaaS 产品、显示器多样 -> 以 **1440x900** 为设计尺寸，方便向上下适配

- ![[B端设计稿到底应该定多大才合适来看看主流的PC端思路  学浪计划  B端设计  UI设计_6982458602069970190.gif]]
[[B端设计稿到底应该定多大才合适来看看主流的PC端思路  学浪计划  B端设计  UI设计_6982458602069970190.md|B端设计稿尺寸选择]]

### 盒子模型与设计师

前端将每个元素装进"盒子"（content + padding + border + margin）再定位。设计师只需记住：**padding 为点击区域，margin 为元素之间的距离**。理解盒子模型能帮助设计师从落地角度思考布局，降低与开发的沟通成本。

- ![[学浪计划 ui设计 b端设计 为什么设计要了解盒子模型如何降低和开发沟通成本_6988423308177853733.gif]]
[[学浪计划 ui设计 b端设计 为什么设计要了解盒子模型如何降低和开发沟通成本_6988423308177853733.md|盒子模型与设计师]]

### 图标规范

B 端图标注重简洁易懂、分类标识。采用面性图标或 2px 线条图标增加识别度，默认大小 **16x16px**，以 **SVG** 格式为主。制作交付：用矢量软件制作后保存 SVG，批量上传到 iconfont。

- ![[如何制作B端中的图标图标规范学浪计划 ui设计 b端设计_6999936752907570463.gif]]
[[如何制作B端中的图标图标规范学浪计划 ui设计 b端设计_6999936752907570463.md|B端图标规范]]

### B端设计参考关键词

搜索优秀 B 端设计参考的关键词：**Dashboard**（仪表盘/数据可视化面板）、**HMI**（人机界面，常指车载界面）、**Forms UI**（表单设计库）、业务垂类 + UI（如 ERP UI、CRM UI）。

- ![[B端设计参考难找不如先来收藏这几个关键词学浪计划 B端设计 UI设计 产业互联网_7000726309135502624.gif]]
[[B端设计参考难找不如先来收藏这几个关键词学浪计划 B端设计 UI设计 产业互联网_7000726309135502624.md|B端设计参考关键词]]

## 大屏可视化设计（来自抖音系列）

> 综合自大屏可视化系列视频，覆盖格式塔原理、主视觉类型、动效选择。

### 格式塔原理在大屏设计中的应用

- **接近性**：元素距离影响感知，靠近的元素被看作一组，距离远的自动划分 -- 因此数据项的分组靠间距控制
- **相似性**：设计风格相似的元素被自动归为一类 -- 大屏面板需统一字号、色彩规范
- **连续性**：视觉倾向于感知连续而非离散 -- 有规律排列后大脑自动联想，快速解读信息

### 大屏主视觉五类

1. **JS 地图**：二维地图和三维城市模型，通常有数据交互
2. **信息结构图**：展示数据构成或流动交换过程，通常添加动态效果
3. **地理空间**：地球和区域地图，侧重视觉效果展示
4. **建筑机械类**：单体建筑、机械体、人体等模型展示
5. **其他主体**：数据指标、视频入口、按钮等

### 大屏动效选择

缺少动效的大屏容易被看作图片。动效可添加在：主视觉、辅助元素、图表和数据上。
- **图表**：轮播数据切换（环形图/柱形图）、数据翻牌效果、重复载入动画（控制循环时间）
- **主视觉**：地图数据流动、信息结构图动态展示

- ![[大屏设计的动效该如何选择13大屏可视化 可视化 ui设计_6988435663435631903.gif]]
[[大屏设计的动效该如何选择13大屏可视化 可视化 ui设计_6988435663435631903.md|大屏动效选择]]

### 侧边导航设计

侧边导航栏通常在屏幕左侧（符合阅读习惯），高度随屏幕变化，宽度根据屏幕宽度变化。以 1440px 画布为基准出尺寸模板，右侧多留白以保持视觉平衡和空间感。

- ![[网页UI设计中的侧边导航 创作灵感 设计灵感 设计教程 知识分享 ui设计 抖音小助手_7036330503317785869.gif]]
[[网页UI设计中的侧边导航 创作灵感 设计灵感 设计教程 知识分享 ui设计 抖音小助手_7036330503317785869.md|侧边导航设计]]

## 抖音短视频补充：UI 与交互趋势

> 综合 [抖音设计短视频 — UI与交互](抖音设计短视频.md) 108 条，与上文 B 端规范互补；不重复已收录的表格/表单/大屏条目。

1. **品牌色与轻量渐变**：2021 趋势报告指出，竞品压力下品牌色普遍「轻微提饱和、提明度」；页面背景与卡片越来越多采用**理性克制的轻量渐变** + **磨砂玻璃**（比传统毛玻璃更通透、有层次），用于氛围烘托而非抢内容。
2. **AI 辅助 B 端图标**：Illustrator 路径 +「3D → 突出与斜角（等角左方）」四步流程，可快速产出科技感面性图标（云朵等），适合不会 C4D 的设计师应急出稿。
3. **设计稿基准尺寸再确认**：PC 办公场景 **1920×1080**、外勤小屏 **1280×720**、SaaS 多屏 **1440×900** 仍是短视频教程中的主流三套基准（与上文 B 端尺寸一致，可作为团队默认值）。
4. **流行色是精英导向**：潘通等机构的年度色往往**先于**大众审美被定义，设计师应区分「趋势参考」与「品牌自有色」，避免盲目追色。
5. **侧边/步骤条/面包屑**：抖音系列强调「返回键可与面包屑共存」「步骤条类型选型」等**导航细节**，与 B 端信息架构直接相关 — 详见本页「B端设计规范」各小节。

### X (Twitter) 书签

> 从 X 书签导入，共 5 条相关条目

- **Base UI 35 组件** — Colm Tuite 发布基于 Base UI 的 35 个组件，含样式和额外 API ([原文](https://x.com/colmtuite/status/1970473706355892583))
- **ReUI 30+ Base UI 组件** — 最大更新，30+ Base UI 组件 + 200+ 高级示例，Free 和 shadcn 默认主题就绪 ([原文](https://x.com/reui_io/status/1970473706355892583))
- **Shaders 组件库** — 首个专注于前端特效的组件库，即将支持 Vue、React、Svelte ([原文](https://x.com/npm_i_shaders/status/1970526500811350397))
- **Nucleo 图标深度效果** — Sebastiano Guerriero 用 Nucleo 图标添加层次感 ([原文](https://x.com/guerriero_se/status/1963245117990412724))
- **Marko Ilic SaaS UI 卡片** — 为 SaaS 客户项目设计的干净 UI 卡片 ([原文](https://x.com/markoilico/status/1994877915201405258))

## See Also

- [[设计系统.md|设计系统]] — 设计系统是 UI 组件的管理体系
- [[UX与交互研究.md|UX与交互研究]] — UX 研究指导 UI 设计决策
- [[材质与拟物.md|材质与拟物]] — 拟物化设计风格的回归
- [[背景与渐变.md|背景与渐变]] — UI 背景和渐变配色
- [[动效与动画.md|动效与动画]] — UI 交互动效设计
- [[前端实现.md|前端实现]] — UI 设计落地到前端代码
- [[Figma技巧与插件.md|Figma技巧与插件]] — Figma 是 UI 设计的主流工具
- [[设计师成长.md|设计师成长]] — UI 设计能力是设计师的基础
- [[行业案例与趋势.md|行业案例与趋势]] — UI 设计趋势和行业案例