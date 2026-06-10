Based on the provided sources from 2023 to 2026, the research landscape of Machine Translation (MT) and Neural Machine Translation (NMT) has shifted from general linguistic accuracy to addressing specific domain challenges, ethical biases, efficiency constraints, and the integration of Large Language Models (LLMs). The following analysis details the latest scientific progress in these areas.

### 1. Integration of Large Language Models and Multi-Agent Frameworks
Recent advancements highlight the transition from traditional NMT to LLM-driven architectures, particularly for complex or resource-scarce languages.

*   **Multi-Agent Frameworks:** For challenging domains like Classical Chinese, standard LLMs often fail to capture intricate semantic nuances and cultural specificities. To address this, a new framework proposes decomposing translation into word-level interpretation, paragraph-level generation, and multi-agent collaboration to improve accuracy and contextual fidelity [2].
*   **LLM Bias and Asymmetry:** While LLMs have revolutionized MT, they mask underlying asymmetries in training data and model architecture. The introduction of **LingualX64**, a benchmark spanning 64 languages, reveals significant performance disparities in zero-shot translation conditions, highlighting that progress in high-resource languages does not automatically translate to equitable performance across all linguistic groups [38].
*   **Psychological and Specialized Assessment:** LLMs are being evaluated for their potential in standardized psychological assessments, showing unprecedented accuracy in language processing tasks compared to traditional computerized methods [18].

### 2. Domain-Specific Applications: Healthcare and Clinical Data
A significant portion of recent research focuses on applying NMT in healthcare, where accuracy is critical and human interpreters are not always available.

*   **Clinical Implementation and Usability:** Systematic reviews indicate that while NMT shows promise in bridging language gaps for patients with non-English language preferences (NELP), its usability varies widely. Challenges include the lack of readily available interpreters and the need for robust evaluation of these tools in real-world clinical settings to prevent miscommunication and diagnostic errors [4], [9], [13].
*   **Low-Latency and Real-Time Processing:** For electronic clinical records in cancer therapy, there is a push toward using low-latency neural networks for real-time Named Entity Recognition (NER). This allows for immediate extraction of entities from unstructured medical data, facilitating faster decision-making in critical care environments [1].
*   **Multilingual Medical Datasets:** The development of high-performance models is hindered by a lack of large-scale, high-quality multilingual datasets. For instance, despite Japan's leadership in CT scanner deployment, the absence of large-scale Japanese radiology datasets has slowed the development of specialized medical language models, necessitating the creation of datasets like those for chest CT reports to enable better model training [5].
*   **Terminology Translation:** NMT is being used to automate the translation of standardized medical terminologies (e.g., SNOMED CT, RadLex). Studies compare machine translations against human-reviewed gold standards, showing that while machine translation can assist in localization projects (such as generating German translation candidates for SNOMED CT), it often requires post-editing to achieve clinical reliability [22], [27], [47].

### 3. Ethical Considerations: Bias and Gender
Research critically examines the ethical implications of NMT, particularly regarding bias.

*   **Gender Bias:** A comprehensive review of over a decade of studies on gender bias in MT reveals that the issue is more complex than initially thought. There is no simple technical fix for bias; persistent gaps remain despite societal and technological shifts. The review argues that bias is deeply embedded in linguistic structures and training data, requiring nuanced solutions beyond algorithmic adjustments [6], [57].
*   **Language Inclusion:** There is a growing recognition of the marginalization of research published in languages other than English (LOTE). Systematic reviews and scoping reviews are increasingly scrutinized for their inclusion of LOTE, as ignoring these sources limits global perspectives and evidence synthesis. Barriers to inclusion include resource limitations and author attitudes, highlighting the need for better translation tools to democratize scientific knowledge [3], [19], [20], [26].

### 4. Technical Advancements in NMT Architecture
Recent papers focus on improving the efficiency, speed, and robustness of NMT models.

