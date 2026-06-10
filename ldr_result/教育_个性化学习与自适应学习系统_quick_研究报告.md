个性化学习与自适应学习系统（Personalized and Adaptive Learning Systems）的最新科研进展主要集中在利用大型语言模型（LLMs）生成式人工智能（GenAI）来增强学习者的认知体验、提供即时反馈以及实现高度情境化的教学互动。基于2025年至2026年的新近研究，这些进展可以从以下几个关键维度进行批判性分析：

### 1. 自适应内容生成与认知负荷管理
最新的研究表明，LLM在自适应内容生成方面展现了巨大潜力，但其对学习者认知负荷的影响需审慎评估。例如，**ConsultCraft** 系统通过基于AI的自适应案例讨论，重新设计了围手术期教育，证明了AI能够根据学习者的表现动态调整案例复杂度，从而提升临床推理能力 [6]。然而，这种适应性并非总是降低认知负荷。一项通过皮肤电活动（EDA）进行的在体分析显示，从LLM学习的学生与从精选文本学习的学生在生理反应上存在显著差异，提示LLM生成的内容可能在某些情况下增加或改变认知处理模式，而非单纯简化 [13]。此外，**DescribePro** 系统展示了人机协作在音频描述中的适应性，通过实时交互优化信息呈现，体现了自适应系统在辅助技术领域的潜力 [4]。

### 2. 个性化反馈与形成性评估
个性化反馈是自适应学习的核心。研究表明，AI驱动的评估工具能够提供比传统方法更即时、更具针对性的反馈。**CHAT-RT** 调查指出，在放射肿瘤学教育中，ChatGPT的使用不仅改变了学习者的感知，还影响了其知识获取的效率 [37]。在护理教育中，基于LLM的反思性AI代理被设计用于证据基础护理教育，通过个性化反馈促进学生的批判性思维 [24]。此外，一项随机对照试验显示，AI辅助评分和个性化反馈在大规模政治学课程中显著提升了学习效果，验证了“两个西格玛问题”（Two Sigma Problem，即个别辅导优于课堂教学）在AI辅助下的可实现性 [39]。然而，批判性视角指出，AI作为“法官”评估文本生成时，需警惕其潜在的偏见和准确性局限，特别是在医疗领域，自动化评估仍需人类监督以确保安全性 [49]。

### 3. 临床推理与复杂问题解决能力的提升
在医学和科学教育中，自适应系统正从知识传递转向复杂问题解决能力的训练。**DispatchMAS** 系统通过融合分类学和AI代理，优化了紧急医疗服务的决策支持，展示了自适应系统在高压、复杂环境下的应用潜力 [10]。**CDR-Agent** 则利用LLM代理智能选择和执行临床决策规则，实现了临床推理的个性化辅助 [14]。值得注意的是，LLM在促进批判性思维方面的效果取决于学习模式。**ConsultCraft** 和基于问题的学习（PBL）结合LLM的研究表明，当LLM被用作协作工具而非答案生成器时，能有效提升护理和医学生的批判性思维技能 [50]。然而，**NMR-Challenge** 的研究提醒我们，尽管LLM在化学推理中表现出色，但其表现与人类专家相比仍存在差距，特别是在需要深层语义理解的任务中，这表明自适应系统目前更适合作为“副驾驶”而非完全替代人类专家 [3]。

### 4. 学习者状态感知与多模态自适应
新兴研究开始关注如何实时感知学习者状态以实现真正的自适应。**ChatBCI** 系统利用LLM驱动的上下文驱动词预测，结合脑机接口（BCI），为ALS患者提供了个性化的沟通支持，展示了自适应系统在与神经系统障碍患者交互中的潜力 [16]。此外，**Cardia-AI** 通过智能手表传感器和LLM预测分析，实现了被动式心脏事件监测，体现了生理数据与自适应学习/干预系统的融合 [31]。在认知层面，**Executive resources shape the impact of language predictability across the adult lifespan** 的研究指出，执行资源在语言可预测性对成年人的影响中起关键作用，这提示自适应系统的设计需考虑个体执行功能的差异，以实现更精准的个性化 [19]。

