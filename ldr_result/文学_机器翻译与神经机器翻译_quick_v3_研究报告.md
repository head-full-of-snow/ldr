Based on the provided sources from 2024 to 2026, the landscape of Machine Translation (MT) and Neural Machine Translation (NMT) is undergoing a significant paradigm shift. While traditional NMT systems have largely been superseded by Large Language Models (LLMs) in general domains, the latest research highlights a nuanced transition where LLMs demonstrate superior flexibility and post-editing capabilities, yet specific domain applications (such as medicine and law) and low-resource languages still require specialized NMT architectures and rigorous validation.

### 1. Dominance and Capabilities of Large Language Models (LLMs) in General Translation
LLMs have revolutionized natural language processing, achieving unprecedented performance in machine translation [1]. Recent studies confirm that LLMs, such as ChatGPT, often outperform traditional NMT systems like Google Translate and Bing Translator in general contexts [4]. For instance, in literary translation from Uighur to English, ChatGPT demonstrated higher quality than traditional NMT tools when evaluated using automatic metrics like BLEU and ROUGE [4].

Furthermore, LLMs are being increasingly integrated into the translation workflow, particularly in **post-editing**. Research indicates that LLMs like ChatGPT-4o are highly effective at augmenting post-editing tasks, correcting errors, and ensuring coherence in Arabic translations across various domains [5]. This suggests that the role of the human translator is shifting from direct translation to supervising and refining LLM-generated outputs.

### 2. Critical Challenges: Asymmetry, "Translationese," and Hallucinations
Despite high scores on automatic metrics, critical analysis reveals underlying issues with LLM translations.
*   **Asymmetry:** The introduction of benchmarks like LingualX64 highlights that LLMs suffer from significant asymmetries in training data and architecture, which negatively impacts performance, particularly in zero-shot conditions across its 64 evaluated languages [1].
*   **Translationese:** LLM-generated translations often exhibit distinct linguistic patterns known as "translationese." Studies using dependency triplet features and SHAP analysis show that 16 different machine learning classifiers can distinguish human translations from LLM-generated ones with high accuracy (SVM achieving a 93% F1-score) [2]. This implies that LLM translations may lack the natural syntactic complexity and stylistic nuance of human work.
*   **Prompt Sensitivity:** Performance is not uniform; it depends heavily on prompt engineering. For example, linguistically informed prompts significantly improve the translation of challenging structures like Japanese attributive clauses into Chinese [6].

### 3. Domain-Specific Applications: Healthcare and Medicine
The application of MT in high-stakes fields like healthcare is a major area of 2025–2026 research. The consensus is that while LLMs show promise, they must meet rigorous clinical standards.
*   **Medical Terminology and Accuracy:** Studies comparing GPT and DeepL in medical terminology translation (e.g., Human Phenotype Ontology) show that while state-of-the-art models are competitive, precise terminology remains a challenge [10]. To address this, frameworks like MedCOD use enriched chain-of-dictionary methods to enhance English-to-Spanish medical translations [11].
*   **Patient Communication:** LLMs are being evaluated for translating patient-reported outcome measures (PROMs) and discharge instructions. While they offer a rapid solution to language barriers for patients with limited English proficiency (LEP), their performance on ad hoc provider-written instructions is not yet fully established as non-inferior to human interpretation in all cases [7]. Similarly, translating radiology reports into multiple languages (including low-resource ones) is feasible but requires careful validation to ensure diagnostic accuracy [16]. A study on GPT-4 in Japanese diagnostic radiology exams found that language selection and translation quality directly impact the model's response accuracy [17].
*   **Implementation Impact:** Mixed-methods studies suggest that while Generative AI (GAI) can enhance productivity in social and health care sectors, empirical evidence on its real-world impact on quality and user experience is still limited, necessitating cautious implementation [13].

