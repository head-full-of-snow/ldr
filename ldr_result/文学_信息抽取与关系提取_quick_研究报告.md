信息抽取（Information Extraction, IE）与关系提取（Relation Extraction, RE）在2026年的科研进展中，呈现出从传统自然语言处理（NLP）向基于大语言模型（LLMs）的范式显著转变的趋势。尽管LLMs展现了强大的零样本（zero-shot）或少样本（few-shot）提取能力，但其在临床和高风险领域的实际应用仍面临幻觉、隐私合规及结构化输出难题。以下从技术方法、应用领域及挑战与优化策略三个维度进行详细阐述。

### 1. 技术范式的演进：从规则/BERT到LLM及其混合架构

传统的基于规则的方法虽然可解释性强且碳足迹低，但在处理非结构化文本时灵活性不足。近年来，研究重点已转向利用LLMs处理复杂的临床叙事，但仍需结合其他技术以确保可靠性。

*   **LLM作为核心提取引擎**：多项研究表明，LLMs在从非结构化文本中提取结构化信息方面表现出色，且只需极少的任务特定微调（fine-tuning）[19]。例如，在骨科手术记录中，LLMs能够实现零样本程序提取，显著减少了手动编码的时间和成本 [16]。在骨扫描叙事中，通过临床逻辑引导的提示框架（clinical-logic-guided prompting），通用LLMs无需领域微调即可实现可靠的结构化信息提取 [17]。
*   **混合架构与知识增强**：为了克服LLMs的局限性，混合架构成为新趋势。例如，结合双向编码器表示（BERT）和图神经网络（GNNs）的AI工作流，利用GNN进行本体对齐和语义推理，有效解决了企业知识管理中非结构化数据提取的上下文相关性难题 [2]。在法国临床叙事中，针对时间关系提取的研究也构建了综合框架，填补了非英语临床NLP资源的空白 [9]。
*   **检索增强生成（RAG）的应用**：在澳大利亚养老护理等非结构化术语异质性高的场景中，RAG技术被证明能显著提高LLM输出的精确性和接地性（grounding），尽管检索策略的选择仍是研究热点 [6]。

### 2. 主要应用领域：从通用医疗到特定专科与跨领域

信息抽取技术已深入多个专业领域，旨在将非结构化报告转化为机器可读的知识。

*   **临床电子健康记录（EHR）与病历处理**：
    *   **实体与概念提取**：研究涵盖了从意大利妇科肿瘤报告、德国EHR到日本临床文本中的广泛实体提取 [5, 10, 18]。特别是在日本研究中，针对长短语（如疾病、病理、症状）的扩展临床概念识别，证明了加权软匹配（weighted soft matching）在评估中的重要性 [18]。
    *   **高危信息与预后预测**：HiRMD系统利用LLM提取与死亡率相关的高危临床信息，整合异质临床证据以改善院内死亡率预测 [7]。
    *   **社会决定因素（SDoH）**：由于SDoH常记录在非结构化笔记中而非结构化EHR字段中，研究比较了基于规则和LLM的方法，发现LLM能有效解锁这些信息以辅助人口健康研究 [21]。
*   **放射学与影像报告**：
    *   RadEx框架提供了从放射学报告中进行端到端结构化信息提取的解决方案，旨在支持临床试验匹配和结果预测 [20]。
    *   在法国PET/CT报告中，LLMs被用于提取大脑代谢、灌注模式及Braak分期等描述性和解释性模式 [15]。
*   **其他专业领域**：
    *   **毒理学与化学品安全**：LLMs被用于从安全数据表（SDS）中筛选化学物质信息 [22]，以及将动物毒理学研究报告转换为符合SEND术语的结构化数据 [23]。
    *   **临床指南与决策支持**：研究比较了LLM/VLM方法与规则基线，以从肿瘤学指南中提取临床建议，尽管存在后续使用的风险，但大多数建议可被成功提取 [27]。

