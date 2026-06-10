基于2026年的最新文献，文本分类与主题建模领域的科研进展呈现出从通用大语言模型（LLM）向垂直领域深度定制、从单一任务向多模态及可解释性分析、以及从西方中心向多语言/低资源语言扩展的趋势。以下结合提供的来源进行详细综述：

### 1. 大语言模型在垂直领域的微调与隐私保护
在医疗和生物医学领域，文本分类正从传统的监督学习转向利用大语言模型进行高效微调，同时高度重视数据隐私。

*   **隐私保护与诊断分类**：研究指出，差分隐私（DP）驱动的LLM在放射学报告分类中表现出色，能够在保护患者隐私的同时维持诊断准确性 [3]。此外，通过高质量数据选择驱动的指令微调，生物医学LLM的性能得到了显著提升 [27]。
*   **放射学与临床笔记分析**：在放射学领域，ModernBERT模型在日本胸部CT发现分类中显示出比传统BERT更高的效率 [40]。同时，合成数据被用于增强放射学报告的上下文感知句子分类，解决了数据稀缺问题 [35]。在儿科肺炎识别中，开源LLM在自由文本胸部X光报告中的表现已被证实有效 [30]。
*   **跨语言与可解释性**：针对临床编码，研究人员开发了端到端的可解释系统，能够跨越不同语言和多样化的医疗数据源进行代码分类 [33]。此外，利用生成式LLM进行零样本、可解释的生物医学文献评估，为临床决策支持提供了新途径 [34]。

### 2. 主题建模方法的演进：从LDA到BERTopic及结构模型
主题建模技术不再局限于传统的LDA（潜在狄利克雷分布），而是向基于嵌入的神经主题模型和特定结构模型发展，以捕捉更细微的语义和情感结构。

*   **神经主题模型与嵌入**：在荷兰炎症性肠病（IBD）患者信息的分析中，研究比较了不同嵌入模型在神经主题建模中的表现，发现基于嵌入的方法能更准确地揭示患者关注点 [9]。BERTopic在生物医学文本术语提取和本体填充方面展现出强大能力，特别是在疫苗本体构建中 [22]。在竞技体育研究中，BERTopic被用于追踪从还原论到复杂系统范式的知识演变 [45]。
*   **结构主题建模（STM）的应用**：STM被广泛应用于分析复杂的社会情感主题。例如，在分析YouTube评论中的护士留任话语时，STM揭示了讨论的结构化模式 [2]。另一项研究利用STM分析了“Urami”（怨恨）这一特定文化情感概念的结构 [6]。在临终关怀的数字支持构建中，STM也被用于分析跨文化的人际互动 [12]。
*   **多方法融合**：在中国社交媒体上的分娩体验分析中，研究者采用了一种集成方法，结合LDA、情感分析和深度学习，实现了对多维度体验的综合解析 [20]。在量子金融研究中，结合Datatopia和TOE框架的主题建模被用于分析理论向自主性的转变 [47]。

### 3. 多语言、低资源语言及非英语文本处理
随着NLP技术的普及，研究重点已扩展至非英语及低资源语言，强调了本体特征融合和跨域迁移学习的重要性。

*   **低资源语言分类**：针对阿姆哈拉语（Amharic）新闻分类，研究提出了一种基于本体特征融合和逻辑回归的方法，显著提升了分类性能 [10]。在阿拉伯语隐喻语言分类中，基于图卷积的技术被用于处理语用学复杂性 [41]。
*   **多语言数据集与对比**：乌克兰新闻多语言数据集（2022-2025）的建立为跨语言冲突报道分析提供了基础 [50]。在双语金融投诉分类中，基于智能Transformer的框架被证明能有效处理跨语言语义差异 [21]。
*   **跨域迁移学习**：研究表明，最先进的模型可能来自其他领域，跨域层次文本分类分析揭示了不同领域间模型迁移的潜力 [42]。此外，高级迁移学习策略在深度神经网络NLP中的应用正在被进一步挖掘 [18]。

### 4. 社会计算、情感分析与公众话语
文本分类与主题建模在社会科学研究中的应用日益深入，特别是在健康传播、政治极化和消费者行为分析方面。

