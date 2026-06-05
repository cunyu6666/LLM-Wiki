---
id: "7287102992338124996"
cubox_url: 
url: https://emilkowal.ski/ui/great-animations
author: ""
collected: 2025-02-06
tags: []
---

# Great Animations

# Great Animations

[emilkowal.ski](https://emilkowal.ski/ui/great-animations)

People increasingly select their tools based on the overall experience rather than just functionality. A predictable and delightful experience is what makes a product stand out from a crowded market. That's why companies invest in design engineers for example. Animations can play a big role in creating such experiences.
How do we create such animations?

Great animations are hard, as there are many aspects to consider. From easing and timing to accessibility and performance. This post is a collection of principles that, in my opinion, make animations great.
Great animations feel natural

People love the dynamic island. It feels natural, almost like a living organism.

This natural motion makes things easier to understand and is a major reason why mobile apps feel better than web apps.

<br />

Changes in web apps often occur instantly, which makes the experience feel artificial and unfamiliar, since nothing in world around us disappears or appears instantly.

I highly suggest playing around with spring animations in your projects. Below is a visualizer that can help you understand how spring animations are influenced by different parameters.

stiffness

damping

mass

This visualizer is inspired by [Morses's work](https://twitter.com/__morse).

Great animations are fast

Fast animations improve the perceived performance. Take a look at these two spinners for example, which one would load faster?

They would both take the same time to load, but the one on the right gives you an impression as if it's working very hard to load the data for you.

<br />

Snappy animations feel responsive and connected to user's actions.

Family's iOS app is a perfect example of a snappy interface.

The best type of easing for this purpose is `ease-out`. It starts fast and slows down at the end, which gives the impression of a quick response, while maintaining a smooth transition. Your animations should also usually be shorter than 300ms.
Great animations have a purpose

It's easy to start adding animations everywhere. The user then becomes overwhelmed and animations lose their impact. We need to pace them through the experience and add them in places where they enrich the information on the page.

<br />

A good example is this animation I made for Vercel. It explains how v0 works. While the animation is arguably entertaining to watch, it's also insightful.

We can also use animations to indicate a change in state, like with the App Store cards. An enter or exit animation for a modal is also a good example.

Before you add an animation, you should also consider how often the user will see it.

<br />

A good tip here is to never animate keyboard initiated actions. These actions are repeated sometimes hundreds of times a day, an animation would make them feel slow and disconnected from user's actions.

<br />

I use Raycast frequently and can't imagine how frustrating it would be if every time I opened it, I was greeted with a 500ms enter animation.

Raycast has no animations and it feels right.

Great animations are performant

If our animations won't run at 60 frames per second, everything else we've talked about becomes useless.

<br />

The rule of thumb here is that you should try to animate with `transform` and `opacity` as they only trigger the third rendering step (composite), while padding or margin triggers all three (layout, paint, composite). The less work the browser has to do, the better the performance.

<br />

If the main thread is busy, you should animate using hardware-accelerated animations like CSS or WAAPI (Web Animation API).

<br />

A hardware-accelerated animation will remain smooth, no matter how busy the main thread is. Keep in mind that even if you do animate with CSS, not all properties are hardware-accelerated, but if you stick to `transform` and `opacity`, you should be fine.

<br />

The more logos you add in the demo below, the laggier the Framer Motion animation will become, as it uses `requestAnimationFrame` under the hood, which is not hardware-accelerated.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2F_next%2Fimage%3Furl%3D%252Flogo.png%26w%3D32%26q%3D75&valid=true)

This example is inspired by the [Sidebar Animation Performance](https://www.joshuawootonn.com/sidebar-animation-performance) post by Josh Wootonn.

This issue happened in Vercel's dashboard where we animated the active tab. The transition was done with [Shared Layout Animations](https://www.framer.com/motion/layout-animations/#shared-layout-animations), and because the browser was busy loading the new page, the animation dropped frames. We fixed this by using CSS animations which moved the animation off the CPU.

Great animations are interruptible

Interruptibility helps your animations feel more natural and responsive. It allows the user to change the state of the animation at any time while maintaining a smooth transition. Try clicking on one of the items below and quickly closing it by pressing the escape key.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2Fgreat-animations%2Fspace.png&valid=true)

## The Oddysey

Explore unknown galaxies.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2Fgreat-animations%2Frabbit.png&valid=true)

