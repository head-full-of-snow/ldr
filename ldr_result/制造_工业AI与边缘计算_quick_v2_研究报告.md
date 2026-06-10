基于2026年的最新科研进展，工业AI与边缘计算（Edge Computing）的结合正处于从“连接”向“智能自治”和“安全可信”深化的关键阶段。最新的研究不再仅仅关注数据上传至云端，而是强调在数据产生的源头（即边缘侧）进行实时处理、决策和安全防护。以下是该领域的主要科研进展综述：

### 1. 工业控制系统的增强安全与数字孪生
随着人工智能被用于规避传统防御，工业控制系统（ICS）面临日益严峻的网络威胁。最新的研究提出了一种结合**数字孪生（Digital Twin）**与**深度学习集成**的安全框架 [1]。该框架通过构建与物理工厂实时同步的、符合物理规律虚拟副本，利用虚拟环境来验证、抑制或确认由深度学习模型产生的异常分数。这种方法超越了传统的基于阈值的检测，能够更准确地识别针对ICS的高级网络攻击 [1]。此外，针对物联网环境下的信任问题，**EdgeGuard-AI** 提出了一种统一的可信驱动和负载感知的调度框架，解决了传统调度器仅优化性能而忽视安全验证的问题，防止任务被分配到虽负载低但可能已被入侵的边缘节点 [5]。

### 2. 异构资源管理与协同计算
随着AI-enabled个人电脑（AI-PC）和异构处理单元（CPU, GPU, NPU）的普及，资源调度变得极为复杂。最新研究提出了**拓扑感知的自适应调度算法**，该算法将实时计算图分析集成到异构资源协调机制中，以应对不同推理阶段和模型架构的动态神经网络拓扑变化 [6]。在更广泛的工业物联网场景中，**雾计算（Fog Computing）** 方法被用于将分析能力更接近设备，通过基于容器的编排实现机器对机器（M2M）架构的自主性和点对点通信，从而满足智能工厂对可扩展性、隐私和低延迟的需求 [2]。此外，针对边缘与云之间的协作，**TinyAct** 框架通过知识蒸馏技术，实现了轻量级的人体动作识别，展示了边缘与云协同处理的潜力 [25]。

### 3. 实时性与低延迟优化
在资源受限的边缘设备上部署大型AI模型（如Transformer）面临高资源需求和“幻觉”（hallucination）风险。**HALL-OPT** 框架旨在同时解决实时边缘智能中的延迟检测和幻觉减少问题，通过单一方案优化Transformer架构在边缘环境的部署 [9]。在工业质检领域，针对烟草质量监控，研究人员开发了基于物联网的数据采集和边缘计算框架，结合深度学习模型实现了实时检测，解决了传统方法效率低和实时性差的问题 [7]。同样，在建筑安全监控中，**MMDet-Edge** 框架通过自适应特征融合架构和可学习的空间-通道注意力机制，在严格的边缘约束下平衡了多目标检测的准确性、实时效率和环境鲁棒性 [8]。

