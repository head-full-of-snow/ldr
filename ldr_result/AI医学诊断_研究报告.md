Based on the provided sources from 2024–2026, the landscape of AI in medical diagnosis is undergoing a significant transformation, moving from isolated image analysis to integrated, multimodal, and reasoning-capable systems. The latest research highlights advancements in Deep Learning (DL) for medical imaging, the emergence of Large Language Models (LLMs) in clinical decision support, and critical challenges regarding bias, privacy, and interpretability.

### 1. Advancements in Deep Learning for Medical Imaging

Deep learning continues to dominate medical image analysis, with recent innovations focusing on multimodal fusion, causal reasoning, and architectural efficiency.

*   **Multimodal Fusion and Integration:** Recent studies emphasize the integration of multiple imaging modalities to improve diagnostic accuracy. For instance, frameworks combining mammography, ultrasound, and MRI using Mixture-of-Experts (MoE) architectures allow for dynamic weighting of each modality’s contribution, addressing issues with unpaired data [6]. Similarly, integrating CT and MRI for brain tumor classification demonstrates that model fusion can leverage complementary structural and functional details [42]. Vision Transformers (ViTs) are also being enhanced with novel dense networks to better capture global structures and long-range dependencies in medical image fusion [1].
*   **Causal Reasoning in Multi-Label Diagnosis:** A critical shift is occurring from correlation-based inference to causal intervention in multi-label medical image diagnosis. Traditional DL models often fail to capture the complexity of concurrent conditions (comorbidities) because they rely on statistical correlations. New frameworks integrating causal reasoning aim to address this gap, offering more robust diagnoses for patients with multiple co-occurring diseases [2].
*   **Specialized Architectures and Optimization:** Researchers are developing specialized models for specific challenges. For example, a Temporal-Spatial Transformer Network (TST-Net) has been proposed for longitudinal brain tumor segmentation to incorporate temporal dynamics, overcoming the limitation of single-time-point analysis [20]. In kidney stone detection, Explainable AI (XAI) is being integrated to ensure transparency alongside high accuracy [4]. Furthermore, hybrid models combining Generative Adversarial Networks (GANs) with ResUNet, optimized by Genetic Algorithms, show promise in precise brain tumor subregion segmentation [24].

### 2. Large Language Models (LLMs) in Clinical Decision Support

LLMs are rapidly expanding beyond text generation into complex clinical decision support systems (CDSS), often augmented by Retrieval-Augmented Generation (RAG) to mitigate hallucinations.

*   **RAG for Accuracy and Reliability:** Standard LLMs are prone to factual errors, which is unacceptable in medical contexts. RAG frameworks are being deployed to ground LLM outputs in authoritative, up-to-date medical guidelines and literature. Studies show that RAG-augmented LLMs significantly improve accuracy in areas such as therapeutic plasma exchange protocols [48], infective endocarditis prophylaxis [68], and interpreting hepatological guidelines for Hepatitis C management [88].
*   **Diagnostic Reasoning and Education:** LLMs are demonstrating value in enhancing diagnostic reasoning for medical students and junior physicians. Randomized controlled trials indicate that LLMs can improve diagnostic accuracy in rheumatology by reducing the cognitive burden compared to traditional CDSS [59]. In emergency departments, a dynamic, time-aware CDSS using RAG improved diagnostic accuracy for critical conditions like aortic dissection and stroke from 69.5% to 86.7% in pilot studies [52]. Additionally, LLMs are being used to extract structured clinical information, such as Crohn’s disease activity scores, from unstructured radiology reports [78].
*   **Limitations and Metacognition:** Despite progress, LLMs lack essential metacognitive abilities for reliable medical reasoning. Benchmarks like MetaMedQA reveal that while LLMs may achieve high accuracy on board exams, their ability to assess their own confidence and detect missing information is limited, posing risks in clinical deployment [86]. Furthermore, LLM performance is susceptible to user-driven factors, such as query phrasing and the omission of critical clinical details [53].

### 3. Multimodal and Cross-Modal Integration

The convergence of imaging data with clinical text and electronic health records (EHRs) is a key trend.

*   **Multimodal Data Fusion:** Systems like BINDS (Breast cancer Intelligent Non-invasive Diagnosis System) integrate multimodal imaging data for risk assessment and subtype classification, matching clinical workflows by starting with ultrasound and refining with other modalities [19]. In dermatology, LLMs are being evaluated for their ability to interpret dermatological images, though their performance compared to human experts remains a subject of ongoing study [82].
*   **EHR and Structured Data:** LLMs are enhancing the extraction of computable phenotypes from EHRs. Selective use of LLMs, guided by uncertainty, allows for scalable and accurate phenotyping while managing computational costs [55]. Frameworks like CDE-Mapper use RAG to automate the alignment of clinical data elements with controlled vocabularies, improving data interoperability [79].

### 4. Critical Challenges: Bias, Privacy, and Explainability

The deployment of AI in healthcare faces significant hurdles related to equity, security, and trust.

*   **Bias and Fairness:** AI models can inherit and amplify societal biases. Research indicates that AI in cardiology may exhibit performance differences between men and women, potentially exacerbating care disparities [97]. LLMs also show cultural and geographic biases, struggling to align with country-specific clinical guidelines that may conflict with the data they were trained on [100]. Debiasing techniques, such as cooperative training with dynamic debiasing, are being explored to mitigate label and keyword biases in medical text classification [21].
*   **Privacy and Federated Learning:** Data privacy regulations (HIPAA, GDPR) hinder centralized data aggregation. Federated Learning (FL) allows institutions to collaboratively train models without sharing raw patient data. Empirical studies demonstrate the effectiveness of FL with differential privacy for breast cancer classification in ultrasound images [10] and skin cancer classification [32], enabling robust model training while preserving patient confidentiality.
*   **Explainability (XAI):** Trust in AI requires transparency. Self-Explaining Neural Networks (SENNs) are being developed to provide intrinsic interpretability, such as in Parkinson’s disease screening via gait analysis, ensuring that explanations faithfully reflect the model’s reasoning rather than being post-hoc approximations [36]. In skin disease diagnosis, hierarchical deep learning frameworks are being used to enhance interpretability and performance in classifying benign vs. malignant lesions [35].

### 5. Emerging Applications and Future Directions

*   **Digital Twins and Precision Oncology:** AI-driven digital twins are being explored for prostate cancer care, creating dynamic virtual models to simulate patient biology and personalize treatment [83]. Precision oncology is increasingly leveraging LLMs and multi-agent systems to integrate cross-modal data (imaging, omics, EHR) for complex clinical decision support [18].
*   **Nursing and Chronic Care:** AI is being integrated into nursing practice, particularly for older adults with dementia, to support care and research priorities [3]. In critical care nursing, AI is utilized for predictive analytics through EHRs to improve patient outcomes [22].
*   **Rare Diseases and Small Samples:** For conditions with limited data, such as parotid gland tumors, few-shot multimodal deep learning frameworks are being developed to enable precision diagnosis using small-sample learning and multi-scale spatial attention [13].

In conclusion, the latest research indicates that AI in medical diagnosis is maturing from simple image classification to complex, multimodal, and reasoning-based systems. While LLMs and RAG architectures offer significant potential for clinical decision support, their clinical adoption hinges on addressing critical issues of bias, privacy, hallucination, and interpretability. The integration of causal reasoning and federated learning represents a promising direction for more robust and secure AI deployment.

[1] MSML-DenseXmer: harnessing vision transformers through integration with novel dense networks for medical image fusion. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215519

[2] Beyond Correlation: Causal Intervention for Multi-Label Medical Image Diagnosis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213561

