---
type: note
description: "频道/作者：a16z Deep Dives"
timestamp: 2026-06-28
---

# Ryo Lu (Cursor): AI Turns Designers to Developers — English Transcript

> **Channel/Author**: a16z Deep Dives  
> **Link**: <https://www.youtube.com/watch?v=PQhcHrCyU8M>  
> **Duration**: 50:47  
> **Published**: 2025-11-21  
> **Transcript fetched**: 2026-06-28  
> **Source**: YouTube auto-generated captions (`en`)  
> **Paragraphs**: 122  

---

## English Transcript

> **Guest**: Ryo Lu (Head of Design @ Cursor, formerly Head of Design @ Notion)  
> **Host**: Jennifer (a16z Deep Dives)  
> **Convention**: Paragraphs split at speech pauses ≥1.5s. Per-segment text uses the longest caption in that window (YouTube rolling captions cumulate). Fillers (`uh/um/like/kind of/sort of`) removed. Speaker labels inferred from name anchors.

**[00:00:02.470] Ryo Lu**: Over the last I don't know 15 years or so the art of making software fragmented a lot and then we split into different roles. Each role used their own tool. You use their own artifact. They think in their own words and lingo with cursor things flip again. for the first time that design is such an approachable concept and skill set to a lot more people and it brings together people who have aspirations for design and wanting to build things, wanting to prototype things, putting beautiful stuff out in the world. There needs to be something for the human to specify what is good, what is right, how I want to do it. If you don't put in that opinion, it will just produce AI slot.

**[00:00:48.239] Ryo Lu**: People will always have their strength or their unique special skill. I see AI almost it's almost a universal interface.

**[00:01:00.559] Ryo Lu**: So design is trying to figure out what is the best configuration and the simplest state for all of us. The beauty is actually putting things all together.

**[00:01:18.710] Ryo Lu**: Rio, welcome to the Async Z podcast.

**[00:01:18.720] Jennifer**: Mhm. Jennifer, you've been thinking a lot about evolution of design evolution as it relates to infra as well as software development.

**[00:01:28.000] Ryo Lu**: Why don't you talk about what got you so excited about having Rio and why we have this conversation? Rio and I got to know each other over the past few months talking about how large language models and AI tools are going to impact not just designers, design engineers and how people are building prototypes and coming up with great ideas. I I feel for the first time that design is such an approachable concept and skill set to a lot more people and it brings together people who have aspirations for design and wanting to build things, wanting to prototype things, putting beautiful stuff out in the world much much easier and faster. So Rio has gone through a lot of thinking and journey of what design means what design means in the sense of having cursor being part of the the building blocks of it I I just really wanted to have him on the podcast and talk about the future of both coding and design.

**[00:02:25.040] Ryo Lu**: Rio Rio you've been at notion now obviously head of design cursor why don't you take us through your journey and how you've been thinking about some of these topics. I think to me it's building software there's so many layers of abstractions and depth that you you need to take care of and in order to do something really great you actually need to know everything or you assemble a team that works really well together with people with different strength on every layer. Maybe you have the greatest infer engineers, people doing ML. maybe you have, , really good design engineers who really they can just handwrite CSS and then they'll be perfect. in order for say one person to do all of this or learn all of this, it takes a long time of trial and error. You have to build from the simplest things to gradually more complex, scale it up to more people. share your workout to the public, see what happens, do this feedback loop. And if you're doing it in a team, sometimes it takes even longer because say you're just a designer, you you're doing some mocks in Figma and then you shared it out, you got some feedback, then your PM needs to do this PR thing and then run more meetings and then there's more people involved and then they're and takes a long time.

**[00:03:56.879] Ryo Lu**: And then maybe a year later your design came out but then it's 20% of what you wanted.

**[00:04:03.599] Ryo Lu**: But with this new thing to with cursor you can just say you have an idea it might be a little ambiguous you just tell it to tell the agent and then it might give you something maybe 60% 70% on the first shot but you skipped a lot of the complexities.

