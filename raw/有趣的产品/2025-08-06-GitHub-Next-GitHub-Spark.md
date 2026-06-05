---
id: "7352747064515628366"
cubox_url: 
url: https://githubnext.com/projects/github-spark
author: ""
collected: 2025-08-06
tags: []
---

# GitHub Next | GitHub Spark

# GitHub Spark

[githubnext.com](https://githubnext.com/projects/github-spark)

🚀 [GitHub Spark](https://github.com/features/spark) is now in public preview!

As developers, we *love* to customize our environment, and to build tools that fit our unique preferences and workflows. We do this not just because it improves productivity and ergonomics, but also, because it makes our daily routine feel more *personal* . And when things feel personal, they're typically more *fun*.

However, while we may invest in things like managing dotfiles, writing automation scripts, or configuring editor settings, how often do we pass up ideas for making our own apps? Not necessarily because we *couldn't* build them, but because they seem too short-lived, niche, or time-consuming to prioritize? 😩

And in this lies the irony with software today: we have powerful computers on our desks and in our pockets, but they aren't nearly as *personalized* as they could be. Instead, we rely on general-purpose tools that were designed by and for someone else, because the complexity of creating bespoke apps is too high.

Which raises two interesting questions: how could we make personalizing our software as easy as personalizing our dev environment? And then enable those around us to do the same? Not because that should be necessary---but because it could be fun 🙌

### Introducing GitHub Spark

GitHub Spark is an AI-powered tool for creating and sharing micro apps ("sparks"), which can be tailored to your exact needs and preferences, and are directly usable from your desktop and mobile devices. **Without needing to write or deploy any code.**

And it enables this through a combination of three tightly-integrated components:

1. An NL-based editor, which allows easily describing your ideas, and then refining them over time
2. A managed runtime environment, which hosts your sparks, and provides them access to data storage, theming, and LLMs
3. A PWA-enabled dashboard, which lets you manage and launch your sparks from anywhere

Additionally, GitHub Spark allows you to share your sparks with others, and control whether they get read-only or read-write permissions. They can then choose to favorite the spark---and use it directly---or remix it, in order to further adapt it to their preferences. Because...ya know...personalization!

So let's take a look at how it works 🎬

<br />

<br />

### What are "micro apps"?

GitHub Spark subscribes to the [Unix philosophy](https://en.m.wikipedia.org/wiki/Unix_philosophy) for apps, where software can be unapologetic about doing one thing, and doing it well--specifically for you, and the duration of time that it's useful. So "micro" doesn't refer to the size of the app's value, but rather, the size of its intended feature complexity.

For example, here are some sparks that the team made (and use!), during the process of creating GitHub Spark. These range from life management tools, learning aids, silly animations, and news clients. But the common thread across them all is: they look and feel exactly how the creator wanted them to. Nothing more and absolutely nothing less ❤️

![](https://image.cubox.pro/cardImg/68l5qv07a3lthte3a428aq2wo48cumq9ej9xkduymz06hot6ve.png?imageMogr2/quality/90/ignore-error/1) *An allowance tracker for kids, which can be shared in either read-only or read-write mode (for parents), and uses an LLM to generate a celebratory message when an earning goal is reached*

![](https://image.cubox.pro/cardImg/25e8fivuezhjka1aopgdy4bb97zlf6l3ngjcx5cifs2tjwl79e.png?imageMogr2/quality/90/ignore-error/1) *An animated world of vehicles, as envisioned--and created--by a six year old*

![](https://image.cubox.pro/cardImg/2z5vwh45j7oqwro1v7yxbg95m6sdot0leva0w3jt4u80fzvqnp.png?imageMogr2/quality/90/ignore-error/1) *An app for tracking a weekly karaoke night, along with the status of each invited guest*

![](https://image.cubox.pro/cardImg/4ixpyrppalzp02t2nzwrsv8grp7jj9x3cttxnzzcb07kstbbum.png?imageMogr2/quality/90/ignore-error/1) *A maps app that allows searching for cities by name, and then using an LLM to generate a fun tldr description of it. Created and used by a 10 year old for school*

![](https://image.cubox.pro/cardImg/1gkec44xx76htq4w3cp3ymkh0da0vw3282xk3ka5by1y2wl9aa.png?imageMogr2/quality/90/ignore-error/1) *A custom HackerNews client that shows the top 20 posts, and uses an LLM to summarize the comment threads (which is really useful!). This is the daily HN driver for the team*

So with that context in mind, let's talk about the "what?" and "why?" behind the major components of GitHub Spark 👍

### NL-based toolchain

When creating an app, you have to know what you want. And not just the general idea, but also the exact set of features, detailed interaction behaviors, and the overall look and feel of it. Unfortunately, this can get quite complicated, and may be overwhelming enough to prevent some from even trying. Which is exactly the problem we're looking to solve!

GitHub Spark mitigates this, by enabling you to start with a simple idea ("An app to track my kid's allowance"), and then allowing complexity to slowly emerge through "assisted exploration". In particular, it's NL-based editor is designed to make forward progress feel easy---and playful!---using four core iteration capabilities:

1. Interactive previews
2. Revision variants
3. Automatic history
4. Model selection

#### Interactive previews

When you type an NL expression into GitHub Spark, it doesn't just generate code--it immediately runs and displays it via an interactive preview. This "app-centric feedback loop" allows you to specify as little or as much detail as you want, and then iterate as you visually learn more about your intent ("Hmm, I guess I wanted a toggle button here!").

![](https://image.cubox.pro/cardImg/2tj51xh47lmtgyult9vcikno9k8hp3o2d8vomz9x4y6to51xfj.png?imageMogr2/quality/90/ignore-error/1)

#### Revision variants

When you create or iterate on a spark, you can optionally request a set of variants. This will generate 3-6 different versions of your request, each with subtle yet meaningful deviations. And since you might know you want a feature, but not quite know how it should look or behave, it can be helpful to get ideas that inform and expand on your thinking. Like an AI thought partner!

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Ftoolchain%2Fvariants.png&valid=true) *Asking for variants on an ambiguous revision ("Make the UI look really silly")*

#### Automatic history

As you iterate on a spark, every revision is automatically saved and can be restored in a single click. This allows you to explore ideas (and variants) without worrying about losing any progress. And more importantly, without requiring you to manage version control yourself. This enables a sort of "curiosity-driven development", where you can have an idea, and then try it out, without any fear of negative consequences (e.g. messing up your app).

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Ftoolchain%2Fhistory.png&valid=true)

From a collaboration perspective, history is also compelling because it provides a form of "semantic view source" whenever someone shares a spark with you. While creating GitHub Spark, we found that we'd naturally share new ideas with each other, and then immediately look at the history to see how they made it. It's almost like being able to peek into the minds of others, and see their serialized thought process.

#### Model selection

When you create or revise a spark, you can choose from one of four AI models: Claude Sonnet 3.5, GPT-4o, o1-preview, and o1-mini. This is neat because it allows you to try an idea, and if you don't get what you expected, you can undo and try again with an entirely different model. Additionally, the history tracks which model you used for each revision, which allows you to see how your sparks evolve over time.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Ftoolchain%2Fmodels-dashboard.png&valid=true)

*Selecting a model when creating a new spark*

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Ftoolchain%2Fmodels-revision.png&valid=true)

*Selecting a model when revising an existing spark*

### Managed runtime environment

We refer to GitHub Spark as an "app centric" tool (vs. a "code centric" tool). Not because it doesn't allow you to see or edit the code (it does!), but because it's designed for creating apps that are meant to be seen, felt, and used---as opposed to simply generating code, and then expecting you to do something with it (build, deploy, provision a database, etc.).

And it enables this by complimenting its toolchain with a managed runtime environment, that is built around four core capabilities:

1. Deployment-free hosting
2. Themable design system
3. Persistent data storage
4. Integrated model prompting

#### Deployment-free hosting

When you create or revise a spark, the changes are automatically deployed, and can be run and installed on your desktop, tablet, or mobile device (via a PWA). In this sense, GitHub Spark is kind of like a micro app cloud, which collapses the act of creating, deploying, and using software into a single gesture: expressing your ideas through natural language 🚀

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Fdashboard.png&valid=true)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Fmobile-app.png&valid=true)

*Viewing your dashboard of sparks and then opening one on your phone*

#### Themable design system

To ensure that your apps look and feel nice, GitHub Spark includes a set of built-in UI components, and a themable design system. So whenever you create a new app, things like form controls, layout, and icons should seem polished out-of-the-box. And if you want to tweak anything further, you can use the theme editor to change the default accent color, border radius, app spacing, and color theme (light/dark).

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Ftheme-before.png&valid=true)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Ftheme-after.png&valid=true)

*Before and after modifying the theme properties of a spark*

#### Persistent data storage

Whether you're making a todo list, a gardening planner, or a tic-tac-toe game, most interesting apps need to store data. And the GitHub Spark runtime has you covered, by providing a managed key-value store, and automatically knowing when to use it. Additionally, GitHub Spark provides a data editor, which lets you easily see and edit the data your spark is using. That way you have full control over any state, but without needing to worry about any of the details.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Fdata.png&valid=true)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Fdata-edit.png&valid=true)

*Viewing the data that a spark is storing, and then editing a specific key/value*

#### Integrated model prompting

The GitHub Spark runtime is integrated with [GitHub Models](https://docs.github.com/en/github-models), and allows you to add generative AI features to your sparks, without any knowledge of LLMs (e.g. summarizing a document, generating stories for a children's bedtime app). Additionally, it provides a prompt editor, which lets you see the prompts that GitHub Spark generates, and enables you to tweak them if needed---without needing to edit any code.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Fprompts.png&valid=true)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fgithubnext.com%2Fassets%2Fprojects%2Fgithub-spark%2Fruntime%2Fprompts-edit.png&valid=true)

*Viewing the AI prompts that your spark is using, and then editing one manually*

Phew! That was a lot. But in order for GitHub Spark to enable the aspiration we have (reducing the cost of app creation to zero), we felt like this toolchain and runtime were absolutely necessary. And we think that's users are going to love the way it feels 🥰

### What's next?

As a technical preview, GitHub Spark is still very early, and has a loooong list of TODOs. But over the next few months, we're looking forward to admitting users off the waitlist, and iterating closely with them [every week](https://gh.io/spark-changelog). So if you're interested in taking this journey with us, then check out the [FAQ](https://gh.io/spark-faq) and then join in on the fun over at the GitHub Next [Discord server](https://gh.io/next-discord) 👋

That said, if you're curious about what things are top of mind, you can expect to see us exploring into the following directions:

1. Expanding the collaboration modalities (e.g. a public gallery, allowing users to perform a semantic merge of changes that someone made in a fork of their spark, multi-player)
2. Expanding the editor surface (e.g. providing an "x-ray mode" that allows summarizing and adjusting precise behaviors of the app)
3. Expanding the runtime environment (e.g. more built-in components, better integration with 3rd party services, enabling file storage and vector search).
4. Lots of other cool stuff that we haven't even thought of!

[githubnext.com](https://githubnext.com/projects/github-spark)