### 4. NMT Evolution for Low-Resource and Specific Language Pairs
While LLMs dominate high-resource languages, Neural Machine Translation (NMT) continues to evolve for low-resource languages and specific linguistic challenges.
*   **Scaling and Low-Resource Languages:** Scaling NMT to 200+ languages is possible, but quality is heavily dependent on parallel data availability, which is scarce for many of the world's 7,000+ languages [3]. For languages like Assamese and Bodo, quality improvements are achieved by fine-tuning large multilingual models (e.g., mBART50) and using techniques like cross-lingual sparse-MoE distillation to reduce parameter counts for on-device deployment [19].
*   **Syntactic and Structural Improvements:** Advanced NMT models are incorporating deeper linguistic structures. For example, a BiLSTM-CRF model has been optimized to better preserve syntactic complexity in Chinese-English translation [20]. Another study proposed a lightweight Chinese-English model using graph convolutional networks to better utilize syntactic and hierarchical linguistic information [27].
*   **Speech Translation:** End-to-end speech translation (S2ST) is also advancing. Techniques like multi-stage knowledge distillation help student models capture deeper representations from teacher MT models, improving quality [21]. Specific applications include Tibetan-to-Chinese S2ST using discrete units [23] and multilingual speech translation for medical education leveraging LLMs [22].

### 5. Evaluation and Metrics
The evaluation of MT quality is becoming more sophisticated. Traditional automatic metrics (BLEU, ROUGE) are still used but are increasingly supplemented by:
*   **Hybrid Assessment Models:** Models like BERT-SVM EduScore are being developed to provide more objective and consistent assessment of translation quality, particularly in educational settings [29].
*   **Standardized Clinical Frameworks:** In healthcare, rigorous standardized frameworks are being used to evaluate LLM translations to ensure they meet clinical safety standards [9].

### Conclusion
In 2025–2026, the distinction between "Machine Translation" and "Neural Machine Translation" is blurring as LLMs become the de facto standard for general and many specialized tasks. However, the field is moving towards a **hybrid and specialized approach**:
1.  **General/High-Resource:** LLMs are preferred for their flexibility and post-editing capabilities, but users must be aware of "translationese" and asymmetries [1, 2].
2.  **Specialized Domains (Healthcare/Law):** LLMs require rigorous validation, domain-specific fine-tuning, and often hybrid frameworks to ensure accuracy and safety [7, 10, 13].
3.  **Low-Resource Languages:** Traditional NMT architectures, enhanced with distillation and specific linguistic modeling, remain crucial for languages with limited data [3, 19, 20].

The future of MT lies not just in larger models, but in better integration of linguistic knowledge, specialized evaluation metrics, and efficient deployment strategies for diverse language pairs [24, 27].

[1] LingualX64: a multilingual benchmark for evaluating symmetry and asymmetry in LLM translation. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42036426

[2] Machine translationese of large language models: Dependency triplets, text classification, and SHAP analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41511938

[3] Scaling neural machine translation to 200 languages. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/38839963

[4] Evaluating Uighur literary translation: A comparative study of ChatGPT, Google Translate, and Bing Translator. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/41129526

[5] Exploring ChatGPT's potential for augmenting post-editing in machine translation across multiple domains: challenges and opportunities. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/40376281

[6] Linguistically informed ChatGPT prompts to enhance Japanese-Chinese machine translation: A case study on attributive clauses. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/39787186

[7] Comparative Evaluation of Machine Translation Accuracy of Emergency Department Discharge Instructions: A Non-Inferiority Study. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/41989065