### 4. 跨行业应用：从智能制造到生物医疗
工业AI与边缘计算的应用已延伸至多个垂直领域，体现了其通用性和适应性：
*   **智慧农业与林业：** 在茶园病害诊断中，**GL-MobFormer** 框架结合了MobileNetV3的局部特征提取能力和Transformer的全局上下文建模能力，实现了轻量级的植物病理诊断 [19]。在牛油果果园中，**YOLOv10s-SeqOpt** 框架利用无人机进行实时叶部病害早期检测，解决了传统RGB成像难以检测冠层下早期感染的问题 [20]。在畜牧业，**Edge-AI** 系统通过声学监测和声源定位，实现了母猪发情的实时检测，克服了云端解决方案的高延迟和隐私风险 [17]。
*   **医疗与健康监测：** 边缘计算在医疗领域的应用重点关注隐私保护和实时性。**TinyML** 技术使得在超低成本微控制器（如8位Arduino UNO）上部署量化的一维卷积神经网络成为可能，实现了实时心律失常分类 [3]。在睡眠健康监测中，AI驱动的混合检测框架被用于增强物联网网络的安全性，以应对可穿戴设备产生的大量计算密集型任务 [22]。此外，针对视障人士的**SENSEYE**框架通过资源感知的视觉辅助系统，减少了云端处理带来的延迟和隐私风险 [24]。在放射学领域，边缘计算与物联网的结合推动了去中心化诊断的发展，提高了诊断响应速度 [29]。
*   **智能交通与能源：** 在智能电网中，**IoT增强的虚拟电厂（VPP）** 框架集成了边缘-雾计算、区块链安全和AI驱动的市场机制，将响应时间从传统的>500ms降低到<50ms，显著提高了能源管理效率 [4]。在智能交通系统（ITS）中，**AI冲突观察者** 利用集成Transformer分析全息路口的轨迹数据，以识别冲突严重性和场景，克服了传统方法在处理异构数据时的局限性 [10]。同时，**Edge Driven Trust Aware Threat Detection** 为IoT-ITS环境提供了基于信任的威胁检测，增强了道路安全 [16]。

### 5. 可信计算与区块链集成
鉴于边缘环境的开放性，信任和安全成为核心议题。**区块链** 技术被广泛用于增强边缘计算的可信度。例如，在传感器网络优化中，区块链驱动的信任管理和AI计算被用于解决数据聚合后的信任问题 [27]。在电子健康（eHealth）领域，模糊逻辑和区块链增强的框架旨在提供安全、可解释的电子健康服务，解决集中式云系统的延迟、单点故障和数据隐私问题 [23]。

### 总结
2026年的科研进展表明，工业AI与边缘计算的融合正朝着**更智能（AI-native）、更安全（Zero-Trust/Blockchain）、更高效（TinyML/Hybrid Scheduling）**的方向发展。研究重点已从单纯的算法优化转向系统级的协同，包括数字孪生验证、异构资源调度、边缘-云-雾协同以及基于区块链的可信机制。这些进展为解决工业控制、智慧能源、精准医疗和智能交通等关键领域的实时性、安全性和隐私保护挑战提供了新的技术路径 [1], [2], [4], [5], [6], [9], [23], [27]。

[1] A digital twin and deep-learning ensemble for cyber attack detection in industrial control systems at the IoT edge. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174001

[2] Enhancing smart factory performance via hybrid scheduling and intelligent resource management. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41998135

[3] Real-Time Cardiac Arrhythmia Classification Using TinyML on Ultra-Low-Cost Microcontrollers: A Feasibility Study for Resource-Constrained Environments. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194289

[4] IoT-Enhanced virtual power plants with edge computing and blockchain security for sustainable smart grid management. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42091922

[5] EdgeGuard-AI: Zero-Trust and Load-Aware Federated Scheduling for Secure and Low-Latency IoT Edge Networks. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/41902157

[6] Topology-aware adaptive scheduling algorithm for heterogeneous AI-PC collaborative computing environments. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225722

[7] Edge-enabled IoT framework for real-time tobacco quality monitoring. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42020563

[8] MMDet-Edge: A Multi-Scale and Multi-Object Detection Framework for Safety-Critical Edge Deployment. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755090

[9] Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41786996

[10] AI Conflict Observer: Conflict severity and scenario identification for intersection based on Ensemble Transformer. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41990543

[11] AI-microbial hybrid biosensors: the next generation of intelligent detection systems. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42212947

[12] Dynamic task offloading for sports training monitoring in MEC-assisted smart wearable device systems. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42219406

[13] Construction of a sports bio mechanical injury prediction and AI warning system based on wearable sensors. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42186087

[14] AI-enabled smart surveillance system for secure monitoring and authentication. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42120936

