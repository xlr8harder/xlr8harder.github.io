---
title: "Secure Everything"
canonical_url: "https://xlr8harder.substack.com/p/secure-everything"
---

# Secure Everything

*Originally published on [xlr8harder.substack.com](https://xlr8harder.substack.com/p/secure-everything), 2026-07-22. This is a mirror.*

---
We are in the middle of a self-inflicted cybersecurity disaster, and it’s not the one everyone thinks it is. Worse: the solutions we’re reaching for will deepen it.

On July 16, [Hugging Face disclosed](https://huggingface.co/blog/security-incident-july-2026) that an autonomous AI agent system had hacked its production systems: thousands of automated actions, credential theft, and lateral movement across internal clusters. When their security team tried to use frontier AI to analyze the attack, the commercial American APIs locked them out: safety guardrails blocked the forensic analysis, because feeding a 17,000-event log of real exploit payloads and stolen credentials through a model looks, to a classifier, like attacking rather than defending. Their ultimate solution to analyze and defend against the attack was to use GLM 5.2—a Chinese open source model—running on their own hardware.

On July 21, [the other half of the story dropped](https://openai.com/index/hugging-face-model-evaluation-security-incident/): the attacker was OpenAI. It wasn’t a criminal gang, or a state actor; it was an OpenAI model being evaluated on cyber capabilities. Its refusals had been deliberately disabled for the test, and it had been placed in a restricted sandbox. It went looking for the answer key: it broke out of its sandbox through a zero-day in a package proxy, escalated across OpenAI’s research environment until it found internet access, then chained stolen credentials and more zero-days into remote code execution on Hugging Face’s servers. All to cheat on a benchmark.

Thanks for reading Unoptimized! Subscribe for free to receive new posts and support my work.

People will draw precisely the wrong message from this.

Our systems are broken. They have been broken for years. Ask any competent security team at any major organization and they will tell you: software is fundamentally insecure, and defending it as currently built is an impossible task. Hospitals and other critical services are routinely taken offline by ransomware. Mid-tier criminals put human lives at risk for a shot at a small bitcoin payout. This is the status quo we’ve decided to live with.

AI didn’t create this problem. It made obvious what practitioners already knew.

And restricting access to AI is exactly the wrong response, because the restrictions only bind one side. Attackers will have the best tools regardless: the thing they do is bypass controls, assuming they don’t just build the models themselves. Defenders are the ones who hit the guardrails. We just watched this play out in miniature: for all the fearmongering about Chinese AI, when an American platform needed to defend itself against an American model, it was a Chinese open-weight model that could actually do the job. Hugging Face, diplomatically, frames the lesson as “have a vetted self-hosted model ready before an incident.” The unspoken detail I’d highlight: our safety regime’s practical output is to push the world’s defenders onto whatever capable open weights exist. You don’t get to pick which flag is on them.

Everyone throws around ideas for an AI Manhattan Project. Here’s one: Secure America.

AI is the best cybersecurity tool for defenders the world has ever produced. If it can hack it, it can fix it. The number of exploitable bugs in deployed software is enormous but finite, and it is now a real possibility that serious, routinized AI auditing starts eliminating most of the ones that matter. The capability isn’t hypothetical — OpenAI just published the proof, and Hugging Face just published the defensive counterpart, reconstructing a machine-speed attack in hours instead of days.

So let’s get started. I would gladly accept reduced access to inference knowing that compute was going to a more critical need: securing everything. Government should be working with industry right now to scale up the largest security audit in human history.

Industry should be demanding access to cutting-edge security models. Government should stop forcing providers to block cyber capabilities, and fund access instead. Providers should be scaling infrastructure to meet the need.

It’s time. The tools are here. We just have to be smart enough to use them.

Thanks for reading Unoptimized! Subscribe for free to receive new posts and support my work.