[3, 93] Artificial intelligence in nursing practice for older adults with dementia: A narrative review informed by bibliometric mapping and implications for nurse-led research. (source nr: 3, 93)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209252

[4, 95] Explainable AI in kidney stone detection and segmentation: a mini review. (source nr: 4, 95)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206076

[5] Artificial intelligence approaches for schizophrenia prediction and its biomarkers using medical imaging data. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206005

[6, 96] Dense-MoE vs Lite-MoE: A Gating-Weight-Aware Pruning Framework for Unpaired Multimodal Breast Cancer Diagnosis. (source nr: 6, 96)
   URL: https://pubmed.ncbi.nlm.nih.gov/42204022

[7] SULBA: A Task-Agnostic Data Augmentation Framework for Deep Learning in Medical Image Analysis. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42196912

[8] Unsupervised Anomaly Detection in Medical Imaging: A Survey of Methods, Challenges, and Future Directions. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194303

[9] Advancing Brain Tumor Diagnosis Using Deep Learning: A Systematic and Critical Review on Methodological Approaches to Glioma Segmentation and Classification Through Multiparametric MRI. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42192781

[10] Federated Learning with Differential Privacy for Ultrasound Breast Cancer Classification: An Empirical Study. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188242

[11] A Robust Intelligent CNN Model Enhanced with Gabor-Based Feature Extraction, SMOTE Balancing, and Adam Optimization for Multi-Grade Diabetic Retinopathy Classification. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188225

[12] Neural Computing Advancements in Cardiac Imaging: A Review of Deep Learning Approaches for Heart Disease Diagnosis. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188217

[13] A Few-shot Multimodal Deep Learning Framework For Precision Diagnosis Of Parotid Gland. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42184237

[14] The Evolving Role of Artificial Intelligence in Fracture Diagnosis and Surgical Planning in Orthopaedics: Current Insights and Future Directions. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42181443

[15] Performance evaluation of large language models in the diagnosis of emergency internal medicine diseases: a retrospective study. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42180499

[16] A deep learning and radiomics fusion model enhances endoscopic ultrasonography diagnosis of gastric tumors. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42180041

[17] Research on multi-stage deep learning based intelligent diagnosis of skin diseases and skin medicine diagnosis community construction concept. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42168500

[18] Precision oncology: from large language models to multi-agent systems. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42158433

[19] A deep learning system for non-invasive breast cancer diagnosis with multimodal data. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42157015

[20] Temporally consistent longitudinal brain tumor segmentation using a temporal spatial transformer network. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42156537

[21] Mitigating Bias in Multi-Label Medical Text Classification: A Cooperative Training Framework with Dynamic Debiasing. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152185

[22] Research Topics and Trends of Artificial Intelligence in Critical Care Nursing: A Bibliometric Analysis. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42151094

[23] Machine Learning in Nonischemic Cardiomyopathy: Phenotyping, Mechanism Discovery, and Clinical Applications. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42150097

[24] A novel hybrid framework integrating GA-driven 3D ResUNetGAN for MRI brain tumor segmentation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149959

[25] Advancements in Image-Based Artificial Intelligence in the Diagnosis and Treatment of Head and Neck Squamous Cell Carcinoma: A Narrative Review. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42147747

[26] Current trends and future directions of artificial intelligence in lung cancer diagnosis. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42147376

[27] Bibliometric Trends in the Integration of Computer Vision With Healthcare. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42145939

[28] Artificial intelligence with deep learning driven entropy-curvature attention mechanism for detection and segmentation of skin lesions using biomedical images. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42140962

[29] Dual-Phase Computed Tomography-Based Deep Learning Architecture for Three-Year Survival Prediction in Hepatocellular Carcinoma. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42135555