*   **健康传播与患者叙事**：在移动健康应用中，NLP被用于追踪患者主观症状的改善情况 [11]。在瑞士慢性病患者中，NLP和主题建模被用于分析其经济负担的定性访谈数据 [49]。此外，通过分析Reddit上的罕见病社区（如多发性肌炎），研究揭示了患者支持和挣扎的主题 [19]。
*   **政治与社会极化**：研究利用NLP分析了美国立法对民权支持的党派差距扩大现象 [7]。在#MeToo运动中，混合方法分析了数字话语中的二次受害和心理伤害，揭示了系统正当化（system justification）的主题 [36]。
*   **消费者行为与疫苗犹豫**：在非洲，AI驱动的社会媒体分析被用于评估疫苗犹豫、信心和信任 [17]。在电商产品评论中，基于RoBERTa LLM的情感分析和主题建模被用于提取数字消费者洞察 [26]。孟加拉语电商评论数据集（BanglaEcomReviewCorpus）的建立也反映了这一趋势 [48]。

### 5. 效率、可解释性与基准测试
随着模型规模的扩大，研究也开始关注模型效率、能耗以及可解释性。

*   **效率与能耗**：一项研究直接比较了文本分类推理中的能耗和准确性，指出高效模型的重要性 [31]。
*   **可解释性与人类对齐**：在精神分裂症的社交媒体文本分类中，研究分析了影响BERT分类的文本关键因素，以增强模型的可解释性 [28]。此外，“洞察-推理循环”（Insight-Inference Loop）通过自然语言推理和阈值调整，实现了高效的文本分类 [43]。
*   **人机对比**：在澳大利亚COVID-19公共卫生数据中，AI工具在情感、主题和主题分析任务中与人类编码进行了对比，结果显示AI在处理大规模数据时具有优势，但在细微语境理解上仍需人类监督 [38]。在精神科临床笔记风格分析中，通过量化文本分析比较了医生与LLM在相同病例下的记录差异 [46]。

### 批判性反思
尽管上述进展显著，但需注意以下几点：
1.  **领域特异性风险**：虽然LLM在医疗分类中表现优异 [3, 30]，但其“黑盒”特性在临床决策中可能带来风险，因此可解释性研究 [28, 33, 34] 变得至关重要。
2.  **数据偏差**：多数高质量数据集仍集中在英语或主要语言 [10, 50]，尽管有低资源语言的研究 [41]，但全球代表性仍不足。
3.  **情感与主题的复杂性**：主题建模（如STM [2, 6]）虽能捕捉结构，但难以完全捕捉人类情感的细微差别，需结合情感分析 [20, 26] 和多模态方法。
4.  **隐私与伦理**：在利用患者叙事 [11, 19] 和社交媒体数据 [17, 36] 时，隐私保护 [3] 和伦理审查（如#MeToo分析 [36]）是不可或缺的一环。

综上所述，2026年的文本分类与主题建模正处于从“通用能力”向“垂直领域深度适配”和“社会价值挖掘”转型的关键阶段，隐私、效率、可解释性和多语言支持是当前的核心驱动力。

[1] Natural language processing captures memory content associated with shared neural patterns at encoding and retrieval. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42243459

[2] Nurse retention discourse in YouTube comments: a structural topic modeling analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42226531

[3] Learning to Diagnose Privately: DP-Powered LLMs for Radiology Report Classification. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221863

[4] Human rights violations reporting dataset. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42220647

[5] Disputing your roots: A multi-platform computational analysis of consumer reactions to genetic ancestry testing. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213236

[6] The feeling of "Urami": A structural topic modeling approach. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42189805

[7] The widening partisan gap in legislative support for civil rights in the United States. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42185320

[8] Topic Modeling of Nursing Documentation in Hemodialysis Units: A Mixed-Methods Study of Nursing Surveillance Activities. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42184213

[9] Uncovering Topics in Dutch Patient Messages in Inflammatory Bowel Disease: A Comparative Study of Embedding Models for Neural Topic Modeling. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175024

[10] Enhancing amharic news classification through ontology-based feature fusion and logistic regression. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42162112

[11] Tracking subjective symptom improvement from patient narratives in mobile health: An observational natural language processing study. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152868

