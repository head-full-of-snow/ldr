基于提供的最新文献（2021-2026年），学习分析（Learning Analytics, LA）和数据驱动评估在教育数据挖掘（Educational Data Mining, EDM）领域的最新科研进展主要体现在以下几个核心方面：预测模型的深化与隐私保护、多模态与物联网（IoT）数据的整合、特定学科（特别是医学与编程）的精细化应用，以及从结果评估向过程性评估的转变。

### 1. 预测性学习分析的发展与挑战：从算法到隐私

预测性建模已成为学习分析的核心实践 [1]。最新的研究不仅关注算法精度的提升，还深入探讨了数据获取的伦理障碍及解决方案。

*   **隐私保护与合成数据：** 由于学生记录受到严格隐私法规的保护，公开数据集的稀缺严重制约了EDM的进展 [3]。为了解决这一矛盾，最新研究引入了隐私保护的合成数据集（如SynEdu-HEDL），旨在在不泄露个人身份信息的前提下，促进协作研究和算法验证 [6]。这表明该领域正从单纯的数据挖掘转向兼顾伦理合规性的数据科学框架 [3]。
*   **模型优化：** 针对早期学生画像和结果预测，研究者提出了包含特征工程在内的机器学习框架，强调在数据收集阶段就需考虑特征的有效性 [3]。在医学教育中，人工神经网络（ANN）和朴素贝叶斯（Naïve Bayes）等模型被用于识别第一年医学生的学业风险，证明了机器学习在早期预警系统中的有效性 [11]。

### 2. 多模态数据与物联网（IoT）在技能评估中的应用

传统的评估往往依赖主观判断或简单的行为日志，最新进展显示，通过整合物理传感器和数字行为数据，可以实现更客观、细粒度的技能评估。

*   **手术技能的客观化评估：** 在医学外科培训中，传统专家评估存在主观性和时间成本高的问题。最新研究利用物联网（IoT）系统和传感器数据，结合机器学习，实现了对手术技术技能的客观、自动化评估 [22], [23]。这种数据驱动的方法减少了评估者之间的变异，提高了评估的信度 [23]。
*   **多模态融合：** 除了传感器数据，研究还关注多模态数据（MMD）的整合，例如将基于运动的教育游戏（MBEG）中的身体动作数据与学习体验相结合，通过AI代理实时支持学习 [20]。此外，视频观看行为分析也被用于衡量学生在异步在线药理学课程中的参与度，发现高度投入的观看模式与良好的自我期望和成绩显著相关 [24]。

### 3. 特定学科领域的精细化学习行为分析

不同学科的数据特征和评估需求存在差异，最新研究针对编程、兽医和医学教育进行了针对性的数据挖掘。

*   **编程教育中的行为洞察：** 针对编程课程高辍学率的问题，研究者利用学习管理系统（LMS）中的日志数据，结合熵（Entropy）和社区检测算法，分析学生的高维学习行为数据，以揭示学习行为与学业成绩之间的关系，从而支持早期干预 [4]。
*   **医学教育的连续性与综合评估：** 在基于能力的医学教育（CBME）中，学习分析被用于解决临床能力委员会（CCC）数据整合困难的问题 [13]。通过整合来自不同来源（如住院医师自评、导师评估、临床数据）的信息，学习分析有助于更全面地监控培训生的进展 [13], [14]。例如，一项研究比较了住院医师自评与导师评估的一致性，为形成性评估在总结性决策中的使用提供了证据 [27]。
*   **兽医教育的早期预警：** 尽管兽医教育在数据驱动研究方面相对滞后，但最新文献指出，利用大数据识别高风险学生并提供个性化支持，可以显著提高学业成功率 [15], [21]。

### 4. 评估范式的转变：从 episodic 到 continuous 及可视化反馈

数据驱动评估正从单一的期末考试转向持续的过程性评估，并强调可视化工具的用户体验。