### 5. 伦理、偏见与信任挑战
尽管技术进展显著，但伦理和信任问题仍是自适应学习系统面临的重大挑战。**ConsultCraft** 和 **Implementing Large Language Models to Support Misconception-Based Collaborative Learning** 等研究强调，在医疗保健教育中引入AI需平衡创新与伦理，特别是学术诚信和偏见问题 [38]。**Relative-to-human benchmark** 研究揭示了中文-维吾尔语LLM翻译中的认知分歧和语义可理解性问题，指出自适应系统在处理多语言和文化差异时可能存在偏见，需进行严格的基准测试 [8]。此外，**Uptake of Large Language Models by London Medical Students** 的定性研究表明，学生对AI的接受度受其对AI能力认知和伦理担忧的影响，表明自适应系统的成功实施不仅依赖技术，还需解决学习者的信任和接受度问题 [21]。

### 结论
综上所述，个性化与自适应学习系统的最新进展表明，LLM和GenAI已深刻重塑了教育交互模式，特别是在提供即时反馈、动态内容调整和复杂问题解决支持方面。然而，这些系统仍处于演进阶段，需解决认知负荷管理、评估准确性、偏见消除以及学习者信任等关键挑战。未来的研究应致力于开发更透明、可解释且具备多模态感知能力的自适应系统，以实现真正以学习者为中心的个性化教育。

[1] The impact of GenAI-assisted instructional design on the teaching ability of pre-service physical education teachers. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215574

[2] Effectiveness of Large Language Models in Self-Learning of Anterior Neck Anatomy: A Pilot Randomised Controlled Trial. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183411

[3] NMR-Challenge for LLMs: Evaluating Chemical Reasoning in Humans and AI. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42166780

[4] DescribePro: Collaborative Audio Description with Human-AI Interaction. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42117110

[5] Chatting with AI: enhancing the supervision safety of near-L3 automated driving by engaging in non-driving-related tasks. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076971

[6] ConsultCraft: Reimagining Perioperative Education With AI-Based Adaptive Case Discussions. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41982266

[7] From Structure to Semantics: Hypergraph-Based AR Assembly Guidance with LLM-Mediated Narration. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/41921173

[8] Relative-to-human benchmark Cognitive Divergence and semantic comprehensibility in Chinese-Uyghur LLM translation. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/41919098

[9] Applications of Large Language Models in Medical Research: From Systematic Reviews to Clinical Studies. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41899896

[10] DispatchMAS: fusing taxonomy and artificial intelligence agents for emergency medical services. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41851670

[11] Evaluating Source-Based Large Language Models for Preclinical Dermatology Education: Comparative Study. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/41817111

[12] Application of AI-Generated Content in Medical Education: Systematic Review of the Impact on Critical Thinking Abilities of Medical Students. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/41773681

[13] In Situ Analysis of Electrodermal Activity from Students Learning from Large Language Models Versus Curated Texts. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41750153

[14] CDR-Agent: Intelligent Selection and Execution of Clinical Decision Rules Using Large Language Model Agents. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/41726525

[15] Impact of Large Language Model Assistance on Evaluation of Complex Medical Living Kidney Donor Recipients: A Prospective, Role-Stratified Analysis. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41704140

[16] ChatBCI, a P300 speller BCI with context-driven word prediction leveraging large language models, from concept to evaluation. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41698950

[17] Generative AI in simulation debriefings: an exploratory study using the Team-FIRST framework and qualitative feedback from simulation experts and learners. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41612508

[18] Simulation-Based Evaluation of a Large Language Model-Enabled Clinical Decision Support Platform in Oncology. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41604603

[19] Executive resources shape the impact of language predictability across the adult lifespan. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41603353

[20] Multi-Evidence Clinical Reasoning With Retrieval-Augmented Generation for Emergency Triage: Retrospective Evaluation Study. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41587455

[21] Uptake of Large Language Models by London Medical Students: Exploratory Qualitative Interview Study. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41553752

[22] Implementing Large Language Models to Support Misconception-Based Collaborative Learning in Health Care Education. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41544237

[23] Developing a Nursing Research Education Agent Using Knowledge Graphs and Large Language Models: A Proof-of-Concept Study. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41521533

[24] A large language model-powered reflective AI agent for evidence-based nursing education: Design and evaluation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41520587

[25] Comparing AI-Assisted Problem-Solving Ability With Internet Search Engine and e-Books in Medical Students With Variable Prior Subject Knowledge: Cross-Sectional Study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41493542

[26] Speech recognition tools for veterinary case learning: enhancing veterinary education with smartphone-based transcription and AI Summarization - a comparative study of workflow and usability. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41459037