*   **Non-Autoregressive (NAR) Generation:** To address the inference speed limitations of traditional autoregressive (AR) models, NAR generation techniques have been explored. While NAR significantly accelerates translation speed, it often sacrifices accuracy. Recent algorithms aim to balance this trade-off, improving the fidelity of NAR models [23], [44].
*   **Incorporating Templates and Rules:** Hybrid approaches are gaining traction. For example, incorporating bilingual translation templates into Transformer-based NMT models helps guide the translation process, mimicking human strategies and improving consistency in specific domains [40]. Similarly, optimizing hyperparameters using enhanced metaheuristic algorithms (like Grey Wolf Optimization) combined with self-attention and Bi-LSTM models has shown improvements in specialized fields like software engineering translation [39].
*   **Self-Supervised and Multimodal Learning:** To overcome the bottleneck of expensive human annotations, self-supervised multimodal learning is being adopted. This approach leverages large-scale unannotated data to pre-train models, which can then be adapted for NMT and other NLP tasks with less labeled data [15], [42].
*   **Evaluation Metrics:** Traditional evaluation metrics based on similarity to reference translations are being critiqued for language bias. New methods, such as clinical weighting for evaluating MeSH translations, provide a more nuanced assessment of translation quality by prioritizing clinically important terms [37], [54].

### 5. Resource-Scarce and Low-Resource Languages
Progress is also being made for languages with limited digital resources.

*   **Amharic-English Translation:** Systematic reviews of Amharic-English MT highlight the evolution from rule-based to neural approaches. However, challenges persist due to inadequate datasets and the complex semantics of Amharic, underscoring the need for more resource development [7].
*   **Bengali Lexicons:** For sentiment analysis and profanity detection in Bengali, new lexicons (BengSentiLex, BengSwearLex) have been created using cross-lingual transfer techniques, addressing the lack of native tools for NLP tasks in this low-resource language [28].

### Conclusion
The latest research in machine and neural machine translation demonstrates a maturation of the field. The focus has moved beyond basic translation accuracy to address **efficiency** (NAR models, low-latency networks), **domain specificity** (healthcare, clinical records), **ethics** (gender bias, language inclusion), and **robustness** (multi-agent LLMs, self-supervised learning). While LLMs offer powerful new capabilities, they introduce new challenges regarding bias and asymmetry, necessitating careful evaluation and hybrid approaches that combine neural networks with traditional linguistic knowledge and templates.

[1] Real-Time Named Entity Recognition from Textual Electronic Clinical Records in Cancer Therapy Using Low-Latency Neural Networks. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41649195

[2] A multi agent classical Chinese translation method based on large language models. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41249275

[3] Language inclusion intentions in scoping reviews. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/41229661

[4] Bridging language gaps in healthcare: a systematic review of the practical implementation of neural machine translation technologies in clinical settings. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/40966445

[5] Development of a Large-Scale Dataset of Chest Computed Tomography Reports in Japanese and a High-Performance Finding Classification Model: Dataset Development and Validation Study. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/40874833

