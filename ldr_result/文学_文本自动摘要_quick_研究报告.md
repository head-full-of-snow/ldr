文本自动摘要（Automatic Text Summarization）的最新科研进展主要集中在解决大型语言模型（LLMs）引入后的新挑战，如事实性幻觉、长文本处理能力、特定领域的适应性以及评估体系的完善。以下是基于2024-2026年最新文献的综合分析：

### 1. 幻觉抑制与事实一致性（Hallucination Mitigation）
随着LLM在摘要生成中的广泛应用，实体级幻觉（Entity Hallucination）成为主要瓶颈。研究人员提出了多种机制来增强摘要的事实忠实度：
*   **基于奖励的微调**：提出了一种使用“实体幻觉指数”（Entity Hallumination Index, EHI）作为引导指标的奖励驱动微调框架，旨在通过量化和惩罚错误实体引入来改善摘要质量 [1]。
*   **检测与缓解框架**：开发了专门的幻觉检测和缓解框架，以解决摘要中包含源文本中不存在信息的问题，从而保障摘要的事实准确性并提升用户满意度 [2]。
*   **提示工程优化**：通过本体论提示微调（Ontology-based prompt tuning），将领域特定知识整合到摘要生成中，以减少通用摘要的泛化缺陷并提高新闻摘要的上下文相关性 [8]。

### 2. 长文本处理与可控摘要（Long Context & Length Control）
针对长文档和复杂数据流的摘要需求，最新研究关注于克服“迷失在中间”（Lost in the Middle）现象及长度控制：
*   **分段摘要策略**：为了解决传统“Stuff”方法在处理长提示时忽略中间信息的缺陷，提出了“Map-Reduce”或“Divide and Summarize”策略，将文本分割后分别摘要再整合，显著提升了小型语言模型（SLMs）和大型语言模型在长文本上的表现 [6]。
*   **长度可控生成**：针对出版等需要固定版面的应用场景，研究了基于摘要输出区域的增强型Transformer架构，通过长度嵌入或词级抽取模块实现摘要长度的精确控制 [3]。
*   **时间推理与纵向摘要**：在临床等领域，研究重点转向处理跨越时间的多模态数据，利用时间推理（Temporal Reasoning）、检索增强生成（RAG）和思维链（Chain-of-Thought）提示来合成结构化与非结构化信息 [17]。

### 3. 特定领域的深度应用（Domain-Specific Applications）
LLM在垂直领域的摘要应用正从通用任务转向高度专业化的场景，特别是医疗和法律领域：
*   **医疗文本摘要**：
    *   **临床决策支持**：LLM被用于生成出院摘要、急诊就诊摘要及转诊文档（如肝病转诊），旨在减轻医护人员行政负担并支持知情决策 [15], [16], [24]。
    *   **安全性与评估挑战**：尽管LLM在匹配人类专家水平方面表现出色，但仅在7%的研究中进行了外部验证，3%进行了患者安全性评估 [13]。研究强调了评估临床影响的四个维度：效用、失败模式、患者安全风险和偏见 [12]。
    *   **新框架与工具**：提出了SAC-VAE强化学习框架用于法律文本摘要 [10]，以及CLEVER框架用于专家审查LLM性能，以解决数据污染和“LLM-as-a-judge”的自我偏好问题 [18]。
*   **法律文本摘要**：结合基于案例的推理（Case-Based Reasoning, CBR）和深度学习，构建了混合摘要方法，在词汇重叠率和领域特定推理指标上优于传统基线 [9]。
*   **其他领域**：包括兽医病理学中的知识提取 [28]、社交媒体的实时摘要分类 [30] 以及商业潜在客户生成的自动化 [25]。

### 4. 评估体系与方法论创新（Evaluation & Methodology）
随着模型能力的提升，评估方法也从简单的ROUGE分数转向更复杂的多维评估：
*   **数据集规模评估**：提出了面向特征的数据集规模评估方法，以应对提示工程在数千个测试实例中评估的复杂性 [5]。
*   **偏见审计**：利用LLM自身来审计模型在种族、性别等方面的偏见，因为人工审查在处理大规模数据时不切实际 [21]。
*   **报告标准**：制定了MEDAI-LLM-SUMM报告清单，旨在规范医疗文本摘要研究中关于安全性验证和评估框架的披露 [13]。
*   **强化学习的应用**：强化学习（RL）被广泛用于优化摘要策略，特别是在处理复杂任务（如医疗和通用NLP任务）时，通过奖励机制获取最优策略 [20]。