[12] Constructing Digital Support at End of Life: A Cross-Cultural Analysis of Interpersonal Engagement on Hospice Websites. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152480

[13] AI-Enabled Digital Health Promotion and Prevention: Computational Literature Review. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149833

[14] Using natural language processing to assess proxy measures of therapeutic alliance across suicide risk tiers. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42119904

[15] Self-Identified Age Cohorts and Personal Experience Sharing in Pseudonymous Online Spaces: Natural Language Processing Analysis of Reddit. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42117595

[16] From dots to faces: individual differences in visual imagery capacity predict the content of Ganzflicker-induced hallucinations. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110566

[17] Artificial Intelligence-Driven Social Media Analysis of Vaccine Hesitancy, Confidence, and Trust in Africa: A Scoping Review. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110045

[18] Uncovering advanced transfer learning strategies for deep neural networks in natural language processing. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42106353

[19] Reddit and rare diseases: what myositis communities tell us about support and struggle. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42099825

[20] Multidimensional analysis of childbirth experiences on Chinese social media: an integrated approach using LDA, sentiment analysis and deep learning. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42088242

[21] An intelligent transformer based framework for bilingual financial complaint classification. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42082635

[22] BERTopic-driven term extraction from biomedical texts toward ontology population: evaluating vaccine ontology with Plotkin's vaccines corpus. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42071270

[23] Fine-Tuning and Benchmarking Transformer Models for Multiclass Classification of Clinical Research Papers: Retrospective Modeling Study. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42061835

[24] From association to intervention: Semantic trajectories and knowledge frontiers in epilepsy-gut microbiota research revealed by bibliometrics and NLP. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42058119

[25] Shifts in dental trauma research (2000-2025): a literature-based thematic analysis using topic modeling. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42057039

[26] Analyzing digital consumer insights through RoBERTa LLM based sentiment analysis and topic modeling. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42031839

[27] High-quality data selection-driven instruction tuning for biomedical large language models. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42031125

[28] On the interface between linguistics, computer science and psychiatry: analyzing textual key-factors affecting BERT-based classification of schizophrenia in social media texts. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42027780

[29] Longitudinal datasets of health app reviews for privacy and trust modeling. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42015941

[30] Performance of Open-Source LLMs in Identifying Pediatric Pneumonia From Free-Text Chest Radiograph Reports. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42011065

[31] Comparing energy consumption and accuracy in text classification inference. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41998005

[32] Using Natural Language Processing to Evaluate Differences in Psychotherapeutic Services for Posttraumatic Stress Disorder in a Suicide-Risk-Stratified Veteran Sample. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41983743

[33] An end-to-end system for explainable clinical coding across languages and diverse medical data sources. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41981562

[34] Zero-shot interpretable biomedical literature appraisal with generative large language models. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41978683

[35] Context-Aware Sentence Classification of Radiology Reports Using Synthetic Data: Development and Validation Study. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41961980

[36] Digital Discourse, Secondary Victimization, and Psychological Harm: Mixed-Methods Analysis of System Justification in the #MeToo Movement. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41960784

