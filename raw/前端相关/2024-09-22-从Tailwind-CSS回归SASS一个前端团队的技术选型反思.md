---
id: "7237501057234896608"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247523737&idx=1&sn=c20fa35b69ac05a8e333a0f3d2def54f&chksm=e87612abd56f96e219d1a036c70dced6092c05edd04d8d44327e42d1aea44f506c67cd64517c&mpshare=1&scene=1&srcid=0922xzF86pmM2Vlo8U6F2n37&sharer_shareinfo=8dc6ec68676e77fecc85717d28da2bed&sharer_shareinfo_first=8dc6ec68676e77fecc85717d28da2bed
author: "dev 大迁世界"
collected: 2024-09-22
tags: []
---

# 从Tailwind CSS回归SASS：一个前端团队的技术选型反思

# 从Tailwind CSS回归SASS：一个前端团队的技术选型反思

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247523737&idx=1&sn=c20fa35b69ac05a8e333a0f3d2def54f&chksm=e87612abd56f96e219d1a036c70dced6092c05edd04d8d44327e42d1aea44f506c67cd64517c&mpshare=1&scene=1&srcid=0922xzF86pmM2Vlo8U6F2n37&sharer_shareinfo=8dc6ec68676e77fecc85717d28da2bed&sharer_shareinfo_first=8dc6ec68676e77fecc85717d28da2bed#rd)dev 大迁世界


在前端开发领域，技术选型往往会对项目的成败产生深远影响。最近，我们团队在开发一个基于React的实时聊天应用时，经历了从采用Tailwind CSS到最终回归SASS和CSS Modules的曲折过程。这段经历不仅让我们深刻认识到了技术选型的重要性，也为其他开发者提供了宝贵的经验教训。

#### **初期的美好愿景**

Tailwind CSS作为一个备受推崇的 utility-first CSS框架，最初吸引我们的是它promises的快速开发和统一设计语言的能力。想象一下，仅通过组合预定义的utility类，就能快速构建出复杂的UI组件，这种promise确实令人兴奋。

例如，一个简单的卡片组件可能看起来像这样：

    <div className="bg-white rounded-lg shadow-md p-6 m-4">
      <h2 className="text-xl font-bold mb-2">Card Title</h2>
      <p className="text-gray-700">Card content goes here.</p>
    </div>

这种方式初看起来确实简洁高效，但随着项目的推进，问题逐渐显现。

#### **问题的浮现**

随着应用规模的扩大，JSX中堆积如山的utility类开始影响代码的可读性和可维护性。一个原本简单的组件可能演变成这样：

    <div className="flex flex-col md:flex-row items-center justify-between p-4 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 ease-in-out">
      <div className="flex items-center mb-4 md:mb-0">
        <img className="w-10 h-10 rounded-full mr-4" src="/avatar.jpg" alt="User avatar" />
        <div>
          <h3 className="text-lg font-semibold text-gray-800">John Doe</h3>
          <p className="text-sm text-gray-600">Software Developer</p>
        </div>
      </div>
      <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors duration-300 ease-in-out">
        Follow
      </button>
    </div>

这种代码不仅难以阅读，更糟糕的是，它开始影响应用的性能。

#### **性能隐患**

随着项目的推进，我们注意到应用的响应速度开始下降。经过深入分析，发现庞大的CSS文件是罪魁祸首之一。尽管Tailwind提供了purge功能来删除未使用的类，但生成的CSS文件仍然相当大。

此外，构建时间的增加也影响了开发效率。每次修改都需要重新编译大量的CSS，这极大地降低了开发体验。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FLDPLltmNy56Wm9Lx3siafsGArdH6vzJ6nhvpwcicx3VG1QcqOB7HTicBTjiaZh8mVwLtyJqGOgDZp12wbqibGQudruA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

#### **回归SASS和CSS Modules**

面对这些挑战，我们决定回归到SASS和CSS Modules的组合。这个决定虽然意味着大量的重构工作，但最终证明是值得的。

重构后的卡片组件可能看起来像这样：

    import styles from './Card.module.scss';

    const Card = ({ title, content }) => (
      <div className={styles.card}>
        <h2 className={styles.title}>{title}</h2>
        <p className={styles.content}>{content}</p>
      </div>
    );

对应的SASS文件：

    .card {
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      padding: 1.5rem;
      margin: 1rem;

      .title {
        font-size: 1.25rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
      }

      .content {
        color: #4a5568;
      }
    }

这种方式不仅提高了代码的可读性，也大大降低了CSS的体积，提升了应用性能。

#### **经验总结**

1.
   **权衡便利性和性能**：Tailwind CSS在快速原型开发中确实很便捷，但在大型应用中可能带来性能问题。
2.
   **可维护性至关重要**：随着应用规模增长，语义化的类名和模块化的CSS变得越发重要。
3.
   **持续关注性能**：定期使用Lighthouse等工具监控CSS对性能的影响。
4.
   **灵活选择技术栈**：对于大型应用，SASS配合CSS Modules可能是更好的选择。

#### **结语**

这次从Tailwind CSS到SASS的转变，让我们深刻认识到技术选型对项目成功的重要性。虽然Tailwind CSS在某些项目中可能表现出色，但对于我们的实时聊天应用而言，SASS和CSS Modules提供了更好的可维护性和性能。

这个经历提醒我们，在选择技术栈时，需要综合考虑项目的长期发展、团队的开发效率以及最终产品的性能表现。希望我们的经验能为其他开发者在技术选型时提供有价值的参考。


**最后：**


[****CSS技巧与案例详解****](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzI0NDQ0ODU3MA==&scene=2&album_id=3545535769677725703&count=3&uin=&key=&devicetype=iMac+MacBookPro18%2C3+OSX+OSX+14.3+build(23D56)&version=13080812&lang=zh_CN&nettype=WIFI&ascene=2&fontScale=100)

[**vue2与vue3技巧合集**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzI0NDQ0ODU3MA==&scene=1&album_id=2509459125236416515&count=3#wechat_redirect)

[**VueUse源码解读**](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI0NDQ0ODU3MA==&action=getalbum&album_id=2854832033280311296&from_itemidx=1&from_msgid=2247515074&scene=173&count=3&nolastread=1#wechat_redirect)

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247523737&idx=1&sn=c20fa35b69ac05a8e333a0f3d2def54f&chksm=e87612abd56f96e219d1a036c70dced6092c05edd04d8d44327e42d1aea44f506c67cd64517c&mpshare=1&scene=1&srcid=0922xzF86pmM2Vlo8U6F2n37&sharer_shareinfo=8dc6ec68676e77fecc85717d28da2bed&sharer_shareinfo_first=8dc6ec68676e77fecc85717d28da2bed#rd)