### 5. 批判性反思
尽管进展显著，但当前研究仍面临严峻挑战：
*   **安全性验证不足**：在医疗等高风险领域，大多数研究缺乏严格的外部验证和患者安全性评估，幻觉率在不同研究中差异巨大 [13]。
*   **评估偏差**：现有的公共基准测试受数据污染影响，且“LLM-as-a-judge”方法存在自我偏好，导致评估结果可能与临床或实际应用场景脱节 [18]。
*   **可解释性与信任**：虽然LLM提高了效率，但其“黑盒”性质使得错误信息的传播风险增加，亟需更透明的评估框架和人类专家监督机制 [12], [21]。

综上所述，文本自动摘要的最新进展正从单纯追求生成流畅度转向追求事实准确性、长度可控性、领域适应性以及严格的安全性评估。未来研究需重点关注幻觉的根治、评估标准的统一以及高风险领域（如医疗、法律）的部署安全。

[1] Fine-Tuning Large Language Models Using Entity Hallucination Index for Text Summarization. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41587186

[2] A hallucination detection and mitigation framework for faithful text summarization using LLMs. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41339465

[3] Enhanced transformer for length-controlled abstractive summarization based on summary output area. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/40134863

[4] Enhancing Persian text summarization through a three-phase fine-tuning and reinforcement learning approach with the mT5 transformer model. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/39747858

[5] Towards Dataset-Scale and Feature-Oriented Evaluation of Text Summarization in Large Language Model Prompts. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/39250398

[6] Divide and summarize: improve SLM text summarization. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/40821952

[7] Large scale summarization using ensemble prompts and in context learning approaches. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/40133382

[8] Ontology-based prompt tuning for news article summarization. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40008010

[9] Case-Based Reasoning with Deep Learning for a Hybrid Approach to Legal Text Summarization. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41460740

[10] Empowering legal justice with AI: A reinforcement learning SAC-VAE framework for advanced legal text summarization. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/39453939

[11] Integrating natural language processing into radiation oncology: a practical guide to transformer architecture and large language models. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42063997

[12] Advancing Knowledge in Evaluating the Clinical Impact of Large Language Models for Clinical Text Summarization: A Narrative Review. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174918

[13] MEDAI-LLM-SUMM: a reporting checklist for medical text summarization studies using large language models. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41847286

[14] Scientific Evidence for Clinical Text Summarization Using Large Language Models: Scoping Review. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/40371947

[15] A comparative study of recent large language models on generating hospital discharge summaries for lung cancer patients. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/40544901

[16] Evaluating large language models for drafting emergency department encounter summaries. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/40526634

[17] Large Language Models with Temporal Reasoning for Longitudinal Clinical Summarization and Prediction. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41399802

[18] Clinical Large Language Model Evaluation by Expert Review (CLEVER): Framework Development and Validation. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41343765

[19] Current applications and challenges in large language models for patient care: a systematic review. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/39838160

[20] A review of reinforcement learning for natural language processing and applications in healthcare. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/39208319

[21] Using Large Language Models to Audit Model Healthcare Biases. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41758166

[22] Awareness, use, and perceived barriers to artificial intelligence in pediatric urology: a multicenter survey. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41705101

[23] Real-Time Named Entity Recognition from Textual Electronic Clinical Records in Cancer Therapy Using Low-Latency Neural Networks. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41649195

[24] A Large Language Model Assistant for Summarizing Hepatology Referral Documents. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41504326

[25] A review of AI-based business lead generation: Scrapus as a case study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41312025

[26] Generative AI and foundation models in medical image. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41051729

[27] Augmenting Large Language Models With Automated, Bibliometrics-Powered Literature Search for Knowledge Distillation: A Pilot Study for Common Spinal Pathologies. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/40662770

[28] Natural language processing in veterinary pathology: A review. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/40589085

[29] A Narrative Review on the Application of Large Language Models to Support Cancer Care and Research. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/40199294

