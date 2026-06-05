---
id: "7366059169826210461"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247509634&idx=1&sn=577c5524c09ec0aa19f89af1f466ba5f&chksm=ead1949e9cedada5173390442be257764cf3b2d8c36d686bf0ae7ff3cf5a43a5bf459587fd2e&mpshare=1&scene=1&srcid=0912x20lKY3WQOcjT9ohVTj6&sharer_shareinfo=18981f8caca2b70b909496ef5fa10027&sharer_shareinfo_first=18981f8caca2b70b909496ef5fa10027
author: "Y Combinator Z Potentials"
collected: 2025-09-12
tags: []
---

# 喝点VC｜YC对谈Anthropic联创：MCP和Claude Code的成功有相似之处，都在于以模型为核心的研发思路

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247509634&idx=1) · Y Combinator Z Potentials


![](https://image.cubox.pro/cardImg/27zbwi1d1jlsvwa2t0p5loxkjoy5hpdzd3ovvbzx1zcpkcxcm4?imageMogr2/quality/90/ignore-error/1)

**Z Potentials**

我们与Z Potentials同频共振

481篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fib38wYqSEotCdIhnkZ0ubZTmIsTI5vVnChyIXouTqxwjqhw8wZEibPLK7rRdLCcaXfp5TPAwptAwVCJWYZJmmpAg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

图片来源：Y Combinator

**Z Highlights**

- 尤其是"Scaling Laws"的曲线------跨越12个数量级，还能保持几乎直线的增长。我不是物理学家，但看到这个结果，我完全被说服了，**决定把所有工作重心转向规模化训练。** 很多研究人员也觉得这不够优雅，就是"堆层数"。不过我们后来也形成了一种心态------**"用最笨的方法做成事"。** Scaling Laws就是最典型的例子：看似简单粗暴，但它真的有效。

<!-- -->

- 我们都觉得这项技术会是颠覆性的：**未来某个时刻，人类会把控制权交到更强大的AI手中** ，我们希望它们能与人类目标一致，顺利完成这个过渡。**但这是高风险的，因此必须有一个机构能承担起这样的使命。** 这也是为什么我们后来选择离开，创立Anthropic。

<!-- -->

- **一个强大且稳定的软件栈意味着能快速迭代，这对突破很关键。** Anthropic现在面对更多平台，挑战更大，所以核心是**能写出优秀的软件，让所有研发人员在低层算力上都有好体验** 。

<!-- -->

- 我们想让平台成为大家构建产品的最好基础，因为AI增长实在太快了。**世界是为人类设计的，但现在要想办法让模型成为经济活动中的"生产力成员"。**

*Tom Brown在OpenAI帮助打造GPT-3后，联合创办了Anthropic。作为一个自学成才的工程师，他从线性代数只拿到B-的学生，成长为推动AI规模化突破的关键人物。现在，Anthropic的Claude已成为开发者首选，他的团队正主导着"人类史上最大规模的基础设施建设"。在本期The Lightcone节目中，他聊到自己从YC创业者到AI研究员的非典型之路、颠覆行业的规模化定律发现，以及他给想进入AI领域的年轻工程师们的建议。*

**从加入初创到自己创业，像狼一样狩猎**

Garry Tan：欢迎来到新一期的《The Lightcone》。今天我们请到了一位重量级嘉宾------Anthropic联合创始人Tom Brown。Tom，很多人想知道，你21岁从MIT毕业进入科技行业，从2009年一路走来，怎么会最终成为Anthropic的联合创始人？

Tom Brown：2009年夏天，我加入了一个叫Linked Language的项目，这是我两个朋友创立的，他们当时看到我们另一个朋友Kyle Vogt在做YC创业公司，所以觉得我们也可以尝试。他们开始后，我成了第一名员工。那时候我其实也可以去大厂做工程师，可能学到更多技术，但我选择和创始人们一起，从零开始，没有人告诉我们该做什么，我们只能自己想办法让公司活下去。在学校时更像是别人分派任务，我按部就班去完成，就像等主人喂食的狗。**而在创业公司，我们更像狼，要自己去狩猎，不然就会饿死。** 这个思维转变对我之后做更大、更有挑战性的事情帮助很大。

Garry Tan：没错，大厂只会教你如何在大厂工作，而做"狼"更有趣。

Harj Taggar：你是怎么从朋友的创业公司转到自己创立公司这一步的？

Tom Brown：Linked Language运营了一段时间后，我回去继续读书。毕业后，我加入了MoPub。

Harj Taggar：就是那个移动广告公司，对吧？

Tom Brown：对，我是那里的第一位工程师。那时候我觉得自己要做"狼"，但编程水平还很一般，常常觉得吃力。虽然知道自己想做更大的事，但还没掌握方法。不过那段经历让我第一次感受到把一个产品做大规模的过程。2012年冬天，我大学里最聪明的一个朋友找我，说要一起做一个YC创业公司。我们当时创立了Solid Stage，这还在Docker出现之前。我们的想法是让DevOps更简单------在没有Docker的年代，就是做一个更灵活版的Heroku，本质上也意味着更复杂的Heroku。我记得我们当时去YC面试，你们似乎没太明白我们要做什么，其实我们自己也不完全清楚。

Garry Tan：做一些全新的事情时，这种情况挺常见。

Tom Brown：是的，但我们可能算比较特别的。面试完开车回旧金山时，我们还被叫了回去。TLB在白板上画了一个生气的表情，写着"你们到底要做什么？"。我们只好重新解释，可能他们觉得我们还是没想明白，但也许他们相信我们会慢慢摸索出来。坦白说，做到一半我依然觉得自己没完全想清楚，不知道如何把这个产品与一个我愿意为之投入一生的使命结合起来。后来，我离开了Solid Stage。Greg Brockman把我介绍给了Grouper创始人Michael Waxman。

Garry Tan：Grouper是一个有趣的社交产品，可以说是早期的"社交实验"。它的形式是三位男生和三位女生配对，一起去酒吧见面。当时还没有现在的AI技术，所以匹配都是人工完成的，常常会发生各种有趣的状况。

Tom Brown：对，基本上每次都会有一些意外发生。当然，并不是每个人都能玩得开心。我自己是一个很内向、甚至有点社交障碍的孩子，所以当时对Grouper的吸引力在于，它为像我这样不擅长社交的人创造了一个安全的环境，让我可以和朋友一起认识女生，不至于尴尬。那时团队招聘很关键，我亲自面试所有工程师。去Grouper约会最多的人其实是Greg Brockman，他有一段时间几乎每周都在参与，还会在当时的Slack或HipChat上分享。

Harj Taggar：因为他那段时间去了纽约，还经常在Recurse Center出没，对吧？

Tom Brown：可能有段时间在Recurse，但更多时候他在Stripe。当时他几乎每周都会在Stripe内部发帖："这周谁要去Grouper？"就这样坚持了大概一年。所以我和Greg成为了朋友，也因为这个关系，后来才有机会加入OpenAI。

Diana Hu：你的经历很有意思。MIT计算机系毕业才21岁，先是加入多个YC创业公司，后来又自己创业。最终成为Anthropic的联合创始人，这条路挺长但很精彩。你是怎么做到的？

Garry Tan：听起来，和Greg的那次连接很重要，你之后也因此成为OpenAI早期的几十名成员之一，对吧？

Tom Brown：2014年6月，我离开Grouper，一年后加入OpenAI。那时我一直在鼓起勇气转型做AI研究。我的想法是：如果我们这代人真能做出具有颠覆性的AI，那将是改变世界的事，我或许能帮上一点忙。但现实是，我大学线性代数只拿了B-，当时觉得做这件事必须是顶级高手才能参与。所以我一直在犹豫，甚至想过干脆继续创业，因为那是我比较熟悉的路。

Harj Taggar：那时候AI研究还不算主流，你的朋友们怎么看？他们觉得这是很酷的事吗？

Tom Brown：其实不是。很多朋友觉得这听起来有点奇怪甚至不靠谱，当时"AI安全"对他们来说就像"火星人口过剩"一样遥远。他们也怀疑我能不能做好。这让我在这件事上犹豫了很久，大概花了半年时间反复挣扎才下定决心。

Harj Taggar：那你那时候具体在做什么？是读论文学习吗？

Tom Brown：一开始其实还没有完全投入研究。我花了三个月时间放松自己，比如参加Titanic 7活动，还做了一辆艺术车。

Garry Tan：听起来挺好玩的。

Tom Brown：是啊，那段时间我其实有点创业倦怠。做Grouper时，高潮很高，但低谷也很低。后期公司发展不顺，收入下滑，而我的主要工作还是招人、画大饼，可心里已经没信心了。所以那时我对自己说："Tom，先休息一下吧，去做瑜伽、CrossFit、造辆艺术车。"

Garry Tan：回头看，Grouper吸引了很多聪明人，早期增长不错，但后来趋于平缓甚至下滑，你觉得问题出在哪？

Tom Brown：当时的竞争对手是OkCupid，主要是网页端。我们想解决的问题是：很多人不敢主动去认识陌生人，担心被拒绝，我们通过"盲配"降低这种尴尬。但就在我们运营Grouper时，Tinder出现了，它用"双向确认"解决了同样的问题------只有双方互相感兴趣才会匹配，这样被拒绝的尴尬就不存在了。说实话，这是一个更好的解决方案。Tinder很厉害，向所有"滑手"致敬。

**自学AI并加入OpenAI**

Harj Taggar：后来你怎么转向AI领域的？

Tom Brown：离开Grouper后，我先休息了三个月玩了一阵，但钱也花得差不多了。那时我觉得，如果真想进入AI研究领域，就必须全力以赴。**我给自己定了六个月的"隐身学习期"** ，**目标是有机会加入DeepMind、Google Brain或MIRI这样的团队。** 但我还不具备相关能力，所以那六个月要完全自学，否则进去也帮不上忙。

Diana Hu：那六个月你是怎么安排学习的？很多年轻工程师也想转型做AI研究。

Tom Brown：其实我先做了个过渡------和Twitch签了一个三个月的合同，赚够生活费，然后全职投入学习。当时的计划在现在看来不一定适用，但2015年我的路径是：学Coursera的机器学习课程，做几个Kaggle项目，研读《Linear Algebra Done Right》和一本统计教材，用YC校友的额度买了块GPU，通过SSH远程学习。那时候AlexNet已经出现，所以我主要在练习图像分类，这是课程里重点教的方向。

Diana Hu：那你是怎么加入OpenAI的？当时团队研究人员为主，工程师很少。

Tom Brown：OpenAI刚成立时，我直接给Greg发消息："我想帮忙，虽然线性代数才拿了B-，但我懂一点工程，也做过分布式系统，如果需要的话我甚至可以扫地。"Greg当时说，其实懂机器学习又懂分布式系统的人不多，他还给我介绍了Peter Abbeel，帮我制定了一点学习计划。那之后我每月和Greg跟进。几个月后，他说正好有个项目需要人------搭建StarCraft环境，所以我就以工程师的身份加入了。前九个月我几乎没做任何机器学习，主要是在搭环境。

Harj Taggar：那时的OpenAI是什么样子？

Tom Brown：我们办公地点是在旧金山Dandelion Chocolate工厂楼上，之前是在Greg的公寓。虽然地方很小，但背后已经有Elon承诺的十亿美元资金，所以感觉很扎实。

Diana Hu：你职业生涯的一个重要节点，是参与了GPT系列的工程搭建，尤其是GPT-3的训练基础设施，对吗？

Tom Brown：对，就是GPT-3。

Diana Hu：那是个怎样的过程？因为GPT-2当时还在用TPU，而GPT-3最大的突破是扩大算力规模，转向GPU，对吧？

Tom Brown：是的。我在OpenAI工作了一年后离开，去了Google Brain一年，然后再回到OpenAI。2018到2019年，我们开始为GPT-3做准备，核心就是扩大规模。当时Dario已经捕捉到了"Scaling Laws"的趋势。

Diana Hu：你们还发表了一篇重要的论文，这篇论文后来被证明非常有前瞻性。

Tom Brown：没错。那篇论文展示了一个非常直观的结论：**只要有正确的训练方法，投入更多算力，模型就会变得更智能。** 当时我们训练所花的资金并不算多，但趋势已经很明显。Danny Hernandez还发表了一篇论文，展示算法效率提升如何不断降低成本，这两个趋势叠加，让我们意识到未来几年智能水平会快速提升。

Garry Tan：当你第一次看到这些结果时，是不是觉得很震撼？

Tom Brown：是的。**尤其是那条"Scaling Laws"的曲线------跨越12个数量级，还能保持几乎直线的增长。我不是物理学家，但看到这个结果，我完全被说服了，决定把所有工作重心转向规模化训练。**

Garry Tan：可以这么理解吗？Scaling Laws不仅适用于语言模型，可能也存在于其他领域，只是我们没投入？

Tom Brown：没错。物理学里类似的规律比比皆是，有一个专门的领域叫"Phenomenology"，研究各种自然现象的规模规律。只是这是我第一次在计算机科学相关领域看到类似的趋势，确实令人惊讶。

Garry Tan：但当时也有人批评这种做法，觉得只是"砸钱买算力"，非常粗暴。

Tom Brown：是的，很多研究人员也觉得这不够优雅，就是"堆层数"。**不过我们后来也形成了一种心态------"用最笨的方法做成事"。Scaling Laws就是最典型的例子：看似简单粗暴，但它真的有效。**

**Anthropic的诞生与Claude的早期探索**

Diana Hu：能不能聊聊你是怎么加入Anthropic的？因为全世界能在OpenAI、DeepMind和Anthropic都待过的人屈指可数，而你还是从GPT-3团队中出来，参与创立了Anthropic。这个转变是怎么发生的？

Tom Brown：当时在OpenAI主要有两个核心团队：一个专注于安全（Safety），一个专注于规模化（Scaling），都直接向Dario和Daniela汇报。我们团队配合非常默契，而且无论在OpenAI还是后来在Anthropic，都有一个很特别的文化------一切沟通都在Slack上完成，而且所有频道都是公开的，信息透明。这个团队也是最认真对待"Scaling Laws"的一群人。我们都觉得这项技术会是颠覆性的：**未来某个时刻，人类会把控制权交到更强大的AI手中** ，我们希望它们能与人类目标一致，顺利完成这个过渡**。但这是高风险的，因此必须有一个机构能承担起这样的使命。** 这也是为什么我们后来选择离开，创立Anthropic。坦白说，当时我并不确定这是"对世界最正确的事"，但回头看，现在似乎是个不错的选择。

有趣的是，刚开始的时候我们一点都不像会成功的样子。OpenAI有十亿美金的资金和明星阵容，而我们七个联合创始人在疫情期间远程工作，甚至不确定能不能做出产品，也不知道产品会是什么样。但当时加入的每一个人都是因为认同这个使命。他们完全可以去更有声望、薪资更高的地方，但他们选择了Anthropic。

Harj Taggar：如果不创立Anthropic，他们可能就留在OpenAI了吧？

Tom Brown：对，没错。这其实也是Anthropic文化的一个关键点：即使现在公司已经扩张到2000人，我们的组织氛围依然相对纯粹。**前一百名加入的人都是为了使命而来** ，如果出现问题，他们会直接站出来说："这个人似乎不符合我们的使命。"**这种文化让我们在扩张中保持了方向感** 。

Jared Friedman：跟我们聊聊Anthropic刚成立那会儿吧。你们七个人从OpenAI出来，带着一个"长远的使命"------维系人类的存在，但第一年具体在做什么？怎么一步步变成了实际的产品？

Tom Brown：第一年的核心任务其实很简单：第一，搭建训练Claude所需的基础设施；第二，搞到足够的算力来训练模型。除此之外，还有很多创业初期的杂事：开公司账户、处理财务、各种运营问题。我们一开始是7个联合创始人，没多久大概又有25个OpenAI的同事加入，团队规模一下子就上来了，而且大家之前都熟悉配合，所以进展算是很快。

Jared Friedman：那第一个产品是什么时候出来的？什么时候觉得事情开始"跑起来"了？

Tom Brown：第一个对外的产品其实是在ChatGPT之后。大概在ChatGPT出来前的9个月，我们做了一个内部的Slack机器人版Claude 1。

Garry Tan：对啊，当时YC的Slack里也有那个机器人。

Tom Brown：对，我还记得Tom Blfield把你们全拉进去玩。但当时我们并不确定要不要把它真的当成产品上线。因为我们没有想清楚上线会不会对世界好，也没有完全理清自己的"影响路径"。而且事后来看，就算当时决定上线，我们的服务基础设施也没做好，根本撑不住。因为犹豫了一阵，导致我们在基础设施这块准备得不够快，这算是我的一个经验教训。

Garry Tan：那个时候ChatGPT还没发布呢。

Tom Brown：对，那时我们也完全不知道它会引起这么大的轰动。

Diana Hu：这是在疫情期间，大概2022年？

Tom Brown：对，2022年夏天。到了当年秋天ChatGPT发布，我们随后更新了API，Claude也在那之后上线。老实说，在Claude 3.5和编码能力真正稳定之前，我们一直觉得公司前景并不确定，大概到一年前才有点"拨云见日"的感觉。

**Claude 3.5 Sonnet的"突破时刻"**

Diana Hu：我们在创业圈里也能感受到这种变化。2023年整年，几乎所有创业公司提到的首选模型都是OpenAI。但到了2024年，情况开始转变。Claude 3.5和特别是Sonnet版本出现后，市场份额在YC的批次里从个位数一路涨到20%-30%。尤其在编程领域，Claude逐渐成了默认选择，非常有意思。能聊聊这个能力突然爆发的过程吗？

Garry Tan：现在应该有80%甚至90%都在用吧？

Diana Hu：是啊，在编程领域尤其如此，现在Claude Code几乎成标配。这个是有意为之，还是自然发展出来的？

Tom Brown：我们其实很早就决定要让Claude在代码上表现得特别好，因为这是我们认为很重要的方向。然后看到市场反馈后，我们就加大了投入。

Jared Friedman：所以在3.5 Sonnet之前，你们就已经在加大对代码的投入了？

Tom Brown：没错。其实这是团队里一些成员的主动选择。他们在3.5 Sonnet之前就坚持要做更好的代码能力。而当我们看到3.5 Sonnet得到了非常强的产品市场匹配反馈后，那就是一个很明确的信号------要更大力度地推进这一方向。

Jared Friedman：当你们推出3.5 Sonnet的那一天，你们是不是已经意识到这会成为公司发展的转折点？还是像OpenAI 推出ChatGP 那样，也是突然爆火、连自己都没想到？

Tom Brown：真希望我们当时有这种远见，但没有。3.5 Sonnet爆火的程度确实让我们很惊讶。后来3.7 Sonnet也让我们意外，它在"智能化编程"上打开了全新空间。其实每次推出新版本，我们的节奏都很快，很难提前预判结果。

Diana Hu：这也是让很多做编程智能代理的创业公司爆发的原因吧。像Replit，从零到1亿美元只用了10个月；Cursor也有类似故事，而这些都建立在Sonnet的能力之上。

Tom Brown：是的，这些案例对我来说同样很意外。甚至在日常和Claude的交互中，我还会被它的能力震惊。比如一个朋友有个老程序想改，但手头只有编译后的二进制文件，没有源代码。她直接问Claude："能不能帮我反编译？"Claude花了10分钟就把它变成了一份C语言版本，还给变量起了合理的名字。她说自己如果手工做，可能要花三天时间处理十六进制表**。这种能力让我觉得，我们的模型总能解锁一些新的可能性。** Claude似乎"记住"了无数十六进制表格，并能一步步推演，这意味着未来它还会带来更多意想不到的突破。

Jared Friedman：很多YC创业者在编程任务上更喜欢用Anthropic的模型，这个差距远比基准测试能预测的要大。似乎有个"X因素"让大家特别喜欢用Claude做编码。你们知道这是为什么吗？这是有意为之，还是模型本身的"黑箱"特性？

Tom Brown：我觉得基准测试很容易被"针对性训练"。其他大厂都有专门的团队负责优化测试分数，而我们没有。我们不想"为了考试而学习"，因为那会带来一些不好的激励机制。

Garry Tan：就是不"应试教育"，对吧？

Tom Brown：对。我们有内部的评测体系，但不对外发布。团队会专注提升内部的指标，同时还有一个很重要的目标------让我们自己的工程师也能被模型加速，所以我们内部会大量使用Claude确保它真的能帮到人。

Diana Hu：那Claude在"人格"上的表现怎么评估呢？

Tom Brown：人格评测更复杂。怎么判断一个模型是不是"善良的"或者"好聊的"？这不容易量化。Amanda Ascll带的团队是专门做这个的，她的比喻挺好------**Claude要像一个"见多识广的旅行者"，不管对话对象来自什么背景，都能让对方觉得舒服、被尊重。** 我认为这就像是一个长期的赌注，现在模型还不算"吓人"，但未来可能会更复杂，我们希望那时候能看清它们内部的逻辑。

Harj Taggar：近期，Claude Code取得了显著成功。能否和我们分享一下，这个项目最初是如何在公司内部启动的？另外，当时你们是否确定它会成功，还是说这次成功出乎预料？

Tom Brown：Claude Code最初也是一款内部工具。当时是为了帮助Anthropic内部的工程师，由Boris临时开发搭建而成。

Harj Taggar：所以是Anthropic的内部工程师想为自己打造这样一款工具？

Tom Brown：准确来说，是为他自己以及其他内部工程师开发的。而且，我们当时完全没预料到它会在外部市场取得成功。在此之前，我们一直把重心放在API上------毕竟市面上有太多初创公司，他们手握大量优秀想法，我们没必要去纠结基于现有技术该打造什么样的产品，因为这些公司肯定能做出比我们更出色的成果。所以，我们当时一门心思投入到API研发中，力求打造出性能最优的API。

**但这次Claude Code的表现确实让我意外：没想到我们居然能打造出这样一款产品，在agentic相关的使用场景下，它的表现比市面上其他同类产品还要好。** 我对此有个看法，这或许源于我们思维上的转变------我们也把Claude视为这款工具的"用户"。比如，我们之前开发面向教师的工具时，教师就是核心用户；开发Grouper时，核心用户大概是纽约的单身人群。而在打造Claude Code时，核心用户不仅包括开发者，还包括Claude本身。我们的思路是：为Claude提供合适的工具，让它能高效完成任务；帮Claude获取必要的上下文信息，确保它能顺畅发挥作用。负责这个项目的团队，是所有团队中最注重"将 Claude视为用户"。

Jared Frieadman：你们最了解Claude，所以能做到这一点也合情合理。

Tom Brown：话虽如此，但初创公司的创始人其实也能做到这一点。**而且我觉得，"打造以模型为用户的工具"这一领域，未来潜力很大，值得大家深入探索。**

Garry Tan：这其实是对LLM本身最贴切的"拟人化"理解------Agent本身就是需要关注的利益相关方，也是需要赋能的用户之一。

Tom Brown：完全同意。

Diana Hu：**这也能解释为什么你们能成功实现MCP的工具调用功能。** 要知道，其他很多实验室都尝试过类似方向，但最终只有你们的方案成为了行业标准，并且得到广泛应用。

Tom Brown：没错，**我认为MCP的成功和Claude Code有相似之处，都在于"以模型为核心"的研发思路。**

Harj Taggar：Claude Code的成功很让人振奋，但对像Cursor这样基于API构建产品的公司来说也有点可怕。毕竟担心有一天Anthropic或其他实验室自己做一个更强的产品，直接抢了市场。你会给这些创业者什么建议？

Tom Brown：老实说，我们自己也有点意外ClaudeCode做得这么好。**我觉得优势更多不是技术层面的，而是我们对开发者的理解和同理心。**

Harj Taggar：这个insight很有意思。就是你们不是靠技术壁垒，而是因为更了解目标用户，对吧？

Tom Brown：对。我觉得初创公司完全可以做同样的事。只是我们可能是最专注开发者的实验室，API也更开放。**我们想让平台成为大家构建产品的最好基础** ，**因为AI增长实在太快了。世界是为人类设计的，但现在要想办法让模型成为经济活动中的"生产力成员"。**

Harj Taggar：那你觉得还有哪些被低估的领域是创业者值得去做的？

Tom Brown：**Claude Code现在更像是个"有潜力的实习生"或"初级工程师"** ，可以帮忙写代码，甚至能做一些高级的拆解、反编译工作，但它需要很多上下文和指导。而在企业里，代码开发只是工作的一小部分。企业里还有大量需要聪明人+工具但不一定需要很深背景的任务，这些都是机会。**谁能找到让Claude或其他模型成为"业务助手"或"团队教练"的路径，机会会非常大。**

**人类正进行史上最大规模的基础设施建设**

Jared Frieadman：Tom，你负责Anthropic的算力基础设施，能说说背后的规模吗？

Tom Brown：现在人类正进行史上最大规模的基础设施建设。

Jared Frieadman：比阿波罗登月、曼哈顿计划还大？

Tom Brown：如果继续这个趋势，明年就会超过它们。AGI算力投入每年几乎3倍增长，真的疯狂。2026已经锁定，2027还在规划中。

Garry Tan：YC内部都不够用啊，Claude额度永远不够，大家都在喊"再多点智能"。

Tom Brown：硬件是关键，会有更多加速器出现，数据中心技术也是大机会。

Jared Frieadman：那现在的瓶颈是什么？电力？GPU？审批？

Garry Tan：甚至有人用喷气发动机发电，这也太疯狂。

Tom Brown：最大瓶颈是电力，尤其在美国。我们很希望更多数据中心能在美国落地，这也是我们的重要政策目标------让建设更快、更容易。

Garry Tan：解决电力问题靠可再生能源还是核能？

Tom Brown：都要。我真希望核电建设能更容易些。

Jared Frieadman：Anthropic是唯一一家同时用三种不同厂商GPU的大模型公司，可以聊聊这个策略吗？

Tom Brown：**我们用了GPU、TPU和Tranium。坏处是性能工程团队要分散在不同平台上，工作量很大。好处是有弹性------一是能更好消化市场上有限的算力资源，二是能把"合适的芯片用在合适的任务"上：有的更适合推理，有的更适合训练。**

Diana Hu：挺有意思的，你早期在OpenAI推动了从TPU转向GPU，让GPT-3能大规模训练，现在你在Anthropic管理更庞大的体系。

Tom Brown：当时转向GPU，很大原因是PyTorch在GPU上的软件生态比TPU上的TensorFlow更好。**一个强大且稳定的软件栈意味着能快速迭代，这对突破很关键。** Anthropic现在面对更多平台，挑战更大，所以核心是能写出优秀的软件，让所有研发人员在低层算力上都有好体验。

Diana Hu：如果现在有个年轻版的你，想加入AI浪潮，你会怎么给他怎样的建议？

Harj Taggar：很多大学生都在犹豫要不要读完书、未来会不会有好工作、该怎么选路。

Tom Brown：我会说：**敢冒险，去做那些让你朋友觉得"哇塞"的事，或者让理想中的自己都为你骄傲的事。别怕挑战。**

Garry Tan：少点外在的追求，多点内在的满足。别纠结学历、名企光环，现在这些没以前那么重要。

Tom Brown：对，完全同意。

*原视频: Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 \& LLM System Design*

*https://www.youtube.com/watch?v=JdT78t1Offo\&t=370s\&ab_channel=YCombinator*

*编译：Mary*

*请注意，本文编译自文未载明的原始链接，不代表Z Potentials立场。如果您对本文有任何想法或见解，欢迎在评论区留言互动探讨。*

*Z Potentials将继续提供更多关于人工智能、机器人、全球化等领域的优质内容。我们減邀对未来充满憧慢的您加入我们的社群，与我们共同分享、学习、成长。*

**-----------END-----------**

****[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FZ300vPwLQkmMISOgKyml4wsGliaUpt2TbuDqbtPLty8Xa4uicSEHNRIr0TGkJmvqChgZNbN7OtwjSbzYFdFyv41g%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D1)](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247506405&idx=1&sn=29bdac1ee34aaceade9e66e9b0867d8f&scene=21#wechat_redirect)****

****🚀** 我们正在招募新一期的实习生**

[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fib38wYqSEotCHKHKStTHING7RWbF185pkmdYZXo4NhwjylmSOc72CH6F34ib5zMeGZqibkibbcxXoEvJmjyLmuzXZQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247503698&idx=4&sn=ade3fdbb8a82ca59be3212c4843bb1a0&scene=21#wechat_redirect)

******🚀** 我们正在寻找有创造力的00后创业****

[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fib38wYqSEotCHKHKStTHING7RWbF185pkNNoicM51qHkAc3kwnwz6ia0ba6icSUnowNkICLtenFRAllGWeQrfv2jpg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247494663&idx=1&sn=8fab67231b9ebc593ac65864fd8f7e00&scene=21#wechat_redirect)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fib38wYqSEotDTv2HTbWFO0Xegic9kT1NvH3NibT7n8o00pEutIKnFS152mZHbmhLBX2EVDXMtvKOYKXGnhgFGVtbg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FZ300vPwLQkm0xDAYwIuGF5bACW3JCUfrsMPLj2aVVzntMonOYicnTDO2lp9qSSacgYWicCGKZl669HL7dShh6pOQ%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%23imgIndex%3D5)

***关于Z Potentials***  


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2Fib38wYqSEotBunsxKxYL82cw1G45XjPzk1ODqQhmOibqk9CjGiavvGBfLkb3zS10dMTdDwMOZ6xTZWbHiazmE9qsTg%2F640%3Fwx_fmt%3Djpeg%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26tp%3Dwxpic%23imgIndex%3D6)

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247509634&idx=1)