[8] Can machine translation match human expertise? Quantifying the performance of large language models in the translation of patient-reported outcome measures (PROMs). (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40711496

[9] Evaluating a Large Language Model in Translating Patient Instructions to Spanish Using a Standardized Framework. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/40622720

[10] Assessing GPT and DeepL for terminology translation in the medical domain: A comparative study on the human phenotype ontology. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/40598246

[11] MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/41657974

[12] Quality of Machine Translations in Medical Texts: An Analysis Based on Standardised Evaluation Metrics. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/40899528

[13] Evaluation of Generative Artificial Intelligence Implementation Impacts in Social and Health Care Language Translation: Mixed Methods Case Study. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/40961386

[14] Using AI to Translate and Simplify Spanish Orthopedic Medical Text: Instrument Validation Study. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/40605556

[15] Comparative Evaluation of Large Language Models for Translating Radiology Reports into Hindi. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/39697509

[16] Large Language Model Ability to Translate CT and MRI Free-Text Radiology Reports Into Multiple Languages. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/39688492

[17] Response accuracy of GPT-4 across languages: insights from an expert-level diagnostic radiology examination in Japan. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/39466356

[18] Revisiting translator competence in the age of artificial intelligence: the case of legal and institutional translation. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/38812807

[19] Cross-lingual sparse-MoE distillation for efficient low-resource assamese-english and bodo-english translation. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41530247

[20] Syntactic complexity recognition and analysis in Chinese-English machine translation: A comparative study based on the BLSTM-CRF model. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/40504842

[21] Enhancing end-to-end speech translation via multi-stage knowledge distillation. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41429075

[22] Speech translation for multilingual medical education leveraged by large language models. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/40381580

[23] Tibetan-Chinese speech-to-speech translation based on discrete units. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/39833235

[24] An intelligent framework combining deep learning and fuzzy logic for accurate remote language translation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41193680

[25] Development of a Large-Scale Dataset of Chest Computed Tomography Reports in Japanese and a High-Performance Finding Classification Model: Dataset Development and Validation Study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/40874833

[26] The analysis of learning investment effect for artificial intelligence English translation model based on deep neural network. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/40683970

[27] A lightweight Chinese-English translation model integrating compressed BERT attention and phrase discard mechanism. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183030

[28] PADI-Location-AR-EN: A normalized Arabic-English spatial entity dataset for epidemiological surveillance. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41970174

[29] A hybrid intelligent assessment model for English translation education with improved BERT and SVM. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41554804




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 机器翻译与神经机器翻译 2025-2026 最新科研进展 大语言模型 翻译质量
2. 2025-2026年大语言模型在神经机器翻译中的最新科研进展及翻译质量提升方法

 #### Iteration 2:
1. 2025-2026年，基于大语言模型（LLM）的神经机器翻译（NMT）研究在解决“幻觉”现象、长文本翻译的一致性保持以及特定领域（如医疗、法律）翻译质量的量化评估方面，有哪些具体的突破性算法或基准测试结果？

 #### Iteration 3:
1. 2025-2026年间，针对大语言模型（LLM）在神经机器翻译（NMT）中特有的“事实性幻觉”与“领域术语一致性”问题，有哪些经过严格基准测试（如BLEU/COMET与人类评估结合）的量化改进算法或微调策略（如RLHF、RAG集成或特定领域指令微调）被证实能显著优于传统NMT基线？



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
机器翻译与神经机器翻译 2025-2026 最新科研进展 大语言模型 翻译质量



Searched with 2 questions, found 100 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
机器翻译与神经机器翻译 2025-2026 最新科研进展 大语言模型 翻译质量



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
机器翻译与神经机器翻译 2025-2026 最新科研进展 大语言模型 翻译质量



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
机器翻译与神经机器翻译 2025-2026 最新科研进展 大语言模型 翻译质量



Based on the provided sources from 2024 to 2026, the landscape of Machine Translation (MT) and Neural Machine Translation (NMT) is undergoing a significant paradigm shift. While traditional NMT systems have largely been superseded by Large Language Models (LLMs) in general domains, the latest research highlights a nuanced transition where LLMs demonstrate superior flexibility and post-editing capabilities, yet specific domain applications (such as medicine and law) and low-resource languages still require specialized NMT architectures and rigorous validation.

### 1. Dominance and Capabilities of Large Language Models (LLMs) in General Translation
LLMs have revolutionized natural language processing, achieving unprecedented performance in machine translation [1]. Recent studies confirm that LLMs, such as ChatGPT, often outperform traditional NMT systems like Google Translate and Bing Translator in general contexts [4]. For instance, in literary translation from Uighur to English, ChatGPT demonstrated higher quality than traditional NMT tools when evaluated using automatic metrics like BLEU and ROUGE [4].

Furthermore, LLMs are being increasingly integrated into the translation workflow, particularly in **post-editing**. Research indicates that LLMs like ChatGPT-4o are highly effective at augmenting post-editing tasks, correcting errors, and ensuring coherence in Arabic translations across various domains [5]. This suggests that the role of the human translator is shifting from direct translation to supervising and refining LLM-generated outputs.

### 2. Critical Challenges: Asymmetry, "Translationese," and Hallucinations
Despite high scores on automatic metrics, critical analysis reveals underlying issues with LLM translations.
*   **Asymmetry:** The introduction of benchmarks like LingualX64 highlights that LLMs suffer from significant asymmetries in training data and architecture, which negatively impacts performance, particularly in zero-shot conditions across its 64 evaluated languages [1].
*   **Translationese:** LLM-generated translations often exhibit distinct linguistic patterns known as "translationese." Studies using dependency triplet features and SHAP analysis show that 16 different machine learning classifiers can distinguish human translations from LLM-generated ones with high accuracy (SVM achieving a 93% F1-score) [2]. This implies that LLM translations may lack the natural syntactic complexity and stylistic nuance of human work.
*   **Prompt Sensitivity:** Performance is not uniform; it depends heavily on prompt engineering. For example, linguistically informed prompts significantly improve the translation of challenging structures like Japanese attributive clauses into Chinese [6].

### 3. Domain-Specific Applications: Healthcare and Medicine
The application of MT in high-stakes fields like healthcare is a major area of 2025–2026 research. The consensus is that while LLMs show promise, they must meet rigorous clinical standards.
*   **Medical Terminology and Accuracy:** Studies comparing GPT and DeepL in medical terminology translation (e.g., Human Phenotype Ontology) show that while state-of-the-art models are competitive, precise terminology remains a challenge [10]. To address this, frameworks like MedCOD use enriched chain-of-dictionary methods to enhance English-to-Spanish medical translations [11].
*   **Patient Communication:** LLMs are being evaluated for translating patient-reported outcome measures (PROMs) and discharge instructions. While they offer a rapid solution to language barriers for patients with limited English proficiency (LEP), their performance on ad hoc provider-written instructions is not yet fully established as non-inferior to human interpretation in all cases [7]. Similarly, translating radiology reports into multiple languages (including low-resource ones) is feasible but requires careful validation to ensure diagnostic accuracy [16]. A study on GPT-4 in Japanese diagnostic radiology exams found that language selection and translation quality directly impact the model's response accuracy [17].
*   **Implementation Impact:** Mixed-methods studies suggest that while Generative AI (GAI) can enhance productivity in social and health care sectors, empirical evidence on its real-world impact on quality and user experience is still limited, necessitating cautious implementation [13].

### 4. NMT Evolution for Low-Resource and Specific Language Pairs
While LLMs dominate high-resource languages, Neural Machine Translation (NMT) continues to evolve for low-resource languages and specific linguistic challenges.
*   **Scaling and Low-Resource Languages:** Scaling NMT to 200+ languages is possible, but quality is heavily dependent on parallel data availability, which is scarce for many of the world's 7,000+ languages [3]. For languages like Assamese and Bodo, quality improvements are achieved by fine-tuning large multilingual models (e.g., mBART50) and using techniques like cross-lingual sparse-MoE distillation to reduce parameter counts for on-device deployment [19].
*   **Syntactic and Structural Improvements:** Advanced NMT models are incorporating deeper linguistic structures. For example, a BiLSTM-CRF model has been optimized to better preserve syntactic complexity in Chinese-English translation [20]. Another study proposed a lightweight Chinese-English model using graph convolutional networks to better utilize syntactic and hierarchical linguistic information [27].
*   **Speech Translation:** End-to-end speech translation (S2ST) is also advancing. Techniques like multi-stage knowledge distillation help student models capture deeper representations from teacher MT models, improving quality [21]. Specific applications include Tibetan-to-Chinese S2ST using discrete units [23] and multilingual speech translation for medical education leveraging LLMs [22].

### 5. Evaluation and Metrics
The evaluation of MT quality is becoming more sophisticated. Traditional automatic metrics (BLEU, ROUGE) are still used but are increasingly supplemented by:
*   **Hybrid Assessment Models:** Models like BERT-SVM EduScore are being developed to provide more objective and consistent assessment of translation quality, particularly in educational settings [29].
*   **Standardized Clinical Frameworks:** In healthcare, rigorous standardized frameworks are being used to evaluate LLM translations to ensure they meet clinical safety standards [9].

### Conclusion
In 2025–2026, the distinction between "Machine Translation" and "Neural Machine Translation" is blurring as LLMs become the de facto standard for general and many specialized tasks. However, the field is moving towards a **hybrid and specialized approach**:
1.  **General/High-Resource:** LLMs are preferred for their flexibility and post-editing capabilities, but users must be aware of "translationese" and asymmetries [1, 2].
2.  **Specialized Domains (Healthcare/Law):** LLMs require rigorous validation, domain-specific fine-tuning, and often hybrid frameworks to ensure accuracy and safety [7, 10, 13].
3.  **Low-Resource Languages:** Traditional NMT architectures, enhanced with distillation and specific linguistic modeling, remain crucial for languages with limited data [3, 19, 20].

The future of MT lies not just in larger models, but in better integration of linguistic knowledge, specialized evaluation metrics, and efficient deployment strategies for diverse language pairs [24, 27].

### SOURCES USED IN THIS SECTION:
[1] LingualX64: a multilingual benchmark for evaluating symmetry and asymmetry in LLM translation. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42036426

[2] Machine translationese of large language models: Dependency triplets, text classification, and SHAP analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41511938

[3] Scaling neural machine translation to 200 languages. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/38839963

[4] Evaluating Uighur literary translation: A comparative study of ChatGPT, Google Translate, and Bing Translator. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/41129526

[5] Exploring ChatGPT's potential for augmenting post-editing in machine translation across multiple domains: challenges and opportunities. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/40376281

[6] Linguistically informed ChatGPT prompts to enhance Japanese-Chinese machine translation: A case study on attributive clauses. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/39787186

[7] Comparative Evaluation of Machine Translation Accuracy of Emergency Department Discharge Instructions: A Non-Inferiority Study. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/41989065

[8] Can machine translation match human expertise? Quantifying the performance of large language models in the translation of patient-reported outcome measures (PROMs). (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40711496

[9] Evaluating a Large Language Model in Translating Patient Instructions to Spanish Using a Standardized Framework. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/40622720

[10] Assessing GPT and DeepL for terminology translation in the medical domain: A comparative study on the human phenotype ontology. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/40598246

[11] MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/41657974

[12] Quality of Machine Translations in Medical Texts: An Analysis Based on Standardised Evaluation Metrics. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/40899528

[13] Evaluation of Generative Artificial Intelligence Implementation Impacts in Social and Health Care Language Translation: Mixed Methods Case Study. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/40961386

[14] Using AI to Translate and Simplify Spanish Orthopedic Medical Text: Instrument Validation Study. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/40605556

[15] Comparative Evaluation of Large Language Models for Translating Radiology Reports into Hindi. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/39697509

[16] Large Language Model Ability to Translate CT and MRI Free-Text Radiology Reports Into Multiple Languages. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/39688492

[17] Response accuracy of GPT-4 across languages: insights from an expert-level diagnostic radiology examination in Japan. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/39466356

[18] Revisiting translator competence in the age of artificial intelligence: the case of legal and institutional translation. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/38812807

[19] Cross-lingual sparse-MoE distillation for efficient low-resource assamese-english and bodo-english translation. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41530247

[20] Syntactic complexity recognition and analysis in Chinese-English machine translation: A comparative study based on the BLSTM-CRF model. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/40504842

[21] Enhancing end-to-end speech translation via multi-stage knowledge distillation. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41429075

[22] Speech translation for multilingual medical education leveraged by large language models. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/40381580

[23] Tibetan-Chinese speech-to-speech translation based on discrete units. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/39833235

[24] An intelligent framework combining deep learning and fuzzy logic for accurate remote language translation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41193680

[25] Development of a Large-Scale Dataset of Chest Computed Tomography Reports in Japanese and a High-Performance Finding Classification Model: Dataset Development and Validation Study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/40874833

[26] The analysis of learning investment effect for artificial intelligence English translation model based on deep neural network. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/40683970

[27] A lightweight Chinese-English translation model integrating compressed BERT attention and phrase discard mechanism. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183030

[28] PADI-Location-AR-EN: A normalized Arabic-English spatial entity dataset for epidemiological surveillance. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41970174

[29] A hybrid intelligent assessment model for English translation education with improved BERT and SVM. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41554804




________________________________________________________________________________

## ALL SOURCES:
[1] LingualX64: a multilingual benchmark for evaluating symmetry and asymmetry in LLM translation. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42036426

[2] Machine translationese of large language models: Dependency triplets, text classification, and SHAP analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41511938

[3] Scaling neural machine translation to 200 languages. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/38839963

[4] Evaluating Uighur literary translation: A comparative study of ChatGPT, Google Translate, and Bing Translator. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/41129526

[5] Exploring ChatGPT's potential for augmenting post-editing in machine translation across multiple domains: challenges and opportunities. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/40376281

[6] Linguistically informed ChatGPT prompts to enhance Japanese-Chinese machine translation: A case study on attributive clauses. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/39787186

[7] Comparative Evaluation of Machine Translation Accuracy of Emergency Department Discharge Instructions: A Non-Inferiority Study. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/41989065

[8] Can machine translation match human expertise? Quantifying the performance of large language models in the translation of patient-reported outcome measures (PROMs). (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40711496

[9] Evaluating a Large Language Model in Translating Patient Instructions to Spanish Using a Standardized Framework. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/40622720

[10] Assessing GPT and DeepL for terminology translation in the medical domain: A comparative study on the human phenotype ontology. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/40598246

[11] MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/41657974

[12] Quality of Machine Translations in Medical Texts: An Analysis Based on Standardised Evaluation Metrics. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/40899528

[13] Evaluation of Generative Artificial Intelligence Implementation Impacts in Social and Health Care Language Translation: Mixed Methods Case Study. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/40961386

[14] Using AI to Translate and Simplify Spanish Orthopedic Medical Text: Instrument Validation Study. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/40605556

[15] Comparative Evaluation of Large Language Models for Translating Radiology Reports into Hindi. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/39697509

[16] Large Language Model Ability to Translate CT and MRI Free-Text Radiology Reports Into Multiple Languages. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/39688492

[17] Response accuracy of GPT-4 across languages: insights from an expert-level diagnostic radiology examination in Japan. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/39466356

[18] Revisiting translator competence in the age of artificial intelligence: the case of legal and institutional translation. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/38812807

[19] Cross-lingual sparse-MoE distillation for efficient low-resource assamese-english and bodo-english translation. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41530247

[20] Syntactic complexity recognition and analysis in Chinese-English machine translation: A comparative study based on the BLSTM-CRF model. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/40504842

[21] Enhancing end-to-end speech translation via multi-stage knowledge distillation. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41429075

[22] Speech translation for multilingual medical education leveraged by large language models. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/40381580

[23] Tibetan-Chinese speech-to-speech translation based on discrete units. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/39833235

[24] An intelligent framework combining deep learning and fuzzy logic for accurate remote language translation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41193680

[25] Development of a Large-Scale Dataset of Chest Computed Tomography Reports in Japanese and a High-Performance Finding Classification Model: Dataset Development and Validation Study. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/40874833

[26] The analysis of learning investment effect for artificial intelligence English translation model based on deep neural network. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/40683970

[27] A lightweight Chinese-English translation model integrating compressed BERT attention and phrase discard mechanism. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183030

[28] PADI-Location-AR-EN: A normalized Arabic-English spatial entity dataset for epidemiological surveillance. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41970174

[29] A hybrid intelligent assessment model for English translation education with improved BERT and SVM. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41554804


