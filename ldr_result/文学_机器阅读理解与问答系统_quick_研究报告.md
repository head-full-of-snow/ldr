基于提供的文献资料，机器阅读理解（Machine Reading Comprehension, MRC）与问答系统（Question Answering, QA）的最新科研进展主要集中在解决文本歧义性、多粒度理解、特定领域（尤其是医疗）的应用、多模态融合以及低资源语言模型的构建等方面。以下是对这些进展的详细综述：

**1. 处理文本歧义性与语义模糊性**
随着预训练语言模型的发展，解决MRC中的文本歧义和语义模糊性成为研究重点。研究者指出，利用生成式预训练Transformer（Generative Pre-trained Transformers）可以有效解决基于MRC的问答中的文本歧义性和语义模糊性问题 [3]。此外，为了更精确地解析段落中的歧义，轻量级Transformer架构被提出并用于解决MRC中的段落歧义问题，这表明模型结构的小型化与精准化是当前的一个趋势 [2]。同时，针对“不可回答”情况（unanswerability）的探索也是关键进展之一，新的基准测试和方法正在被开发以评估模型在无法从文本中找到答案时的表现 [1]。

**2. 多粒度与跨模态理解**
在模型架构方面，端到端的多粒度阅读理解模型（MGRC）被提出，旨在通过不同粒度的信息交互来提升问答性能 [4]。在多模态领域，视觉问答（Visual Question Answering, VQA）与阅读理解的结合日益紧密。例如，RCVQA模型结合了视觉元素与阅读理解能力，增强了多模态问答的效果 [5]。此外，可视化解释技术也被应用于开放域问答系统中，利用BERT等模型提供可视化的推理依据，以提高系统的可解释性 [18]。

**3. 医疗与健康领域的垂直应用**
医疗领域的MRC/QA系统是近年来应用研究的热点。研究涵盖了从通用医疗信息提取到特定专科的深度应用：
*   **通用与特定疾病**：开发了高效的MRC算法用于从病历中提取癫痫发作频率等关键信息 [23]，并从弱结构的放射科报告中提取信息 [26]。此外，还有研究致力于从医学影像报告中识别中风诊断相关特征，以辅助临床决策 [28]。
*   **知识增强**：通过知识增强的阅读理解方法进行生物医学关系抽取 [24]，以及构建多维公理模糊集知识图谱用于开放域问答 [21]。
*   **中文医疗特定模型**：针对中文医疗文本，提出了基于层级协作Transformer的问答模型（HCT） [9]，以及用于中文医疗文本匹配的胶囊网络（CapsTM） [25]。
*   **大模型与生成式AI**：随着大语言模型（LLM）的兴起，针对生物医学问答的ChatGPT类应用得到了全面回顾 [17]。在中医药领域，TCMChat等生成式大语言模型被专门开发以服务于传统中医问答 [29]。

**4. 多语言与低资源语言的发展**
除了英语和中文，其他语言的MRC资源也在丰富。孟加拉语（Bangla）方面，研究者发布了NOIRBETTIK和UDDIPOK两个基于阅读理解的多选题问答数据集 [11], [12]，并构建了基于Transformer的孟加拉语阅读理解问答系统 [13]。在越南语方面，构建了基于话语-论证混合系统的“为什么”类问答系统 [15]，以及越南语口语问答的基准数据集ViSQA [16]。此外，针对阿拉伯语的开放域问答也提出了基于深度学习的方法 [20]。

**5. 可解释性与评估基准**
可解释性是MRC模型落地的关键。研究对MRC模型进行了多语言、多方面的可解释性分析 [7]。在评估方面，ScienceQA等资源被创建用于学术文章的问答评估 [19]，而HQA-Data数据集则通过历史多视角对话生成问题，丰富了问答数据的多样性 [27]。

**6. 人机交互与阅读能力提升**
从更广泛的角度看，研究也关注AI如何辅助人类阅读。例如，基于人机交互策略被提出用于改善文本阅读能力 [22]，同时也有研究探讨读者和文本特征对六年级学生推理能力的影响，这为理解人类与AI在阅读理解中的差异提供了参考 [10]。

综上所述，最新的MRC与QA研究正从单一的文本匹配向多粒度、多模态、知识增强以及垂直领域深度应用转变，同时高度重视模型的可解释性、处理歧义的能力以及多语言资源的构建。

[1] Exploring unanswerability in machine reading comprehension: approaches, benchmarks, and open challenges. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41312427

[2] Resolving passage ambiguity in machine reading comprehension using lightweight transformer architectures. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41309905