[30] An adaptive search mechanism with convolutional learning networks for online social media text summarization and classification model. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/40169845




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 文本自动摘要的最新科研进展
2. latest research advances in automatic text summarization 2024 2025

 #### Iteration 2:
1. What are the specific performance benchmarks, hallucination rates, and clinical safety protocols for Large Language Model-based text summarization systems deployed in real-world healthcare settings in 2025 and 2026, given that previous studies (2023-2024) primarily focused on retrospective evaluations or specific niche domains like radiology and oncology?

 #### Iteration 3:
1. What are the specific hallucination rates, clinical safety protocols, and performance benchmarks for Large Language Model-based text summarization systems deployed in real-world healthcare settings in 2025 and 2026, given that previous studies primarily focused on retrospective evaluations or niche domains?



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
文本自动摘要的最新科研进展



Searched with 2 questions, found 50 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
文本自动摘要的最新科研进展



Searched with 1 questions, found 40 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
文本自动摘要的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
文本自动摘要的最新科研进展



文本自动摘要（Automatic Text Summarization）的最新科研进展主要集中在解决大型语言模型（LLMs）引入后的新挑战，如事实性幻觉、长文本处理能力、特定领域的适应性以及评估体系的完善。以下是基于2024-2026年最新文献的综合分析：

### 1. 幻觉抑制与事实一致性（Hallucination Mitigation）
随着LLM在摘要生成中的广泛应用，实体级幻觉（Entity Hallucination）成为主要瓶颈。研究人员提出了多种机制来增强摘要的事实忠实度：
*   **基于奖励的微调**：提出了一种使用“实体幻觉指数”（Entity Hallumination Index, EHI）作为引导指标的奖励驱动微调框架，旨在通过量化和惩罚错误实体引入来改善摘要质量 [1]。
*   **检测与缓解框架**：开发了专门的幻觉检测和缓解框架，以解决摘要中包含源文本中不存在信息的问题，从而保障摘要的事实准确性并提升用户满意度 [2]。
*   **提示工程优化**：通过本体论提示微调（Ontology-based prompt tuning），将领域特定知识整合到摘要生成中，以减少通用摘要的泛化缺陷并提高新闻摘要的上下文相关性 [8]。

### 2. 长文本处理与可控摘要（Long Context & Length Control）
针对长文档和复杂数据流的摘要需求，最新研究关注于克服“迷失在中间”（Lost in the Middle）现象及长度控制：
*   **分段摘要策略**：为了解决传统“Stuff”方法在处理长提示时忽略中间信息的缺陷，提出了“Map-Reduce”或“Divide and Summarize”策略，将文本分割后分别摘要再整合，显著提升了小型语言模型（SLMs）和大型语言模型在长文本上的表现 [6]。
*   **长度可控生成**：针对出版等需要固定版面的应用场景，研究了基于摘要输出区域的增强型Transformer架构，通过长度嵌入或词级抽取模块实现摘要长度的精确控制 [3]。
*   **时间推理与纵向摘要**：在临床等领域，研究重点转向处理跨越时间的多模态数据，利用时间推理（Temporal Reasoning）、检索增强生成（RAG）和思维链（Chain-of-Thought）提示来合成结构化与非结构化信息 [17]。

### 3. 特定领域的深度应用（Domain-Specific Applications）
LLM在垂直领域的摘要应用正从通用任务转向高度专业化的场景，特别是医疗和法律领域：
*   **医疗文本摘要**：
    *   **临床决策支持**：LLM被用于生成出院摘要、急诊就诊摘要及转诊文档（如肝病转诊），旨在减轻医护人员行政负担并支持知情决策 [15], [16], [24]。
    *   **安全性与评估挑战**：尽管LLM在匹配人类专家水平方面表现出色，但仅在7%的研究中进行了外部验证，3%进行了患者安全性评估 [13]。研究强调了评估临床影响的四个维度：效用、失败模式、患者安全风险和偏见 [12]。
    *   **新框架与工具**：提出了SAC-VAE强化学习框架用于法律文本摘要 [10]，以及CLEVER框架用于专家审查LLM性能，以解决数据污染和“LLM-as-a-judge”的自我偏好问题 [18]。