[15] NetworkGuard: An Edge-Based Virtual Network Sensing Architecture for Real-Time Security Monitoring in Smart Home Environments. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41978016

[16] Edge Driven Trust Aware Threat Detection for IoT Enabled Intelligent Transportation Systems. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755056

[17] Edge-AI Enabled Acoustic Monitoring and Spatial Localisation for Sow Oestrus Detection. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829012

[18] Two-Stage Wildlife Event Classification for Edge Deployment. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755305

[19] Bridging CNNs and vision transformers for efficient tea leaf phytopathogen diagnosis: GL-MobFormer. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206155

[20] Spectrally optimised YOLOv10s-SeqOpt framework for real-time UAV-based early detection of avocado foliar diseases in indian orchards. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42135362

[21] An Intelligent Micromachine Perception System for Elevator Fault Diagnosis. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076178

[22] AI-Driven Hybrid Detection and Classification Framework for Secure Sleep Health IoT Networks. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200970

[23] A fuzzy logic and blockchain-enhanced framework for secure, explainable eHealth in Society 5.0. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129248

[24] SENSEYE: a resource-aware visionary framework for assisting individuals with visual disabilities. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115269

[25] TinyAct: A framework for real-time action recognition in the cloud through distillation learning. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42008450

[26] Editorial: Advancing gastrointestinal disease diagnosis with interpretable AI and edge computing for enhanced patient care. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41958550

[27] Blockchain-driven trust management and AI computing for sensor networks optimization. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41844731

[28] Real-Time Vibration Energy Prediction for Semi-Active Suspensions Using Inertial Sensors: A Physics-Guided Deep Learning Approach. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829656

[29] Teleradiology, Edge Computing, and the Internet of Things in Radiology: A RRA Perspective on Decentralized Diagnostics. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41781094

[30] Navigating AI deployment in precision livestock farming: current trends and future prospects. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42137895




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 工业AI与边缘计算的最新科研进展
2. 2025-2026年工业AI与边缘计算融合的最新科研进展与关键技术突破

 #### Iteration 2:
1. 2025-2026年工业AI与边缘计算融合的最新科研进展与关键技术突破

 #### Iteration 3:
1. 2026年工业AI与边缘计算融合在实时性、能效与模型精度权衡方面的最新突破性算法或硬件架构有哪些？



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
工业AI与边缘计算的最新科研进展



Searched with 2 questions, found 0 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
工业AI与边缘计算的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
工业AI与边缘计算的最新科研进展



Searched with 1 questions, found 50 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
工业AI与边缘计算的最新科研进展



基于2026年的最新科研进展，工业AI与边缘计算（Edge Computing）的结合正处于从“连接”向“智能自治”和“安全可信”深化的关键阶段。最新的研究不再仅仅关注数据上传至云端，而是强调在数据产生的源头（即边缘侧）进行实时处理、决策和安全防护。以下是该领域的主要科研进展综述：

### 1. 工业控制系统的增强安全与数字孪生
随着人工智能被用于规避传统防御，工业控制系统（ICS）面临日益严峻的网络威胁。最新的研究提出了一种结合**数字孪生（Digital Twin）**与**深度学习集成**的安全框架 [1]。该框架通过构建与物理工厂实时同步的、符合物理规律虚拟副本，利用虚拟环境来验证、抑制或确认由深度学习模型产生的异常分数。这种方法超越了传统的基于阈值的检测，能够更准确地识别针对ICS的高级网络攻击 [1]。此外，针对物联网环境下的信任问题，**EdgeGuard-AI** 提出了一种统一的可信驱动和负载感知的调度框架，解决了传统调度器仅优化性能而忽视安全验证的问题，防止任务被分配到虽负载低但可能已被入侵的边缘节点 [5]。