[3] On solving textual ambiguities and semantic vagueness in MRC based question answering using generative pre-trained transformers. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/37547420

[4] MGRC: An End-to-End Multigranularity Reading Comprehension Model for Question Answering. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/34478387

[5] RCVQA: Visual question answering model based on reading comprehension. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/41349178

[6] Discourse-Aware Language Representation. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41086082

[7] Multilingual multi-aspect explainability analyses on machine reading comprehension models. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/35465050

[8] Efficient Machine Reading Comprehension for Health Care Applications: Algorithm Development and Validation of a Context Extraction Approach. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/38526545

[9] HCT: Chinese Medical Machine Reading Comprehension Question-Answering via Hierarchically Collaborative Transformer. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/38381639

[10] The influence of reader and text characteristics on sixth graders' inference making. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41394219

[11] NOIRBETTIK: A reading comprehension based multiple choice question answering dataset in Bangla language. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/40103763

[12] UDDIPOK: A reading comprehension based question answering dataset in Bangla language. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/36819905

[13] Reading comprehension based question answering system in Bangla language with transformer-based learning. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/36254291

[14] Analysis of English Multitext Reading Comprehension Model Based on Deep Belief Neural Network. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/34567102

[15] Building a Discourse-Argument Hybrid System for Vietnamese Why-Question Answering. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/34992649

[16] ViSQA: A benchmark dataset and baseline models for Vietnamese spoken question answering. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41525409

[17] Developing ChatGPT for biology and medicine: a complete review of biomedical question answering. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/39027317

[18] Visual Explanation for Open-Domain Question Answering With BERT. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/37027746

[19] ScienceQA: a novel resource for question answering on scholarly articles. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/35873651

[20] Deep learning-based approach for Arabic open domain question answering. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/35634104

[21] AFS Graph: Multidimensional Axiomatic Fuzzy Set Knowledge Graph for Open-Domain Question Answering. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/35544488

[22] Strategies for Improving Text Reading Ability Based on Human-Computer Interaction in Artificial Intelligence. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/35360634

[23] Extracting seizure frequency from epilepsy clinic notes: a machine reading approach to natural language processing. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/35190834

[24] Biomedical relation extraction via knowledge-enhanced reading comprehension. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/34991458

[25] CapsTM: capsule network for Chinese medical text matching. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/34330253

[26] Information extraction from weakly structured radiological reports with natural language queries. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/37505252

[27] HQA-Data: A historical question answer generation dataset from previous multi perspective conversation. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/37383776

[28] Identifying stroke diagnosis-related features from medical imaging reports to improve clinical decision-making support. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/36266650

[29] TCMChat: A generative large language model for traditional Chinese medicine. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/39617279




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 机器阅读理解与问答系统的最新科研进展
2. 2024-2026年机器阅读理解与问答系统（MRC & QA）的最新科研进展、关键模型架构及评测基准更新

 #### Iteration 2:
1. 2025年至2026年间，基于大型语言模型（LLM）的机器阅读理解系统在处理长上下文依赖、复杂多跳推理及幻觉抑制方面的具体架构创新（如新型Agent框架或推理增强机制）有哪些最新突破？

 #### Iteration 3:
1. 2025年至2026年间，针对机器阅读理解（MRC）与问答系统在处理极度长上下文（如100k+ tokens）时的计算效率瓶颈，基于混合注意力机制或线性注意力近似（如Mamba/SSM架构）的最新模型在保持推理精度与降低显存占用方面取得了哪些具体的量化突破及开源基准测试结果？



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
机器阅读理解与问答系统的最新科研进展



Searched with 2 questions, found 87 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
机器阅读理解与问答系统的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
机器阅读理解与问答系统的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
机器阅读理解与问答系统的最新科研进展



基于提供的文献资料，机器阅读理解（Machine Reading Comprehension, MRC）与问答系统（Question Answering, QA）的最新科研进展主要集中在解决文本歧义性、多粒度理解、特定领域（尤其是医疗）的应用、多模态融合以及低资源语言模型的构建等方面。以下是对这些进展的详细综述：

**1. 处理文本歧义性与语义模糊性**
随着预训练语言模型的发展，解决MRC中的文本歧义和语义模糊性成为研究重点。研究者指出，利用生成式预训练Transformer（Generative Pre-trained Transformers）可以有效解决基于MRC的问答中的文本歧义性和语义模糊性问题 [3]。此外，为了更精确地解析段落中的歧义，轻量级Transformer架构被提出并用于解决MRC中的段落歧义问题，这表明模型结构的小型化与精准化是当前的一个趋势 [2]。同时，针对“不可回答”情况（unanswerability）的探索也是关键进展之一，新的基准测试和方法正在被开发以评估模型在无法从文本中找到答案时的表现 [1]。