*   **法律文本摘要**：结合基于案例的推理（Case-Based Reasoning, CBR）和深度学习，构建了混合摘要方法，在词汇重叠率和领域特定推理指标上优于传统基线 [9]。
*   **其他领域**：包括兽医病理学中的知识提取 [28]、社交媒体的实时摘要分类 [30] 以及商业潜在客户生成的自动化 [25]。

### 4. 评估体系与方法论创新（Evaluation & Methodology）
随着模型能力的提升，评估方法也从简单的ROUGE分数转向更复杂的多维评估：
*   **数据集规模评估**：提出了面向特征的数据集规模评估方法，以应对提示工程在数千个测试实例中评估的复杂性 [5]。
*   **偏见审计**：利用LLM自身来审计模型在种族、性别等方面的偏见，因为人工审查在处理大规模数据时不切实际 [21]。
*   **报告标准**：制定了MEDAI-LLM-SUMM报告清单，旨在规范医疗文本摘要研究中关于安全性验证和评估框架的披露 [13]。
*   **强化学习的应用**：强化学习（RL）被广泛用于优化摘要策略，特别是在处理复杂任务（如医疗和通用NLP任务）时，通过奖励机制获取最优策略 [20]。

### 5. 批判性反思
尽管进展显著，但当前研究仍面临严峻挑战：
*   **安全性验证不足**：在医疗等高风险领域，大多数研究缺乏严格的外部验证和患者安全性评估，幻觉率在不同研究中差异巨大 [13]。
*   **评估偏差**：现有的公共基准测试受数据污染影响，且“LLM-as-a-judge”方法存在自我偏好，导致评估结果可能与临床或实际应用场景脱节 [18]。
*   **可解释性与信任**：虽然LLM提高了效率，但其“黑盒”性质使得错误信息的传播风险增加，亟需更透明的评估框架和人类专家监督机制 [12], [21]。

综上所述，文本自动摘要的最新进展正从单纯追求生成流畅度转向追求事实准确性、长度可控性、领域适应性以及严格的安全性评估。未来研究需重点关注幻觉的根治、评估标准的统一以及高风险领域（如医疗、法律）的部署安全。

### SOURCES USED IN THIS SECTION:
[1] Fine-Tuning Large Language Models Using Entity Hallucination Index for Text Summarization. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41587186

[2] A hallucination detection and mitigation framework for faithful text summarization using LLMs. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41339465

[3] Enhanced transformer for length-controlled abstractive summarization based on summary output area. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/40134863

[4] Enhancing Persian text summarization through a three-phase fine-tuning and reinforcement learning approach with the mT5 transformer model. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/39747858

[5] Towards Dataset-Scale and Feature-Oriented Evaluation of Text Summarization in Large Language Model Prompts. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/39250398

[6] Divide and summarize: improve SLM text summarization. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/40821952

[7] Large scale summarization using ensemble prompts and in context learning approaches. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/40133382

[8] Ontology-based prompt tuning for news article summarization. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40008010

[9] Case-Based Reasoning with Deep Learning for a Hybrid Approach to Legal Text Summarization. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41460740

[10] Empowering legal justice with AI: A reinforcement learning SAC-VAE framework for advanced legal text summarization. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/39453939

[11] Integrating natural language processing into radiation oncology: a practical guide to transformer architecture and large language models. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42063997

[12] Advancing Knowledge in Evaluating the Clinical Impact of Large Language Models for Clinical Text Summarization: A Narrative Review. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174918

[13] MEDAI-LLM-SUMM: a reporting checklist for medical text summarization studies using large language models. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41847286

[14] Scientific Evidence for Clinical Text Summarization Using Large Language Models: Scoping Review. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/40371947

[15] A comparative study of recent large language models on generating hospital discharge summaries for lung cancer patients. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/40544901

[16] Evaluating large language models for drafting emergency department encounter summaries. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/40526634

[17] Large Language Models with Temporal Reasoning for Longitudinal Clinical Summarization and Prediction. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41399802

[18] Clinical Large Language Model Evaluation by Expert Review (CLEVER): Framework Development and Validation. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41343765

[19] Current applications and challenges in large language models for patient care: a systematic review. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/39838160

[20] A review of reinforcement learning for natural language processing and applications in healthcare. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/39208319