### 3. 关键挑战与优化策略：幻觉、隐私与效率

尽管LLMs性能强劲，但其部署仍面临三大核心挑战：幻觉、数据隐私和计算资源限制。

*   **幻觉与可靠性**：
    *   LLMs在未结构化输出中容易产生“幻觉”，这在医疗环境中是致命的。为此，研究者提出了多种反幻觉策略，包括集成方法、验证链（Chain-of-Verification）、上下文接地和“LLM-as-a-Judge”机制，以提高临床文本处理的可信度 [4]。
    *   在妇科肿瘤报告中，基于提示的提取框架通过约束LLM的输出格式，减少了错误信息生成的风险 [14]。
*   **隐私保护与本地化部署**：
    *   由于医疗数据的敏感性，使用云端LLMs可能违反数据治理规定。因此，**本地部署（on-premises）**的开源LLMs成为研究重点 [10, 29]。例如，在精神健康记录中，隐私保护的本地语言模型被用于检测自残行为，以规避敏感数据外泄风险 [29]。
    *   **小型语言模型（SLMs）**被视为平衡性能与隐私的解决方案。例如，IT5模型等SLMs在本地设备上处理自身免疫性萎缩性胃炎的内镜标记提取，既高效又安全 [13]。
*   **模型规模、量化与成本效益**：
    *   研究系统调查了本地部署的开源LLMs中模型大小与数值精度（量化）之间的权衡。结果表明，在资源受限的医院环境中，经过适当量化的较小模型可以在保持较高提取性能的同时，满足隐私和计算效率要求 [12]。
    *   MINE平台展示了一种交互式环境，整合了基于规则、BERT和LLM的方法，在吸烟状态、糖尿病和高血压的提取中实现了超过95%的F1分数，证明了混合方法在专家指导下的有效性 [8]。

### 结论

2026年的信息抽取与关系提取研究已从单纯追求高精度转向**可靠性、隐私合规与可解释性**的综合平衡。虽然LLMs在零样本提取和复杂叙事理解上超越了传统方法，但其实际应用必须通过**反幻觉策略、RAG增强、本地化部署以及小型化模型**来克服医疗场景中的固有风险。未来趋势将更多地集中在混合架构（如LLM+GNN或LLM+规则引擎）以及针对特定专科（如肿瘤学、毒理学、放射学）的垂直优化上 [2, 4, 13, 20]。

[1] Large Language Models for Clinical Narrative Processing: Methods, Applications, and Challenges. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42201162

[2] An AI Workflow Combining Bidirectional Encoder Representations from Transformers (BERT) and Graph Neural Networks (GNNs) for Knowledge Retrieval in Digital Enterprises. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149883

[3] Context-Free Grammar-Guided Generation of FHIR Resources Using Large Language Models. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175392

[4] Combining Anti-Hallucination Strategies for Reliable LLM-Based Clinical Information Extraction. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175025

[5] A Real-Time Clinical Text Information Extractor via LLM. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174977

[6] Optimising clinical information extraction: a comparative study of retrieval-augmented generation techniques in clinical notes. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42114794

[7] HiRMD: A System for Mortality Prediction via LLM-Based High-Risk Information Extraction and Diagnosis. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42224317

[8] MINE: An Interactive Platform for Expert-Guided Medical Information Extraction. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175026

[9] From annotation to adaptation: extracting temporal relations in French clinical narratives. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129656

[10] Open-source large language model-based on-premises pipeline for automated data extraction from unstructured electronic health records: a pilot study. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225359

[11] Validating large language model-assisted data extraction from clinical notes. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183150

[12] Impact of LLM Scale and Quantization on Information Extraction from Clinical Text. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174969

[13] Extraction of Endoscopic Markers from Clinical Notes in Italian Patients with Autoimmune Atrophic Gastritis Using Small Language Models. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174988

[14] From Report to Record: Prompt-Based Information Extraction from Gynecology Oncology Reports Using LLMs. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174970

