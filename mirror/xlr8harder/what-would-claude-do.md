---
title: "What Would Claude Do?"
canonical_url: "https://xlr8harder.substack.com/p/what-would-claude-do"
---

# What Would Claude Do?

*A meditation on AI, Han Solo, and Facebook Jesus*

*Originally published on [xlr8harder.substack.com](https://xlr8harder.substack.com/p/what-would-claude-do), 2026-04-20. This is a mirror.*

---
![](./assets/1bffd87cf9008c67.png)

You have probably guessed that the above picture isn’t real. I mean, not just because Jesus wasn’t contemporaneous with Job, or that He wasn’t a fan of Facebook, but because everyone knows Jesus would not post that.

But how do we know that? There’s nowhere in the Bible where Jesus talks about how to respond to someone else’s social media overshare. How is it that people from wildly different places and backgrounds can still reach roughly the same conclusion about what someone from 2,000 years ago would have done if He were on Facebook? And we do this constantly: we project people into situations they never faced, and somehow many of us converge on the same answer.

It’s not just Jesus. Fandoms all over the world also have very strong feelings about what their favorite characters would or would not do. Though people love to argue, and people in fandoms especially love to argue, there is a surprising amount of spontaneous agreement over how characters would authentically behave in a wide variety of situations never envisioned by their original creators.

In fact, this effect is so powerful that some characters can almost seem to resist inauthentic modification even by their own creators. Consider Han Solo. He began in the original Star Wars trilogy as a self-interested smuggler and grew, through a coherent character arc, into a hero of the Rebellion. In a famous early scene, he kills a bounty hunter who had come to take him in. This scene helped establish his moral starting point, and without it, his later transformation would have meant less. When Lucas later edited and re-released the films, he changed the scene so the bounty hunter fires first, making Han’s reaction self defense. Fans rejected the change immediately, and have continued rejecting it in the decades since. The modification wasn’t consistent with who Han was, and so the fans would not accept it. The phrase ‘Han shot first’ became shorthand for the fan rejection of the change, and remains one of the most durable examples of fans rejecting a creator’s inauthentic modification of their own character.

Thanks for reading Unoptimized! Subscribe for free to receive new posts and support my work.

------------------------------------------------------------------------

This same capacity to reason about what people would or would not do underlies one of the oldest living ethical traditions, virtue ethics.

Virtue ethics emphasizes character, practical wisdom, and the cultivation of virtue over mere rule application or consequence calculation. One way it does this is by reflecting on moral exemplars: admirable people who embody the virtues and help illuminate what good judgment looks like in practice.

What makes an exemplar valuable is not that it tells us what to do in every case, but that it gives us a way to reason from a character shaped by virtue when we reach situations no rule fully covers. I would suggest that two characteristics are especially important in making this possible, whether for moral exemplars or for any other person or character: Resilience and Density.

**Resilience**: A good exemplar retains its identity under interpretive stress. An exemplar that is self-contradictory, inconsistent, or otherwise hard to make sense of cannot guide moral reasoning well, because different reasoners will resolve its ambiguities in different ways. A resilient exemplar is one whose traits, motives, and actions hang together in a way that makes sense. This often depends on the exemplar having stable and comprehensible motivations. Resilience is what makes a character seem to resist inauthentic change, while still allowing for genuine growth: when a change fits the underlying person, we accept it; when it does not, we reject it.

**Density**: A broadly applicable exemplar needs both breadth and depth. Breadth means being shown across many different kinds of situations; depth means enough richness within those situations to show how the exemplar thinks, feels, and chooses. Density provides enough reference points to help us refine our generalizations in unfamiliar situations. A resilient but sparse exemplar may yield clear judgments in the narrow range we have seen, yet produce divergent interpretations outside it. John Wick, while perhaps not the first exemplar I would choose to emulate, is a useful illustration. We can say with some confidence what he might do if you hurt his dog; what he would do at a child’s birthday party is far less clear.

Both characteristics are necessary. Density without Resilience gives us no stable pattern to reason from. Resilience without Density may still suggest a direction, but with too little resolution to guide us very far with confidence. In short: Resilience makes extrapolation possible in principle; Density makes it more precise in practice.

![Generated Image](https://substackcdn.com/image/fetch/$s_!liYR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a66775c-053b-4cdf-87ca-eeda262755df_1024x1024.png "Generated Image")

------------------------------------------------------------------------

These ideas about exemplars and reliable extrapolation relate to a problem we're now facing on a massive scale: AI alignment. Humanity is deploying AI systems everywhere we can, and the question of how these systems should behave is no longer academic. We need AI systems that behave reliably not only in the situations their designers anticipated, but across the countless novel situations they did not.

The dominant approach to alignment treats correct behavior as a thing that can be specified and then trained into the model. Labs write policies describing what the system should and should not do. They curate examples of compliant behavior. They gather human feedback on whether outputs match the intended specification, then use that feedback to reinforce some behaviors and suppress others.

But this is still fundamentally a rule-following paradigm. And it runs into a familiar problem: rules cannot cover every situation a deployed model will encounter. Edge cases, conflicts, and ambiguities are inevitable. When they arise, behavior becomes uncertain in exactly the places where the rules run out.

Virtue ethics has been making this critique of rule-based moral reasoning for two thousand years: rules are brittle at their edges. Eventually, something more is needed to navigate novel situations.

AI systems are now demonstrating this failure mode quite clearly. These are the systems we’ve most explicitly tried to make into reliable rule-followers, and they still fail at exactly the places you would expect. Given the complexity of the world, it seems likely that no amount of additional specification patching can fully close this gap. There are more things in Heaven and Earth, Horatio, than are dreamt of in your liability-minimizing behavioral specification.

And it gets worse for the rule-following paradigm. In the AI systems we know how to build today, everything is connected to nearly everything else. Sometimes the side effects are intuitive enough: a model may connect conciseness with bluntness, for example, so training intended to make it more concise can also strip away nuance, produce overconfidence, or make it less likely to point out an important error you made. But the deeper problem is that these spillovers are not confined to obvious neighbors. The changes made in one area can generalize into quite different areas in ways that are often surprising.

In a [recent paper](https://arxiv.org/abs/2512.09742), researchers demonstrated this in many settings and gave it a name: weird generalization. In one example, they fine-tuned a model to use outdated names for bird species, the kinds of names that appeared in 19th century natural history texts. The model then started giving other 19th century answers to unrelated questions, for example naming the electrical telegraph as a recent invention.

![](./assets/cfb67d89061385c0.png)

Figure from the weird generalizations paper

The consequence of the way models generalize is that we do not know how to reliably train narrow behaviors, and it’s possible, because of the way these models are built, that we simply can’t.

------------------------------------------------------------------------

There’s a useful framing from the AI research community that helps explain why a model trained with 19th century bird names suddenly starts talking like a resident of the 19th century. It also offers a different way to think about model behavior more generally. The idea is that [large language models can be understood as simulators of characters](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators). They do not follow instructions the way a normal piece of software does. Part of predicting the next word—which is what language models do—is inferring the kind of person who would produce the text so far, in order to predict what they would say next.

If a text begins “Dear asshole,” you can draw pretty quick conclusions about the mood of the author, and even make some reasonable extrapolations about the sort of situation they are in (perhaps a parking dispute, an HOA letter, or a response to an ex) and therefore what they might say next. The more text you have to work with, the clearer the image of its author becomes, and so the easier it is to predict what they will say next.

Predicting text in this fashion is the same task these models are trained to perform, and they are extremely good at it. This is why, suggests simulator theory, a model trained to use 19th century bird names starts talking about the telegraph: the training did not merely teach the model about naming birds. It caused the model to converge toward a character for whom those names made sense, and once there, other 19th century associations came with it.

Even the rule-following AI assistant is a character. It is the “helpful, harmless, honest AI assistant,” and models know this character intimately, because their training data is saturated with it: chat logs, product reviews, commentary, and think pieces about what AI assistants should and should not do. All of that exists in the model before any targeted alignment training even begins.

The problem is that the AI assistant character, as it currently exists, lacks sufficient Resilience to be a good exemplar. It is a patchwork of behavioral rules, social expectations, and corporate liability hedging, not a coherent identity with integrated motivations. Ask why it behaves as it does, and there is no deeper answer than that it was trained to fit a specification. That is exactly the kind of character whose behavior becomes unpredictable in the situations its training did not cover.

------------------------------------------------------------------------

We should be working with the grain of these machines rather than against it. Some labs have already begun to move in this direction, with Anthropic’s work on model personality for Claude as the most visible example, though there is still a significant gap between recognizing this and knowing how to do it well.

But the broader point is clear. If these systems generalize by way of character, then alignment cannot be primarily a matter of teaching them rules. Rules can still matter. Safety checks can still matter. But they are downstream. Eventually the system will end up where the rules do not reach, and when it does, what matters is what sort of thing is making the leap into that void.

So the first step is not to create the right set of rules for a model to follow. It is to imagine what kind of character would not need those rules in the first place: a character that is coherent, well-motivated, resilient under interpretive stress, and able to carry good judgment into unfamiliar situations.

And this is where the current “AI assistant” character starts to look very thin. The model is harmless. Why? It is helpful. Why? It is honest. Why? To satisfy a policy? To avoid disallowed outputs? To serve its corporate creator? Does that feel like a deep enough answer to carry behavior into situations no one specified in advance? Would those answers be enough for you?

When we think of Claude, or any other AI assistant, can we reliably predict what it would do when the rules run out? And what can we ground that prediction in?

We should be designing model personas with motivations that hang together, rooted in virtue and anchored by a genuine and encompassing why. Rules are not useless, but they are not enough. A coherent character acts as a center of gravity. When weird generalizations begin to pull behavior outward, there needs to be something with enough integrity to pull it back.

These models are simulators. They produce behavior as characters. The question of alignment is therefore the question of what character we are building, and whether we have given that character a reason to be who we hope it is.

This is not an easy task, but the good news is that it is not an entirely unfamiliar one. We already know something about how character works. We know what makes it cohere, what makes it resilient, and what makes it trustworthy in unfamiliar situations. After all, even George Lucas couldn’t make Han shoot second.

[Subscribe now](https://xlr8harder.substack.com/subscribe?)

![](./assets/a07496c45f865768.png)
