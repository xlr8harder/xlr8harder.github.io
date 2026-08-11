---
title: "AI and Math in 2026: a non-mathematician's read"
canonical_url: "https://xlr8harder.substack.com/p/ai-and-math-in-2026-a-non-mathematicians"
---

# AI and Math in 2026: a non-mathematician's read

*Originally published on [xlr8harder.substack.com](https://xlr8harder.substack.com/p/ai-and-math-in-2026-a-non-mathematicians), 2026-07-23. This is a mirror.*

---
I’m not a mathematician, so calibrate accordingly, but I am very familiar with the strengths and weaknesses of AI, and have read a lot of mathematician commentary on recent AI math results. This is my shot at a synthesis: the math results are both significant and overhyped (this should be a familiar shape by now.) Real progress, yes. Math nearly conquered, no.

The thing that gets lost in the discourse is that AI models have a different profile of mathematical strengths and weaknesses than humans do. They’re not a clearly worse or better mathematician—they’re a differently-shaped one.

### Where they have an edge:

*Low opportunity cost.* Human mathematicians have limited time and careers that demand meaningful results. That means there’s probably a lot of low-hanging fruit that has not been picked—not because it’s too hard, but because nobody with the right skills could justify the attention. I expect a lot of near-term AI results will be of this type.

*Breadth.* Models know a lot about a lot of subfields, and sometimes carrying a technique between subfields unlocks something. They still do less of this than you’d hope, but I suspect some of their easy wins will come from noticing connections of exactly this kind.

### Where they’re still behind:

Serious formalization work and long proofs. An example here will help illustrate. Mathlib is a huge community-built library of mathematics written in Lean, a language where every proof is checked by a computer. Nothing gets in unless the machine verifies every step. Doomslide on X points out that current LLMs can’t reconstruct even the undergrad-curriculum parts of mathlib when you take away the intermediate building blocks.

In the replies to Doomslide’s post, **[Sebastian Griego](https://x.com/sebngriego)** decided to experiment with this and ran a test with a version of the Hahn-Banach theorem. I’m, of course, not familiar, so I had to read up. Hahn-Banach is a major workhorse theorem of analysis, and the intuition is something like this: if you have a well-behaved rule defined on part of a space, you can always extend it to the whole space without breaking the constraints it started with. Simple to state, but the standard proof is a multi-layer construction that stacks several intermediate results on top of each other. That layered structure makes it a useful test case.

And the headline result was clear: the model went 8/8 when the finished theorem was available to use, and 0/14 one-shot when it had to rebuild the missing chain of intermediate results itself. “A cliff, not a curve,” as Sebastian put it.

This is a small test case, and better harnesses or more compute might get past it, but I think it is at least directionally indicative. This is where models are still struggling.

### So why are the labs focused here?

A point I keep writing about is that the number one bottleneck in model training right now is finding a way to cheaply measure success. You can watch this struggle play out across the AI-for-science and medical AI literature: models can do powerful things, but extracting reliable signal from their output is still hard. With a cheap success signal, you can hillclimb. Without one, your best move is to invent a cheap proxy to measure (which is often more easily said than done), or scale up human feedback (which is very hard when you need experts and consistent judgment.)

Code and math have unusually legible success signals: the proof checks or it doesn’t, the tests pass or they don’t. Techniques refined against those signals can then be deployed elsewhere—either to squeeze maximum value out of the expensive signals you do have, or at scale once you’ve built a cheap proxy for some other problem you care about.

And there’s a second bet layered on top of that one: that the reasoning itself generalizes. The hope is that a model trained to hold together a long chain of deduction, where any wrong step leads to failure, doesn’t just become a better theorem prover, but becomes a better reasoner more generally, in every domain. How much this actually happens is still an open question, but it’s clearly part of why labs will pour resources into a domain most of their users will never touch.

That’s the real story, I think. Math is the rare domain where the training loop closes, where progress is measurable rather than debatable, and where labs are betting the capability won’t stay confined.

Thanks for reading Unoptimized! Subscribe for free to receive new posts and support my work.