[21] Using Large Language Models to Audit Model Healthcare Biases. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41758166

[22] Awareness, use, and perceived barriers to artificial intelligence in pediatric urology: a multicenter survey. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41705101

[23] Real-Time Named Entity Recognition from Textual Electronic Clinical Records in Cancer Therapy Using Low-Latency Neural Networks. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41649195

[24] A Large Language Model Assistant for Summarizing Hepatology Referral Documents. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41504326

[25] A review of AI-based business lead generation: Scrapus as a case study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41312025

[26] Generative AI and foundation models in medical image. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41051729

[27] Augmenting Large Language Models With Automated, Bibliometrics-Powered Literature Search for Knowledge Distillation: A Pilot Study for Common Spinal Pathologies. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/40662770

[28] Natural language processing in veterinary pathology: A review. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/40589085

[29] A Narrative Review on the Application of Large Language Models to Support Cancer Care and Research. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/40199294

[30] An adaptive search mechanism with convolutional learning networks for online social media text summarization and classification model. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/40169845




________________________________________________________________________________

## ALL SOURCES:
[1] Fine-Tuning Large Language Models Using Entity Hallucination Index for Text Summarization. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41587186

[2] A hallucination detection and mitigation framework for faithful text summarization using LLMs. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41339465

[3] Enhanced transformer for length-controlled abstractive summarization based on summary output area. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/40134863

[4] Enhancing Persian text summarization through a three-phase fine-tuning and reinforcement learning approach with the mT5 transformer model. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/39747858

[5] Towards Dataset-Scale and Feature-Oriented Evaluation of Text Summarization in Large Language Model Prompts. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/39250398

[6] Divide and summarize: improve SLM text summarization. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/40821952

[7] Large scale summarization using ensemble prompts and in context learning approaches. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/40133382

[8] Ontology-based prompt tuning for news article summarization. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40008010

[9] Case-Based Reasoning with Deep Learning for a Hybrid Approach to Legal Text Summarization. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41460740

[10] Empowering legal justice with AI: A reinforcement learning SAC-VAE framework for advanced legal text summarization. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/39453939

[11] Integrating natural language processing into radiation oncology: a practical guide to transformer architecture and large language models. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42063997

[12] Advancing Knowledge in Evaluating the Clinical Impact of Large Language Models for Clinical Text Summarization: A Narrative Review. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174918

[13] MEDAI-LLM-SUMM: a reporting checklist for medical text summarization studies using large language models. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41847286

[14] Scientific Evidence for Clinical Text Summarization Using Large Language Models: Scoping Review. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/40371947

[15] A comparative study of recent large language models on generating hospital discharge summaries for lung cancer patients. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/40544901

[16] Evaluating large language models for drafting emergency department encounter summaries. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/40526634

[17] Large Language Models with Temporal Reasoning for Longitudinal Clinical Summarization and Prediction. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41399802

[18] Clinical Large Language Model Evaluation by Expert Review (CLEVER): Framework Development and Validation. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41343765

[19] Current applications and challenges in large language models for patient care: a systematic review. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/39838160

[20] A review of reinforcement learning for natural language processing and applications in healthcare. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/39208319

[21] Using Large Language Models to Audit Model Healthcare Biases. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41758166

[22] Awareness, use, and perceived barriers to artificial intelligence in pediatric urology: a multicenter survey. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41705101

[23] Real-Time Named Entity Recognition from Textual Electronic Clinical Records in Cancer Therapy Using Low-Latency Neural Networks. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41649195

[24] A Large Language Model Assistant for Summarizing Hepatology Referral Documents. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41504326

[25] A review of AI-based business lead generation: Scrapus as a case study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41312025

[26] Generative AI and foundation models in medical image. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41051729

[27] Augmenting Large Language Models With Automated, Bibliometrics-Powered Literature Search for Knowledge Distillation: A Pilot Study for Common Spinal Pathologies. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/40662770

[28] Natural language processing in veterinary pathology: A review. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/40589085

[29] A Narrative Review on the Application of Large Language Models to Support Cancer Care and Research. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/40199294

[30] An adaptive search mechanism with convolutional learning networks for online social media text summarization and classification model. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/40169845