[57, 6] A decade of gender bias in machine translation. (source nr: 57, 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/40575128

[7] Exploring the evolution and future prospects of Amharic to English machine translation: a systematic review. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/40486917

[8] Clinical document corpora-real ones, translated and synthetic substitutes, and assorted domain proxies: a survey of diversity in corpus design, with focus on German text data. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40371384

[9] Usability of technological tools to overcome language barriers in healthcare- a scoping review. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/40001263

[10] A systematic review of Machine Learning and Deep Learning approaches in Mexico: challenges and opportunities. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/39845096

[11] Visual insights into translation: demystifying trends of adopting eye-tracking techniques in translation studies. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/39654929

[12] Overview and challenges of machine translation for contextually appropriate translations. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/39391737

[13] Machine Translation Technology in Health: A Scoping Review. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/39320185

[14] A review of reinforcement learning for natural language processing and applications in healthcare. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/39208319

[15, 42] Self-Supervised Multimodal Learning: A Survey. (source nr: 15, 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/39110564

[16] Using Machine Translation and Post-Editing in the TRAPD Approach: Effects on the Quality of Translated Survey Texts. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/38617051

[17] Usability of technological tools to overcome language barriers in health care: a scoping review protocol. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/38458787

[18] Beyond rating scales: With targeted evaluation, large language models are poised for psychological assessment. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/38290286

[19] Language inclusion in ecological systematic reviews and maps: Barriers and perspectives. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/38286438

[20] The Use of Machine Translation for Outreach and Health Communication in Epidemiology and Public Health: Scoping Review. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/37983078

[21] What Are the English to Spanish Translation Methods Used on Written Health-Related Information? (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/37848223

[22] Machine translation of standardised medical terminology using natural language processing: A scoping review. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/37652265

[23, 44] A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond. (source nr: 23, 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/37200120

[24] Computational Methods for Single-cell Multi-omics Integration and Alignment. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/36581065

[25] How does artificial intelligence empower EFL teaching and learning nowadays? A review on artificial intelligence in the EFL context. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/36467167

[26] Overcoming Language Barriers in Academia: Machine Translation Tools and a Vision for a Multilingual Future. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/36196221

[27] Machine vs. Radiologist-Based Translations of RadLex: Implications for Multi-language Report Interoperability. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/35166969

[28] BengSentiLex and BengSwearLex: creating lexicons for sentiment analysis and profanity detection in low-resource Bengali language. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/34901419

[29] A review of the state-of-the-art in automatic post-editing. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/34720417

[30] Perceptions and knowledge of telemedicine in Ecuadorian practicing physicians: an instrument adaptation, validation and translation from English to Spanish. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/34600498

[31] Human versus machine editing of electronic prescription directions. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/33766549

[32] Development of machine translation technology for assisting health communication: A systematic review. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/30031857

[33, 52] A Bag of Concepts Approach for Biomedical Document Classification Using Wikipedia Knowledge*. Spanish-English Cross-language Case Study. (source nr: 33, 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/28816337

[34, 53] Integrating language models into classifiers for BCI communication: a review. (source nr: 34, 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/27153565

[35] Modeling workflow to design machine translation applications for public health practice. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/25445922

[36] A multi-lingual web service for drug side-effect data. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/20351818

[37] Clinically-weighted terms in the evaluation of MeSH translations: BabelMeSH in Portuguese as a model. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/18998783

[38] LingualX64: a multilingual benchmark for evaluating symmetry and asymmetry in LLM translation. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/42036426

[39] Optimizing software engineering English translation using an enhanced Grey Wolf Optimization with self-attention and Bi-LSTM model. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41073576

[40] Incorporating bilingual translation templates into neural machine translation. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/39953064

[41] Image-to-image machine translation enables computational defogging in real-world images. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/39573075

[43] Pre-trained language models in medicine: A survey. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/38917600

[45] Measuring the global response to antimicrobial resistance, 2020-21: a systematic governance analysis of 114 countries. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/36657475

[46] Concept recognition as a machine translation problem. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/34920707

[47] Automatic Generation of German Translation Candidates for SNOMED CT Textual Descriptions. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/34042729

[48] An Improved Sign Language Translation Model with Explainable Adaptations for Processing Long Sign Sentences. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/33163072

[49] Facile Solutions to the Problems Associated with Chemical Information and Mathematical Symbolism While Using Machine Translation Tools. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/32584030

[50] Automatic retrosynthetic route planning using template-free models. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/34122843

[51] Natural language generation for electronic health records. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/30687797

[54] Unsupervised quality estimation model for English to German translation and its application in extensive supervised evaluation. (source nr: 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/24892086

[55] Combining MEDLINE and publisher data to create parallel corpora for the automatic translation of biomedical text. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/23631733

[56] Low-Code/No-Code AI for Machine Translation: Democratising Generative AI for Blue Transformation. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/41728732

[58] A multimodal approach to cross-lingual sentiment analysis with ensemble of transformer and LLM. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/38671064

[59] Neural machine translation of clinical text: an empirical investigation into multilingual pre-trained language models and transfer-learning. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/38468693




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 机器翻译与神经机器翻译 最新科研进展
2. 2025-2026年机器翻译与神经机器翻译最新科研进展综述

 #### Iteration 2:
1. 2026年基于大语言模型（LLM）的神经机器翻译在低资源语言零样本翻译中的具体性能瓶颈及对称性偏差解决方案是什么？

 #### Iteration 3:
1. 2026年基于大语言模型（LLM）的神经机器翻译在应对多语言非对称性（如LingualX64基准所揭示的）时，具体的架构改进或训练策略是什么？



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
机器翻译与神经机器翻译 最新科研进展



Searched with 2 questions, found 55 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
机器翻译与神经机器翻译 最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
机器翻译与神经机器翻译 最新科研进展



Searched with 1 questions, found 4 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
机器翻译与神经机器翻译 最新科研进展



Based on the provided sources from 2023 to 2026, the research landscape of Machine Translation (MT) and Neural Machine Translation (NMT) has shifted from general linguistic accuracy to addressing specific domain challenges, ethical biases, efficiency constraints, and the integration of Large Language Models (LLMs). The following analysis details the latest scientific progress in these areas.

### 1. Integration of Large Language Models and Multi-Agent Frameworks
Recent advancements highlight the transition from traditional NMT to LLM-driven architectures, particularly for complex or resource-scarce languages.

*   **Multi-Agent Frameworks:** For challenging domains like Classical Chinese, standard LLMs often fail to capture intricate semantic nuances and cultural specificities. To address this, a new framework proposes decomposing translation into word-level interpretation, paragraph-level generation, and multi-agent collaboration to improve accuracy and contextual fidelity [2].
*   **LLM Bias and Asymmetry:** While LLMs have revolutionized MT, they mask underlying asymmetries in training data and model architecture. The introduction of **LingualX64**, a benchmark spanning 64 languages, reveals significant performance disparities in zero-shot translation conditions, highlighting that progress in high-resource languages does not automatically translate to equitable performance across all linguistic groups [38].
*   **Psychological and Specialized Assessment:** LLMs are being evaluated for their potential in standardized psychological assessments, showing unprecedented accuracy in language processing tasks compared to traditional computerized methods [18].

### 2. Domain-Specific Applications: Healthcare and Clinical Data
A significant portion of recent research focuses on applying NMT in healthcare, where accuracy is critical and human interpreters are not always available.

*   **Clinical Implementation and Usability:** Systematic reviews indicate that while NMT shows promise in bridging language gaps for patients with non-English language preferences (NELP), its usability varies widely. Challenges include the lack of readily available interpreters and the need for robust evaluation of these tools in real-world clinical settings to prevent miscommunication and diagnostic errors [4], [9], [13].
*   **Low-Latency and Real-Time Processing:** For electronic clinical records in cancer therapy, there is a push toward using low-latency neural networks for real-time Named Entity Recognition (NER). This allows for immediate extraction of entities from unstructured medical data, facilitating faster decision-making in critical care environments [1].
*   **Multilingual Medical Datasets:** The development of high-performance models is hindered by a lack of large-scale, high-quality multilingual datasets. For instance, despite Japan's leadership in CT scanner deployment, the absence of large-scale Japanese radiology datasets has slowed the development of specialized medical language models, necessitating the creation of datasets like those for chest CT reports to enable better model training [5].
*   **Terminology Translation:** NMT is being used to automate the translation of standardized medical terminologies (e.g., SNOMED CT, RadLex). Studies compare machine translations against human-reviewed gold standards, showing that while machine translation can assist in localization projects (such as generating German translation candidates for SNOMED CT), it often requires post-editing to achieve clinical reliability [22], [27], [47].

### 3. Ethical Considerations: Bias and Gender
Research critically examines the ethical implications of NMT, particularly regarding bias.

*   **Gender Bias:** A comprehensive review of over a decade of studies on gender bias in MT reveals that the issue is more complex than initially thought. There is no simple technical fix for bias; persistent gaps remain despite societal and technological shifts. The review argues that bias is deeply embedded in linguistic structures and training data, requiring nuanced solutions beyond algorithmic adjustments [6], [57].
*   **Language Inclusion:** There is a growing recognition of the marginalization of research published in languages other than English (LOTE). Systematic reviews and scoping reviews are increasingly scrutinized for their inclusion of LOTE, as ignoring these sources limits global perspectives and evidence synthesis. Barriers to inclusion include resource limitations and author attitudes, highlighting the need for better translation tools to democratize scientific knowledge [3], [19], [20], [26].

### 4. Technical Advancements in NMT Architecture
Recent papers focus on improving the efficiency, speed, and robustness of NMT models.

*   **Non-Autoregressive (NAR) Generation:** To address the inference speed limitations of traditional autoregressive (AR) models, NAR generation techniques have been explored. While NAR significantly accelerates translation speed, it often sacrifices accuracy. Recent algorithms aim to balance this trade-off, improving the fidelity of NAR models [23], [44].
*   **Incorporating Templates and Rules:** Hybrid approaches are gaining traction. For example, incorporating bilingual translation templates into Transformer-based NMT models helps guide the translation process, mimicking human strategies and improving consistency in specific domains [40]. Similarly, optimizing hyperparameters using enhanced metaheuristic algorithms (like Grey Wolf Optimization) combined with self-attention and Bi-LSTM models has shown improvements in specialized fields like software engineering translation [39].
*   **Self-Supervised and Multimodal Learning:** To overcome the bottleneck of expensive human annotations, self-supervised multimodal learning is being adopted. This approach leverages large-scale unannotated data to pre-train models, which can then be adapted for NMT and other NLP tasks with less labeled data [15], [42].
*   **Evaluation Metrics:** Traditional evaluation metrics based on similarity to reference translations are being critiqued for language bias. New methods, such as clinical weighting for evaluating MeSH translations, provide a more nuanced assessment of translation quality by prioritizing clinically important terms [37], [54].

### 5. Resource-Scarce and Low-Resource Languages
Progress is also being made for languages with limited digital resources.

*   **Amharic-English Translation:** Systematic reviews of Amharic-English MT highlight the evolution from rule-based to neural approaches. However, challenges persist due to inadequate datasets and the complex semantics of Amharic, underscoring the need for more resource development [7].
*   **Bengali Lexicons:** For sentiment analysis and profanity detection in Bengali, new lexicons (BengSentiLex, BengSwearLex) have been created using cross-lingual transfer techniques, addressing the lack of native tools for NLP tasks in this low-resource language [28].

### Conclusion
The latest research in machine and neural machine translation demonstrates a maturation of the field. The focus has moved beyond basic translation accuracy to address **efficiency** (NAR models, low-latency networks), **domain specificity** (healthcare, clinical records), **ethics** (gender bias, language inclusion), and **robustness** (multi-agent LLMs, self-supervised learning). While LLMs offer powerful new capabilities, they introduce new challenges regarding bias and asymmetry, necessitating careful evaluation and hybrid approaches that combine neural networks with traditional linguistic knowledge and templates.

### SOURCES USED IN THIS SECTION:
[1] Real-Time Named Entity Recognition from Textual Electronic Clinical Records in Cancer Therapy Using Low-Latency Neural Networks. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41649195

[2] A multi agent classical Chinese translation method based on large language models. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41249275

[3] Language inclusion intentions in scoping reviews. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/41229661

[4] Bridging language gaps in healthcare: a systematic review of the practical implementation of neural machine translation technologies in clinical settings. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/40966445

[5] Development of a Large-Scale Dataset of Chest Computed Tomography Reports in Japanese and a High-Performance Finding Classification Model: Dataset Development and Validation Study. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/40874833

[57, 6] A decade of gender bias in machine translation. (source nr: 57, 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/40575128

[7] Exploring the evolution and future prospects of Amharic to English machine translation: a systematic review. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/40486917

[8] Clinical document corpora-real ones, translated and synthetic substitutes, and assorted domain proxies: a survey of diversity in corpus design, with focus on German text data. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40371384

[9] Usability of technological tools to overcome language barriers in healthcare- a scoping review. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/40001263

[10] A systematic review of Machine Learning and Deep Learning approaches in Mexico: challenges and opportunities. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/39845096

[11] Visual insights into translation: demystifying trends of adopting eye-tracking techniques in translation studies. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/39654929

[12] Overview and challenges of machine translation for contextually appropriate translations. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/39391737

[13] Machine Translation Technology in Health: A Scoping Review. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/39320185

[14] A review of reinforcement learning for natural language processing and applications in healthcare. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/39208319

[15, 42] Self-Supervised Multimodal Learning: A Survey. (source nr: 15, 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/39110564

[16] Using Machine Translation and Post-Editing in the TRAPD Approach: Effects on the Quality of Translated Survey Texts. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/38617051

[17] Usability of technological tools to overcome language barriers in health care: a scoping review protocol. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/38458787

[18] Beyond rating scales: With targeted evaluation, large language models are poised for psychological assessment. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/38290286

[19] Language inclusion in ecological systematic reviews and maps: Barriers and perspectives. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/38286438

[20] The Use of Machine Translation for Outreach and Health Communication in Epidemiology and Public Health: Scoping Review. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/37983078

[21] What Are the English to Spanish Translation Methods Used on Written Health-Related Information? (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/37848223

[22] Machine translation of standardised medical terminology using natural language processing: A scoping review. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/37652265

[23, 44] A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond. (source nr: 23, 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/37200120

[24] Computational Methods for Single-cell Multi-omics Integration and Alignment. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/36581065

[25] How does artificial intelligence empower EFL teaching and learning nowadays? A review on artificial intelligence in the EFL context. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/36467167

[26] Overcoming Language Barriers in Academia: Machine Translation Tools and a Vision for a Multilingual Future. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/36196221

[27] Machine vs. Radiologist-Based Translations of RadLex: Implications for Multi-language Report Interoperability. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/35166969

[28] BengSentiLex and BengSwearLex: creating lexicons for sentiment analysis and profanity detection in low-resource Bengali language. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/34901419

[29] A review of the state-of-the-art in automatic post-editing. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/34720417

[30] Perceptions and knowledge of telemedicine in Ecuadorian practicing physicians: an instrument adaptation, validation and translation from English to Spanish. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/34600498

[31] Human versus machine editing of electronic prescription directions. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/33766549

[32] Development of machine translation technology for assisting health communication: A systematic review. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/30031857

[33, 52] A Bag of Concepts Approach for Biomedical Document Classification Using Wikipedia Knowledge*. Spanish-English Cross-language Case Study. (source nr: 33, 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/28816337

[34, 53] Integrating language models into classifiers for BCI communication: a review. (source nr: 34, 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/27153565

[35] Modeling workflow to design machine translation applications for public health practice. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/25445922

[36] A multi-lingual web service for drug side-effect data. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/20351818

[37] Clinically-weighted terms in the evaluation of MeSH translations: BabelMeSH in Portuguese as a model. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/18998783

[38] LingualX64: a multilingual benchmark for evaluating symmetry and asymmetry in LLM translation. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/42036426

[39] Optimizing software engineering English translation using an enhanced Grey Wolf Optimization with self-attention and Bi-LSTM model. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41073576

[40] Incorporating bilingual translation templates into neural machine translation. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/39953064

[41] Image-to-image machine translation enables computational defogging in real-world images. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/39573075

[43] Pre-trained language models in medicine: A survey. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/38917600

[45] Measuring the global response to antimicrobial resistance, 2020-21: a systematic governance analysis of 114 countries. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/36657475

[46] Concept recognition as a machine translation problem. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/34920707

[47] Automatic Generation of German Translation Candidates for SNOMED CT Textual Descriptions. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/34042729

[48] An Improved Sign Language Translation Model with Explainable Adaptations for Processing Long Sign Sentences. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/33163072

[49] Facile Solutions to the Problems Associated with Chemical Information and Mathematical Symbolism While Using Machine Translation Tools. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/32584030

[50] Automatic retrosynthetic route planning using template-free models. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/34122843

[51] Natural language generation for electronic health records. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/30687797

[54] Unsupervised quality estimation model for English to German translation and its application in extensive supervised evaluation. (source nr: 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/24892086

[55] Combining MEDLINE and publisher data to create parallel corpora for the automatic translation of biomedical text. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/23631733

[56] Low-Code/No-Code AI for Machine Translation: Democratising Generative AI for Blue Transformation. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/41728732

[58] A multimodal approach to cross-lingual sentiment analysis with ensemble of transformer and LLM. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/38671064

[59] Neural machine translation of clinical text: an empirical investigation into multilingual pre-trained language models and transfer-learning. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/38468693




________________________________________________________________________________

## ALL SOURCES:
[1] Real-Time Named Entity Recognition from Textual Electronic Clinical Records in Cancer Therapy Using Low-Latency Neural Networks. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/41649195

[2] A multi agent classical Chinese translation method based on large language models. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41249275

[3] Language inclusion intentions in scoping reviews. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/41229661

[4] Bridging language gaps in healthcare: a systematic review of the practical implementation of neural machine translation technologies in clinical settings. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/40966445

[5] Development of a Large-Scale Dataset of Chest Computed Tomography Reports in Japanese and a High-Performance Finding Classification Model: Dataset Development and Validation Study. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/40874833

[57, 6] A decade of gender bias in machine translation. (source nr: 57, 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/40575128

[7] Exploring the evolution and future prospects of Amharic to English machine translation: a systematic review. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/40486917

[8] Clinical document corpora-real ones, translated and synthetic substitutes, and assorted domain proxies: a survey of diversity in corpus design, with focus on German text data. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40371384

[9] Usability of technological tools to overcome language barriers in healthcare- a scoping review. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/40001263

[10] A systematic review of Machine Learning and Deep Learning approaches in Mexico: challenges and opportunities. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/39845096

[11] Visual insights into translation: demystifying trends of adopting eye-tracking techniques in translation studies. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/39654929

[12] Overview and challenges of machine translation for contextually appropriate translations. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/39391737

[13] Machine Translation Technology in Health: A Scoping Review. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/39320185

[14] A review of reinforcement learning for natural language processing and applications in healthcare. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/39208319

[15, 42] Self-Supervised Multimodal Learning: A Survey. (source nr: 15, 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/39110564

[16] Using Machine Translation and Post-Editing in the TRAPD Approach: Effects on the Quality of Translated Survey Texts. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/38617051

[17] Usability of technological tools to overcome language barriers in health care: a scoping review protocol. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/38458787

[18] Beyond rating scales: With targeted evaluation, large language models are poised for psychological assessment. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/38290286

[19] Language inclusion in ecological systematic reviews and maps: Barriers and perspectives. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/38286438

[20] The Use of Machine Translation for Outreach and Health Communication in Epidemiology and Public Health: Scoping Review. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/37983078

[21] What Are the English to Spanish Translation Methods Used on Written Health-Related Information? (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/37848223

[22] Machine translation of standardised medical terminology using natural language processing: A scoping review. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/37652265

[23, 44] A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond. (source nr: 23, 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/37200120

[24] Computational Methods for Single-cell Multi-omics Integration and Alignment. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/36581065

[25] How does artificial intelligence empower EFL teaching and learning nowadays? A review on artificial intelligence in the EFL context. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/36467167

[26] Overcoming Language Barriers in Academia: Machine Translation Tools and a Vision for a Multilingual Future. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/36196221

[27] Machine vs. Radiologist-Based Translations of RadLex: Implications for Multi-language Report Interoperability. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/35166969

[28] BengSentiLex and BengSwearLex: creating lexicons for sentiment analysis and profanity detection in low-resource Bengali language. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/34901419

[29] A review of the state-of-the-art in automatic post-editing. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/34720417

[30] Perceptions and knowledge of telemedicine in Ecuadorian practicing physicians: an instrument adaptation, validation and translation from English to Spanish. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/34600498

[31] Human versus machine editing of electronic prescription directions. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/33766549

[32] Development of machine translation technology for assisting health communication: A systematic review. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/30031857

[33, 52] A Bag of Concepts Approach for Biomedical Document Classification Using Wikipedia Knowledge*. Spanish-English Cross-language Case Study. (source nr: 33, 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/28816337

[34, 53] Integrating language models into classifiers for BCI communication: a review. (source nr: 34, 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/27153565

[35] Modeling workflow to design machine translation applications for public health practice. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/25445922

[36] A multi-lingual web service for drug side-effect data. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/20351818

[37] Clinically-weighted terms in the evaluation of MeSH translations: BabelMeSH in Portuguese as a model. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/18998783

[38] LingualX64: a multilingual benchmark for evaluating symmetry and asymmetry in LLM translation. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/42036426

[39] Optimizing software engineering English translation using an enhanced Grey Wolf Optimization with self-attention and Bi-LSTM model. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41073576

[40] Incorporating bilingual translation templates into neural machine translation. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/39953064

[41] Image-to-image machine translation enables computational defogging in real-world images. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/39573075

[43] Pre-trained language models in medicine: A survey. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/38917600

[45] Measuring the global response to antimicrobial resistance, 2020-21: a systematic governance analysis of 114 countries. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/36657475

[46] Concept recognition as a machine translation problem. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/34920707

[47] Automatic Generation of German Translation Candidates for SNOMED CT Textual Descriptions. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/34042729

[48] An Improved Sign Language Translation Model with Explainable Adaptations for Processing Long Sign Sentences. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/33163072

[49] Facile Solutions to the Problems Associated with Chemical Information and Mathematical Symbolism While Using Machine Translation Tools. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/32584030

[50] Automatic retrosynthetic route planning using template-free models. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/34122843

[51] Natural language generation for electronic health records. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/30687797

[54] Unsupervised quality estimation model for English to German translation and its application in extensive supervised evaluation. (source nr: 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/24892086

[55] Combining MEDLINE and publisher data to create parallel corpora for the automatic translation of biomedical text. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/23631733

[56] Low-Code/No-Code AI for Machine Translation: Democratising Generative AI for Blue Transformation. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/41728732

[58] A multimodal approach to cross-lingual sentiment analysis with ensemble of transformer and LLM. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/38671064

[59] Neural machine translation of clinical text: an empirical investigation into multilingual pre-trained language models and transfer-learning. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/38468693