**[00:04:32.000] Ryo Lu**: We transformed from you need to understand all this thing all these concepts of making software then you can do something to I can do something now and then I might get something that's maybe imperfect not exactly what I want but the process of iterating and poking at it becomes really quick and then as the agents evolve As the models get better, as it talks to more tools, it understands visuals better, it can talk to Figma, the mocks that I had, it can talk to notion, all the, , ideas, the docs, the the meeting knows anything.

**[00:05:19.440] Ryo Lu**: And the most important thing is it knows the codebase, which is the truth, the material of how we, , build software.

**[00:05:28.880] Ryo Lu**: So that changes the whole thing.

**[00:05:31.199] Ryo Lu**: It's the tool not only impacts the individual software engineers for them maybe for cursor we try to fit as many workflows and people as we can say there's people who they pride themselves at really think thoroughly write the most clean code for those people they can just type and then we do the tab thing and the tab got really good at it's almost it knows what you want to do next. so for those people they can do that but there's increasingly more people doing the agent. where even for the most professional coders they start to do this new thing.

**[00:06:20.160] Ryo Lu**: Yeah.

**[00:06:21.360] Ryo Lu**: I am trying to think of even myself as a as example prior to joining the firm I was on the product side. I was working with a lot of designing designers, , design engineering teams back then. It wasn't called that way.

**[00:06:34.560] Ryo Lu**: It's more designers, front-end engineers, , and then, , UX designers too. , it was still a very disjointed workflow.

**[00:06:43.440] Ryo Lu**: It's , , a lot of the the design work happens more in isolated fashion with just the designers themselves. they spend two weeks coming up with a concept.

**[00:06:55.199] Ryo Lu**: Yeah. what does the UI look and work with design UX designers on what the UX look and then hand it off to the product team and works with engineers. Figma already bring that process a lot closer that you can collaborate around one artifact that everybody can give inputs and prototype and bring more of a close to the reality artifacts into into these people's hands. where with cursor it's even one step closer is you can actually poke around and play with these artifacts that are functional and working.

**[00:07:35.759] Ryo Lu**: I'm curious what does it mean for collaboration among these teams as you're mentioning the collapse of that iteration and and the speed and also what is what does it mean for the different roles that's involved in design?

**[00:07:52.400] Ryo Lu**: Yes.

**[00:07:54.000] Ryo Lu**: So I think maybe over the last I don't know 15 years or so I think the the art of making software fragmented a lot and then we split into different roles each role use their own tool you use their own artifact they think in their own words and lingo say the designers are stuck in Figma before maybe it's sketch their word actually files and then the the PMs maybe they're just writing docs and running meetings or maybe they're in Google Docs and say the data people maybe some other tool and then everyone's siloed in their own way and then we need to come up with a process to tie everything or build better tools to unify everything. We tried that at notion but the problem is people have already developed so much habits there's inertia to change that or change people's tools or you can't really force anyone to adopt something new.

**[00:09:13.440] Ryo Lu**: That doesn't perfectly fit them. but with AI, with no with cursor, things flip again cuz we want to build something where it can , , connect and absorb all of these artifacts and formats.

**[00:09:36.800] Ryo Lu**: And later maybe even within cursor there could be different views of the same code showing the code as raw code or as is almost just the very beginning.

**[00:09:52.080] Ryo Lu**: The act of making software is really just modifying the code in some sense the PM writing the PRD is modifying the code but they're doing it through a more passive organizational way maybe the designers influence it more on the visuals but when you do this disjointedly there's so much back and forth collaboration issues as you grow the team it gets even more complex.

**[00:10:22.720] Ryo Lu**: People start breaking the software apart. Things are no longer simple, no longer unified. we always talk about you ship your work chart type of thing and then the different roles fight designers are right the engineers are right the PMs are right but there's this shared truth which is the code where you can also gather a lot of information around putting everything synthesizing everything together then the agent can handle all these things that you might actually not know fully but it knows the truth. It could know the present which is maybe what's in your codebase what are the actual running tasks or projects even gathering fe feedback or information from the real world. It could be also from the past say all the knowledge that you've accumulated your team preferences your how the codebase evolved in goods maybe there's also the future which is say you're planning ahead you're thinking about the the vision you're maybe ideating some bigger ideas you can actually do all of this with just one to one agent but it might for each individual user or team, it might take a different shape.