**2. 多粒度与跨模态理解**
在模型架构方面，端到端的多粒度阅读理解模型（MGRC）被提出，旨在通过不同粒度的信息交互来提升问答性能 [4]。在多模态领域，视觉问答（Visual Question Answering, VQA）与阅读理解的结合日益紧密。例如，RCVQA模型结合了视觉元素与阅读理解能力，增强了多模态问答的效果 [5]。此外，可视化解释技术也被应用于开放域问答系统中，利用BERT等模型提供可视化的推理依据，以提高系统的可解释性 [18]。

**3. 医疗与健康领域的垂直应用**
医疗领域的MRC/QA系统是近年来应用研究的热点。研究涵盖了从通用医疗信息提取到特定专科的深度应用：
*   **通用与特定疾病**：开发了高效的MRC算法用于从病历中提取癫痫发作频率等关键信息 [23]，并从弱结构的放射科报告中提取信息 [26]。此外，还有研究致力于从医学影像报告中识别中风诊断相关特征，以辅助临床决策 [28]。
*   **知识增强**：通过知识增强的阅读理解方法进行生物医学关系抽取 [24]，以及构建多维公理模糊集知识图谱用于开放域问答 [21]。
*   **中文医疗特定模型**：针对中文医疗文本，提出了基于层级协作Transformer的问答模型（HCT） [9]，以及用于中文医疗文本匹配的胶囊网络（CapsTM） [25]。
*   **大模型与生成式AI**：随着大语言模型（LLM）的兴起，针对生物医学问答的ChatGPT类应用得到了全面回顾 [17]。在中医药领域，TCMChat等生成式大语言模型被专门开发以服务于传统中医问答 [29]。

**4. 多语言与低资源语言的发展**
除了英语和中文，其他语言的MRC资源也在丰富。孟加拉语（Bangla）方面，研究者发布了NOIRBETTIK和UDDIPOK两个基于阅读理解的多选题问答数据集 [11], [12]，并构建了基于Transformer的孟加拉语阅读理解问答系统 [13]。在越南语方面，构建了基于话语-论证混合系统的“为什么”类问答系统 [15]，以及越南语口语问答的基准数据集ViSQA [16]。此外，针对阿拉伯语的开放域问答也提出了基于深度学习的方法 [20]。

**5. 可解释性与评估基准**
可解释性是MRC模型落地的关键。研究对MRC模型进行了多语言、多方面的可解释性分析 [7]。在评估方面，ScienceQA等资源被创建用于学术文章的问答评估 [19]，而HQA-Data数据集则通过历史多视角对话生成问题，丰富了问答数据的多样性 [27]。

**6. 人机交互与阅读能力提升**
从更广泛的角度看，研究也关注AI如何辅助人类阅读。例如，基于人机交互策略被提出用于改善文本阅读能力 [22]，同时也有研究探讨读者和文本特征对六年级学生推理能力的影响，这为理解人类与AI在阅读理解中的差异提供了参考 [10]。

综上所述，最新的MRC与QA研究正从单一的文本匹配向多粒度、多模态、知识增强以及垂直领域深度应用转变，同时高度重视模型的可解释性、处理歧义的能力以及多语言资源的构建。

### SOURCES USED IN THIS SECTION:
[1] Exploring unanswerability in machine reading comprehension: approaches, benchmarks, and open challenges. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41312427

[2] Resolving passage ambiguity in machine reading comprehension using lightweight transformer architectures. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41309905

[3] On solving textual ambiguities and semantic vagueness in MRC based question answering using generative pre-trained transformers. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/37547420

[4] MGRC: An End-to-End Multigranularity Reading Comprehension Model for Question Answering. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/34478387

[5] RCVQA: Visual question answering model based on reading comprehension. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/41349178

[6] Discourse-Aware Language Representation. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41086082

[7] Multilingual multi-aspect explainability analyses on machine reading comprehension models. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/35465050

[8] Efficient Machine Reading Comprehension for Health Care Applications: Algorithm Development and Validation of a Context Extraction Approach. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/38526545

[9] HCT: Chinese Medical Machine Reading Comprehension Question-Answering via Hierarchically Collaborative Transformer. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/38381639

[10] The influence of reader and text characteristics on sixth graders' inference making. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41394219

[11] NOIRBETTIK: A reading comprehension based multiple choice question answering dataset in Bangla language. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/40103763

[12] UDDIPOK: A reading comprehension based question answering dataset in Bangla language. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/36819905