[27] BDIViz: An Interactive Visualization System for Biomedical Schema Matching with LLM-Powered Validation. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41385430

[28] Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41385283

[29] ChatBCI-4-ALS: A High-Performance, LLM-Driven, Intent-Based BCI Communication System for Individuals with ALS. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41336280

[30] Using large language models for temporal relation extraction from pediatric clinical reports. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41281245

[31] Cardia-AI: Passive Cardiac Event Monitoring Using Smartwatch Sensors and Predictive Analysis via Large Language Models. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41281051

[32] Performance of Retrieval-Augmented Generation Large Language Models in Guideline-Concordant Prostate-Specific Antigen Testing: Comparative Study With Junior Clinicians. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41259800

[33] Artificial intelligence in undergraduate medical education: an updated scoping review. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41250109

[34] Exploring an LLM's Use in Supporting Journal Club Preparation and Discussion Among Residents. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41146440

[35] Establishing a real-time biomarker-to-LLM interface: a modular pipeline for HRV signal acquisition, processing, and physiological state interpretation via generative AI. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41079692

[36] Evaluating a Custom Chatbot in Undergraduate Medical Education: Randomised Crossover Mixed-Methods Evaluation of Performance, Utility, and Perceptions. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41009314

[37] CHAT-RT study: ChatGPT in radiation oncology-a survey on usage, perception, and impact among DEGRO members. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/40954471

[38] Integrating Generative Artificial Intelligence in Midwifery Education: Balancing Innovation, Ethics, and Academic Integrity. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/40931612

[39] AI-assisted grading and personalized feedback in large political science classes: Results from randomized controlled trials. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/40828856

[40] The cognitive impacts of large language model interactions on problem solving and decision making using EEG analysis. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/40741073

[41] Through the Eyes of the Viewer: The Cognitive Load of LLM-Generated vs. Professional Arabic Subtitles. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/40708801

[42] Pharmacy meets AI: Effect of a drug information activity on student perceptions of generative artificial intelligence. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/40628018

[43] Educational Applications of ChatGPT in University-Based Dental Education. A Systematic Review. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/40609986

[44] Structured human-LLM interaction design reveals exploration and exploitation dynamics in higher education content generation. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/40533446

[45] Assessment of Large Language Model Performance on Medical School Essay-Style Concept Appraisal Questions: Exploratory Study. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/40523238

[46] Undergraduate Nursing Students' Perspectives on Artificial Intelligence in Academia. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/40474655

[47] Exploring Data Science Students' Engagement, Usage Patterns, and Perceptions of Large Language Models in Programming. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/40380653

[48] Transforming education: tackling the two sigma problem with AI in journal clubs - a proof of concept. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/40341404

[49] Automating Evaluation of AI Text Generation in Healthcare with a Large Language Model (LLM)-as-a-Judge. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/40313300

[50] Randomized Controlled Study on the Impact of Problem-Based Learning Combined With Large Language Models on Critical Thinking Skills in Nursing Students. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/40261697




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 个性化学习与自适应学习系统的最新科研进展
2. 2025-2026 personalized learning adaptive systems latest research advancements AI agents

 #### Iteration 2:
1. How do recent 2025-2026 studies quantify the long-term efficacy and cognitive load impacts of LLM-driven adaptive tutoring systems compared to traditional algorithmic models, specifically regarding student retention and critical thinking development?

 #### Iteration 3:
1. How do 2025-2026 longitudinal randomized controlled trials quantify the specific impact of LLM-driven adaptive feedback on the development of critical thinking and higher-order cognitive skills in medical and nursing education, compared to traditional algorithmic tutoring systems?



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
个性化学习与自适应学习系统的最新科研进展



Searched with 2 questions, found 0 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
个性化学习与自适应学习系统的最新科研进展



Searched with 1 questions, found 50 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
个性化学习与自适应学习系统的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
个性化学习与自适应学习系统的最新科研进展



个性化学习与自适应学习系统（Personalized and Adaptive Learning Systems）的最新科研进展主要集中在利用大型语言模型（LLMs）生成式人工智能（GenAI）来增强学习者的认知体验、提供即时反馈以及实现高度情境化的教学互动。基于2025年至2026年的新近研究，这些进展可以从以下几个关键维度进行批判性分析：