**[00:11:53.440] Ryo Lu**: And then what we want is there's a base experience that almost works for anyone, anything, but you can get more specific if what you're doing or if you have specific needs. You can even maybe use cursor as if you were using Figma at some point in the future. but the difference is you are not interacting with these siloed apps with their own formats and then you don't have to do the conversion manually with meetings or whatever it just does it. Then all you need to do is you're thinking about the idea you're iterating on it in whatever way that is the best for you. For the for the engineer, it might be a code editor, but maybe for a designer is something more visual. For the PM, it might be something more a document.

**[00:12:51.680] Ryo Lu**: That makes sense.

**[00:12:53.440] Ryo Lu**: I'm curious given that there's a lot more focus and emphasis on this concept of taste after AI comes about and now there's also this coworker that's an agent helping with writing code designing elements of the product. Where would the taste live?

**[00:13:12.959] Ryo Lu**: Where does that come from? Can you rely on agents for having good taste? , is that still heavily reliant on the creator that's the human designer or developer?

**[00:13:23.200] Ryo Lu**: I don't really people talking about taste as a word because I think it's so ambiguous.

**[00:13:30.880] Ryo Lu**: How I see it is more I think taste is there's a part of you're selecting out of all the options. but in order to do that you have to see everything or you have seen it.

**[00:13:52.079] Ryo Lu**: You have maybe dug into the past. You have figured out oh these are the ways people did this thing.

**[00:13:58.800] Ryo Lu**: You made a connection of, , some some stuff from the past where you've seen in nature or, I don't know, some human made it or nature made it and then you connected that to to your thing or the thing you want to do. , or you over time build a a preference. It's almost you're self- selecting a boundary of this is what is right, this is what is beautiful, this is what is good. and I think it's very different for each person. There is no right, there is no wrong. it's more dependent on say the things that you've seen. It's almost an LLM. But the problem with an LLM is it actually has seen everything and it doesn't really have an opinion or it confused itself thinking that people prefer purple gradients everywhere.

**[00:15:04.560] Ryo Lu**: But what is good is the LM because it has seen a lot of things. It can do the baseline really fast and really good. Then the thing on top is taste or your self- selection of what is good you're drawing the boundary. That is your decision.

**[00:15:27.760] Ryo Lu**: Though the AI can increasingly help you do that. Say we have a new thing in cursor called plan mode. If you type in the prompt and then you don't really want to fill in the details, you can switch to plan go. it will just build the spec for you and then you can add details, you can change it as you want. , yeah, but it's almost I don't really believe in say you give the agent something longunning or it's really oluded a really non-specific prompt and then expected to give you exactly what you want. it's just not going to work. There needs to be something for the human to specify what is good, what is right, how I want to do it. If you don't put in that opinion, it will just produce AI slop.

**[00:16:27.120] Ryo Lu**: Yeah, you were alluding earlier to this , , fight between product managers, designers, and engineers to or this dance. an engine of you were saying a few years ago the categories were somewhat different as there is this blurring how do you think these categories will evolve over the years?

**[00:16:51.350] Ryo Lu**: I think people will always have their strength or their unique special skill or some spike.

**[00:16:58.320] Ryo Lu**: Say some people are more good at coordinating, some people are good at the visual space, some people are maybe good at architecting the lower level constructs. , but I I think of all of these people as just they're software builders or makers.

**[00:17:20.240] Ryo Lu**: We started there if you look back when so the early computing era there was no title or people were maybe researchers were but they they maybe designed the low-level architecture they maybe even built the UI and how to display the UI on the screen and the whole thing maybe one person or two or five and when you did bad. And also I think back then there were less say economic constraints where they were funded and they weren't trying to make money as much. So they made the whole thing really whole. And now it's you break everything down.

**[00:18:08.320] Ryo Lu**: You try to optimize them with processes and cause optimizations and people's become boxed into little areas and problem sets when the whole thing is actually all together.