### 2. 异构资源管理与协同计算
随着AI-enabled个人电脑（AI-PC）和异构处理单元（CPU, GPU, NPU）的普及，资源调度变得极为复杂。最新研究提出了**拓扑感知的自适应调度算法**，该算法将实时计算图分析集成到异构资源协调机制中，以应对不同推理阶段和模型架构的动态神经网络拓扑变化 [6]。在更广泛的工业物联网场景中，**雾计算（Fog Computing）** 方法被用于将分析能力更接近设备，通过基于容器的编排实现机器对机器（M2M）架构的自主性和点对点通信，从而满足智能工厂对可扩展性、隐私和低延迟的需求 [2]。此外，针对边缘与云之间的协作，**TinyAct** 框架通过知识蒸馏技术，实现了轻量级的人体动作识别，展示了边缘与云协同处理的潜力 [25]。

### 3. 实时性与低延迟优化
在资源受限的边缘设备上部署大型AI模型（如Transformer）面临高资源需求和“幻觉”（hallucination）风险。**HALL-OPT** 框架旨在同时解决实时边缘智能中的延迟检测和幻觉减少问题，通过单一方案优化Transformer架构在边缘环境的部署 [9]。在工业质检领域，针对烟草质量监控，研究人员开发了基于物联网的数据采集和边缘计算框架，结合深度学习模型实现了实时检测，解决了传统方法效率低和实时性差的问题 [7]。同样，在建筑安全监控中，**MMDet-Edge** 框架通过自适应特征融合架构和可学习的空间-通道注意力机制，在严格的边缘约束下平衡了多目标检测的准确性、实时效率和环境鲁棒性 [8]。

### 4. 跨行业应用：从智能制造到生物医疗
工业AI与边缘计算的应用已延伸至多个垂直领域，体现了其通用性和适应性：
*   **智慧农业与林业：** 在茶园病害诊断中，**GL-MobFormer** 框架结合了MobileNetV3的局部特征提取能力和Transformer的全局上下文建模能力，实现了轻量级的植物病理诊断 [19]。在牛油果果园中，**YOLOv10s-SeqOpt** 框架利用无人机进行实时叶部病害早期检测，解决了传统RGB成像难以检测冠层下早期感染的问题 [20]。在畜牧业，**Edge-AI** 系统通过声学监测和声源定位，实现了母猪发情的实时检测，克服了云端解决方案的高延迟和隐私风险 [17]。
*   **医疗与健康监测：** 边缘计算在医疗领域的应用重点关注隐私保护和实时性。**TinyML** 技术使得在超低成本微控制器（如8位Arduino UNO）上部署量化的一维卷积神经网络成为可能，实现了实时心律失常分类 [3]。在睡眠健康监测中，AI驱动的混合检测框架被用于增强物联网网络的安全性，以应对可穿戴设备产生的大量计算密集型任务 [22]。此外，针对视障人士的**SENSEYE**框架通过资源感知的视觉辅助系统，减少了云端处理带来的延迟和隐私风险 [24]。在放射学领域，边缘计算与物联网的结合推动了去中心化诊断的发展，提高了诊断响应速度 [29]。
*   **智能交通与能源：** 在智能电网中，**IoT增强的虚拟电厂（VPP）** 框架集成了边缘-雾计算、区块链安全和AI驱动的市场机制，将响应时间从传统的>500ms降低到<50ms，显著提高了能源管理效率 [4]。在智能交通系统（ITS）中，**AI冲突观察者** 利用集成Transformer分析全息路口的轨迹数据，以识别冲突严重性和场景，克服了传统方法在处理异构数据时的局限性 [10]。同时，**Edge Driven Trust Aware Threat Detection** 为IoT-ITS环境提供了基于信任的威胁检测，增强了道路安全 [16]。

### 5. 可信计算与区块链集成
鉴于边缘环境的开放性，信任和安全成为核心议题。**区块链** 技术被广泛用于增强边缘计算的可信度。例如，在传感器网络优化中，区块链驱动的信任管理和AI计算被用于解决数据聚合后的信任问题 [27]。在电子健康（eHealth）领域，模糊逻辑和区块链增强的框架旨在提供安全、可解释的电子健康服务，解决集中式云系统的延迟、单点故障和数据隐私问题 [23]。

