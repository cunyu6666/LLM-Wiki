---
id: "7237023242085466255"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg4MjY5MTU1MA==&mid=2247502987&idx=1&sn=ad1cae955ce0a1b1513cbd9d5560ebc2&chksm=ce856e40c7ca85abf2045b9a888e12c0f05df9044c4ebede834faa1cd4143683fd64ddfeaaf2&mpshare=1&scene=1&srcid=0921DVCDrSrsXCMpHLLe6I8F&sharer_shareinfo=02c317f2a6d3072ee60169f95ab61cff&sharer_shareinfo_first=02c317f2a6d3072ee60169f95ab61cff
author: "了不起 前端实验室"
collected: 2024-09-21
tags: []
---

# 比Draggable还要简单！这轻量级页面拖拽小工具，高效到爆！

# 比Draggable还要简单！这轻量级页面拖拽小工具，高效到爆！

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=Mzg4MjY5MTU1MA==&mid=2247502987&idx=1&sn=ad1cae955ce0a1b1513cbd9d5560ebc2&chksm=ce856e40c7ca85abf2045b9a888e12c0f05df9044c4ebede834faa1cd4143683fd64ddfeaaf2&mpshare=1&scene=1&srcid=0921DVCDrSrsXCMpHLLe6I8F&sharer_shareinfo=02c317f2a6d3072ee60169f95ab61cff&sharer_shareinfo_first=02c317f2a6d3072ee60169f95ab61cff#rd)了不起 前端实验室


大家注意：因为微信最近又改了推送机制，经常有小伙伴说错过了之前被删的文章，或者一些限时福利，错过了就是错过了。所以建议大家加个星标，就能第一时间收到推送。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FWqeajEMWSax6eOMTMqiayuT0IQWzhjVWia6HtpLsiazQXic9SMNnXh02SfumGCJ1cdwibu2c9YabPLg6Bdicv5YyzKcQ%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1)大家好，我是`「前端实验室」`爱分享的了不起\~

### 前言

前不久，我们一起分享了一个非常实用的 Vue 拖拽组件 ------ `Vue Draggable Plus`。今天，我们再分享一个新的拖拽小工具：`Swapy`

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FWqeajEMWSazDYNJTFQb6tR5wxGXPvzNGLawsgOAiajqhlFKEd6CyXFolnRYiaOTjmpIWEhwIY4uCtibgSQFiaph9dg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

### 简介

`Swapy`是由TahaSh开发的一款开源JavaScript工具。它的核心功能是**将静态布局转换为可以拖拽交换的动态布局**。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FWqeajEMWSazDYNJTFQb6tR5wxGXPvzNGWjWtiaEVpeR0Gia7UYgsia4LDh2ZJLmic0xqkFib7K7YWCd4F9DRnJh6DcA%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

因此，`Swapy`的使用场景和`Vue Draggable Plus`还是有点差异的。

`Swapy` 是一个与框架无关的工具。它几乎可以和市面上常用的所有框架衔接使用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FWqeajEMWSazDYNJTFQb6tR5wxGXPvzNGZVyjGpKBAcEwX6xicQe0OGXZhc1OkBHxhNMYTCrBNZYAGsp6K57TxjQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

你可以在不大幅修改原有项目结构的情况下，快速的通过增加`Swapy`，来对页面中的图片、文字等各种内容增加拖拽布局。

### Swapy的主要特点

*
  简单易用：`Swapy`的设计哲学是简单性。它不需要复杂的配置或大量的代码，使得开发者可以快速上手。

*
  高度可定制：通过CSS和JavaScript，开发者可以轻松地定制拖拽项的外观和行为。

*
  跨浏览器兼容性：`Swapy`在所有主流浏览器上都能正常工作，包括Chrome、Firefox、Safari和Edge。

*
  开源：`Swapy`是一个开源项目，开发者可以自由地下载、使用和修改源代码。

### 安装使用

#### 安装

我们可以直接在文件中通过CDN的方式来安装`Swapy`，可以参考如下：

    <script src="<https://unpkg.com/swapy/dist/swapy.min.js>"></script><script>  
    // You can then use it like this  
    const swapy = Swapy.createSwapy(container)</script>