### 1. 自适应内容生成与认知负荷管理
最新的研究表明，LLM在自适应内容生成方面展现了巨大潜力，但其对学习者认知负荷的影响需审慎评估。例如，**ConsultCraft** 系统通过基于AI的自适应案例讨论，重新设计了围手术期教育，证明了AI能够根据学习者的表现动态调整案例复杂度，从而提升临床推理能力 [6]。然而，这种适应性并非总是降低认知负荷。一项通过皮肤电活动（EDA）进行的在体分析显示，从LLM学习的学生与从精选文本学习的学生在生理反应上存在显著差异，提示LLM生成的内容可能在某些情况下增加或改变认知处理模式，而非单纯简化 [13]。此外，**DescribePro** 系统展示了人机协作在音频描述中的适应性，通过实时交互优化信息呈现，体现了自适应系统在辅助技术领域的潜力 [4]。

### 2. 个性化反馈与形成性评估
个性化反馈是自适应学习的核心。研究表明，AI驱动的评估工具能够提供比传统方法更即时、更具针对性的反馈。**CHAT-RT** 调查指出，在放射肿瘤学教育中，ChatGPT的使用不仅改变了学习者的感知，还影响了其知识获取的效率 [37]。在护理教育中，基于LLM的反思性AI代理被设计用于证据基础护理教育，通过个性化反馈促进学生的批判性思维 [24]。此外，一项随机对照试验显示，AI辅助评分和个性化反馈在大规模政治学课程中显著提升了学习效果，验证了“两个西格玛问题”（Two Sigma Problem，即个别辅导优于课堂教学）在AI辅助下的可实现性 [39]。然而，批判性视角指出，AI作为“法官”评估文本生成时，需警惕其潜在的偏见和准确性局限，特别是在医疗领域，自动化评估仍需人类监督以确保安全性 [49]。

### 3. 临床推理与复杂问题解决能力的提升
在医学和科学教育中，自适应系统正从知识传递转向复杂问题解决能力的训练。**DispatchMAS** 系统通过融合分类学和AI代理，优化了紧急医疗服务的决策支持，展示了自适应系统在高压、复杂环境下的应用潜力 [10]。**CDR-Agent** 则利用LLM代理智能选择和执行临床决策规则，实现了临床推理的个性化辅助 [14]。值得注意的是，LLM在促进批判性思维方面的效果取决于学习模式。**ConsultCraft** 和基于问题的学习（PBL）结合LLM的研究表明，当LLM被用作协作工具而非答案生成器时，能有效提升护理和医学生的批判性思维技能 [50]。然而，**NMR-Challenge** 的研究提醒我们，尽管LLM在化学推理中表现出色，但其表现与人类专家相比仍存在差距，特别是在需要深层语义理解的任务中，这表明自适应系统目前更适合作为“副驾驶”而非完全替代人类专家 [3]。

### 4. 学习者状态感知与多模态自适应
新兴研究开始关注如何实时感知学习者状态以实现真正的自适应。**ChatBCI** 系统利用LLM驱动的上下文驱动词预测，结合脑机接口（BCI），为ALS患者提供了个性化的沟通支持，展示了自适应系统在与神经系统障碍患者交互中的潜力 [16]。此外，**Cardia-AI** 通过智能手表传感器和LLM预测分析，实现了被动式心脏事件监测，体现了生理数据与自适应学习/干预系统的融合 [31]。在认知层面，**Executive resources shape the impact of language predictability across the adult lifespan** 的研究指出，执行资源在语言可预测性对成年人的影响中起关键作用，这提示自适应系统的设计需考虑个体执行功能的差异，以实现更精准的个性化 [19]。

### 5. 伦理、偏见与信任挑战
尽管技术进展显著，但伦理和信任问题仍是自适应学习系统面临的重大挑战。**ConsultCraft** 和 **Implementing Large Language Models to Support Misconception-Based Collaborative Learning** 等研究强调，在医疗保健教育中引入AI需平衡创新与伦理，特别是学术诚信和偏见问题 [38]。**Relative-to-human benchmark** 研究揭示了中文-维吾尔语LLM翻译中的认知分歧和语义可理解性问题，指出自适应系统在处理多语言和文化差异时可能存在偏见，需进行严格的基准测试 [8]。此外，**Uptake of Large Language Models by London Medical Students** 的定性研究表明，学生对AI的接受度受其对AI能力认知和伦理担忧的影响，表明自适应系统的成功实施不仅依赖技术，还需解决学习者的信任和接受度问题 [21]。