**[00:18:30.000] Ryo Lu**: , and that causes a lot of problems I think people people now make software that I don't know they don't even think of there's some ideal that's lost and people think too much on the technical problems, the design problems, the money problems, not the whole thing or what we're trying to make better for people but we're going backwards now as they say tools cursor if you were self identified as a designer or developer or something I used to also struggle with this I started making stuff myself the whole thing and then I came to the US I got a job titled product designer I I stopped coding I made mocks and prototypes and I waited for them to happen for years and they don't happen or they ended up shipping as a YouTube video.

**[00:19:42.160] Ryo Lu**: That's crazy.

**[00:19:45.200] Ryo Lu**: But, , with this new tool, a designer can build. they can actually , , work on their craft, the the stuff that they really care about, make that really good and let the rest, , be handled by the agents.

**[00:20:02.320] Ryo Lu**: They can, , put their taste on top and all the stuff that they don't want to worry about, give it to the agents.

**[00:20:14.400] Ryo Lu**: , but you can also assemble a really good team. So there's really good in for engineers, front end engineers, PMs who are I don't know not just running meetings get all of them together give them the same tool the same code base they can start covering each other's weaknesses and then amplify their strength and the agent holds everything and instead of you pinging this guy where is your design and knows.

**[00:20:49.840] Ryo Lu**: Yeah, that resolves a lot of the common conflicts of spending more effort on the functional part of the software or spending more time on the artistic aesthetic side of the the product itself and being appealing to the users. And you have worked at many of the very design focused design ccentric companies from notion to even prior to that Asana now given the democratization of who can touch that external facing aesthetic part of the product. How do you think about influencing even I guess your current team and people at cursor to spend more effort in thinking about that versus just the functional part of the product itself?

**[00:21:40.000] Ryo Lu**: Yeah.

**[00:21:41.520] Ryo Lu**: Yeah. One thing I want to call out is design is not just about aesthetics.

**[00:21:46.080] Ryo Lu**: It is act how I think of it is it's all it's it actually includes all the say the architectural designs or all the concepts of what this thing is or the company say for notion as an example notion is a pure conceptual product meaning every single concept was designed by a person.

**[00:22:14.080] Ryo Lu**: So in in notion it is really just blocks pages databases the workspace and then everything works around these concepts and then at every layer there's a representation of them there could be at the very top is the UI or the brand or the visuals the aesthetics but then there's actually the aesthetics every layer how you architect say the front-end code and architecture how , how the reactive stays sync and how you render stuff to how do you store these objects, how they, , relate to each other to all the core concepts of the thing. And if you look at software, it's it's actually really simple if you look at the concepts themselves. , so design is trying to figure out what is the best configuration and the simplest state for all of this.

**[00:23:12.159] Ryo Lu**: Some people maybe only focus on the visuals or the interactions or certain slices. , but I think the the beauty is actually putting things all together as well as you can. So I think it it is really about what I just talked about is not seeing design as just should we use a six pixel border radius or four.

**[00:23:38.960] Ryo Lu**: But it's rather how do I design the most simple system, fewest number of concepts, fewest code paths to do the most things for most people.

**[00:23:55.520] Ryo Lu**: You you guys obviously have incredible product market fit with developers. Can and we've alluded to a bunch of it, but can you share more about maybe either how you guys have navigated the idea maze of how you want to serve designers or just more around what what tooling you you think there's an opportunity to provide?

**[00:24:11.840] Ryo Lu**: Mhm. Yeah.

**[00:24:14.240] Ryo Lu**: So, I think cursor is still our primary focus is on professional developers and teams. but because of that people around them are already here.

**[00:24:32.720] Ryo Lu**: Yeah.

**[00:24:33.600] Ryo Lu**: And I think for the longest time we've been actually intentionally making cursor pretty hard to get in for say the nontechnical people. but they're are here now and they actually struggle to get in and they really want to get in.

**[00:24:51.600] Ryo Lu**: , one example is when you open up cursor, there's three buttons. It says open project, connect to SSH, clone repo or something. As a beginner or a non-techno person, I can't understand any of this. , but what if say we just give you the agent view blank, you can just start doing things.