当然，我们也可以通过包管理器来安装。

    npm install swapy

#### 使用

使用`Swapy`前，需要在HTML中定义插槽(slot)和项目(item)。

插槽(slot)是放置项目的容器。通过在容器中添加`data-swapy-slot`属性来指定。

项目(item)则是可以被拖拽的元素。通过属性`data-swapy-item`来标识。

下面是官方的示例：

    <div class="container">
      <div class="section-1" data-swapy-slot="foo">
        <div class="content-a" data-swapy-item="a">
          <!-- Your content for content-a goes here -->
        </div>
      </div>

      \<div class="section-2" data-swapy-slot="bar"\>
        \<div class="content-b" data-swapy-item="b"\>
          \<!-- Your content for content-b goes here --\>
          \<div class="handle" data-swapy-handle\>\</div\>
        \</div\>
      \</div\>

      \<div class="section-3" data-swapy-slot="baz"\>
        \<div class="content-c" data-swapy-item="c"\>
          \<!-- Your content for content-c goes here --\>
        \</div\>
      \</div\>
    \</div\>

一个`data-swapy-slot`包含一个`data-swapy-item`，就这么简单！

接着，就可以使用`Swapy`方法了。获取包含插槽(slot)和项目(item)的容器元素，并将该元素传递给`createSwapy()`函数。

    import { createSwapy } from 'swapy'

    const container = document.querySelector('.container')

    const swapy = createSwapy(container, {
      animation: 'dynamic' // or spring or none
    })

默认情况下，`Swapy`将使用`dynamic`动画。当然，你也可以使用`spring`或者`none`进行配置。

最后，调用`enable`函数来触发。

    //可以随时打开或关闭这儿拖拽布局
    swapy.enable(true)

至此，一个简单的拖拽布局示例就完成了。此外，官方还提供了事件监听的函数，用于监听和获取拖拽中的数据变化。

    import { createSwapy } from 'swapy'

    const container = document.querySelector('.container')

    const swapy = createSwapy(container)

    swapy.onSwap((event) =\> {
      console.log(event.data.object);
      console.log(event.data.array);
      console.log(event.data.map);

      // event.data.object:
      // {
      //   'foo': 'a',
      //   'bar': 'b',
      //   'baz': 'c'
      // }

      // event.data.array:
      // \[
      //   { slot: 'foo', item: 'a' },
      //   { slot: 'bar', item: 'b' },
      //   { slot: 'baz', item: 'c' }
      // \]

      // event.data.map:
      // Map(3) {
      // 'foo' =\> 'a',
      // 'bar' =\> 'b',
      // 'baz' =\> 'c'
      // }
    })

好了，今天的分享就先到这里了。需要了解更多详情的小伙伴，请查阅官方网站。
> 官方地址  
> https://swapy.tahazsh.com/

### 最后

**我创建了一个副业交流群，方便我的读者可以在群里讨论、交流大家尝试过的副业。**

但是任何人在群里打任何广告，都会被我T掉。如果你对这个特别的群，感兴趣，请加我微信回复：**副业**，微信通过后会拉你入群。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FWqeajEMWSawe9Qr45lheRJTOBDxw9vyfvKLDzYMUeafkSYcKGtykpxIrgNCSiaavTP0GsbArXV1K1PggJCuzOicA%2F640%3Fwx_fmt%3Dother%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26tp%3Dwebp)

（加我微信，备注：副业）

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=Mzg4MjY5MTU1MA==&mid=2247502987&idx=1&sn=ad1cae955ce0a1b1513cbd9d5560ebc2&chksm=ce856e40c7ca85abf2045b9a888e12c0f05df9044c4ebede834faa1cd4143683fd64ddfeaaf2&mpshare=1&scene=1&srcid=0921DVCDrSrsXCMpHLLe6I8F&sharer_shareinfo=02c317f2a6d3072ee60169f95ab61cff&sharer_shareinfo_first=02c317f2a6d3072ee60169f95ab61cff#rd)