*   **持续评估与过程挖掘：** 研究强调连续性监督的重要性，利用学习分析比较持续督导者与阶段性督导者在评估形式上的差异，以支持基于能力的教育程序重构 [14]。在网络安全训练中，过程挖掘（Process Mining）技术被用于分析事件日志，以理解学习者的行为路径 [17]。
*   **仪表板（Dashboard）的用户中心设计：** 学习分析仪表板（LADs）不仅用于提供数据可视化，更需考虑学习者的实际需求。研究表明，对于远程和在线学习者，仪表板的设计必须与他们的具体需求对齐，才能有效支持自我调节学习 [9]。在医学教育中，开发用户中心的反馈工具，将分散的反馈信息整合到单一平台，是提高反馈有效性的关键 [25]。
*   **电子档案袋（E-portfolio）的整合：** 电子档案袋作为学习成果和能力发展的可视化工具，其成功实施依赖于与课程学习成果的明确对齐，并需要学生和教师的共同支持 [26]。

### 5. 新兴技术与未来方向

*   **元宇宙与模拟：** 元宇宙增强的模拟技术（如VR/AR）正在改变医学教育，提供逼真的诊断和治疗体验 [29]。这些沉浸式环境产生了大量交互数据，为学习分析提供了新的数据源 [29]。
*   **应用程序生成数据：** 除了传统的LMS数据，学习应用程序生成的使用数据（如阅读速度、应用内互动）也被证明具有监测学习进展的潜力 [18]。

### 批判性反思

尽管进展显著，但该领域仍面临挑战：
1.  **数据孤岛与整合难题：** 尽管有电子政府分析平台等尝试 [7]，但跨系统的数据整合（如行政数据与应用数据 [18]）仍然困难，且数据质量参差不齐 [13]。
2.  **可解释性与伦理：** 虽然合成数据缓解了隐私问题 [6]，但黑箱模型（如深度学习）的可解释性仍是教育者采纳的关键障碍。此外，算法偏见可能加剧教育不平等，需在模型设计中加以警惕。
3.  **从数据到行动的鸿沟：** 拥有大量数据并不等同于改善学习。研究指出，必须将分析结果转化为具体的、个性化的干预措施 [3]，并且需要教育者具备相应的数据素养 [21]。

综上所述，最新科研进展表明，学习分析与数据驱动评估正朝着**多模态融合、隐私保护、客观化技能评估以及用户中心化的反馈机制**方向发展，特别是在医学和STEM教育中展现出巨大的应用潜力。