[30] Role of Artificial Intelligence and Machine Learning in Diagnosing Knee Lesions: Where Are We Now? (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42131654

[31] Metaheuristic optimization of deep CNNs for multi-class diagnosis of cervical cancer and lymphoma. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129228

[32] Federated learning for privacy-preserving skin cancer classification using deep neural networks. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/42125708

[33] Liquid Biopsy in Colorectal Cancer: Future Perspectives Through the Lens of Artificial Intelligence-A Comprehensive Review of Novel Literature. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/42123533

[34] Are AI Neuroimaging Models Ready for Clinical Use? A Systematic Methodological Review. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/42123173

[35] Hierarchical Deep Learning Framework for Skin Disease and Cancer Classification Performance Enhancement. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122557

[36] Self-Explaining Neural Networks for Transparent Parkinson's Disease Screening. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122390

[37] Private Ensembles, Public Confidence: A PATE-to-MedPrompt System for Autism Detection. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/42121994

[38] Performance and generalization analysis of machine learning, deep learning, and transformer models for histopathology image classification. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/42120655

[39] Deep Learning Framework for Early Detection of Pancreatic Cancer Using Multi-modal Medical Imaging Analysis. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/42118516

[40] Automated Lesion Segmentation in Medical Imaging via Integration of nnU-Net Optimization and SAM Approach. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/42116853

[41] Dissecting self-supervised learning strategies for transfer learning in MRI prostate cancer diagnosis. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115652

[42] Bridging modalities: a deep learning framework for brain tumor classification via CT-MRI integration and model fusion. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110680

[43] Exploring AI as a Diagnostic Tool in Medical Imaging for Dermatopathological Diseases. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/42109557

[44] Mamba-Based Deep Learning Model for Automated Periapical Index Classification Using Periapical Radiographs and Clinical Metadata. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/42108657

[45] A Systematic Review: The Application of Attention Mechanisms in Medical Ultrasound Image Processing. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/42106306

[46] A deep learning model for automated identification of age-related macular degeneration atrophy. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/42105087

[47] A modular deep learning architecture for interpretable disease prediction across tabular clinical and biometric datasets. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/42102106

[48, 54] An automatic consult reply system for therapeutic plasma exchange using retrieval-augmented generation. (source nr: 48, 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/42091449

[49] Artificial intelligence in migraine: a narrative review on the diagnostic, prognostic, and therapeutic applications. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/42088847

[50] Pancreatic tumor detection in computed tomography images through a rotary positional siamese vision transformer. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/42086843

[51] Quality of AI-generated temporomandibular disorder information: A comparative analysis based on Turkish patient queries. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198915

[52] Modeling the Clinical Reasoning Workflow: A Dynamic, Time-Aware CDSS for the Emergency Department. (source nr: 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174892

[53] Susceptibility of Large Language Models to User-Driven Factors in Medical Queries. (source nr: 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110657

[55] Targeted use of large language models for EHR-based computable phenotyping. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/41990328

[56] Precision Grounding: augmenting large language models with evidence-based databases for trustworthy genetic variant summarization. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/41950627

[57] Collaborative multi-agent conversational artificial intelligence for clinical support in Parkinson disease. (source nr: 57)
   URL: https://pubmed.ncbi.nlm.nih.gov/41925479

[58] Performance of Large Language Models vs Conventional Machine Learning for Predicting Clinical Outcomes With Limited Data: Comparative Study. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/41921208

[59] Large language models enhance diagnostic reasoning of medical students in rheumatology: a randomized controlled trial. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/41877128

[60] A Feasibility Study of Literature-Guided HRV Stratification Using Large Language Models. (source nr: 60)
   URL: https://pubmed.ncbi.nlm.nih.gov/41750688

[61] Retrieval-Augmented Generation for Medical Question Answering on a Heart Failure Dataset: Performance Analysis. (source nr: 61)
   URL: https://pubmed.ncbi.nlm.nih.gov/41747226

[62] Using LLMs to Interpret Arterial Blood Gases: Comparison of a Novel Math Scratchpad with Different Prompting Methods in a Three-Arm Trial. (source nr: 62)
   URL: https://pubmed.ncbi.nlm.nih.gov/41726393

[63] Evolving Consultation: Enhancing Ophthalmic Diagnostic Performance Using Large Language Model. (source nr: 63)
   URL: https://pubmed.ncbi.nlm.nih.gov/41725833

[64] Deriving wisdom from data: The value and continued rationale for structured data in the era of artificial intelligence-driven oncology care. (source nr: 64)
   URL: https://pubmed.ncbi.nlm.nih.gov/41701629

[65] Interpretable ensemble machine learning framework for cardiovascular disease prediction using EMR data and large language models in Ethiopia. (source nr: 65)
   URL: https://pubmed.ncbi.nlm.nih.gov/41662408

[66] Comparative evaluation of large language models for hip fracture-related patient questions: DeepSeek-V3-FW, Gemini 2.0 Flash, and ChatGPT-4.5. (source nr: 66)
   URL: https://pubmed.ncbi.nlm.nih.gov/41623725

[67] Large language models and conditional rules in clinical decision support systems. (source nr: 67)
   URL: https://pubmed.ncbi.nlm.nih.gov/41584932

[68] Evaluating Retrieval-Augmented Generation-Large Language Models for Infective Endocarditis Prophylaxis: Clinical Accuracy and Efficiency. (source nr: 68)
   URL: https://pubmed.ncbi.nlm.nih.gov/41453288

[69] Comparative Evaluation of Advanced Chunking for Retrieval-Augmented Generation in Large Language Models for Clinical Decision Support. (source nr: 69)
   URL: https://pubmed.ncbi.nlm.nih.gov/41301150

[70] MicroRAG: Development of a Novel Artificial Intelligence Retrieval-Augmented Generation Model for Microsurgery Clinical Decision Support. (source nr: 70)
   URL: https://pubmed.ncbi.nlm.nih.gov/41235700

[71] Locally deployed context-aware chatbot outperforms generic large language models for guideline-concordant pediatric imaging recommendations. (source nr: 71)
   URL: https://pubmed.ncbi.nlm.nih.gov/41231298

[72] Web based AI-driven framework combining multi-modal data with CNN and LLM for Parkinson's disease diagnosis. (source nr: 72)
   URL: https://pubmed.ncbi.nlm.nih.gov/41188323

[73] Large language models with retrieval-augmented generation enhance expert modelling of Bayesian network for clinical decision support. (source nr: 73)
   URL: https://pubmed.ncbi.nlm.nih.gov/41182676

[74] Development and Evaluation of a Retrieval-Augmented Generation Chatbot for Orthopedic and Trauma Surgery Patient Education: Mixed-Methods Study. (source nr: 74)
   URL: https://pubmed.ncbi.nlm.nih.gov/41134117

[75] Sleep, interrupted - when short nights take their toll. (source nr: 75)
   URL: https://pubmed.ncbi.nlm.nih.gov/41038089

[76] Large language models for clinical decision support in gastroenterology and hepatology. (source nr: 76)
   URL: https://pubmed.ncbi.nlm.nih.gov/40846793

[77] Assessing DeepSeek-R1 for Clinical Decision Support in Multidisciplinary Laboratory Medicine. (source nr: 77)
   URL: https://pubmed.ncbi.nlm.nih.gov/40823482

[78] LLM-Based Extraction of Imaging Features from Radiology Reports: Automating Disease Activity Scoring in Crohn's Disease. (source nr: 78)
   URL: https://pubmed.ncbi.nlm.nih.gov/40783343

[79] CDE-Mapper: Using retrieval-augmented language models for linking clinical data elements to controlled vocabularies. (source nr: 79)
   URL: https://pubmed.ncbi.nlm.nih.gov/40743885

[80] A structured evaluation of LLM-generated step-by-step instructions in cadaveric brachial plexus dissection. (source nr: 80)
   URL: https://pubmed.ncbi.nlm.nih.gov/40598351

[81] Advancing large language models as patient education tools for inflammatory bowel disease. (source nr: 81)
   URL: https://pubmed.ncbi.nlm.nih.gov/40495941

[82] Large language models for dermatological image interpretation - a comparative study. (source nr: 82)
   URL: https://pubmed.ncbi.nlm.nih.gov/40420705

[83] A systematic review of AI as a digital twin for prostate cancer care. (source nr: 83)
   URL: https://pubmed.ncbi.nlm.nih.gov/40347618

[84] Benchmarking LLM chatbots' oncological knowledge with the Turkish Society of Medical Oncology's annual board examination questions. (source nr: 84)
   URL: https://pubmed.ncbi.nlm.nih.gov/39905358

[85] Leveraging Guideline-Based Clinical Decision Support Systems with Large Language Models: A Case Study with Breast Cancer. (source nr: 85)
   URL: https://pubmed.ncbi.nlm.nih.gov/39880005

[86] Large Language Models lack essential metacognition for reliable medical reasoning. (source nr: 86)
   URL: https://pubmed.ncbi.nlm.nih.gov/39809759

[87] The Use of Generative AI for Scientific Literature Searches for Systematic Reviews: ChatGPT and Microsoft Bing AI Performance Evaluation. (source nr: 87)
   URL: https://pubmed.ncbi.nlm.nih.gov/38771247

[88] Optimization of hepatological clinical guidelines interpretation by large language models: a retrieval augmented generation-based framework. (source nr: 88)
   URL: https://pubmed.ncbi.nlm.nih.gov/38654102

[89] Automated HEART score determination via ChatGPT: Honing a framework for iterative prompt development. (source nr: 89)
   URL: https://pubmed.ncbi.nlm.nih.gov/38481520

[90] Leveraging large language models for gastrointestinal injury detection in athletes: a medical image analysis approach. (source nr: 90)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215522

[91] Artificial Intelligence for Sleep Instability and Motor Phenotyping: Clinical Translation Beyond Sleep Staging. (source nr: 91)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213077

[92] Current Approaches to the Management of Acute Surgical and Medical Emergencies: A Structured Narrative Review. (source nr: 92)
   URL: https://pubmed.ncbi.nlm.nih.gov/42211600

[94] Capturing multi-disease states on a spectrum with machine learning and routine clinical data. (source nr: 94)
   URL: https://pubmed.ncbi.nlm.nih.gov/42208537

[97] [Gender bias and artificial intelligence in cardiology: evidence, clinical implications, and future perspectives]. (source nr: 97)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200232

[98] Artificial Intelligence-Based Risk Stratification in Obesity Care: From Diagnosis to Personalised Treatment Pathways. (source nr: 98)
   URL: https://pubmed.ncbi.nlm.nih.gov/42196828

[99] A Review of Data Engineering in United States Healthcare Infrastructure. (source nr: 99)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194493

[100] Cultural bias in large language models' ability to follow neuroradiology guidelines. (source nr: 100)
   URL: https://pubmed.ncbi.nlm.nih.gov/42189215




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. AI医学诊断 深度学习 医学影像AI 大语言模型医疗诊断 临床决策支持 最新科研进展
2. 2025-2026年AI医学诊断最新科研进展：深度学习与多模态大语言模型在医学影像分析及临床决策支持系统中的突破与应用

 #### Iteration 2:
1. 2026年临床指南中，针对大语言模型（LLM）结合检索增强生成（RAG）在复杂临床决策支持（如治疗性血浆置换）中的具体性能指标（如幻觉率、事实准确性阈值）及监管审批状态有哪些最新实证数据？

 #### Iteration 3:
1. 截至2026年5月，结合检索增强生成（RAG）与多模态大语言模型（MLLMs）的临床决策支持系统，在通过FDA或NMPA等监管机构针对“高风险医疗诊断”（如癌症分期或复杂影像解读）的实时前瞻性临床试验中，其具体的敏感性、特异性及幻觉率阈值达标情况如何？



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
AI医学诊断 深度学习 医学影像AI 大语言模型医疗诊断 临床决策支持 最新科研进展



Searched with 2 questions, found 50 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
AI医学诊断 深度学习 医学影像AI 大语言模型医疗诊断 临床决策支持 最新科研进展



Searched with 1 questions, found 39 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
AI医学诊断 深度学习 医学影像AI 大语言模型医疗诊断 临床决策支持 最新科研进展



Searched with 1 questions, found 50 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
AI医学诊断 深度学习 医学影像AI 大语言模型医疗诊断 临床决策支持 最新科研进展



Based on the provided sources from 2024–2026, the landscape of AI in medical diagnosis is undergoing a significant transformation, moving from isolated image analysis to integrated, multimodal, and reasoning-capable systems. The latest research highlights advancements in Deep Learning (DL) for medical imaging, the emergence of Large Language Models (LLMs) in clinical decision support, and critical challenges regarding bias, privacy, and interpretability.

### 1. Advancements in Deep Learning for Medical Imaging

Deep learning continues to dominate medical image analysis, with recent innovations focusing on multimodal fusion, causal reasoning, and architectural efficiency.

*   **Multimodal Fusion and Integration:** Recent studies emphasize the integration of multiple imaging modalities to improve diagnostic accuracy. For instance, frameworks combining mammography, ultrasound, and MRI using Mixture-of-Experts (MoE) architectures allow for dynamic weighting of each modality’s contribution, addressing issues with unpaired data [6]. Similarly, integrating CT and MRI for brain tumor classification demonstrates that model fusion can leverage complementary structural and functional details [42]. Vision Transformers (ViTs) are also being enhanced with novel dense networks to better capture global structures and long-range dependencies in medical image fusion [1].
*   **Causal Reasoning in Multi-Label Diagnosis:** A critical shift is occurring from correlation-based inference to causal intervention in multi-label medical image diagnosis. Traditional DL models often fail to capture the complexity of concurrent conditions (comorbidities) because they rely on statistical correlations. New frameworks integrating causal reasoning aim to address this gap, offering more robust diagnoses for patients with multiple co-occurring diseases [2].
*   **Specialized Architectures and Optimization:** Researchers are developing specialized models for specific challenges. For example, a Temporal-Spatial Transformer Network (TST-Net) has been proposed for longitudinal brain tumor segmentation to incorporate temporal dynamics, overcoming the limitation of single-time-point analysis [20]. In kidney stone detection, Explainable AI (XAI) is being integrated to ensure transparency alongside high accuracy [4]. Furthermore, hybrid models combining Generative Adversarial Networks (GANs) with ResUNet, optimized by Genetic Algorithms, show promise in precise brain tumor subregion segmentation [24].

### 2. Large Language Models (LLMs) in Clinical Decision Support

LLMs are rapidly expanding beyond text generation into complex clinical decision support systems (CDSS), often augmented by Retrieval-Augmented Generation (RAG) to mitigate hallucinations.

*   **RAG for Accuracy and Reliability:** Standard LLMs are prone to factual errors, which is unacceptable in medical contexts. RAG frameworks are being deployed to ground LLM outputs in authoritative, up-to-date medical guidelines and literature. Studies show that RAG-augmented LLMs significantly improve accuracy in areas such as therapeutic plasma exchange protocols [48], infective endocarditis prophylaxis [68], and interpreting hepatological guidelines for Hepatitis C management [88].
*   **Diagnostic Reasoning and Education:** LLMs are demonstrating value in enhancing diagnostic reasoning for medical students and junior physicians. Randomized controlled trials indicate that LLMs can improve diagnostic accuracy in rheumatology by reducing the cognitive burden compared to traditional CDSS [59]. In emergency departments, a dynamic, time-aware CDSS using RAG improved diagnostic accuracy for critical conditions like aortic dissection and stroke from 69.5% to 86.7% in pilot studies [52]. Additionally, LLMs are being used to extract structured clinical information, such as Crohn’s disease activity scores, from unstructured radiology reports [78].
*   **Limitations and Metacognition:** Despite progress, LLMs lack essential metacognitive abilities for reliable medical reasoning. Benchmarks like MetaMedQA reveal that while LLMs may achieve high accuracy on board exams, their ability to assess their own confidence and detect missing information is limited, posing risks in clinical deployment [86]. Furthermore, LLM performance is susceptible to user-driven factors, such as query phrasing and the omission of critical clinical details [53].

### 3. Multimodal and Cross-Modal Integration

The convergence of imaging data with clinical text and electronic health records (EHRs) is a key trend.

*   **Multimodal Data Fusion:** Systems like BINDS (Breast cancer Intelligent Non-invasive Diagnosis System) integrate multimodal imaging data for risk assessment and subtype classification, matching clinical workflows by starting with ultrasound and refining with other modalities [19]. In dermatology, LLMs are being evaluated for their ability to interpret dermatological images, though their performance compared to human experts remains a subject of ongoing study [82].
*   **EHR and Structured Data:** LLMs are enhancing the extraction of computable phenotypes from EHRs. Selective use of LLMs, guided by uncertainty, allows for scalable and accurate phenotyping while managing computational costs [55]. Frameworks like CDE-Mapper use RAG to automate the alignment of clinical data elements with controlled vocabularies, improving data interoperability [79].

### 4. Critical Challenges: Bias, Privacy, and Explainability

The deployment of AI in healthcare faces significant hurdles related to equity, security, and trust.

*   **Bias and Fairness:** AI models can inherit and amplify societal biases. Research indicates that AI in cardiology may exhibit performance differences between men and women, potentially exacerbating care disparities [97]. LLMs also show cultural and geographic biases, struggling to align with country-specific clinical guidelines that may conflict with the data they were trained on [100]. Debiasing techniques, such as cooperative training with dynamic debiasing, are being explored to mitigate label and keyword biases in medical text classification [21].
*   **Privacy and Federated Learning:** Data privacy regulations (HIPAA, GDPR) hinder centralized data aggregation. Federated Learning (FL) allows institutions to collaboratively train models without sharing raw patient data. Empirical studies demonstrate the effectiveness of FL with differential privacy for breast cancer classification in ultrasound images [10] and skin cancer classification [32], enabling robust model training while preserving patient confidentiality.
*   **Explainability (XAI):** Trust in AI requires transparency. Self-Explaining Neural Networks (SENNs) are being developed to provide intrinsic interpretability, such as in Parkinson’s disease screening via gait analysis, ensuring that explanations faithfully reflect the model’s reasoning rather than being post-hoc approximations [36]. In skin disease diagnosis, hierarchical deep learning frameworks are being used to enhance interpretability and performance in classifying benign vs. malignant lesions [35].

### 5. Emerging Applications and Future Directions

*   **Digital Twins and Precision Oncology:** AI-driven digital twins are being explored for prostate cancer care, creating dynamic virtual models to simulate patient biology and personalize treatment [83]. Precision oncology is increasingly leveraging LLMs and multi-agent systems to integrate cross-modal data (imaging, omics, EHR) for complex clinical decision support [18].
*   **Nursing and Chronic Care:** AI is being integrated into nursing practice, particularly for older adults with dementia, to support care and research priorities [3]. In critical care nursing, AI is utilized for predictive analytics through EHRs to improve patient outcomes [22].
*   **Rare Diseases and Small Samples:** For conditions with limited data, such as parotid gland tumors, few-shot multimodal deep learning frameworks are being developed to enable precision diagnosis using small-sample learning and multi-scale spatial attention [13].

In conclusion, the latest research indicates that AI in medical diagnosis is maturing from simple image classification to complex, multimodal, and reasoning-based systems. While LLMs and RAG architectures offer significant potential for clinical decision support, their clinical adoption hinges on addressing critical issues of bias, privacy, hallucination, and interpretability. The integration of causal reasoning and federated learning represents a promising direction for more robust and secure AI deployment.

### SOURCES USED IN THIS SECTION:
[1] MSML-DenseXmer: harnessing vision transformers through integration with novel dense networks for medical image fusion. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215519

[2] Beyond Correlation: Causal Intervention for Multi-Label Medical Image Diagnosis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213561

[3, 93] Artificial intelligence in nursing practice for older adults with dementia: A narrative review informed by bibliometric mapping and implications for nurse-led research. (source nr: 3, 93)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209252

[4, 95] Explainable AI in kidney stone detection and segmentation: a mini review. (source nr: 4, 95)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206076

[5] Artificial intelligence approaches for schizophrenia prediction and its biomarkers using medical imaging data. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206005

[6, 96] Dense-MoE vs Lite-MoE: A Gating-Weight-Aware Pruning Framework for Unpaired Multimodal Breast Cancer Diagnosis. (source nr: 6, 96)
   URL: https://pubmed.ncbi.nlm.nih.gov/42204022

[7] SULBA: A Task-Agnostic Data Augmentation Framework for Deep Learning in Medical Image Analysis. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42196912

[8] Unsupervised Anomaly Detection in Medical Imaging: A Survey of Methods, Challenges, and Future Directions. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194303

[9] Advancing Brain Tumor Diagnosis Using Deep Learning: A Systematic and Critical Review on Methodological Approaches to Glioma Segmentation and Classification Through Multiparametric MRI. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42192781

[10] Federated Learning with Differential Privacy for Ultrasound Breast Cancer Classification: An Empirical Study. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188242

[11] A Robust Intelligent CNN Model Enhanced with Gabor-Based Feature Extraction, SMOTE Balancing, and Adam Optimization for Multi-Grade Diabetic Retinopathy Classification. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188225

[12] Neural Computing Advancements in Cardiac Imaging: A Review of Deep Learning Approaches for Heart Disease Diagnosis. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188217

[13] A Few-shot Multimodal Deep Learning Framework For Precision Diagnosis Of Parotid Gland. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42184237

[14] The Evolving Role of Artificial Intelligence in Fracture Diagnosis and Surgical Planning in Orthopaedics: Current Insights and Future Directions. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42181443

[15] Performance evaluation of large language models in the diagnosis of emergency internal medicine diseases: a retrospective study. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42180499

[16] A deep learning and radiomics fusion model enhances endoscopic ultrasonography diagnosis of gastric tumors. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42180041

[17] Research on multi-stage deep learning based intelligent diagnosis of skin diseases and skin medicine diagnosis community construction concept. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42168500

[18] Precision oncology: from large language models to multi-agent systems. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42158433

[19] A deep learning system for non-invasive breast cancer diagnosis with multimodal data. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42157015

[20] Temporally consistent longitudinal brain tumor segmentation using a temporal spatial transformer network. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42156537

[21] Mitigating Bias in Multi-Label Medical Text Classification: A Cooperative Training Framework with Dynamic Debiasing. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152185

[22] Research Topics and Trends of Artificial Intelligence in Critical Care Nursing: A Bibliometric Analysis. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42151094

[23] Machine Learning in Nonischemic Cardiomyopathy: Phenotyping, Mechanism Discovery, and Clinical Applications. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42150097

[24] A novel hybrid framework integrating GA-driven 3D ResUNetGAN for MRI brain tumor segmentation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149959

[25] Advancements in Image-Based Artificial Intelligence in the Diagnosis and Treatment of Head and Neck Squamous Cell Carcinoma: A Narrative Review. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42147747

[26] Current trends and future directions of artificial intelligence in lung cancer diagnosis. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42147376

[27] Bibliometric Trends in the Integration of Computer Vision With Healthcare. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42145939

[28] Artificial intelligence with deep learning driven entropy-curvature attention mechanism for detection and segmentation of skin lesions using biomedical images. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42140962

[29] Dual-Phase Computed Tomography-Based Deep Learning Architecture for Three-Year Survival Prediction in Hepatocellular Carcinoma. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42135555

[30] Role of Artificial Intelligence and Machine Learning in Diagnosing Knee Lesions: Where Are We Now? (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42131654

[31] Metaheuristic optimization of deep CNNs for multi-class diagnosis of cervical cancer and lymphoma. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129228

[32] Federated learning for privacy-preserving skin cancer classification using deep neural networks. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/42125708

[33] Liquid Biopsy in Colorectal Cancer: Future Perspectives Through the Lens of Artificial Intelligence-A Comprehensive Review of Novel Literature. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/42123533

[34] Are AI Neuroimaging Models Ready for Clinical Use? A Systematic Methodological Review. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/42123173

[35] Hierarchical Deep Learning Framework for Skin Disease and Cancer Classification Performance Enhancement. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122557

[36] Self-Explaining Neural Networks for Transparent Parkinson's Disease Screening. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122390

[37] Private Ensembles, Public Confidence: A PATE-to-MedPrompt System for Autism Detection. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/42121994

[38] Performance and generalization analysis of machine learning, deep learning, and transformer models for histopathology image classification. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/42120655

[39] Deep Learning Framework for Early Detection of Pancreatic Cancer Using Multi-modal Medical Imaging Analysis. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/42118516

[40] Automated Lesion Segmentation in Medical Imaging via Integration of nnU-Net Optimization and SAM Approach. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/42116853

[41] Dissecting self-supervised learning strategies for transfer learning in MRI prostate cancer diagnosis. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115652

[42] Bridging modalities: a deep learning framework for brain tumor classification via CT-MRI integration and model fusion. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110680

[43] Exploring AI as a Diagnostic Tool in Medical Imaging for Dermatopathological Diseases. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/42109557

[44] Mamba-Based Deep Learning Model for Automated Periapical Index Classification Using Periapical Radiographs and Clinical Metadata. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/42108657

[45] A Systematic Review: The Application of Attention Mechanisms in Medical Ultrasound Image Processing. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/42106306

[46] A deep learning model for automated identification of age-related macular degeneration atrophy. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/42105087

[47] A modular deep learning architecture for interpretable disease prediction across tabular clinical and biometric datasets. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/42102106

[48, 54] An automatic consult reply system for therapeutic plasma exchange using retrieval-augmented generation. (source nr: 48, 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/42091449

[49] Artificial intelligence in migraine: a narrative review on the diagnostic, prognostic, and therapeutic applications. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/42088847

[50] Pancreatic tumor detection in computed tomography images through a rotary positional siamese vision transformer. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/42086843

[51] Quality of AI-generated temporomandibular disorder information: A comparative analysis based on Turkish patient queries. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198915

[52] Modeling the Clinical Reasoning Workflow: A Dynamic, Time-Aware CDSS for the Emergency Department. (source nr: 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174892

[53] Susceptibility of Large Language Models to User-Driven Factors in Medical Queries. (source nr: 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110657

[55] Targeted use of large language models for EHR-based computable phenotyping. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/41990328

[56] Precision Grounding: augmenting large language models with evidence-based databases for trustworthy genetic variant summarization. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/41950627

[57] Collaborative multi-agent conversational artificial intelligence for clinical support in Parkinson disease. (source nr: 57)
   URL: https://pubmed.ncbi.nlm.nih.gov/41925479

[58] Performance of Large Language Models vs Conventional Machine Learning for Predicting Clinical Outcomes With Limited Data: Comparative Study. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/41921208

[59] Large language models enhance diagnostic reasoning of medical students in rheumatology: a randomized controlled trial. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/41877128

[60] A Feasibility Study of Literature-Guided HRV Stratification Using Large Language Models. (source nr: 60)
   URL: https://pubmed.ncbi.nlm.nih.gov/41750688

[61] Retrieval-Augmented Generation for Medical Question Answering on a Heart Failure Dataset: Performance Analysis. (source nr: 61)
   URL: https://pubmed.ncbi.nlm.nih.gov/41747226

[62] Using LLMs to Interpret Arterial Blood Gases: Comparison of a Novel Math Scratchpad with Different Prompting Methods in a Three-Arm Trial. (source nr: 62)
   URL: https://pubmed.ncbi.nlm.nih.gov/41726393

[63] Evolving Consultation: Enhancing Ophthalmic Diagnostic Performance Using Large Language Model. (source nr: 63)
   URL: https://pubmed.ncbi.nlm.nih.gov/41725833

[64] Deriving wisdom from data: The value and continued rationale for structured data in the era of artificial intelligence-driven oncology care. (source nr: 64)
   URL: https://pubmed.ncbi.nlm.nih.gov/41701629

[65] Interpretable ensemble machine learning framework for cardiovascular disease prediction using EMR data and large language models in Ethiopia. (source nr: 65)
   URL: https://pubmed.ncbi.nlm.nih.gov/41662408

[66] Comparative evaluation of large language models for hip fracture-related patient questions: DeepSeek-V3-FW, Gemini 2.0 Flash, and ChatGPT-4.5. (source nr: 66)
   URL: https://pubmed.ncbi.nlm.nih.gov/41623725

[67] Large language models and conditional rules in clinical decision support systems. (source nr: 67)
   URL: https://pubmed.ncbi.nlm.nih.gov/41584932

[68] Evaluating Retrieval-Augmented Generation-Large Language Models for Infective Endocarditis Prophylaxis: Clinical Accuracy and Efficiency. (source nr: 68)
   URL: https://pubmed.ncbi.nlm.nih.gov/41453288

[69] Comparative Evaluation of Advanced Chunking for Retrieval-Augmented Generation in Large Language Models for Clinical Decision Support. (source nr: 69)
   URL: https://pubmed.ncbi.nlm.nih.gov/41301150

[70] MicroRAG: Development of a Novel Artificial Intelligence Retrieval-Augmented Generation Model for Microsurgery Clinical Decision Support. (source nr: 70)
   URL: https://pubmed.ncbi.nlm.nih.gov/41235700

[71] Locally deployed context-aware chatbot outperforms generic large language models for guideline-concordant pediatric imaging recommendations. (source nr: 71)
   URL: https://pubmed.ncbi.nlm.nih.gov/41231298

[72] Web based AI-driven framework combining multi-modal data with CNN and LLM for Parkinson's disease diagnosis. (source nr: 72)
   URL: https://pubmed.ncbi.nlm.nih.gov/41188323

[73] Large language models with retrieval-augmented generation enhance expert modelling of Bayesian network for clinical decision support. (source nr: 73)
   URL: https://pubmed.ncbi.nlm.nih.gov/41182676

[74] Development and Evaluation of a Retrieval-Augmented Generation Chatbot for Orthopedic and Trauma Surgery Patient Education: Mixed-Methods Study. (source nr: 74)
   URL: https://pubmed.ncbi.nlm.nih.gov/41134117

[75] Sleep, interrupted - when short nights take their toll. (source nr: 75)
   URL: https://pubmed.ncbi.nlm.nih.gov/41038089

[76] Large language models for clinical decision support in gastroenterology and hepatology. (source nr: 76)
   URL: https://pubmed.ncbi.nlm.nih.gov/40846793

[77] Assessing DeepSeek-R1 for Clinical Decision Support in Multidisciplinary Laboratory Medicine. (source nr: 77)
   URL: https://pubmed.ncbi.nlm.nih.gov/40823482

[78] LLM-Based Extraction of Imaging Features from Radiology Reports: Automating Disease Activity Scoring in Crohn's Disease. (source nr: 78)
   URL: https://pubmed.ncbi.nlm.nih.gov/40783343

[79] CDE-Mapper: Using retrieval-augmented language models for linking clinical data elements to controlled vocabularies. (source nr: 79)
   URL: https://pubmed.ncbi.nlm.nih.gov/40743885

[80] A structured evaluation of LLM-generated step-by-step instructions in cadaveric brachial plexus dissection. (source nr: 80)
   URL: https://pubmed.ncbi.nlm.nih.gov/40598351

[81] Advancing large language models as patient education tools for inflammatory bowel disease. (source nr: 81)
   URL: https://pubmed.ncbi.nlm.nih.gov/40495941

[82] Large language models for dermatological image interpretation - a comparative study. (source nr: 82)
   URL: https://pubmed.ncbi.nlm.nih.gov/40420705

[83] A systematic review of AI as a digital twin for prostate cancer care. (source nr: 83)
   URL: https://pubmed.ncbi.nlm.nih.gov/40347618

[84] Benchmarking LLM chatbots' oncological knowledge with the Turkish Society of Medical Oncology's annual board examination questions. (source nr: 84)
   URL: https://pubmed.ncbi.nlm.nih.gov/39905358

[85] Leveraging Guideline-Based Clinical Decision Support Systems with Large Language Models: A Case Study with Breast Cancer. (source nr: 85)
   URL: https://pubmed.ncbi.nlm.nih.gov/39880005

[86] Large Language Models lack essential metacognition for reliable medical reasoning. (source nr: 86)
   URL: https://pubmed.ncbi.nlm.nih.gov/39809759

[87] The Use of Generative AI for Scientific Literature Searches for Systematic Reviews: ChatGPT and Microsoft Bing AI Performance Evaluation. (source nr: 87)
   URL: https://pubmed.ncbi.nlm.nih.gov/38771247

[88] Optimization of hepatological clinical guidelines interpretation by large language models: a retrieval augmented generation-based framework. (source nr: 88)
   URL: https://pubmed.ncbi.nlm.nih.gov/38654102

[89] Automated HEART score determination via ChatGPT: Honing a framework for iterative prompt development. (source nr: 89)
   URL: https://pubmed.ncbi.nlm.nih.gov/38481520

[90] Leveraging large language models for gastrointestinal injury detection in athletes: a medical image analysis approach. (source nr: 90)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215522

[91] Artificial Intelligence for Sleep Instability and Motor Phenotyping: Clinical Translation Beyond Sleep Staging. (source nr: 91)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213077

[92] Current Approaches to the Management of Acute Surgical and Medical Emergencies: A Structured Narrative Review. (source nr: 92)
   URL: https://pubmed.ncbi.nlm.nih.gov/42211600

[94] Capturing multi-disease states on a spectrum with machine learning and routine clinical data. (source nr: 94)
   URL: https://pubmed.ncbi.nlm.nih.gov/42208537

[97] [Gender bias and artificial intelligence in cardiology: evidence, clinical implications, and future perspectives]. (source nr: 97)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200232

[98] Artificial Intelligence-Based Risk Stratification in Obesity Care: From Diagnosis to Personalised Treatment Pathways. (source nr: 98)
   URL: https://pubmed.ncbi.nlm.nih.gov/42196828

[99] A Review of Data Engineering in United States Healthcare Infrastructure. (source nr: 99)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194493

[100] Cultural bias in large language models' ability to follow neuroradiology guidelines. (source nr: 100)
   URL: https://pubmed.ncbi.nlm.nih.gov/42189215




________________________________________________________________________________

## ALL SOURCES:
[1] MSML-DenseXmer: harnessing vision transformers through integration with novel dense networks for medical image fusion. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215519

[2] Beyond Correlation: Causal Intervention for Multi-Label Medical Image Diagnosis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213561

[3, 93] Artificial intelligence in nursing practice for older adults with dementia: A narrative review informed by bibliometric mapping and implications for nurse-led research. (source nr: 3, 93)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209252

[4, 95] Explainable AI in kidney stone detection and segmentation: a mini review. (source nr: 4, 95)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206076

[5] Artificial intelligence approaches for schizophrenia prediction and its biomarkers using medical imaging data. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206005

[6, 96] Dense-MoE vs Lite-MoE: A Gating-Weight-Aware Pruning Framework for Unpaired Multimodal Breast Cancer Diagnosis. (source nr: 6, 96)
   URL: https://pubmed.ncbi.nlm.nih.gov/42204022

[7] SULBA: A Task-Agnostic Data Augmentation Framework for Deep Learning in Medical Image Analysis. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42196912

[8] Unsupervised Anomaly Detection in Medical Imaging: A Survey of Methods, Challenges, and Future Directions. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194303

[9] Advancing Brain Tumor Diagnosis Using Deep Learning: A Systematic and Critical Review on Methodological Approaches to Glioma Segmentation and Classification Through Multiparametric MRI. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42192781

[10] Federated Learning with Differential Privacy for Ultrasound Breast Cancer Classification: An Empirical Study. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188242

[11] A Robust Intelligent CNN Model Enhanced with Gabor-Based Feature Extraction, SMOTE Balancing, and Adam Optimization for Multi-Grade Diabetic Retinopathy Classification. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188225

[12] Neural Computing Advancements in Cardiac Imaging: A Review of Deep Learning Approaches for Heart Disease Diagnosis. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188217

[13] A Few-shot Multimodal Deep Learning Framework For Precision Diagnosis Of Parotid Gland. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42184237

[14] The Evolving Role of Artificial Intelligence in Fracture Diagnosis and Surgical Planning in Orthopaedics: Current Insights and Future Directions. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42181443

[15] Performance evaluation of large language models in the diagnosis of emergency internal medicine diseases: a retrospective study. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42180499

[16] A deep learning and radiomics fusion model enhances endoscopic ultrasonography diagnosis of gastric tumors. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42180041

[17] Research on multi-stage deep learning based intelligent diagnosis of skin diseases and skin medicine diagnosis community construction concept. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/42168500

[18] Precision oncology: from large language models to multi-agent systems. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/42158433

[19] A deep learning system for non-invasive breast cancer diagnosis with multimodal data. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42157015

[20] Temporally consistent longitudinal brain tumor segmentation using a temporal spatial transformer network. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42156537

[21] Mitigating Bias in Multi-Label Medical Text Classification: A Cooperative Training Framework with Dynamic Debiasing. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42152185

[22] Research Topics and Trends of Artificial Intelligence in Critical Care Nursing: A Bibliometric Analysis. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42151094

[23] Machine Learning in Nonischemic Cardiomyopathy: Phenotyping, Mechanism Discovery, and Clinical Applications. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42150097

[24] A novel hybrid framework integrating GA-driven 3D ResUNetGAN for MRI brain tumor segmentation. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42149959

[25] Advancements in Image-Based Artificial Intelligence in the Diagnosis and Treatment of Head and Neck Squamous Cell Carcinoma: A Narrative Review. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42147747

[26] Current trends and future directions of artificial intelligence in lung cancer diagnosis. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/42147376

[27] Bibliometric Trends in the Integration of Computer Vision With Healthcare. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/42145939

[28] Artificial intelligence with deep learning driven entropy-curvature attention mechanism for detection and segmentation of skin lesions using biomedical images. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/42140962

[29] Dual-Phase Computed Tomography-Based Deep Learning Architecture for Three-Year Survival Prediction in Hepatocellular Carcinoma. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/42135555

[30] Role of Artificial Intelligence and Machine Learning in Diagnosing Knee Lesions: Where Are We Now? (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42131654

[31] Metaheuristic optimization of deep CNNs for multi-class diagnosis of cervical cancer and lymphoma. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129228

[32] Federated learning for privacy-preserving skin cancer classification using deep neural networks. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/42125708

[33] Liquid Biopsy in Colorectal Cancer: Future Perspectives Through the Lens of Artificial Intelligence-A Comprehensive Review of Novel Literature. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/42123533

[34] Are AI Neuroimaging Models Ready for Clinical Use? A Systematic Methodological Review. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/42123173

[35] Hierarchical Deep Learning Framework for Skin Disease and Cancer Classification Performance Enhancement. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122557

[36] Self-Explaining Neural Networks for Transparent Parkinson's Disease Screening. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122390

[37] Private Ensembles, Public Confidence: A PATE-to-MedPrompt System for Autism Detection. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/42121994

[38] Performance and generalization analysis of machine learning, deep learning, and transformer models for histopathology image classification. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/42120655

[39] Deep Learning Framework for Early Detection of Pancreatic Cancer Using Multi-modal Medical Imaging Analysis. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/42118516

[40] Automated Lesion Segmentation in Medical Imaging via Integration of nnU-Net Optimization and SAM Approach. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/42116853

[41] Dissecting self-supervised learning strategies for transfer learning in MRI prostate cancer diagnosis. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115652

[42] Bridging modalities: a deep learning framework for brain tumor classification via CT-MRI integration and model fusion. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110680

[43] Exploring AI as a Diagnostic Tool in Medical Imaging for Dermatopathological Diseases. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/42109557

[44] Mamba-Based Deep Learning Model for Automated Periapical Index Classification Using Periapical Radiographs and Clinical Metadata. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/42108657

[45] A Systematic Review: The Application of Attention Mechanisms in Medical Ultrasound Image Processing. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/42106306

[46] A deep learning model for automated identification of age-related macular degeneration atrophy. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/42105087

[47] A modular deep learning architecture for interpretable disease prediction across tabular clinical and biometric datasets. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/42102106

[48, 54] An automatic consult reply system for therapeutic plasma exchange using retrieval-augmented generation. (source nr: 48, 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/42091449

[49] Artificial intelligence in migraine: a narrative review on the diagnostic, prognostic, and therapeutic applications. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/42088847

[50] Pancreatic tumor detection in computed tomography images through a rotary positional siamese vision transformer. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/42086843

[51] Quality of AI-generated temporomandibular disorder information: A comparative analysis based on Turkish patient queries. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198915

[52] Modeling the Clinical Reasoning Workflow: A Dynamic, Time-Aware CDSS for the Emergency Department. (source nr: 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174892

[53] Susceptibility of Large Language Models to User-Driven Factors in Medical Queries. (source nr: 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/42110657

[55] Targeted use of large language models for EHR-based computable phenotyping. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/41990328

[56] Precision Grounding: augmenting large language models with evidence-based databases for trustworthy genetic variant summarization. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/41950627

[57] Collaborative multi-agent conversational artificial intelligence for clinical support in Parkinson disease. (source nr: 57)
   URL: https://pubmed.ncbi.nlm.nih.gov/41925479

[58] Performance of Large Language Models vs Conventional Machine Learning for Predicting Clinical Outcomes With Limited Data: Comparative Study. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/41921208

[59] Large language models enhance diagnostic reasoning of medical students in rheumatology: a randomized controlled trial. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/41877128

[60] A Feasibility Study of Literature-Guided HRV Stratification Using Large Language Models. (source nr: 60)
   URL: https://pubmed.ncbi.nlm.nih.gov/41750688

[61] Retrieval-Augmented Generation for Medical Question Answering on a Heart Failure Dataset: Performance Analysis. (source nr: 61)
   URL: https://pubmed.ncbi.nlm.nih.gov/41747226

[62] Using LLMs to Interpret Arterial Blood Gases: Comparison of a Novel Math Scratchpad with Different Prompting Methods in a Three-Arm Trial. (source nr: 62)
   URL: https://pubmed.ncbi.nlm.nih.gov/41726393

[63] Evolving Consultation: Enhancing Ophthalmic Diagnostic Performance Using Large Language Model. (source nr: 63)
   URL: https://pubmed.ncbi.nlm.nih.gov/41725833

[64] Deriving wisdom from data: The value and continued rationale for structured data in the era of artificial intelligence-driven oncology care. (source nr: 64)
   URL: https://pubmed.ncbi.nlm.nih.gov/41701629

[65] Interpretable ensemble machine learning framework for cardiovascular disease prediction using EMR data and large language models in Ethiopia. (source nr: 65)
   URL: https://pubmed.ncbi.nlm.nih.gov/41662408

[66] Comparative evaluation of large language models for hip fracture-related patient questions: DeepSeek-V3-FW, Gemini 2.0 Flash, and ChatGPT-4.5. (source nr: 66)
   URL: https://pubmed.ncbi.nlm.nih.gov/41623725

[67] Large language models and conditional rules in clinical decision support systems. (source nr: 67)
   URL: https://pubmed.ncbi.nlm.nih.gov/41584932

[68] Evaluating Retrieval-Augmented Generation-Large Language Models for Infective Endocarditis Prophylaxis: Clinical Accuracy and Efficiency. (source nr: 68)
   URL: https://pubmed.ncbi.nlm.nih.gov/41453288

[69] Comparative Evaluation of Advanced Chunking for Retrieval-Augmented Generation in Large Language Models for Clinical Decision Support. (source nr: 69)
   URL: https://pubmed.ncbi.nlm.nih.gov/41301150

[70] MicroRAG: Development of a Novel Artificial Intelligence Retrieval-Augmented Generation Model for Microsurgery Clinical Decision Support. (source nr: 70)
   URL: https://pubmed.ncbi.nlm.nih.gov/41235700

[71] Locally deployed context-aware chatbot outperforms generic large language models for guideline-concordant pediatric imaging recommendations. (source nr: 71)
   URL: https://pubmed.ncbi.nlm.nih.gov/41231298

[72] Web based AI-driven framework combining multi-modal data with CNN and LLM for Parkinson's disease diagnosis. (source nr: 72)
   URL: https://pubmed.ncbi.nlm.nih.gov/41188323

[73] Large language models with retrieval-augmented generation enhance expert modelling of Bayesian network for clinical decision support. (source nr: 73)
   URL: https://pubmed.ncbi.nlm.nih.gov/41182676

[74] Development and Evaluation of a Retrieval-Augmented Generation Chatbot for Orthopedic and Trauma Surgery Patient Education: Mixed-Methods Study. (source nr: 74)
   URL: https://pubmed.ncbi.nlm.nih.gov/41134117

[75] Sleep, interrupted - when short nights take their toll. (source nr: 75)
   URL: https://pubmed.ncbi.nlm.nih.gov/41038089

[76] Large language models for clinical decision support in gastroenterology and hepatology. (source nr: 76)
   URL: https://pubmed.ncbi.nlm.nih.gov/40846793

[77] Assessing DeepSeek-R1 for Clinical Decision Support in Multidisciplinary Laboratory Medicine. (source nr: 77)
   URL: https://pubmed.ncbi.nlm.nih.gov/40823482

[78] LLM-Based Extraction of Imaging Features from Radiology Reports: Automating Disease Activity Scoring in Crohn's Disease. (source nr: 78)
   URL: https://pubmed.ncbi.nlm.nih.gov/40783343

[79] CDE-Mapper: Using retrieval-augmented language models for linking clinical data elements to controlled vocabularies. (source nr: 79)
   URL: https://pubmed.ncbi.nlm.nih.gov/40743885

[80] A structured evaluation of LLM-generated step-by-step instructions in cadaveric brachial plexus dissection. (source nr: 80)
   URL: https://pubmed.ncbi.nlm.nih.gov/40598351

[81] Advancing large language models as patient education tools for inflammatory bowel disease. (source nr: 81)
   URL: https://pubmed.ncbi.nlm.nih.gov/40495941

[82] Large language models for dermatological image interpretation - a comparative study. (source nr: 82)
   URL: https://pubmed.ncbi.nlm.nih.gov/40420705

[83] A systematic review of AI as a digital twin for prostate cancer care. (source nr: 83)
   URL: https://pubmed.ncbi.nlm.nih.gov/40347618

[84] Benchmarking LLM chatbots' oncological knowledge with the Turkish Society of Medical Oncology's annual board examination questions. (source nr: 84)
   URL: https://pubmed.ncbi.nlm.nih.gov/39905358

[85] Leveraging Guideline-Based Clinical Decision Support Systems with Large Language Models: A Case Study with Breast Cancer. (source nr: 85)
   URL: https://pubmed.ncbi.nlm.nih.gov/39880005

[86] Large Language Models lack essential metacognition for reliable medical reasoning. (source nr: 86)
   URL: https://pubmed.ncbi.nlm.nih.gov/39809759

[87] The Use of Generative AI for Scientific Literature Searches for Systematic Reviews: ChatGPT and Microsoft Bing AI Performance Evaluation. (source nr: 87)
   URL: https://pubmed.ncbi.nlm.nih.gov/38771247

[88] Optimization of hepatological clinical guidelines interpretation by large language models: a retrieval augmented generation-based framework. (source nr: 88)
   URL: https://pubmed.ncbi.nlm.nih.gov/38654102

[89] Automated HEART score determination via ChatGPT: Honing a framework for iterative prompt development. (source nr: 89)
   URL: https://pubmed.ncbi.nlm.nih.gov/38481520

[90] Leveraging large language models for gastrointestinal injury detection in athletes: a medical image analysis approach. (source nr: 90)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215522

[91] Artificial Intelligence for Sleep Instability and Motor Phenotyping: Clinical Translation Beyond Sleep Staging. (source nr: 91)
   URL: https://pubmed.ncbi.nlm.nih.gov/42213077

[92] Current Approaches to the Management of Acute Surgical and Medical Emergencies: A Structured Narrative Review. (source nr: 92)
   URL: https://pubmed.ncbi.nlm.nih.gov/42211600

[94] Capturing multi-disease states on a spectrum with machine learning and routine clinical data. (source nr: 94)
   URL: https://pubmed.ncbi.nlm.nih.gov/42208537

[97] [Gender bias and artificial intelligence in cardiology: evidence, clinical implications, and future perspectives]. (source nr: 97)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200232

[98] Artificial Intelligence-Based Risk Stratification in Obesity Care: From Diagnosis to Personalised Treatment Pathways. (source nr: 98)
   URL: https://pubmed.ncbi.nlm.nih.gov/42196828

[99] A Review of Data Engineering in United States Healthcare Infrastructure. (source nr: 99)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194493

[100] Cultural bias in large language models' ability to follow neuroradiology guidelines. (source nr: 100)
   URL: https://pubmed.ncbi.nlm.nih.gov/42189215