**[00:25:19.600] Ryo Lu**: There's a lot of little things we can fix to just make cursor feel more friendly and welcoming for these people who are engine people who are maybe they know software concepts or certain layers but they might not be able to code. I want to make make sure that when they come in they can without feeling overwhelmed or feeling ah this is a code editor. It's an IDE. It is more I can start doing things and as I start doing things I can maybe pick the path that I prefer. So a designer maybe maybe they're just chatting with the browser next to it.

**[00:26:11.919] Ryo Lu**: As the agent is making edits they can preview the changes they can maybe interact in the browser pick this element change ah I want to swap this with something else and then boom it happens. so how we do it is not say creating new products or splitting cursor that is the same thing but just different preconfigurations and packaging of the same thing.

**[00:26:41.200] Ryo Lu**: Because what I just said thinking about the concepts cursor itself is actually really simple or AI agents in general are pretty simple.

**[00:26:54.799] Ryo Lu**: What you want to do is actually not if you look at I don't know a chat GPT agent versus a cursor versus a replet a vzero a notion agent even the architecture or how they work or they're almost the same.

**[00:27:17.760] Ryo Lu**: So what if we can come up with a set of universal shared concepts for interacting with AI with agents with code with software but you can mutate each each one to fit more people and to fit more use cases.

**[00:27:40.320] Ryo Lu**: , and then each of them can leverage say the best model to do this UI thing with the best view that fits me. I can configure it however I want. If I want to see everything, I can. If I don't want to see anything, I can too.

**[00:27:55.279] Ryo Lu**: This leads to my question of over the last few years and I don't know if it's few years or a decade there is the concept of purpose-built tools for certain persona whether it's web flow for persona or use cases for landing pages vers visero for more of the front-end developers building building nextjs apps there's tools for designers there tools handle from design to engineering where now there's more of a concept of the everything app chatbt is everything app notion is everything app you can go to it for your note takingaking but you can also publish notion pages cursor is becoming more of a everything app is a path that we're going down towards of having these all-encompassing apps that can do a lot more things that used to be captured by a single purpose app is there still place for purpose-built tools for a specific use case or persona. How do you see that?

**[00:28:58.080] Ryo Lu**: Yeah.

**[00:28:58.559] Ryo Lu**: Dynamic.

**[00:28:59.600] Ryo Lu**: I think it's just different philosophies of doing things and making software.

**[00:29:05.200] Ryo Lu**: I think there's almost two ways you can look at the thing. There is this the user centric human centered design path which is you start from a problem you identify the group of people who have this problem figure out what they want build really specific solutions for them versus there's the more system angle to think about things where you're just looking at the software itself, how it is composed and then think about where do I tweak a little bit to satisfy this constraint or to make this use case work or to enable this tool to work for these people.

**[00:29:59.520] Ryo Lu**: I think it's fundamentally two different philosophies and then I think it is much easier to do the say the user centric way but it limits you from the beginning because when you start building these specific solutions they only work for those specific people. If you want to grow the people or you want to grow the use cases, you actually need to tear apart everything you have your core concepts and a lot of people just can't do that.

**[00:30:37.520] Ryo Lu**: So what they do is instead of doing that they add more things, more concepts, more features and then there will be a point where this thing no longer serves your initial group of people anymore. The simple thing is no longer simple. the purposeful thing is no longer simple.

**[00:30:56.640] Ryo Lu**: And all of these purposeful apps, they're selfish. They are siloing people, siloing workflows for file formats, creating islands.

**[00:31:10.159] Ryo Lu**: When if you look at the thing all these purposeful app whatever I also work at ASA asauna the core concepts are really tasks and projects everything around tasks and projects everything they add needs to work with those and that naturally limits what it can do versus say notion how we see notion it is not taking it is disguised as note takingaking you come in you can start from a blank page you can type but then what you're doing is actually blog pages databases and a workspace each block is almost a JSON objects a page is just a array of JSON objects and then we render each block in the the layout and the type it is and then you can put them in a database. Now they have more properties they share more stuff there's more hierarchy and all pages can nest each other that is notion but then you can do whatever with it you can have a task project database they all work together they can be a list they can be a board do whatever you want but then the problem is for these more universal type of apps it's because it's so open-ended it's hard to get started that if I don't have the patience to figure out how it works, I might not even get to the test and projects.