## Angry Rabbits

They are coming for you.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2Fgreat-animations%2Fghost.webp&valid=true)

## Ghost town

Scarry ghosts.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2Fgreat-animations%2Fpirate.png&valid=true)

## Pirates in the jungle

Find the treasure.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Femilkowal.ski%2Fgreat-animations%2Fboy.webp&valid=true)

## Lost in the mountains

Be careful.

The example above is built with Framer Motion, which supports interruptible animations. If you prefer to stick with CSS, you can replace your animations with transitions. A CSS transition can be interrupted and smoothly transition to a new value, even before the first transition has finished. You can see the difference below.
Great animations are accessible

Animations are used to strategically improve an experience. To some people, animations actually degrade the experience. [Animations can make people feel sick](https://www.a11yproject.com/posts/understanding-vestibular-disorders/) or get distracted. That's not the experience we want to build. To prevent degrading the experience, our animations need to account for people who don't want animations.

## This is step one

Usually in this step we would explain why this thing exists and what it does. Also, we would show a button to go to the next step.

This component animates opacity only when the user prefers reduced motion.

We can use a media query in CSS to adjust the animation based on the user's preference.

    .element {
      animation: bounce 0.2s;
    }
     
    @media (prefers-reduced-motion: reduce) {
      .element {
        animation: fade 0.2s;
      }
    }

    .element {
      animation: bounce 0.2s;
    }
     
    @media (prefers-reduced-motion: reduce) {
      .element {
        animation: fade 0.2s;
      }
    }

Or use a hook if we are using Framer Motion for example.

    import { useReducedMotion, motion } from "framer-motion"
     
    export function Sidebar({ isOpen }) {
      const shouldReduceMotion = useReducedMotion();
      const closedX = shouldReduceMotion ? 0 : "-100%";
     
      return (
        <motion.div animate={{
          opacity: isOpen ? 1 : 0,
          x: isOpen ? 0 : closedX
        }} />
      )
    }

    import { useReducedMotion, motion } from "framer-motion"
     
    export function Sidebar({ isOpen }) {
      const shouldReduceMotion = useReducedMotion();
      const closedX = shouldReduceMotion ? 0 : "-100%";
     
      return (
        <motion.div animate={{
          opacity: isOpen ? 1 : 0,
          x: isOpen ? 0 : closedX
        }} />
      )
    }

Great animations feel right

People love using [Sonner](https://sonner.emilkowal.ski/) mainly, because the animation feels satisfying. But I also think it's because the whole experience of using it is cohesive.

The easing and duration of the animation fits the vibe of the whole library. It's a bit slower than usual and uses `ease` as the easing type rather than `ease-out` to make it feel more elegant. It's in line with the toast design, page design, its name etc.

<br />

Another example of this is Family's drawer that I recreated on the web. I don't know the exact animation values that Family used, so it's not as good, but people still seem to love it.

I think it's because the easing used in the animation feels right. The opacity change in exiting and entering items works well with the height animation. In this case, it was a matter of trial and error until it felt right. But that's often the case with animations---you have to be patient.

<br />

Take some time to review your animations. I like to review my work the next day because I can see it with fresh eyes and notice imperfections I didn't see before.
Great animations are hard

This post should give you a good starting point for creating great animations. But if you'd want to learn more, I cover all the principles we talked about in-depth in my course called Animations on the Web. We also build all the components above and more there.

[Check out "Animations on the Web"](https://animations.dev/)

## More content like this

The goal of these posts is to create helpful content for engineers and designers, I try to do the same with my newsletter. I'll let you know when I publish new content, and share **exclusive, newsletter-only content** once a month.

No spam, unsubscribe at any time.

[emilkowal.ski](https://emilkowal.ski/ui/great-animations)