[15] Can LLMs Turn French PET/CT Narrative Reports into Structured Knowledge? (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174838

[16] Large language models for zero-shot procedure extraction in orthopedic surgery: a comparative evaluation. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42168275

[17] A workflow utilizing general-purpose large language models for efficient structuring and data mining of bone scintigraphy narratives. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42144441

[18] Evaluating Encoder and Decoder Models for Extended Clinical Concept Recognition in Japanese Clinical Texts: Comparative Study With Weighted Soft Matching. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133937

[19] Natural Language Processing of Clinical Notes for Cancer Research and Patient Care Prior to Widespread Adoption of Generative AI: Scoping Review. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133609

[20] RadEx: A Framework for Structured Information Extraction from Radiology Reports Based on Large Language Models. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42119089

[21] Extracting Social Determinants of Health From Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42155986

[22] Large language model-based screening of substances and their composition from safety data sheets for high-resolution chemical exposure assessment. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129497

[23] Transforming animal study toxicology reports into structured, harmonized data using large language models. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133063

[24] Evaluating large language models for structuring cardiology reports: a real-world clinical study on patient subtyping and trial recruitment. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42202663

[25] Privacy-preserving augmentation of structured telehealth activity data in diabetes patients using natural language processing. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179818

[26] Democratizing Artificial Intelligence in Toxicology: Real-World Applications and Automated Computational Workflows. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42212723

[27] Extracting Clinical Recommendations from Oncology Guidelines: An Exploratory Comparison of Automated Approaches. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175017

[28] Development Parameters of the Decision Aid Rule-Based Evaluation and Support Tool (REST) for Optimizing the Resources of an Information Extraction Task. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174963

[29] Detection of Self-Harm in Electronic Mental Health Records Using Privacy-Preserving Local Language Models: Methodological Study. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227874




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 信息抽取与关系提取的最新科研进展
2. 2025-2026 latest research advances in information extraction and relation extraction using large language models

 #### Iteration 2:
1. How do closed-loop AI agent architectures with self-reflection mechanisms compare to standard retrieval-augmented generation (RAG) pipelines in terms of accuracy and hallucination rates for complex, multi-hop relation extraction tasks in 2026?

 #### Iteration 3:
1. How do closed-loop AI agent architectures with self-reflection mechanisms compare to standard retrieval-augmented generation (RAG) pipelines in terms of accuracy and hallucination rates for complex, multi-hop relation extraction tasks in 2026?



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
信息抽取与关系提取的最新科研进展



Searched with 2 questions, found 50 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
信息抽取与关系提取的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
信息抽取与关系提取的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
信息抽取与关系提取的最新科研进展



信息抽取（Information Extraction, IE）与关系提取（Relation Extraction, RE）在2026年的科研进展中，呈现出从传统自然语言处理（NLP）向基于大语言模型（LLMs）的范式显著转变的趋势。尽管LLMs展现了强大的零样本（zero-shot）或少样本（few-shot）提取能力，但其在临床和高风险领域的实际应用仍面临幻觉、隐私合规及结构化输出难题。以下从技术方法、应用领域及挑战与优化策略三个维度进行详细阐述。

### 1. 技术范式的演进：从规则/BERT到LLM及其混合架构

传统的基于规则的方法虽然可解释性强且碳足迹低，但在处理非结构化文本时灵活性不足。近年来，研究重点已转向利用LLMs处理复杂的临床叙事，但仍需结合其他技术以确保可靠性。

*   **LLM作为核心提取引擎**：多项研究表明，LLMs在从非结构化文本中提取结构化信息方面表现出色，且只需极少的任务特定微调（fine-tuning）[19]。例如，在骨科手术记录中，LLMs能够实现零样本程序提取，显著减少了手动编码的时间和成本 [16]。在骨扫描叙事中，通过临床逻辑引导的提示框架（clinical-logic-guided prompting），通用LLMs无需领域微调即可实现可靠的结构化信息提取 [17]。
*   **混合架构与知识增强**：为了克服LLMs的局限性，混合架构成为新趋势。例如，结合双向编码器表示（BERT）和图神经网络（GNNs）的AI工作流，利用GNN进行本体对齐和语义推理，有效解决了企业知识管理中非结构化数据提取的上下文相关性难题 [2]。在法国临床叙事中，针对时间关系提取的研究也构建了综合框架，填补了非英语临床NLP资源的空白 [9]。
*   **检索增强生成（RAG）的应用**：在澳大利亚养老护理等非结构化术语异质性高的场景中，RAG技术被证明能显著提高LLM输出的精确性和接地性（grounding），尽管检索策略的选择仍是研究热点 [6]。

### 2. 主要应用领域：从通用医疗到特定专科与跨领域

信息抽取技术已深入多个专业领域，旨在将非结构化报告转化为机器可读的知识。

*   **临床电子健康记录（EHR）与病历处理**：
    *   **实体与概念提取**：研究涵盖了从意大利妇科肿瘤报告、德国EHR到日本临床文本中的广泛实体提取 [5, 10, 18]。特别是在日本研究中，针对长短语（如疾病、病理、症状）的扩展临床概念识别，证明了加权软匹配（weighted soft matching）在评估中的重要性 [18]。
    *   **高危信息与预后预测**：HiRMD系统利用LLM提取与死亡率相关的高危临床信息，整合异质临床证据以改善院内死亡率预测 [7]。
    *   **社会决定因素（SDoH）**：由于SDoH常记录在非结构化笔记中而非结构化EHR字段中，研究比较了基于规则和LLM的方法，发现LLM能有效解锁这些信息以辅助人口健康研究 [21]。
*   **放射学与影像报告**：
    *   RadEx框架提供了从放射学报告中进行端到端结构化信息提取的解决方案，旨在支持临床试验匹配和结果预测 [20]。
    *   在法国PET/CT报告中，LLMs被用于提取大脑代谢、灌注模式及Braak分期等描述性和解释性模式 [15]。
*   **其他专业领域**：
    *   **毒理学与化学品安全**：LLMs被用于从安全数据表（SDS）中筛选化学物质信息 [22]，以及将动物毒理学研究报告转换为符合SEND术语的结构化数据 [23]。
    *   **临床指南与决策支持**：研究比较了LLM/VLM方法与规则基线，以从肿瘤学指南中提取临床建议，尽管存在后续使用的风险，但大多数建议可被成功提取 [27]。

### 3. 关键挑战与优化策略：幻觉、隐私与效率

尽管LLMs性能强劲，但其部署仍面临三大核心挑战：幻觉、数据隐私和计算资源限制。

*   **幻觉与可靠性**：
    *   LLMs在未结构化输出中容易产生“幻觉”，这在医疗环境中是致命的。为此，研究者提出了多种反幻觉策略，包括集成方法、验证链（Chain-of-Verification）、上下文接地和“LLM-as-a-Judge”机制，以提高临床文本处理的可信度 [4]。
    *   在妇科肿瘤报告中，基于提示的提取框架通过约束LLM的输出格式，减少了错误信息生成的风险 [14]。
*   **隐私保护与本地化部署**：
    *   由于医疗数据的敏感性，使用云端LLMs可能违反数据治理规定。因此，**本地部署（on-premises）**的开源LLMs成为研究重点 [10, 29]。例如，在精神健康记录中，隐私保护的本地语言模型被用于检测自残行为，以规避敏感数据外泄风险 [29]。
    *   **小型语言模型（SLMs）**被视为平衡性能与隐私的解决方案。例如，IT5模型等SLMs在本地设备上处理自身免疫性萎缩性胃炎的内镜标记提取，既高效又安全 [13]。
*   **模型规模、量化与成本效益**：
    *   研究系统调查了本地部署的开源LLMs中模型大小与数值精度（量化）之间的权衡。结果表明，在资源受限的医院环境中，经过适当量化的较小模型可以在保持较高提取性能的同时，满足隐私和计算效率要求 [12]。
    *   MINE平台展示了一种交互式环境，整合了基于规则、BERT和LLM的方法，在吸烟状态、糖尿病和高血压的提取中实现了超过95%的F1分数，证明了混合方法在专家指导下的有效性 [8]。

### 结论

2026年的信息抽取与关系提取研究已从单纯追求高精度转向**可靠性、隐私合规与可解释性**的综合平衡。虽然LLMs在零样本提取和复杂叙事理解上超越了传统方法，但其实际应用必须通过**反幻觉策略、RAG增强、本地化部署以及小型化模型**来克服医疗场景中的固有风险。未来趋势将更多地集中在混合架构（如LLM+GNN或LLM+规则引擎）以及针对特定专科（如肿瘤学、毒理学、放射学）的垂直优化上 [2, 4, 13, 20]。

### SOURCES USED IN THIS SECTION:
[1] Large Language Models for Clinical Narrative Processing: Methods, Applications, and Challenges. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42201162

[2] An AI Workflow Combining Bidirectional Encoder Representations from Transformers (BERT) and Graph Neural Networks (GNNs) for Knowledge Retrieval in Digital Enterprises. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149883

[3] Context-Free Grammar-Guided Generation of FHIR Resources Using Large Language Models. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175392

[4] Combining Anti-Hallucination Strategies for Reliable LLM-Based Clinical Information Extraction. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175025

[5] A Real-Time Clinical Text Information Extractor via LLM. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174977

[6] Optimising clinical information extraction: a comparative study of retrieval-augmented generation techniques in clinical notes. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42114794

[7] HiRMD: A System for Mortality Prediction via LLM-Based High-Risk Information Extraction and Diagnosis. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42224317

[8] MINE: An Interactive Platform for Expert-Guided Medical Information Extraction. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175026

[9] From annotation to adaptation: extracting temporal relations in French clinical narratives. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129656

[10] Open-source large language model-based on-premises pipeline for automated data extraction from unstructured electronic health records: a pilot study. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225359

[11] Validating large language model-assisted data extraction from clinical notes. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183150

[12] Impact of LLM Scale and Quantization on Information Extraction from Clinical Text. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174969

[13] Extraction of Endoscopic Markers from Clinical Notes in Italian Patients with Autoimmune Atrophic Gastritis Using Small Language Models. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174988

[14] From Report to Record: Prompt-Based Information Extraction from Gynecology Oncology Reports Using LLMs. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174970

[15] Can LLMs Turn French PET/CT Narrative Reports into Structured Knowledge? (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174838

[16] Large language models for zero-shot procedure extraction in orthopedic surgery: a comparative evaluation. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42168275

[17] A workflow utilizing general-purpose large language models for efficient structuring and data mining of bone scintigraphy narratives. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42144441

[18] Evaluating Encoder and Decoder Models for Extended Clinical Concept Recognition in Japanese Clinical Texts: Comparative Study With Weighted Soft Matching. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133937

[19] Natural Language Processing of Clinical Notes for Cancer Research and Patient Care Prior to Widespread Adoption of Generative AI: Scoping Review. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133609

[20] RadEx: A Framework for Structured Information Extraction from Radiology Reports Based on Large Language Models. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42119089

[21] Extracting Social Determinants of Health From Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42155986

[22] Large language model-based screening of substances and their composition from safety data sheets for high-resolution chemical exposure assessment. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129497

[23] Transforming animal study toxicology reports into structured, harmonized data using large language models. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133063

[24] Evaluating large language models for structuring cardiology reports: a real-world clinical study on patient subtyping and trial recruitment. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42202663

[25] Privacy-preserving augmentation of structured telehealth activity data in diabetes patients using natural language processing. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179818

[26] Democratizing Artificial Intelligence in Toxicology: Real-World Applications and Automated Computational Workflows. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42212723

[27] Extracting Clinical Recommendations from Oncology Guidelines: An Exploratory Comparison of Automated Approaches. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175017

[28] Development Parameters of the Decision Aid Rule-Based Evaluation and Support Tool (REST) for Optimizing the Resources of an Information Extraction Task. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174963

[29] Detection of Self-Harm in Electronic Mental Health Records Using Privacy-Preserving Local Language Models: Methodological Study. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227874




________________________________________________________________________________

## ALL SOURCES:
[1] Large Language Models for Clinical Narrative Processing: Methods, Applications, and Challenges. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42201162

[2] An AI Workflow Combining Bidirectional Encoder Representations from Transformers (BERT) and Graph Neural Networks (GNNs) for Knowledge Retrieval in Digital Enterprises. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149883

[3] Context-Free Grammar-Guided Generation of FHIR Resources Using Large Language Models. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175392

[4] Combining Anti-Hallucination Strategies for Reliable LLM-Based Clinical Information Extraction. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175025

[5] A Real-Time Clinical Text Information Extractor via LLM. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174977

[6] Optimising clinical information extraction: a comparative study of retrieval-augmented generation techniques in clinical notes. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42114794

[7] HiRMD: A System for Mortality Prediction via LLM-Based High-Risk Information Extraction and Diagnosis. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42224317

[8] MINE: An Interactive Platform for Expert-Guided Medical Information Extraction. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175026

[9] From annotation to adaptation: extracting temporal relations in French clinical narratives. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129656

[10] Open-source large language model-based on-premises pipeline for automated data extraction from unstructured electronic health records: a pilot study. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225359

[11] Validating large language model-assisted data extraction from clinical notes. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183150

[12] Impact of LLM Scale and Quantization on Information Extraction from Clinical Text. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174969

[13] Extraction of Endoscopic Markers from Clinical Notes in Italian Patients with Autoimmune Atrophic Gastritis Using Small Language Models. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174988

[14] From Report to Record: Prompt-Based Information Extraction from Gynecology Oncology Reports Using LLMs. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174970

[15] Can LLMs Turn French PET/CT Narrative Reports into Structured Knowledge? (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174838

[16] Large language models for zero-shot procedure extraction in orthopedic surgery: a comparative evaluation. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42168275

[17] A workflow utilizing general-purpose large language models for efficient structuring and data mining of bone scintigraphy narratives. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42144441

[18] Evaluating Encoder and Decoder Models for Extended Clinical Concept Recognition in Japanese Clinical Texts: Comparative Study With Weighted Soft Matching. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133937

[19] Natural Language Processing of Clinical Notes for Cancer Research and Patient Care Prior to Widespread Adoption of Generative AI: Scoping Review. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133609

[20] RadEx: A Framework for Structured Information Extraction from Radiology Reports Based on Large Language Models. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42119089

[21] Extracting Social Determinants of Health From Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42155986

[22] Large language model-based screening of substances and their composition from safety data sheets for high-resolution chemical exposure assessment. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129497

[23] Transforming animal study toxicology reports into structured, harmonized data using large language models. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42133063

[24] Evaluating large language models for structuring cardiology reports: a real-world clinical study on patient subtyping and trial recruitment. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42202663

[25] Privacy-preserving augmentation of structured telehealth activity data in diabetes patients using natural language processing. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179818

[26] Democratizing Artificial Intelligence in Toxicology: Real-World Applications and Automated Computational Workflows. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42212723

[27] Extracting Clinical Recommendations from Oncology Guidelines: An Exploratory Comparison of Automated Approaches. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42175017

[28] Development Parameters of the Decision Aid Rule-Based Evaluation and Support Tool (REST) for Optimizing the Resources of an Information Extraction Task. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174963

[29] Detection of Self-Harm in Electronic Mental Health Records Using Privacy-Preserving Local Language Models: Methodological Study. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227874