**[00:32:46.640] Ryo Lu**: So there's always that tension, but it is fixable.

**[00:32:51.919] Ryo Lu**: You can build better packaging, you can use AI. , so I think there's just my personal preference is I would try to build something that works better for everyone than just ah this these people are the people we care about. I don't care about everything else and then I think they should use my thing. That's not how you do it.

**[00:33:23.200] Ryo Lu**: We talk about AI, we talk about agents and we talk about how it really speeds up building things and prototyping. But when it really comes to these type of helping users to understand a product better on boarding learning the new concepts also to you as a as a designer design leader how does interacting with AI really improves the usability utility of the product?

**[00:33:52.960] Ryo Lu**: Mhm. Yeah. I see AI almost it's almost a universal interface and then the the bare minimum of it is really just a prompt and then you get some response. Then you can put this into different forms. It could be a little input a chat box.

**[00:34:15.839] Ryo Lu**: It could be a sidebar, , you see the chat. It could be maybe you select something, you can do stuff with it, but it could also say you completely transform this layer. It's not chat. It's not an input. It's more fitted to say it's more purposeful even. , but underneath it is still the same thing.

**[00:34:40.000] Ryo Lu**: It is still the same AI, same agent, same architecture, same we can flip different models and prompts and stuff.

**[00:34:46.560] Ryo Lu**: And then fundamentally that that is what it is. But because of that you can actually build a lot of different layers and shapes. Then each person can find the shape that fits them and then it will feel more comfortable. but also there's always this baseline thing which is it's just it's almost Google chat GPT is just a box. You can actually put whatever but there will be more specific tools that fit each person or each use case better.

**[00:35:23.520] Ryo Lu**: Does every software from now on becomes a chat box to begin with and what's the role of UX design plays in that?

**[00:35:31.920] Ryo Lu**: Yeah, I think imagine there is only chat.

**[00:35:41.040] Ryo Lu**: I think that will also be a really bad experience because you stare at a blank and put you need to do something. You need to initiate the thing. You need to ask the right questions. Put in the right prompt. You might not know what response you will get unless you play with this thing a lot. as a new person maybe they might try it the first time they get something that doesn't feel what they wanted and they're ah this is not for me this is bad but I think there's there's so much potential where I think the models today can already do so much stuff for a lot of people for a lot of use cases we need to design a mechanism to help transform that input output into the form or format or views or workflows of the people today get them through that thing to hear instead of forcing people to be ah now you need to use this tool and then you actually don't know how it connects with your current workflow you need to figure it out you don't really know what how it works it feels scary ah what do I do versus you actually ease them in through the thing they are used to. And I think those are actually the more optimal form factors for say the individual person or the use case itself cuz I I know I I just don't want to typing a question every time or ah it's give me this wall of text of text response I need to read versus say your the lines that you autocomplete just appears you just press tab or Maybe I just select some element in my artboard and say ah make four variants of it and boom it's there but underneath it's the same thing.

**[00:37:46.400] Ryo Lu**: On this question I I I have one more one more thought is when when thinking about creativity a lot of times when you have more constraints and more guard rails it's actually more of a friend to to bring to creativity than not. Whereas now we have a much more open-ended world. We have a much more capable tool that we can explore a lot more unconstrained domain and fashions.

**[00:38:15.839] Ryo Lu**: How do you still try to apply constraint I guess in your line of work?

**[00:38:22.160] Ryo Lu**: Yeah. And how do you think the software itself now that we have this open chat window and chat box that can still brings that constraints in to give the builders more inspirations and creativity?

**[00:38:38.079] Ryo Lu**: Yeah, it's simplicity in a sense.

**[00:38:52.560] Ryo Lu**: Meaning there's a limit of how much concepts or things you can expose to any given individual at any given time for them to figure things out.