### 总结
2026年的科研进展表明，工业AI与边缘计算的融合正朝着**更智能（AI-native）、更安全（Zero-Trust/Blockchain）、更高效（TinyML/Hybrid Scheduling）**的方向发展。研究重点已从单纯的算法优化转向系统级的协同，包括数字孪生验证、异构资源调度、边缘-云-雾协同以及基于区块链的可信机制。这些进展为解决工业控制、智慧能源、精准医疗和智能交通等关键领域的实时性、安全性和隐私保护挑战提供了新的技术路径 [1], [2], [4], [5], [6], [9], [23], [27]。

### SOURCES USED IN THIS SECTION:
[1] A digital twin and deep-learning ensemble for cyber attack detection in industrial control systems at the IoT edge. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174001

[2] Enhancing smart factory performance via hybrid scheduling and intelligent resource management. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41998135

[3] Real-Time Cardiac Arrhythmia Classification Using TinyML on Ultra-Low-Cost Microcontrollers: A Feasibility Study for Resource-Constrained Environments. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194289

[4] IoT-Enhanced virtual power plants with edge computing and blockchain security for sustainable smart grid management. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42091922

[5] EdgeGuard-AI: Zero-Trust and Load-Aware Federated Scheduling for Secure and Low-Latency IoT Edge Networks. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/41902157

[6] Topology-aware adaptive scheduling algorithm for heterogeneous AI-PC collaborative computing environments. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225722

[7] Edge-enabled IoT framework for real-time tobacco quality monitoring. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42020563

[8] MMDet-Edge: A Multi-Scale and Multi-Object Detection Framework for Safety-Critical Edge Deployment. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755090

[9] Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41786996

[10] AI Conflict Observer: Conflict severity and scenario identification for intersection based on Ensemble Transformer. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41990543

[11] AI-microbial hybrid biosensors: the next generation of intelligent detection systems. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42212947

[12] Dynamic task offloading for sports training monitoring in MEC-assisted smart wearable device systems. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42219406

[13] Construction of a sports bio mechanical injury prediction and AI warning system based on wearable sensors. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42186087

[14] AI-enabled smart surveillance system for secure monitoring and authentication. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42120936

[15] NetworkGuard: An Edge-Based Virtual Network Sensing Architecture for Real-Time Security Monitoring in Smart Home Environments. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41978016

[16] Edge Driven Trust Aware Threat Detection for IoT Enabled Intelligent Transportation Systems. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755056

[17] Edge-AI Enabled Acoustic Monitoring and Spatial Localisation for Sow Oestrus Detection. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829012

[18] Two-Stage Wildlife Event Classification for Edge Deployment. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755305

[19] Bridging CNNs and vision transformers for efficient tea leaf phytopathogen diagnosis: GL-MobFormer. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206155

[20] Spectrally optimised YOLOv10s-SeqOpt framework for real-time UAV-based early detection of avocado foliar diseases in indian orchards. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42135362

[21] An Intelligent Micromachine Perception System for Elevator Fault Diagnosis. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076178

[22] AI-Driven Hybrid Detection and Classification Framework for Secure Sleep Health IoT Networks. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200970

[23] A fuzzy logic and blockchain-enhanced framework for secure, explainable eHealth in Society 5.0. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129248

[24] SENSEYE: a resource-aware visionary framework for assisting individuals with visual disabilities. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115269

[25] TinyAct: A framework for real-time action recognition in the cloud through distillation learning. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42008450

[26] Editorial: Advancing gastrointestinal disease diagnosis with interpretable AI and edge computing for enhanced patient care. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41958550

[27] Blockchain-driven trust management and AI computing for sensor networks optimization. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41844731