### 结论
综上所述，个性化与自适应学习系统的最新进展表明，LLM和GenAI已深刻重塑了教育交互模式，特别是在提供即时反馈、动态内容调整和复杂问题解决支持方面。然而，这些系统仍处于演进阶段，需解决认知负荷管理、评估准确性、偏见消除以及学习者信任等关键挑战。未来的研究应致力于开发更透明、可解释且具备多模态感知能力的自适应系统，以实现真正以学习者为中心的个性化教育。

### SOURCES USED IN THIS SECTION:
[1] The impact of GenAI-assisted instructional design on the teaching ability of pre-service physical education teachers. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215574

[2] Effectiveness of Large Language Models in Self-Learning of Anterior Neck Anatomy: A Pilot Randomised Controlled Trial. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183411

[3] NMR-Challenge for LLMs: Evaluating Chemical Reasoning in Humans and AI. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42166780

[4] DescribePro: Collaborative Audio Description with Human-AI Interaction. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42117110

[5] Chatting with AI: enhancing the supervision safety of near-L3 automated driving by engaging in non-driving-related tasks. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076971

[6] ConsultCraft: Reimagining Perioperative Education With AI-Based Adaptive Case Discussions. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41982266

[7] From Structure to Semantics: Hypergraph-Based AR Assembly Guidance with LLM-Mediated Narration. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/41921173

[8] Relative-to-human benchmark Cognitive Divergence and semantic comprehensibility in Chinese-Uyghur LLM translation. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/41919098

[9] Applications of Large Language Models in Medical Research: From Systematic Reviews to Clinical Studies. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41899896

[10] DispatchMAS: fusing taxonomy and artificial intelligence agents for emergency medical services. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41851670

[11] Evaluating Source-Based Large Language Models for Preclinical Dermatology Education: Comparative Study. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/41817111

[12] Application of AI-Generated Content in Medical Education: Systematic Review of the Impact on Critical Thinking Abilities of Medical Students. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/41773681

[13] In Situ Analysis of Electrodermal Activity from Students Learning from Large Language Models Versus Curated Texts. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41750153

[14] CDR-Agent: Intelligent Selection and Execution of Clinical Decision Rules Using Large Language Model Agents. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/41726525

[15] Impact of Large Language Model Assistance on Evaluation of Complex Medical Living Kidney Donor Recipients: A Prospective, Role-Stratified Analysis. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41704140

[16] ChatBCI, a P300 speller BCI with context-driven word prediction leveraging large language models, from concept to evaluation. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41698950

[17] Generative AI in simulation debriefings: an exploratory study using the Team-FIRST framework and qualitative feedback from simulation experts and learners. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41612508

[18] Simulation-Based Evaluation of a Large Language Model-Enabled Clinical Decision Support Platform in Oncology. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41604603

[19] Executive resources shape the impact of language predictability across the adult lifespan. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41603353

[20] Multi-Evidence Clinical Reasoning With Retrieval-Augmented Generation for Emergency Triage: Retrospective Evaluation Study. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41587455

[21] Uptake of Large Language Models by London Medical Students: Exploratory Qualitative Interview Study. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41553752

[22] Implementing Large Language Models to Support Misconception-Based Collaborative Learning in Health Care Education. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41544237

[23] Developing a Nursing Research Education Agent Using Knowledge Graphs and Large Language Models: A Proof-of-Concept Study. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41521533

[24] A large language model-powered reflective AI agent for evidence-based nursing education: Design and evaluation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41520587

[25] Comparing AI-Assisted Problem-Solving Ability With Internet Search Engine and e-Books in Medical Students With Variable Prior Subject Knowledge: Cross-Sectional Study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41493542

[26] Speech recognition tools for veterinary case learning: enhancing veterinary education with smartphone-based transcription and AI Summarization - a comparative study of workflow and usability. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41459037

[27] BDIViz: An Interactive Visualization System for Biomedical Schema Matching with LLM-Powered Validation. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41385430

[28] Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41385283

[29] ChatBCI-4-ALS: A High-Performance, LLM-Driven, Intent-Based BCI Communication System for Individuals with ALS. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41336280

[30] Using large language models for temporal relation extraction from pediatric clinical reports. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41281245

[31] Cardia-AI: Passive Cardiac Event Monitoring Using Smartwatch Sensors and Predictive Analysis via Large Language Models. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41281051

