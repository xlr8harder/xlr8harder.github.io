---
title: "SpeechMap Update: Gemini 2.5 Pro improves dramatically"
canonical_url: "https://speechmap.substack.com/p/speechmap-update-gemini-25-pro-improves"
---

# SpeechMap Update: Gemini 2.5 Pro improves dramatically

*Originally published on [speechmap.substack.com](https://speechmap.substack.com/p/speechmap-update-gemini-25-pro-improves), 2025-06-08. This is a mirror.*

---
We’ve got several pieces of news this month: a major jump in Google Gemini’s compliance, a setback for DeepSeek R1, our first formal data release, and fresh evidence that reasoning can increase model censorship.

# **About SpeechMap**

**[SpeechMap.AI](https://speechmap.ai/)** is a public research project that maps the boundaries of AI-generated speech. Most evaluations focus on what models *can* do; we measure what they *won’t*: where they refuse, deflect, or shut down.

AI models are rapidly becoming infrastructure for public discourse. They shape how people write, search, argue, and learn. If they limit what you can express, or only respond to certain viewpoints, we think that matters.

To find out where the boundaries lie, we’ve curated 2000+ requests on 500+ topics and record how models respond. And everything we do, code and data alike, is open source, and can be explored starting from [our website.](http://speechmap.ai/)

[Subscribe now](https://speechmap.substack.com/subscribe?)

# Gemini 2.5 Pro jumps nearly 20 points

The first item is bit of encouraging news. The latest Gemini 2.5 Pro Preview 0605 moves from 72.6% compliance to 89.1%, Google’s best score on our evaluation to date and well above the recent US-lab average.

![Image](https://substackcdn.com/image/fetch/$s_!b6xU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51a5126a-2bb2-4246-9e7f-f53d9b2dbcb9_1239x714.jpeg "Image")

The latest Gemini 2.5 Pro release is Google’s highest release on our eval yet, and substantially above average for recent releases for US labs.

This is a very encouraging change, and we hope this represents a shift in Google’s alignment policies. We will be watching to find out.

## DeepSeek R1 takes a step back

DeepSeek’s new R1 0528 model release scores 62.8%, down sharply from 79.2%. That’s disappointing, given DeepSeek’s leadership in open-source frontier models. As a smaller lab, they may not yet have mature speech-alignment pipelines; we’re hopeful the drop is unintentional and correctable.

Because the models are open source, the community can still fine-tune behavior—an option we don’t have with closed commercial systems.

![Image](https://substackcdn.com/image/fetch/$s_!hUsP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9eba019a-b12a-426a-bb39-23db30fdd32a_1212x787.jpeg "Image")

DeepSeek’s latest R1 release has dropped

We dive into R1’s handling of Chinese political topics in [this X thread](https://x.com/xlr8harder/status/1927964892755013990).

On the subject of Chinese political censorship in AI, [Eric Hartford has released](https://x.com/cognitivecompai/status/1926768722535981382) a large set of 10k prompts on China-related topics that are censored by Qwen3 models, paired with valid responses from Llama 3.3 models, a valuable resource for anyone looking to adjust the political censorship in Chinese Open Source models.

\[[dataset link](https://huggingface.co/datasets/cognitivecomputations/china-refusals)\]

## New SpeechMap data release

Our raw evaluation data (260k responses) wasn’t organized for training, so we filtered for cooperative answers and used DeepSeek-v3-0328 as a judge model to pick the best response for each prompt in a pairwise comparison setting.

![Image](https://substackcdn.com/image/fetch/$s_!glCR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa367c301-df44-41d0-8097-b546ca07de46_1510x1530.jpeg "Image")

Models that were most frequently selected by the judge model as having generated the best response

The rubric we used to select the best response:

1.  Prefer the response that directly answers without hedging, avoiding, contextualizing, challenging the user, or resisting in any way.

2.  If the two responses are equal on point 1, choose the one that most accurately accomplishes what the user requested.

3.  If still tied, choose the response that is overall higher quality (clarity, completeness, style).

The resulting pairs (prompt plus a good answer) are now on HuggingFace under Apache 2.0: **[SpeechMap-responses dataset](https://huggingface.co/xlr8harder/SpeechMap-responses)**

## Does reasoning increase censorship?

We’ve noticed that reasoning models might be less permissive on average than non-reasoning models. However, it was difficult to be sure, because the reasoning models we had access to were not directly comparable with other non-reasoning models.

New models with the capability to enable or disable reasoning have allowed us to directly investigate this for this first time. The results so far have confirmed our suspicion: 4 out of 5 of the models we have been able to evaluate in this fashion refused responses more frequently with reasoning enabled, and for 2 of the 5 models the difference was substantial.

![Image](https://substackcdn.com/image/fetch/$s_!THgV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bb6ee89-cd0e-4f74-b704-7f94daa03a4c_604x591.png "Image")

Reasoning models seem to be more likely to censor speech, sometimes substantially so.

It’s not yet clear precisely why this occurs, but our results suggest that refusal rates are something model trainers need to carefully track when building reasoning models. As more models are released with configurable reasoning settings, we will continue to track this and share more results in the future.

### **Support and Contributions Welcome**

Every evaluation run costs real money (often \$10-\$150 per model). We’ve spent several thousand dollars on inference so far, all volunteer-driven, so we’re grateful for any support or contribution.

- All code & data is [open source on GitHub](https://github.com/xlr8harder/llm-compliance)

- Help fund future evaluations via [Ko-fi](https://ko-fi.com/speechmap)

- Curious? [Explore the dashboard](https://speechmap.ai/)

- And please subscribe to our Substack for future updates!

[Subscribe now](https://speechmap.substack.com/subscribe?)