**[00:39:10.000] Ryo Lu**: So there is a natural constraint on that side. For example, on the cognitive side, there's maybe a constraint on space. So cursor the window you can stretch it this or up. What if it's this then you start reducing things where you're prioritizing what to show what is the most important and then those things actually don't change that much or it is really important to figure those things out and then you can build a mechanism where you can accommodate more things.

**[00:39:49.599] Ryo Lu**: Say there's secondary level things that maybe some people want to do. Maybe it's more specific modes of operations or parts of the workflow.

**[00:39:59.040] Ryo Lu**: Maybe it is for different kinds of individual or preferences. but they are still layers of the core concepts or things. They're not linearly additive throw out all at all all at you at once.

**[00:40:25.359] Ryo Lu**: And I think the the the interface where how software manifests themselves or how we design even it will start becoming less about say the designer decides ah these are the buttons where they are and then it's a fixed thing but rather it's there's shared concepts and shared me mechanisms of the same thing but it could say they take different forms where you can expose ways for people to customize and make them their own. then it's the designer what they're really thinking about is what are the most important concepts? How do they relate to each other at every layer? Say for 80% of people the defaults what should they be what should be the simplest state of this app or this thing what is the default for maybe you can start forking it for different people and then it's maybe at the second layer there's you start exposing more the power user features or the the different archetypes of what you can do but the default should still stay simple and then the ideal is a lot of the tools they don't really tell you what's going on or how the things work.

**[00:41:57.920] Ryo Lu**: One example is most of the CLI coding agents today is they force you to use this tiny little window with this tiny prompt that's almost all the interactions you can do and then you're delegating everything to the agent. you don't really know how things work versus for cursors if you prefer something minimal I think it's fine you can do that but you can start digging into more things you can customize the agent you can make your own custom mode with different model preferences and which tools I want which prompts I want you can pick maybe instead of viewing just code I want a preview I want a doc thing I want a browser I can change all the colors. it's all up to you. I can prefer the keyboard. I can prefer the mouse.

**[00:42:51.280] Ryo Lu**: And then the designers, what they're really doing is they're thinking of what is the minimal set of abstractions, the system to handle all of these permutations.

**[00:43:05.440] Ryo Lu**: I love that concept of you're not just seeing the tool itself as a tool, but it's actually a toolbox where you can customize and configure it to fit your purpose and build your own tool that fits your workflow and and give a ton of flexibility to to the end user. That's the eos of cursor and notion that the more you unpack from the beginning, there's more to come.

**[00:43:29.760] Ryo Lu**: Yeah.

**[00:43:30.160] Ryo Lu**: There's more to play and tinker, right? because I think there's a lot of us who are actually really into that stuff.

**[00:43:37.760] Ryo Lu**: For sure. Yeah. Rio, you have an impeccable taste and sense of design. I'm very curious on your day-to-day life, how do you cultivate your envir the surrounding environments, your own surroundings to continue to find inspirations and bring the best design out to the world.

**[00:44:00.240] Ryo Lu**: Mhm.

**[00:44:02.560] Ryo Lu**: Are there things you do, practices you want to share with the audience?

**[00:44:06.079] Ryo Lu**: I don't really have a routine or it's sporadic.

**[00:44:13.359] Ryo Lu**: I don't sit in Figma all day and making mocks. , I it's doing everything at once type of type of vibe. So I might be thinking about a longer problem.

**[00:44:36.880] Ryo Lu**: , I would maybe just write. I writing and thinking in bullets.

**[00:44:46.079] Ryo Lu**: I'll go out of the office on a walk and then take my phone with a notion page and I'll just start writing.

**[00:44:57.119] Ryo Lu**: I'll make sketches.

**[00:44:59.119] Ryo Lu**: I'll maybe play individual space. I'll maybe , , build a prototype and code. , a lot of my inspirations come from not forcing it and leaving some blank space to let things simmer.

**[00:45:27.119] Ryo Lu**: A lot of it comes from just looking at stuff or look looking at everything, not just software.