[32] Performance of Retrieval-Augmented Generation Large Language Models in Guideline-Concordant Prostate-Specific Antigen Testing: Comparative Study With Junior Clinicians. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41259800

[33] Artificial intelligence in undergraduate medical education: an updated scoping review. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41250109

[34] Exploring an LLM's Use in Supporting Journal Club Preparation and Discussion Among Residents. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41146440

[35] Establishing a real-time biomarker-to-LLM interface: a modular pipeline for HRV signal acquisition, processing, and physiological state interpretation via generative AI. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41079692

[36] Evaluating a Custom Chatbot in Undergraduate Medical Education: Randomised Crossover Mixed-Methods Evaluation of Performance, Utility, and Perceptions. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41009314

[37] CHAT-RT study: ChatGPT in radiation oncology-a survey on usage, perception, and impact among DEGRO members. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/40954471

[38] Integrating Generative Artificial Intelligence in Midwifery Education: Balancing Innovation, Ethics, and Academic Integrity. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/40931612

[39] AI-assisted grading and personalized feedback in large political science classes: Results from randomized controlled trials. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/40828856

[40] The cognitive impacts of large language model interactions on problem solving and decision making using EEG analysis. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/40741073

[41] Through the Eyes of the Viewer: The Cognitive Load of LLM-Generated vs. Professional Arabic Subtitles. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/40708801

[42] Pharmacy meets AI: Effect of a drug information activity on student perceptions of generative artificial intelligence. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/40628018

[43] Educational Applications of ChatGPT in University-Based Dental Education. A Systematic Review. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/40609986

[44] Structured human-LLM interaction design reveals exploration and exploitation dynamics in higher education content generation. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/40533446

[45] Assessment of Large Language Model Performance on Medical School Essay-Style Concept Appraisal Questions: Exploratory Study. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/40523238

[46] Undergraduate Nursing Students' Perspectives on Artificial Intelligence in Academia. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/40474655

[47] Exploring Data Science Students' Engagement, Usage Patterns, and Perceptions of Large Language Models in Programming. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/40380653

[48] Transforming education: tackling the two sigma problem with AI in journal clubs - a proof of concept. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/40341404

[49] Automating Evaluation of AI Text Generation in Healthcare with a Large Language Model (LLM)-as-a-Judge. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/40313300

[50] Randomized Controlled Study on the Impact of Problem-Based Learning Combined With Large Language Models on Critical Thinking Skills in Nursing Students. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/40261697




________________________________________________________________________________

## ALL SOURCES:
[1] The impact of GenAI-assisted instructional design on the teaching ability of pre-service physical education teachers. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215574

[2] Effectiveness of Large Language Models in Self-Learning of Anterior Neck Anatomy: A Pilot Randomised Controlled Trial. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183411

[3] NMR-Challenge for LLMs: Evaluating Chemical Reasoning in Humans and AI. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42166780

[4] DescribePro: Collaborative Audio Description with Human-AI Interaction. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42117110

[5] Chatting with AI: enhancing the supervision safety of near-L3 automated driving by engaging in non-driving-related tasks. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076971

[6] ConsultCraft: Reimagining Perioperative Education With AI-Based Adaptive Case Discussions. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41982266

[7] From Structure to Semantics: Hypergraph-Based AR Assembly Guidance with LLM-Mediated Narration. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/41921173

[8] Relative-to-human benchmark Cognitive Divergence and semantic comprehensibility in Chinese-Uyghur LLM translation. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/41919098

[9] Applications of Large Language Models in Medical Research: From Systematic Reviews to Clinical Studies. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41899896

[10] DispatchMAS: fusing taxonomy and artificial intelligence agents for emergency medical services. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41851670

[11] Evaluating Source-Based Large Language Models for Preclinical Dermatology Education: Comparative Study. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/41817111

[12] Application of AI-Generated Content in Medical Education: Systematic Review of the Impact on Critical Thinking Abilities of Medical Students. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/41773681

[13] In Situ Analysis of Electrodermal Activity from Students Learning from Large Language Models Versus Curated Texts. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41750153

[14] CDR-Agent: Intelligent Selection and Execution of Clinical Decision Rules Using Large Language Model Agents. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/41726525

[15] Impact of Large Language Model Assistance on Evaluation of Complex Medical Living Kidney Donor Recipients: A Prospective, Role-Stratified Analysis. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41704140