[1] Recent advances in Predictive Learning Analytics: A decade systematic review (2012-2022). (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/36571084

[2] Educational Data Mining Techniques for Student Performance Prediction: Method Review and Comparison Analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/34950079

[3] A machine learning framework with a public synthetic data set for early student profiling and outcome prediction. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42248989

[4] Students' Learning Behaviour in Programming Education Analysis: Insights from Entropy and Community Detection. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/37628255

[5] Student learning performance prediction based on online behavior: an empirical study during the COVID-19 pandemic. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/38077563

[6] A privacy preserving synthetic learner dataset for learning analytics in technology enhanced higher education. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41872404

[7] Academic data derived from a university e-government analytic platform: An educational data mining approach. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/37456117

[8] Learning analytics in virtual laboratories: a systematic literature review of empirical research. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40477836

[9] Exploring critical factors of the perceived usefulness of a learning analytics dashboard for distance university students. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/34778534

[10] Revealing latent traits in the social behavior of distance learning students. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/34602848

[11] Predicting students' academic progress and related attributes in first-year medical students: an analysis with artificial neural networks and Naïve Bayes. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/38243257

[12] Utilizing Learning Analytics in Radiology: A Pilot Study of an e-Learning Platform in Medical Student Education. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/37331868

[13] Using learning analytics in clinical competency committees: Increasing the impact of competency-based medical education. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/36821373

[14] Using Learning Analytics to Examine Differences in Assessment Forms From Continuous Versus Episodic Supervisors of Family Medicine Residents. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/36274777

[15] Adopting Learning Analytics in a First-Year Veterinarian Professional Program: What We Could Know in Advance about Student Learning Progress. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/34898397

[16] Discriminable Multi-Label Attribute Selection for Pre-Course Student Performance Prediction. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/34681977

[17] Hands-on cybersecurity training behavior data for process mining. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/38186737

[18] Both sides of the story: comparing student-level data on reading performance from administrative registers to application generated data from a reading app. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/34426779

[19] Students' performance in interactive environments: an intelligent model. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/37346604

[20] Keep Calm and Do Not Carry-Forward: Toward Sensor-Data Driven AI Agent to Enhance Human Learning. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/35098109

[21] Using Machine Learning in Veterinary Medical Education: An Introduction for Veterinary Medicine Educators. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/37756059

[22] A cost-effective IoT learning environment for the training and assessment of surgical technical skills with visual learning analytics. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/34798158

[23] Objective and automated assessment of surgical technical skills with IoT systems: A systematic literature review. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/33581827

[24] Highly Engaged Video-Watching Pattern in Asynchronous Online Pharmacology Course in Pre-clinical 4th-Year Medical Students Was Associated With a Good Self-Expectation, Understanding, and Performance. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/35127756

[25] Design and usability testing of an in-house developed performance feedback tool for medical students. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/34162382

[26] [Portfolio - a tool for making learning and competence development visible]. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/34542895

[27] A Comparison of Resident-Completed and Preceptor-Completed Formative Workplace-Based Assessments in a Competency-Based Medical Education Program. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/36098690

[28] A machine learning approach to carbon emissions prediction of the top eleven emitters by 2030 and their prospects for meeting Paris agreement targets. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/40461645

[29] Metaverse-based simulation: a scoping review of charting medical education over the last two decades in the lens of the 'marvelous medical education machine'. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/39535116

[30] Dynamic risk assessment to improve quality of care in patients with atrial fibrillation: the 7th AFNET/EHRA Consensus Conference. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/33555020




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 学习分析与数据驱动评估 教育数据挖掘 学习行为分析 最新科研进展
2. 2025-2026年学习分析、教育数据挖掘与学习行为分析领域的最新科研进展与前沿趋势

 #### Iteration 2:
1. 2025-2026年生成式AI（GenAI）与大语言模型（LLM）如何从根本上重构学习行为分析的底层逻辑，特别是在从“行为日志预测”向“认知状态实时推理”转变的过程中，现有的教育数据挖掘模型在应对AI辅助下的非自然学习行为（如AI-generated content interaction）时面临哪些具体的方法学失效或偏差挑战？

 #### Iteration 3:
1. 鉴于2025-2026年生成式AI已深度融入学习过程，现有的教育数据挖掘模型在处理由LLM辅助生成的“非自然”或“合成”学习行为数据（如AI生成的代码、文本交互日志）时，如何具体量化并消除由此产生的算法偏差，以实现对学习者真实认知状态（而非AI代理行为）的精准实时推理与评估？



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
学习分析与数据驱动评估 教育数据挖掘 学习行为分析 最新科研进展



Searched with 2 questions, found 35 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
学习分析与数据驱动评估 教育数据挖掘 学习行为分析 最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
学习分析与数据驱动评估 教育数据挖掘 学习行为分析 最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
学习分析与数据驱动评估 教育数据挖掘 学习行为分析 最新科研进展



基于提供的最新文献（2021-2026年），学习分析（Learning Analytics, LA）和数据驱动评估在教育数据挖掘（Educational Data Mining, EDM）领域的最新科研进展主要体现在以下几个核心方面：预测模型的深化与隐私保护、多模态与物联网（IoT）数据的整合、特定学科（特别是医学与编程）的精细化应用，以及从结果评估向过程性评估的转变。

### 1. 预测性学习分析的发展与挑战：从算法到隐私

预测性建模已成为学习分析的核心实践 [1]。最新的研究不仅关注算法精度的提升，还深入探讨了数据获取的伦理障碍及解决方案。

*   **隐私保护与合成数据：** 由于学生记录受到严格隐私法规的保护，公开数据集的稀缺严重制约了EDM的进展 [3]。为了解决这一矛盾，最新研究引入了隐私保护的合成数据集（如SynEdu-HEDL），旨在在不泄露个人身份信息的前提下，促进协作研究和算法验证 [6]。这表明该领域正从单纯的数据挖掘转向兼顾伦理合规性的数据科学框架 [3]。
*   **模型优化：** 针对早期学生画像和结果预测，研究者提出了包含特征工程在内的机器学习框架，强调在数据收集阶段就需考虑特征的有效性 [3]。在医学教育中，人工神经网络（ANN）和朴素贝叶斯（Naïve Bayes）等模型被用于识别第一年医学生的学业风险，证明了机器学习在早期预警系统中的有效性 [11]。

### 2. 多模态数据与物联网（IoT）在技能评估中的应用

传统的评估往往依赖主观判断或简单的行为日志，最新进展显示，通过整合物理传感器和数字行为数据，可以实现更客观、细粒度的技能评估。

*   **手术技能的客观化评估：** 在医学外科培训中，传统专家评估存在主观性和时间成本高的问题。最新研究利用物联网（IoT）系统和传感器数据，结合机器学习，实现了对手术技术技能的客观、自动化评估 [22], [23]。这种数据驱动的方法减少了评估者之间的变异，提高了评估的信度 [23]。
*   **多模态融合：** 除了传感器数据，研究还关注多模态数据（MMD）的整合，例如将基于运动的教育游戏（MBEG）中的身体动作数据与学习体验相结合，通过AI代理实时支持学习 [20]。此外，视频观看行为分析也被用于衡量学生在异步在线药理学课程中的参与度，发现高度投入的观看模式与良好的自我期望和成绩显著相关 [24]。

### 3. 特定学科领域的精细化学习行为分析

不同学科的数据特征和评估需求存在差异，最新研究针对编程、兽医和医学教育进行了针对性的数据挖掘。

*   **编程教育中的行为洞察：** 针对编程课程高辍学率的问题，研究者利用学习管理系统（LMS）中的日志数据，结合熵（Entropy）和社区检测算法，分析学生的高维学习行为数据，以揭示学习行为与学业成绩之间的关系，从而支持早期干预 [4]。
*   **医学教育的连续性与综合评估：** 在基于能力的医学教育（CBME）中，学习分析被用于解决临床能力委员会（CCC）数据整合困难的问题 [13]。通过整合来自不同来源（如住院医师自评、导师评估、临床数据）的信息，学习分析有助于更全面地监控培训生的进展 [13], [14]。例如，一项研究比较了住院医师自评与导师评估的一致性，为形成性评估在总结性决策中的使用提供了证据 [27]。
*   **兽医教育的早期预警：** 尽管兽医教育在数据驱动研究方面相对滞后，但最新文献指出，利用大数据识别高风险学生并提供个性化支持，可以显著提高学业成功率 [15], [21]。

### 4. 评估范式的转变：从 episodic 到 continuous 及可视化反馈

数据驱动评估正从单一的期末考试转向持续的过程性评估，并强调可视化工具的用户体验。

*   **持续评估与过程挖掘：** 研究强调连续性监督的重要性，利用学习分析比较持续督导者与阶段性督导者在评估形式上的差异，以支持基于能力的教育程序重构 [14]。在网络安全训练中，过程挖掘（Process Mining）技术被用于分析事件日志，以理解学习者的行为路径 [17]。
*   **仪表板（Dashboard）的用户中心设计：** 学习分析仪表板（LADs）不仅用于提供数据可视化，更需考虑学习者的实际需求。研究表明，对于远程和在线学习者，仪表板的设计必须与他们的具体需求对齐，才能有效支持自我调节学习 [9]。在医学教育中，开发用户中心的反馈工具，将分散的反馈信息整合到单一平台，是提高反馈有效性的关键 [25]。
*   **电子档案袋（E-portfolio）的整合：** 电子档案袋作为学习成果和能力发展的可视化工具，其成功实施依赖于与课程学习成果的明确对齐，并需要学生和教师的共同支持 [26]。

### 5. 新兴技术与未来方向

*   **元宇宙与模拟：** 元宇宙增强的模拟技术（如VR/AR）正在改变医学教育，提供逼真的诊断和治疗体验 [29]。这些沉浸式环境产生了大量交互数据，为学习分析提供了新的数据源 [29]。
*   **应用程序生成数据：** 除了传统的LMS数据，学习应用程序生成的使用数据（如阅读速度、应用内互动）也被证明具有监测学习进展的潜力 [18]。

### 批判性反思

尽管进展显著，但该领域仍面临挑战：
1.  **数据孤岛与整合难题：** 尽管有电子政府分析平台等尝试 [7]，但跨系统的数据整合（如行政数据与应用数据 [18]）仍然困难，且数据质量参差不齐 [13]。
2.  **可解释性与伦理：** 虽然合成数据缓解了隐私问题 [6]，但黑箱模型（如深度学习）的可解释性仍是教育者采纳的关键障碍。此外，算法偏见可能加剧教育不平等，需在模型设计中加以警惕。
3.  **从数据到行动的鸿沟：** 拥有大量数据并不等同于改善学习。研究指出，必须将分析结果转化为具体的、个性化的干预措施 [3]，并且需要教育者具备相应的数据素养 [21]。

综上所述，最新科研进展表明，学习分析与数据驱动评估正朝着**多模态融合、隐私保护、客观化技能评估以及用户中心化的反馈机制**方向发展，特别是在医学和STEM教育中展现出巨大的应用潜力。

### SOURCES USED IN THIS SECTION:
[1] Recent advances in Predictive Learning Analytics: A decade systematic review (2012-2022). (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/36571084

[2] Educational Data Mining Techniques for Student Performance Prediction: Method Review and Comparison Analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/34950079

[3] A machine learning framework with a public synthetic data set for early student profiling and outcome prediction. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42248989

[4] Students' Learning Behaviour in Programming Education Analysis: Insights from Entropy and Community Detection. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/37628255

[5] Student learning performance prediction based on online behavior: an empirical study during the COVID-19 pandemic. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/38077563

[6] A privacy preserving synthetic learner dataset for learning analytics in technology enhanced higher education. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41872404

[7] Academic data derived from a university e-government analytic platform: An educational data mining approach. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/37456117

[8] Learning analytics in virtual laboratories: a systematic literature review of empirical research. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40477836

[9] Exploring critical factors of the perceived usefulness of a learning analytics dashboard for distance university students. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/34778534

[10] Revealing latent traits in the social behavior of distance learning students. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/34602848

[11] Predicting students' academic progress and related attributes in first-year medical students: an analysis with artificial neural networks and Naïve Bayes. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/38243257

[12] Utilizing Learning Analytics in Radiology: A Pilot Study of an e-Learning Platform in Medical Student Education. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/37331868

[13] Using learning analytics in clinical competency committees: Increasing the impact of competency-based medical education. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/36821373

[14] Using Learning Analytics to Examine Differences in Assessment Forms From Continuous Versus Episodic Supervisors of Family Medicine Residents. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/36274777

[15] Adopting Learning Analytics in a First-Year Veterinarian Professional Program: What We Could Know in Advance about Student Learning Progress. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/34898397

[16] Discriminable Multi-Label Attribute Selection for Pre-Course Student Performance Prediction. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/34681977

[17] Hands-on cybersecurity training behavior data for process mining. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/38186737

[18] Both sides of the story: comparing student-level data on reading performance from administrative registers to application generated data from a reading app. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/34426779

[19] Students' performance in interactive environments: an intelligent model. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/37346604

[20] Keep Calm and Do Not Carry-Forward: Toward Sensor-Data Driven AI Agent to Enhance Human Learning. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/35098109

[21] Using Machine Learning in Veterinary Medical Education: An Introduction for Veterinary Medicine Educators. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/37756059

[22] A cost-effective IoT learning environment for the training and assessment of surgical technical skills with visual learning analytics. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/34798158

[23] Objective and automated assessment of surgical technical skills with IoT systems: A systematic literature review. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/33581827

[24] Highly Engaged Video-Watching Pattern in Asynchronous Online Pharmacology Course in Pre-clinical 4th-Year Medical Students Was Associated With a Good Self-Expectation, Understanding, and Performance. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/35127756

[25] Design and usability testing of an in-house developed performance feedback tool for medical students. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/34162382

[26] [Portfolio - a tool for making learning and competence development visible]. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/34542895

[27] A Comparison of Resident-Completed and Preceptor-Completed Formative Workplace-Based Assessments in a Competency-Based Medical Education Program. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/36098690

[28] A machine learning approach to carbon emissions prediction of the top eleven emitters by 2030 and their prospects for meeting Paris agreement targets. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/40461645

[29] Metaverse-based simulation: a scoping review of charting medical education over the last two decades in the lens of the 'marvelous medical education machine'. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/39535116

[30] Dynamic risk assessment to improve quality of care in patients with atrial fibrillation: the 7th AFNET/EHRA Consensus Conference. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/33555020




________________________________________________________________________________

## ALL SOURCES:
[1] Recent advances in Predictive Learning Analytics: A decade systematic review (2012-2022). (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/36571084

[2] Educational Data Mining Techniques for Student Performance Prediction: Method Review and Comparison Analysis. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/34950079

[3] A machine learning framework with a public synthetic data set for early student profiling and outcome prediction. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42248989

[4] Students' Learning Behaviour in Programming Education Analysis: Insights from Entropy and Community Detection. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/37628255

[5] Student learning performance prediction based on online behavior: an empirical study during the COVID-19 pandemic. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/38077563

[6] A privacy preserving synthetic learner dataset for learning analytics in technology enhanced higher education. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/41872404

[7] Academic data derived from a university e-government analytic platform: An educational data mining approach. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/37456117

[8] Learning analytics in virtual laboratories: a systematic literature review of empirical research. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/40477836

[9] Exploring critical factors of the perceived usefulness of a learning analytics dashboard for distance university students. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/34778534

[10] Revealing latent traits in the social behavior of distance learning students. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/34602848

[11] Predicting students' academic progress and related attributes in first-year medical students: an analysis with artificial neural networks and Naïve Bayes. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/38243257

[12] Utilizing Learning Analytics in Radiology: A Pilot Study of an e-Learning Platform in Medical Student Education. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/37331868

[13] Using learning analytics in clinical competency committees: Increasing the impact of competency-based medical education. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/36821373

[14] Using Learning Analytics to Examine Differences in Assessment Forms From Continuous Versus Episodic Supervisors of Family Medicine Residents. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/36274777

[15] Adopting Learning Analytics in a First-Year Veterinarian Professional Program: What We Could Know in Advance about Student Learning Progress. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/34898397

[16] Discriminable Multi-Label Attribute Selection for Pre-Course Student Performance Prediction. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/34681977

[17] Hands-on cybersecurity training behavior data for process mining. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/38186737

[18] Both sides of the story: comparing student-level data on reading performance from administrative registers to application generated data from a reading app. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/34426779

[19] Students' performance in interactive environments: an intelligent model. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/37346604

[20] Keep Calm and Do Not Carry-Forward: Toward Sensor-Data Driven AI Agent to Enhance Human Learning. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/35098109

[21] Using Machine Learning in Veterinary Medical Education: An Introduction for Veterinary Medicine Educators. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/37756059

[22] A cost-effective IoT learning environment for the training and assessment of surgical technical skills with visual learning analytics. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/34798158

[23] Objective and automated assessment of surgical technical skills with IoT systems: A systematic literature review. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/33581827

[24] Highly Engaged Video-Watching Pattern in Asynchronous Online Pharmacology Course in Pre-clinical 4th-Year Medical Students Was Associated With a Good Self-Expectation, Understanding, and Performance. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/35127756

[25] Design and usability testing of an in-house developed performance feedback tool for medical students. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/34162382

[26] [Portfolio - a tool for making learning and competence development visible]. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/34542895

[27] A Comparison of Resident-Completed and Preceptor-Completed Formative Workplace-Based Assessments in a Competency-Based Medical Education Program. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/36098690

[28] A machine learning approach to carbon emissions prediction of the top eleven emitters by 2030 and their prospects for meeting Paris agreement targets. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/40461645

[29] Metaverse-based simulation: a scoping review of charting medical education over the last two decades in the lens of the 'marvelous medical education machine'. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/39535116

[30] Dynamic risk assessment to improve quality of care in patients with atrial fibrillation: the 7th AFNET/EHRA Consensus Conference. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/33555020