[28] Real-Time Vibration Energy Prediction for Semi-Active Suspensions Using Inertial Sensors: A Physics-Guided Deep Learning Approach. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829656

[29] Teleradiology, Edge Computing, and the Internet of Things in Radiology: A RRA Perspective on Decentralized Diagnostics. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41781094

[30] Navigating AI deployment in precision livestock farming: current trends and future prospects. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42137895




________________________________________________________________________________

## ALL SOURCES:
[1] A digital twin and deep-learning ensemble for cyber attack detection in industrial control systems at the IoT edge. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174001

[2] Enhancing smart factory performance via hybrid scheduling and intelligent resource management. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/41998135

[3] Real-Time Cardiac Arrhythmia Classification Using TinyML on Ultra-Low-Cost Microcontrollers: A Feasibility Study for Resource-Constrained Environments. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194289

[4] IoT-Enhanced virtual power plants with edge computing and blockchain security for sustainable smart grid management. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42091922

[5] EdgeGuard-AI: Zero-Trust and Load-Aware Federated Scheduling for Secure and Low-Latency IoT Edge Networks. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/41902157

[6] Topology-aware adaptive scheduling algorithm for heterogeneous AI-PC collaborative computing environments. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225722

[7] Edge-enabled IoT framework for real-time tobacco quality monitoring. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42020563

[8] MMDet-Edge: A Multi-Scale and Multi-Object Detection Framework for Safety-Critical Edge Deployment. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755090

[9] Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/41786996

[10] AI Conflict Observer: Conflict severity and scenario identification for intersection based on Ensemble Transformer. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/41990543

[11] AI-microbial hybrid biosensors: the next generation of intelligent detection systems. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42212947

[12] Dynamic task offloading for sports training monitoring in MEC-assisted smart wearable device systems. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42219406

[13] Construction of a sports bio mechanical injury prediction and AI warning system based on wearable sensors. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42186087

[14] AI-enabled smart surveillance system for secure monitoring and authentication. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42120936

[15] NetworkGuard: An Edge-Based Virtual Network Sensing Architecture for Real-Time Security Monitoring in Smart Home Environments. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41978016

[16] Edge Driven Trust Aware Threat Detection for IoT Enabled Intelligent Transportation Systems. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755056

[17] Edge-AI Enabled Acoustic Monitoring and Spatial Localisation for Sow Oestrus Detection. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829012

[18] Two-Stage Wildlife Event Classification for Edge Deployment. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755305

[19] Bridging CNNs and vision transformers for efficient tea leaf phytopathogen diagnosis: GL-MobFormer. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/42206155

[20] Spectrally optimised YOLOv10s-SeqOpt framework for real-time UAV-based early detection of avocado foliar diseases in indian orchards. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/42135362

[21] An Intelligent Micromachine Perception System for Elevator Fault Diagnosis. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076178

[22] AI-Driven Hybrid Detection and Classification Framework for Secure Sleep Health IoT Networks. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200970

[23] A fuzzy logic and blockchain-enhanced framework for secure, explainable eHealth in Society 5.0. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/42129248

[24] SENSEYE: a resource-aware visionary framework for assisting individuals with visual disabilities. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115269

[25] TinyAct: A framework for real-time action recognition in the cloud through distillation learning. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/42008450

[26] Editorial: Advancing gastrointestinal disease diagnosis with interpretable AI and edge computing for enhanced patient care. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41958550

[27] Blockchain-driven trust management and AI computing for sensor networks optimization. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41844731

[28] Real-Time Vibration Energy Prediction for Semi-Active Suspensions Using Inertial Sensors: A Physics-Guided Deep Learning Approach. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829656

[29] Teleradiology, Edge Computing, and the Internet of Things in Radiology: A RRA Perspective on Decentralized Diagnostics. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41781094

[30] Navigating AI deployment in precision livestock farming: current trends and future prospects. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/42137895