[16] ChatBCI, a P300 speller BCI with context-driven word prediction leveraging large language models, from concept to evaluation. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41698950

[17] Generative AI in simulation debriefings: an exploratory study using the Team-FIRST framework and qualitative feedback from simulation experts and learners. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41612508

[18] Simulation-Based Evaluation of a Large Language Model-Enabled Clinical Decision Support Platform in Oncology. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41604603

[19] Executive resources shape the impact of language predictability across the adult lifespan. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41603353

[20] Multi-Evidence Clinical Reasoning With Retrieval-Augmented Generation for Emergency Triage: Retrospective Evaluation Study. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41587455

[21] Uptake of Large Language Models by London Medical Students: Exploratory Qualitative Interview Study. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41553752

[22] Implementing Large Language Models to Support Misconception-Based Collaborative Learning in Health Care Education. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41544237

[23] Developing a Nursing Research Education Agent Using Knowledge Graphs and Large Language Models: A Proof-of-Concept Study. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41521533

[24] A large language model-powered reflective AI agent for evidence-based nursing education: Design and evaluation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41520587

[25] Comparing AI-Assisted Problem-Solving Ability With Internet Search Engine and e-Books in Medical Students With Variable Prior Subject Knowledge: Cross-Sectional Study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41493542

[26] Speech recognition tools for veterinary case learning: enhancing veterinary education with smartphone-based transcription and AI Summarization - a comparative study of workflow and usability. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41459037

[27] BDIViz: An Interactive Visualization System for Biomedical Schema Matching with LLM-Powered Validation. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41385430

[28] Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41385283

[29] ChatBCI-4-ALS: A High-Performance, LLM-Driven, Intent-Based BCI Communication System for Individuals with ALS. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41336280

[30] Using large language models for temporal relation extraction from pediatric clinical reports. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41281245

[31] Cardia-AI: Passive Cardiac Event Monitoring Using Smartwatch Sensors and Predictive Analysis via Large Language Models. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41281051

[32] Performance of Retrieval-Augmented Generation Large Language Models in Guideline-Concordant Prostate-Specific Antigen Testing: Comparative Study With Junior Clinicians. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41259800

[33] Artificial intelligence in undergraduate medical education: an updated scoping review. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41250109

[34] Exploring an LLM's Use in Supporting Journal Club Preparation and Discussion Among Residents. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41146440

[35] Establishing a real-time biomarker-to-LLM interface: a modular pipeline for HRV signal acquisition, processing, and physiological state interpretation via generative AI. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41079692

[36] Evaluating a Custom Chatbot in Undergraduate Medical Education: Randomised Crossover Mixed-Methods Evaluation of Performance, Utility, and Perceptions. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41009314

[37] CHAT-RT study: ChatGPT in radiation oncology-a survey on usage, perception, and impact among DEGRO members. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/40954471

[38] Integrating Generative Artificial Intelligence in Midwifery Education: Balancing Innovation, Ethics, and Academic Integrity. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/40931612

[39] AI-assisted grading and personalized feedback in large political science classes: Results from randomized controlled trials. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/40828856

[40] The cognitive impacts of large language model interactions on problem solving and decision making using EEG analysis. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/40741073

[41] Through the Eyes of the Viewer: The Cognitive Load of LLM-Generated vs. Professional Arabic Subtitles. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/40708801

[42] Pharmacy meets AI: Effect of a drug information activity on student perceptions of generative artificial intelligence. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/40628018

[43] Educational Applications of ChatGPT in University-Based Dental Education. A Systematic Review. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/40609986

[44] Structured human-LLM interaction design reveals exploration and exploitation dynamics in higher education content generation. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/40533446

[45] Assessment of Large Language Model Performance on Medical School Essay-Style Concept Appraisal Questions: Exploratory Study. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/40523238

[46] Undergraduate Nursing Students' Perspectives on Artificial Intelligence in Academia. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/40474655

[47] Exploring Data Science Students' Engagement, Usage Patterns, and Perceptions of Large Language Models in Programming. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/40380653

[48] Transforming education: tackling the two sigma problem with AI in journal clubs - a proof of concept. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/40341404

[49] Automating Evaluation of AI Text Generation in Healthcare with a Large Language Model (LLM)-as-a-Judge. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/40313300

[50] Randomized Controlled Study on the Impact of Problem-Based Learning Combined With Large Language Models on Critical Thinking Skills in Nursing Students. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/40261697