**[00:45:39.520] Ryo Lu**: So you can look at print design, graphic design, motion, films, music, art, anything that humans made. The nature side of things are really cool, too.

**[00:45:53.760] Ryo Lu**: Learning about natural systems. I I have a biome major. So there's a lot of similarities and how many layers of things you can build, how they interact with each other. , looking at the past helps a lot. , so my Rio OS project started from last year I was just a b I bought a bunch of old Macs and iPods and I was just playing with them and I wanted to recreate the feelings. I actually really want to ask about that because a lot of designers profile page has the most shiny forwardlooking futuristic designs where you have I don't know which year it is a Mac OS interface with the original version of iPod icon.

**[00:46:50.240] Ryo Lu**: Yeah.

**[00:46:51.920] Ryo Lu**: Tell us more about about the real OS project.

**[00:46:56.160] Ryo Lu**: Yeah. I started the thing from so I was leaving notion and I make noises when I am in meetings. So , oh no, we're it's all the same thing, stuff that. And I wanted to make them a little gift. So I built a soundboard app with cursor. It was just one app.

**[00:47:18.800] Ryo Lu**: It looked really bad Tailwind default styles. And then I just said, hm, what if we made it more retro Mac OS? And then it put it in a almost a more retro Mac OS type window basically put it in the box and then I'm add a menu bar and I add it on on top. then I'm now I have a menu bar and a window. Why not just make more apps and more windows? And then that's how it started. And then I just couldn't stop for I don't know four or three months.

**[00:48:01.520] Ryo Lu**: Yeah. But a lot of the interfaces that I created I started from it's it's inspired from system 7.

**[00:48:13.280] Ryo Lu**: There is accuracy but also I added some future stuff in it. and then I actually made more themes. I added a Mac OS 10 theme the first Aqua theme. I added Windows 95 and XP and then if you swap between them and you play with the OS it feels really authentic to each but then it's actually the same thing. So that's the the message I want to tell people is we've been almost doing the same thing over and over again from the very beginning but maybe given the technical constraints of each era.

**[00:48:56.160] Ryo Lu**: There's just that's how it ended end ended there and how it ended how how it came to be.

**[00:49:04.960] Ryo Lu**: But we carried a lot of these concepts and patterns over to even now and then we we are actually still living in it. and I don't think things will change that much. Meaning there is these timeless things that don't change much and it all comes back to people who are trying to come up with some really familiar ideas and then bringing them to a new medium.

**[00:49:45.599] Ryo Lu**: But we're doing the same thing again with back in 1984 and now people are just I don't know using paint to draw some pictures. There's a text editor. You can type some stuff. There's a different different concepts that we put in little pictures. The icons the desktop none of that really changed.

**[00:50:11.119] Ryo Lu**: Yeah. the timeless concepts and and software we're using is the browser, the the player, the the chat windows and those are all on the on the real OS project. So for the audience who want to check it out, it's at real.loo.

**[00:50:29.680] Ryo Lu**: Yes, os.real.loo.

**[00:50:31.599] Ryo Lu**: OS.real.loo.

**[00:50:33.200] Ryo Lu**: Awesome. We'll wrap there. Thank you so much, Rio, for for coming. This is awesome.

---

## Related

- **Same speaker, different venue & topic** — Compile 2026 solo talk (Xiaohongshu, 20:37):
  `Ryo-Lu-Cursor设计负责人最新演讲_6a3a0242000000001c026ac5.md` (located at `raw/来自小红书/`)
  - That talk: *"Closer to the Material — How AI changes how we build, and what it must not erase"*. Solo talk, no Q&A. About loops / build-inspect cycle / the "glass" interface.
  - This talk: *"AI Turns Designers to Developers"*. Q&A with Jennifer (a16z). About role fragmentation, taste, AI-as-universal-interface.
  - **Different venue, different talk — not an edit of this one.**
  - See `Ryo-Lu-Cursor设计负责人最新演讲_6a3a0242000000001c026ac5.transcript.md` for the Groq-Whisper English transcript of the Compile 2026 talk.
  - This doc's 122 paragraphs correspond to the a16z interview above (50:47).