[13] Reading comprehension based question answering system in Bangla language with transformer-based learning. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/36254291

[14] Analysis of English Multitext Reading Comprehension Model Based on Deep Belief Neural Network. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/34567102

[15] Building a Discourse-Argument Hybrid System for Vietnamese Why-Question Answering. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/34992649

[16] ViSQA: A benchmark dataset and baseline models for Vietnamese spoken question answering. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41525409

[17] Developing ChatGPT for biology and medicine: a complete review of biomedical question answering. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/39027317

[18] Visual Explanation for Open-Domain Question Answering With BERT. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/37027746

[19] ScienceQA: a novel resource for question answering on scholarly articles. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/35873651

[20] Deep learning-based approach for Arabic open domain question answering. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/35634104

[21] AFS Graph: Multidimensional Axiomatic Fuzzy Set Knowledge Graph for Open-Domain Question Answering. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/35544488

[22] Strategies for Improving Text Reading Ability Based on Human-Computer Interaction in Artificial Intelligence. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/35360634

[23] Extracting seizure frequency from epilepsy clinic notes: a machine reading approach to natural language processing. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/35190834

[24] Biomedical relation extraction via knowledge-enhanced reading comprehension. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/34991458

[25] CapsTM: capsule network for Chinese medical text matching. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/34330253

[26] Information extraction from weakly structured radiological reports with natural language queries. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/37505252

[27] HQA-Data: A historical question answer generation dataset from previous multi perspective conversation. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/37383776

[28] Identifying stroke diagnosis-related features from medical imaging reports to improve clinical decision-making support. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/36266650

[29] TCMChat: A generative large language model for traditional Chinese medicine. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/39617279




________________________________________________________________________________

## ALL SOURCES:
[1] Exploring unanswerability in machine reading comprehension: approaches, benchmarks, and open challenges. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41312427

[2] Resolving passage ambiguity in machine reading comprehension using lightweight transformer architectures. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41309905

[3] On solving textual ambiguities and semantic vagueness in MRC based question answering using generative pre-trained transformers. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/37547420

[4] MGRC: An End-to-End Multigranularity Reading Comprehension Model for Question Answering. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/34478387

[5] RCVQA: Visual question answering model based on reading comprehension. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/41349178

[6] Discourse-Aware Language Representation. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41086082

[7] Multilingual multi-aspect explainability analyses on machine reading comprehension models. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/35465050

[8] Efficient Machine Reading Comprehension for Health Care Applications: Algorithm Development and Validation of a Context Extraction Approach. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/38526545

[9] HCT: Chinese Medical Machine Reading Comprehension Question-Answering via Hierarchically Collaborative Transformer. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/38381639

[10] The influence of reader and text characteristics on sixth graders' inference making. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41394219

[11] NOIRBETTIK: A reading comprehension based multiple choice question answering dataset in Bangla language. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/40103763

[12] UDDIPOK: A reading comprehension based question answering dataset in Bangla language. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/36819905

[13] Reading comprehension based question answering system in Bangla language with transformer-based learning. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/36254291

[14] Analysis of English Multitext Reading Comprehension Model Based on Deep Belief Neural Network. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/34567102

[15] Building a Discourse-Argument Hybrid System for Vietnamese Why-Question Answering. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/34992649

[16] ViSQA: A benchmark dataset and baseline models for Vietnamese spoken question answering. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41525409

[17] Developing ChatGPT for biology and medicine: a complete review of biomedical question answering. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/39027317

[18] Visual Explanation for Open-Domain Question Answering With BERT. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/37027746

[19] ScienceQA: a novel resource for question answering on scholarly articles. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/35873651

[20] Deep learning-based approach for Arabic open domain question answering. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/35634104

[21] AFS Graph: Multidimensional Axiomatic Fuzzy Set Knowledge Graph for Open-Domain Question Answering. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/35544488

[22] Strategies for Improving Text Reading Ability Based on Human-Computer Interaction in Artificial Intelligence. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/35360634

[23] Extracting seizure frequency from epilepsy clinic notes: a machine reading approach to natural language processing. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/35190834

[24] Biomedical relation extraction via knowledge-enhanced reading comprehension. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/34991458

[25] CapsTM: capsule network for Chinese medical text matching. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/34330253

[26] Information extraction from weakly structured radiological reports with natural language queries. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/37505252

[27] HQA-Data: A historical question answer generation dataset from previous multi perspective conversation. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/37383776

[28] Identifying stroke diagnosis-related features from medical imaging reports to improve clinical decision-making support. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/36266650

[29] TCMChat: A generative large language model for traditional Chinese medicine. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/39617279