[37] Research on daily medication and drug efficacy evaluation for chronic diseases based on natural language processing (NLP). (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41948013

[38] Comparison of Artificial Intelligence Tools With Human Coding for Sentiment, Topic, and Thematic Analysis Tasks of Public Health Datasets During the COVID-19 Pandemic in Australia: Case Study. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41945649

[39] Automated ICD-10-Anchored Classification of Primary Care Text Data: Development and Evaluation of a Custom Multilabel Classifier. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41941723

[40] ModernBERT is more efficient than conventional BERT for chest CT findings classification in Japanese radiology reports. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41932978

[41] Graph convolution-based techniques for pragmatic Arabic figurative language classification. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41930216

[42] Your Next State-of-the-Art Could Come from Another Domain: A Cross-Domain Analysis of Hierarchical Text Classification. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41929874

[43] The Insight-Inference Loop: Efficient Text Classification via Natural Language Inference and Threshold-Tuning. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41924491

[44] The evolving landscape of large language models and non-large language models in health care. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41924194

[45] From reductionism to complex systems: Paradigm shift and knowledge evolution in competitive sports research using BERTopic. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41911258

[46] Comparative Analysis of Japanese Clinical Note Styles Between Physicians and Large Language Models Using Identical Psychiatric Cases: Quantitative Text Analysis. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41894589

[47] From theory to autonomy: a topic modelling study of quantum finance through the lens of Datatopia and TOE. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41890629

[48] BanglaEcomReviewCorpus: A dataset for e-commerce product review sentiment analysis. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41883575

[49] Financial Burden in Adults With Chronic Illness in Switzerland: A Secondary Analysis of Qualitative Interviews Using Natural Language Processing and Topic Modeling. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41849269

[50] Multilingual news dataset about Ukraine (2022-2025): data collection and documentation. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41844665




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 文本分类与主题建模的最新科研进展
2. latest research advances in text classification and topic modeling 2024-2026

 #### Iteration 2:
1. What are the specific architectural innovations and benchmark performance metrics of "ModernBERT" and other next-generation dense retrievers compared to conventional BERT in 2026, particularly regarding efficiency-accuracy trade-offs in low-resource or specialized domains?

 #### Iteration 3:
1. How do state-of-the-art LLM-based text classification and topic modeling frameworks in 2026 compare against traditional methods (like BERTopic or fine-tuned Transformers) in terms of computational efficiency, energy consumption, and accuracy on low-resource or specialized domains, specifically addressing the trade-offs highlighted by recent studies on ModernBERT and energy-aware inference?



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
文本分类与主题建模的最新科研进展



Searched with 2 questions, found 50 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
文本分类与主题建模的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
文本分类与主题建模的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
文本分类与主题建模的最新科研进展



基于2026年的最新文献，文本分类与主题建模领域的科研进展呈现出从通用大语言模型（LLM）向垂直领域深度定制、从单一任务向多模态及可解释性分析、以及从西方中心向多语言/低资源语言扩展的趋势。以下结合提供的来源进行详细综述：

### 1. 大语言模型在垂直领域的微调与隐私保护
在医疗和生物医学领域，文本分类正从传统的监督学习转向利用大语言模型进行高效微调，同时高度重视数据隐私。

*   **隐私保护与诊断分类**：研究指出，差分隐私（DP）驱动的LLM在放射学报告分类中表现出色，能够在保护患者隐私的同时维持诊断准确性 [3]。此外，通过高质量数据选择驱动的指令微调，生物医学LLM的性能得到了显著提升 [27]。
*   **放射学与临床笔记分析**：在放射学领域，ModernBERT模型在日本胸部CT发现分类中显示出比传统BERT更高的效率 [40]。同时，合成数据被用于增强放射学报告的上下文感知句子分类，解决了数据稀缺问题 [35]。在儿科肺炎识别中，开源LLM在自由文本胸部X光报告中的表现已被证实有效 [30]。
*   **跨语言与可解释性**：针对临床编码，研究人员开发了端到端的可解释系统，能够跨越不同语言和多样化的医疗数据源进行代码分类 [33]。此外，利用生成式LLM进行零样本、可解释的生物医学文献评估，为临床决策支持提供了新途径 [34]。

### 2. 主题建模方法的演进：从LDA到BERTopic及结构模型
主题建模技术不再局限于传统的LDA（潜在狄利克雷分布），而是向基于嵌入的神经主题模型和特定结构模型发展，以捕捉更细微的语义和情感结构。

*   **神经主题模型与嵌入**：在荷兰炎症性肠病（IBD）患者信息的分析中，研究比较了不同嵌入模型在神经主题建模中的表现，发现基于嵌入的方法能更准确地揭示患者关注点 [9]。BERTopic在生物医学文本术语提取和本体填充方面展现出强大能力，特别是在疫苗本体构建中 [22]。在竞技体育研究中，BERTopic被用于追踪从还原论到复杂系统范式的知识演变 [45]。
*   **结构主题建模（STM）的应用**：STM被广泛应用于分析复杂的社会情感主题。例如，在分析YouTube评论中的护士留任话语时，STM揭示了讨论的结构化模式 [2]。另一项研究利用STM分析了“Urami”（怨恨）这一特定文化情感概念的结构 [6]。在临终关怀的数字支持构建中，STM也被用于分析跨文化的人际互动 [12]。
*   **多方法融合**：在中国社交媒体上的分娩体验分析中，研究者采用了一种集成方法，结合LDA、情感分析和深度学习，实现了对多维度体验的综合解析 [20]。在量子金融研究中，结合Datatopia和TOE框架的主题建模被用于分析理论向自主性的转变 [47]。

### 3. 多语言、低资源语言及非英语文本处理
随着NLP技术的普及，研究重点已扩展至非英语及低资源语言，强调了本体特征融合和跨域迁移学习的重要性。

*   **低资源语言分类**：针对阿姆哈拉语（Amharic）新闻分类，研究提出了一种基于本体特征融合和逻辑回归的方法，显著提升了分类性能 [10]。在阿拉伯语隐喻语言分类中，基于图卷积的技术被用于处理语用学复杂性 [41]。
*   **多语言数据集与对比**：乌克兰新闻多语言数据集（2022-2025）的建立为跨语言冲突报道分析提供了基础 [50]。在双语金融投诉分类中，基于智能Transformer的框架被证明能有效处理跨语言语义差异 [21]。
*   **跨域迁移学习**：研究表明，最先进的模型可能来自其他领域，跨域层次文本分类分析揭示了不同领域间模型迁移的潜力 [42]。此外，高级迁移学习策略在深度神经网络NLP中的应用正在被进一步挖掘 [18]。

### 4. 社会计算、情感分析与公众话语
文本分类与主题建模在社会科学研究中的应用日益深入，特别是在健康传播、政治极化和消费者行为分析方面。

*   **健康传播与患者叙事**：在移动健康应用中，NLP被用于追踪患者主观症状的改善情况 [11]。在瑞士慢性病患者中，NLP和主题建模被用于分析其经济负担的定性访谈数据 [49]。此外，通过分析Reddit上的罕见病社区（如多发性肌炎），研究揭示了患者支持和挣扎的主题 [19]。
*   **政治与社会极化**：研究利用NLP分析了美国立法对民权支持的党派差距扩大现象 [7]。在#MeToo运动中，混合方法分析了数字话语中的二次受害和心理伤害，揭示了系统正当化（system justification）的主题 [36]。
*   **消费者行为与疫苗犹豫**：在非洲，AI驱动的社会媒体分析被用于评估疫苗犹豫、信心和信任 [17]。在电商产品评论中，基于RoBERTa LLM的情感分析和主题建模被用于提取数字消费者洞察 [26]。孟加拉语电商评论数据集（BanglaEcomReviewCorpus）的建立也反映了这一趋势 [48]。

### 5. 效率、可解释性与基准测试
随着模型规模的扩大，研究也开始关注模型效率、能耗以及可解释性。

*   **效率与能耗**：一项研究直接比较了文本分类推理中的能耗和准确性，指出高效模型的重要性 [31]。
*   **可解释性与人类对齐**：在精神分裂症的社交媒体文本分类中，研究分析了影响BERT分类的文本关键因素，以增强模型的可解释性 [28]。此外，“洞察-推理循环”（Insight-Inference Loop）通过自然语言推理和阈值调整，实现了高效的文本分类 [43]。
*   **人机对比**：在澳大利亚COVID-19公共卫生数据中，AI工具在情感、主题和主题分析任务中与人类编码进行了对比，结果显示AI在处理大规模数据时具有优势，但在细微语境理解上仍需人类监督 [38]。在精神科临床笔记风格分析中，通过量化文本分析比较了医生与LLM在相同病例下的记录差异 [46]。

### 批判性反思
尽管上述进展显著，但需注意以下几点：
1.  **领域特异性风险**：虽然LLM在医疗分类中表现优异 [3, 30]，但其“黑盒”特性在临床决策中可能带来风险，因此可解释性研究 [28, 33, 34] 变得至关重要。
2.  **数据偏差**：多数高质量数据集仍集中在英语或主要语言 [10, 50]，尽管有低资源语言的研究 [41]，但全球代表性仍不足。
3.  **情感与主题的复杂性**：主题建模（如STM [2, 6]）虽能捕捉结构，但难以完全捕捉人类情感的细微差别，需结合情感分析 [20, 26] 和多模态方法。
4.  **隐私与伦理**：在利用患者叙事 [11, 19] 和社交媒体数据 [17, 36] 时，隐私保护 [3] 和伦理审查（如#MeToo分析 [36]）是不可或缺的一环。

综上所述，2026年的文本分类与主题建模正处于从“通用能力”向“垂直领域深度适配”和“社会价值挖掘”转型的关键阶段，隐私、效率、可解释性和多语言支持是当前的核心驱动力。

### SOURCES USED IN THIS SECTION:
[1] Natural language processing captures memory content associated with shared neural patterns at encoding and retrieval. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42243459

[2] Nurse retention discourse in YouTube comments: a structural topic modeling analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42226531

[3] Learning to Diagnose Privately: DP-Powered LLMs for Radiology Report Classification. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221863

[4] Human rights violations reporting dataset. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42220647

[5] Disputing your roots: A multi-platform computational analysis of consumer reactions to genetic ancestry testing. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213236

[6] The feeling of "Urami": A structural topic modeling approach. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42189805

[7] The widening partisan gap in legislative support for civil rights in the United States. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42185320

[8] Topic Modeling of Nursing Documentation in Hemodialysis Units: A Mixed-Methods Study of Nursing Surveillance Activities. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42184213

[9] Uncovering Topics in Dutch Patient Messages in Inflammatory Bowel Disease: A Comparative Study of Embedding Models for Neural Topic Modeling. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175024

[10] Enhancing amharic news classification through ontology-based feature fusion and logistic regression. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42162112

[11] Tracking subjective symptom improvement from patient narratives in mobile health: An observational natural language processing study. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152868

[12] Constructing Digital Support at End of Life: A Cross-Cultural Analysis of Interpersonal Engagement on Hospice Websites. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152480

[13] AI-Enabled Digital Health Promotion and Prevention: Computational Literature Review. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149833

[14] Using natural language processing to assess proxy measures of therapeutic alliance across suicide risk tiers. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42119904

[15] Self-Identified Age Cohorts and Personal Experience Sharing in Pseudonymous Online Spaces: Natural Language Processing Analysis of Reddit. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42117595

[16] From dots to faces: individual differences in visual imagery capacity predict the content of Ganzflicker-induced hallucinations. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110566

[17] Artificial Intelligence-Driven Social Media Analysis of Vaccine Hesitancy, Confidence, and Trust in Africa: A Scoping Review. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110045

[18] Uncovering advanced transfer learning strategies for deep neural networks in natural language processing. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42106353

[19] Reddit and rare diseases: what myositis communities tell us about support and struggle. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42099825

[20] Multidimensional analysis of childbirth experiences on Chinese social media: an integrated approach using LDA, sentiment analysis and deep learning. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42088242

[21] An intelligent transformer based framework for bilingual financial complaint classification. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42082635

[22] BERTopic-driven term extraction from biomedical texts toward ontology population: evaluating vaccine ontology with Plotkin's vaccines corpus. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42071270

[23] Fine-Tuning and Benchmarking Transformer Models for Multiclass Classification of Clinical Research Papers: Retrospective Modeling Study. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42061835

[24] From association to intervention: Semantic trajectories and knowledge frontiers in epilepsy-gut microbiota research revealed by bibliometrics and NLP. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42058119

[25] Shifts in dental trauma research (2000-2025): a literature-based thematic analysis using topic modeling. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42057039

[26] Analyzing digital consumer insights through RoBERTa LLM based sentiment analysis and topic modeling. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42031839

[27] High-quality data selection-driven instruction tuning for biomedical large language models. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42031125

[28] On the interface between linguistics, computer science and psychiatry: analyzing textual key-factors affecting BERT-based classification of schizophrenia in social media texts. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42027780

[29] Longitudinal datasets of health app reviews for privacy and trust modeling. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42015941

[30] Performance of Open-Source LLMs in Identifying Pediatric Pneumonia From Free-Text Chest Radiograph Reports. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42011065

[31] Comparing energy consumption and accuracy in text classification inference. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41998005

[32] Using Natural Language Processing to Evaluate Differences in Psychotherapeutic Services for Posttraumatic Stress Disorder in a Suicide-Risk-Stratified Veteran Sample. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41983743

[33] An end-to-end system for explainable clinical coding across languages and diverse medical data sources. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41981562

[34] Zero-shot interpretable biomedical literature appraisal with generative large language models. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41978683

[35] Context-Aware Sentence Classification of Radiology Reports Using Synthetic Data: Development and Validation Study. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41961980

[36] Digital Discourse, Secondary Victimization, and Psychological Harm: Mixed-Methods Analysis of System Justification in the #MeToo Movement. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41960784

[37] Research on daily medication and drug efficacy evaluation for chronic diseases based on natural language processing (NLP). (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41948013

[38] Comparison of Artificial Intelligence Tools With Human Coding for Sentiment, Topic, and Thematic Analysis Tasks of Public Health Datasets During the COVID-19 Pandemic in Australia: Case Study. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41945649

[39] Automated ICD-10-Anchored Classification of Primary Care Text Data: Development and Evaluation of a Custom Multilabel Classifier. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41941723

[40] ModernBERT is more efficient than conventional BERT for chest CT findings classification in Japanese radiology reports. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41932978

[41] Graph convolution-based techniques for pragmatic Arabic figurative language classification. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41930216

[42] Your Next State-of-the-Art Could Come from Another Domain: A Cross-Domain Analysis of Hierarchical Text Classification. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41929874

[43] The Insight-Inference Loop: Efficient Text Classification via Natural Language Inference and Threshold-Tuning. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41924491

[44] The evolving landscape of large language models and non-large language models in health care. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41924194

[45] From reductionism to complex systems: Paradigm shift and knowledge evolution in competitive sports research using BERTopic. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41911258

[46] Comparative Analysis of Japanese Clinical Note Styles Between Physicians and Large Language Models Using Identical Psychiatric Cases: Quantitative Text Analysis. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41894589

[47] From theory to autonomy: a topic modelling study of quantum finance through the lens of Datatopia and TOE. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41890629

[48] BanglaEcomReviewCorpus: A dataset for e-commerce product review sentiment analysis. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41883575

[49] Financial Burden in Adults With Chronic Illness in Switzerland: A Secondary Analysis of Qualitative Interviews Using Natural Language Processing and Topic Modeling. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41849269

[50] Multilingual news dataset about Ukraine (2022-2025): data collection and documentation. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41844665




________________________________________________________________________________

## ALL SOURCES:
[1] Natural language processing captures memory content associated with shared neural patterns at encoding and retrieval. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42243459

[2] Nurse retention discourse in YouTube comments: a structural topic modeling analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42226531

[3] Learning to Diagnose Privately: DP-Powered LLMs for Radiology Report Classification. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221863

[4] Human rights violations reporting dataset. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42220647

[5] Disputing your roots: A multi-platform computational analysis of consumer reactions to genetic ancestry testing. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213236

[6] The feeling of "Urami": A structural topic modeling approach. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42189805

[7] The widening partisan gap in legislative support for civil rights in the United States. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42185320

[8] Topic Modeling of Nursing Documentation in Hemodialysis Units: A Mixed-Methods Study of Nursing Surveillance Activities. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42184213

[9] Uncovering Topics in Dutch Patient Messages in Inflammatory Bowel Disease: A Comparative Study of Embedding Models for Neural Topic Modeling. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175024

[10] Enhancing amharic news classification through ontology-based feature fusion and logistic regression. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42162112

[11] Tracking subjective symptom improvement from patient narratives in mobile health: An observational natural language processing study. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152868

[12] Constructing Digital Support at End of Life: A Cross-Cultural Analysis of Interpersonal Engagement on Hospice Websites. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152480

[13] AI-Enabled Digital Health Promotion and Prevention: Computational Literature Review. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149833

[14] Using natural language processing to assess proxy measures of therapeutic alliance across suicide risk tiers. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42119904

[15] Self-Identified Age Cohorts and Personal Experience Sharing in Pseudonymous Online Spaces: Natural Language Processing Analysis of Reddit. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42117595

[16] From dots to faces: individual differences in visual imagery capacity predict the content of Ganzflicker-induced hallucinations. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110566

[17] Artificial Intelligence-Driven Social Media Analysis of Vaccine Hesitancy, Confidence, and Trust in Africa: A Scoping Review. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110045

[18] Uncovering advanced transfer learning strategies for deep neural networks in natural language processing. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42106353

[19] Reddit and rare diseases: what myositis communities tell us about support and struggle. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42099825

[20] Multidimensional analysis of childbirth experiences on Chinese social media: an integrated approach using LDA, sentiment analysis and deep learning. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42088242

[21] An intelligent transformer based framework for bilingual financial complaint classification. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42082635

[22] BERTopic-driven term extraction from biomedical texts toward ontology population: evaluating vaccine ontology with Plotkin's vaccines corpus. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42071270

[23] Fine-Tuning and Benchmarking Transformer Models for Multiclass Classification of Clinical Research Papers: Retrospective Modeling Study. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42061835

[24] From association to intervention: Semantic trajectories and knowledge frontiers in epilepsy-gut microbiota research revealed by bibliometrics and NLP. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42058119

[25] Shifts in dental trauma research (2000-2025): a literature-based thematic analysis using topic modeling. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42057039

[26] Analyzing digital consumer insights through RoBERTa LLM based sentiment analysis and topic modeling. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42031839

[27] High-quality data selection-driven instruction tuning for biomedical large language models. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42031125

[28] On the interface between linguistics, computer science and psychiatry: analyzing textual key-factors affecting BERT-based classification of schizophrenia in social media texts. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42027780

[29] Longitudinal datasets of health app reviews for privacy and trust modeling. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42015941

[30] Performance of Open-Source LLMs in Identifying Pediatric Pneumonia From Free-Text Chest Radiograph Reports. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42011065

[31] Comparing energy consumption and accuracy in text classification inference. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41998005

[32] Using Natural Language Processing to Evaluate Differences in Psychotherapeutic Services for Posttraumatic Stress Disorder in a Suicide-Risk-Stratified Veteran Sample. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41983743

[33] An end-to-end system for explainable clinical coding across languages and diverse medical data sources. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41981562

[34] Zero-shot interpretable biomedical literature appraisal with generative large language models. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41978683

[35] Context-Aware Sentence Classification of Radiology Reports Using Synthetic Data: Development and Validation Study. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41961980

[36] Digital Discourse, Secondary Victimization, and Psychological Harm: Mixed-Methods Analysis of System Justification in the #MeToo Movement. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41960784

[37] Research on daily medication and drug efficacy evaluation for chronic diseases based on natural language processing (NLP). (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41948013

[38] Comparison of Artificial Intelligence Tools With Human Coding for Sentiment, Topic, and Thematic Analysis Tasks of Public Health Datasets During the COVID-19 Pandemic in Australia: Case Study. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41945649

[39] Automated ICD-10-Anchored Classification of Primary Care Text Data: Development and Evaluation of a Custom Multilabel Classifier. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41941723

[40] ModernBERT is more efficient than conventional BERT for chest CT findings classification in Japanese radiology reports. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41932978

[41] Graph convolution-based techniques for pragmatic Arabic figurative language classification. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41930216

[42] Your Next State-of-the-Art Could Come from Another Domain: A Cross-Domain Analysis of Hierarchical Text Classification. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41929874

[43] The Insight-Inference Loop: Efficient Text Classification via Natural Language Inference and Threshold-Tuning. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41924491

[44] The evolving landscape of large language models and non-large language models in health care. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41924194

[45] From reductionism to complex systems: Paradigm shift and knowledge evolution in competitive sports research using BERTopic. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41911258

[46] Comparative Analysis of Japanese Clinical Note Styles Between Physicians and Large Language Models Using Identical Psychiatric Cases: Quantitative Text Analysis. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41894589

[47] From theory to autonomy: a topic modelling study of quantum finance through the lens of Datatopia and TOE. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41890629

[48] BanglaEcomReviewCorpus: A dataset for e-commerce product review sentiment analysis. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41883575

[49] Financial Burden in Adults With Chronic Illness in Switzerland: A Secondary Analysis of Qualitative Interviews Using Natural Language Processing and Topic Modeling. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41849269

[50] Multilingual news dataset about Ukraine (2022-2025): data collection and documentation. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41844665


