Based on the provided sources from 2025 and 2026, the latest research progress in industrial robots and autonomous navigation can be categorized into several key areas: advanced perception and sensing, robust path planning and control, bio-inspired and novel actuation mechanisms, and domain-specific applications ranging from industrial automation to healthcare.

### 1. Advanced Perception and Sensing Mechanisms
Recent advancements focus on enhancing the robustness of visual and multi-modal perception in complex environments.

*   **Visual Navigation and Robustness:** Research has moved towards integrating strategic algorithms with visual data. For instance, a strategic gradient-REINFORCE algorithm has been proposed for visual navigation in autonomous driving robots, aiming to improve decision-making stability [7]. To handle adversarial attacks, empirical analyses have been conducted on the robustness of 3D Gaussian Splatting under multi-view inconsistency attacks, highlighting the need for more resilient scene representations [2]. Additionally, transformers with global context awareness (GCA-Trans) are being developed to improve segmentation of transparent objects, which are notoriously difficult for traditional computer vision systems [4].
*   **Multi-Modal Sensor Fusion and Enhancement:** To overcome limitations in single-sensor systems, researchers are fusing thermal, visual, and inertial data. AI-enhanced thermal-visual-inertial odometry allows for autonomous planning in GPS-denied environments, crucial for search-and-rescue operations [10]. In underwater environments, GAN-based image enhancement combined with transfer learning improves scene classification in murky waters [24]. Furthermore, multi-scale self-supervised learning techniques are being applied to cross-modal place recognition between cameras and LiDAR, improving localization accuracy [27].
*   **Bio-inspired Sensing:** Nature continues to inspire new sensor designs. Adaptive tunneling photodiodes enable visual recognition in high-contrast scenes by mimicking biological adaptation mechanisms [5]. Similarly, soft, insect-inspired distributed tactile sensors allow for effective touch perception, enhancing the robot's ability to interact with fragile or unknown objects [26].

### 2. Robust Path Planning and Control Algorithms
The control and planning layers are leveraging artificial intelligence to handle dynamic and unstructured environments.

*   **Deep Reinforcement Learning (DRL):** DRL is widely applied to navigation tasks. A comparative study on autonomous underwater navigation demonstrated that DRL methods can outperform traditional Dynamic Window Approach (DWA) methods, validated through digital twin simulations [19]. In industrial settings, a path planning algorithm for substation robots combines deep reinforcement learning with ant colony optimization to enhance efficiency [41]. For wheeled mobile robots, adaptive fuzzy PID controllers are being used to enhance trajectory tracking accuracy [16].
*   **Semantic and Geometric Reasoning:** Path planning is increasingly informed by semantic understanding. In unstructured agricultural environments, global feasible path planning for pest monitoring robots accounts for crop rows and obstacles [22]. For dense 3D point clouds, entropy-regularized path planning (S3PM) helps autonomous mobile robots navigate cluttered spaces more effectively [50]. Furthermore, geometry-aware multimodal fusion techniques are improving large-scale 3D scene understanding, which is foundational for accurate planning [42].
*   **Simulation and Digital Twins:** The use of digital twins is critical for validation. A digital twin framework was developed for coal mine rescue robots to enhance intelligence and visualization capabilities [6]. Another study utilized a digital twin to validate deep reinforcement learning agents for underwater navigation [19]. Simulation platforms like SimNav-XR, which integrates ROS2 and Unity3D, are also being advanced to facilitate safer testing of mobile robot navigation strategies [32].

### 3. Bio-inspired and Novel Actuation for Navigation
Innovative actuation methods, often inspired by biology, are enabling navigation in previously inaccessible environments.

*   **Insect and Animal Inspiration:** Researchers are observing bee flight strategies in cluttered environments to inspire visually guided autonomous navigation, particularly for micro-drones [1]. Similarly, the active tactile perception inspired by mosquitoes is being applied to rigid-soft coupling blimp robots for indoor navigation and escape [49]. For terrestrial navigation, cyborg beetles are being guided via bust stimulation to achieve sustained locomotion and autonomous navigation [30].
*   **Microrobotics and Soft Robotics:** At the micro-scale, untethered tripodal microrobots achieve omnidirectional motion using radial piezoelectric actuators, useful for targeted delivery or sensing [11]. In larger scales, HydroAir, an air-propelled surface vehicle, is designed for autonomous navigation and 3D reconstruction in shallow, obstacle-rich aquatic environments [3].

### 4. Domain-Specific Applications: Industry and Healthcare
The convergence of AI and robotics is transforming specific industrial and medical sectors.

*   **Industrial and Agricultural Automation:** In agriculture, lightweight detection networks like NRLC-YOLO are used for the grasp positioning of latex cups in rubber plantations [97]. For greenhouse maintenance, structural optimization of roof-cleaning robots improves their operational efficiency [79]. In laboratories, "Chemist Eye," a visual language model, enhances safety monitoring and robot decision-making in self-driving labs [14]. The ADePT framework provides a benchmark for assessing autonomous laboratory robotics, ensuring reliability in chemical discovery [40].
*   **Healthcare and Surgical Robotics:** AI is reshaping surgical precision and care. In spinal surgery, fully motorized C-arms are being integrated for better positioning [13]. AI-driven procedural guidance is improving the accuracy of spinal epidural steroid injections [52]. In oncology, intelligent therapeutic robotic-assisted surgery is emerging as a frontier for precision [53]. Furthermore, AI-assisted vision systems are being developed for blind and vision-impaired individuals, aiding in navigation [87]. However, the integration of AI in nursing and healthcare also raises ethical considerations, with studies emphasizing that while AI can replace tasks, it cannot replace the human element of nursing care, necessitating careful ethical frameworks [72].

### Critical Reflection
While the sources highlight significant technological leaps, critical analysis reveals several challenges. The reliance on AI models, such as those for semantic segmentation [28] or adversarial robustness [2], indicates that current systems remain vulnerable to data distribution shifts and malicious attacks. Furthermore, the shift towards "embodied intelligence" [29] and complex multi-modal fusion [42] increases computational demands, potentially limiting deployment on resource-constrained edge devices. The validation of these systems often relies on digital twins or controlled simulations [6, 19], which may not fully capture the stochastic nature of real-world unstructured environments. Additionally, the rapid integration of AI into healthcare [53, 76] necessitates rigorous legal and ethical scrutiny [67, 100] to ensure patient safety and data privacy, which lags behind technical development.

In conclusion, the latest progress in industrial robotics and autonomous navigation is characterized by a shift from rule-based systems to AI-driven, bio-inspired, and multi-modal intelligent systems. These systems demonstrate improved robustness in perception and planning but face ongoing challenges regarding safety, ethical integration, and real-world generalization.

[1] Bees in clutter: observing flight strategies to inspire visually guided autonomous navigation. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42229505

[2] Empirical analysis of adversarial robustness in 3D Gaussian Splatting under multi-view inconsistency attacks. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225699

[3] HydroAir: An Air-Propelled Surface Vehicle for Autonomous Navigation and 3D Reconstruction in Shallow and Obstacle-Rich Aquatic Environments. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198033

[4] GCA-Trans: Global Context-Aware Transformer for Robust Transparent Object Segmentation in Robotic Environments. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188248

[5] Adaptive tunneling photodiodes enable visual recognition in high-contrast scenes. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42160418

[6] Digital Twin of Coal Mine Rescue Robot-Research on Intelligence and Visualization. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122561

[7] Visual navigation technology for autonomous driving robots based on strategic gradient-REINFORCE algorithm. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42113866

[8] Electronics-free soft robotic minitablet for on-demand gastric molecular sensing and diagnostics in vivo. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42102190

[9] NFL-BA: Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42099776

[10] AI-Enhanced Thermal-Visual-Inertial Odometry and Autonomous Planning for GPS-Denied Search-and- Rescue Robotics. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076571

[11] Omnidirectional motion of an untethered tripodal microrobot using radial piezoelectric actuators. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42069677

[12] Interactive Cognition of Self-driving: A Multidimensional Analysis Model and Implementation. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42058501

[13] [Self-driving, fully motorized C-arm in spinal surgery: a comparative study]. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42053630

[14] Chemist Eye: a visual language model-powered system for safety monitoring and robot decision-making in self-driving laboratories. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42023166

[15] Recent Advances in Artificial Intelligence in Organic Electronic Research. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42007884

[16] Enhanced trajectory tracking for autonomous navigation of wheeled mobile robots using an adaptive fuzzy PID controller. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42000744

[17] Multi-View Images Suffice 3D Reasoning Through Chain-of-Thought Selection and Question-Guided Fusion. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41996434

[18] Band-Engineerable Ferroelectric 2D CuInP(2)S(6) Heterojunctions for Adaptive Visual Contrast. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41982077

[19] Deep Reinforcement Learning for Autonomous Underwater Navigation: A Comparative Study with DWA and Digital Twin Validation. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41977967

[20] MSCNet: Efficient and accurate semantic segmentation of LiDAR data using Multi-scale Convolution. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41945568

[21] Humanizing virtual agents through mutual self-disclosure: enhancing interpersonal engagement and cooperative behavior. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41931979

[22] Global feasible path planning for pest monitoring robots in unstructured agricultural environments. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41929831

[23] Design, framework and benchmark of safety monitors for black-box classifiers. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41927668

[24] GAN-based underwater image enhancement and scene classification using transfer learning. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41894524

[25] Out-of-Sight Embodied Agents: Multimodal Tracking, Sensor Fusion, and Trajectory Forecasting. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41870930

[26] A Soft, Insect-Inspired, Distributed Tactile Sensor Enables Effective Touch Perception. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41849202

[27] MS2-CL: Multi-Scale Self-Supervised Learning for Camera to LiDAR Cross-Modal Place Recognition. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829525

[28] GENet: A Geometry-Enhanced Network for LiDAR Semantic Segmentation. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829421

[29] Embodied Artificial Intelligence in Healthcare: A Systematic Review of Robotic Perception, Decision-Making, and Clinical Impact. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41827523

[30] Bust Stimulation for Sustained Locomotion Control and Autonomous Navigation of Terrestrial Cyborg Beetles. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41808673

[31] Bioinspired multi-compartment mesoporous nanoreactors: modular assembly and functional applications. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41797677

[32] SimNav-XR: an extended reality platform for mobile robot simulation using ROS2 and Unity3D. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41789161

[33] Vision-Controlled autonomous navigation in unstructured environments: Integrating image processing, path planning, and trajectory control in robotic systems. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41785215

[34] Toward Generating Realistic 3D Semantic Training Data for Autonomous Driving. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41770974

[35] RepACNet: A Lightweight Reparameterized Asymmetric Convolution Network for Monocular Depth Estimation. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755140

[36] Survey of Latest Advancements in Deep Learning for Point Cloud Completion. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41747119

[37] SREF: Semantics-Refined Feature Extraction for Long-Term Visual Localization. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41745450

[38] LUMI-lab: A foundation model-driven autonomous platform enabling discovery of ionizable lipid designs for mRNA delivery. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41742414

[39] Autonomous microfluidic labs: progress and prospects. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41732020

[40] The ADePT framework for assessing autonomous laboratory robotics. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41720921

[41] A substation robot path planning algorithm based on deep reinforcement learning enhanced by ant colony optimization. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41716744

[42] Geometry-aware multimodal fusion for large-scale 3D scene understanding. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41715735

[43] PlatROB: An open-source, modular, and low-cost hardware platform for mobile robotics and AI education. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41704540

[44] HBEVOcc: Height-Aware Bird's-Eye-View Representation for 3D Occupancy Prediction from Multi-Camera Images. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682450

[45] Quantifying the Trajectory Tracking Accuracy in UGVs: The Role of Traffic Scheduling in Wi-Fi-Enabled Time-Sensitive Networking. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682396

[46] Research on Motion Trajectory Correction Method for Wall-Climbing Robots Based on External Visual Localization System. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682289

[47] RFGLNet for adverse weather domain-generalized semantic segmentation with frequency low-rank enhancement. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41667736

[48] The role of diagnosticity in judging robot competence. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41651890

[49] Mosquito-inspired active tactile perception for indoor navigation and escape of a rigid-soft coupling blimp robot. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41643317

[50] S3PM: Entropy-Regularized Path Planning for Autonomous Mobile Robots in Dense 3D Point Clouds of Unstructured Environments. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600525

[51] Defining the Era of Shoulder Arthroscopy 2.0: A Perspective on Integrating Precision, Biology, and Smart Technology. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/42246018

[52] Artificial Intelligence for Procedural Guidance of Spinal Epidural Steroid Injections: A Scoping Review. (source nr: 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245875

[53] Intelligent therapeutic robotic-assisted surgery as the next frontier of precision oncology. (source nr: 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245705

[54] High-throughput phenotyping for climate-resilient forests: integrating multi-sensor fusion and root-shoot dynamics. (source nr: 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245104

[55] Artificial intelligence in pediatric pain: a systematic review. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/42243763

[56] A multi-stage, pixel-level annotated apple dataset for precision agriculture research. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/42239800

[57] Artificial intelligence and ChatGPT literacy among surgical healthcare professionals: knowledge, attitudes, and perceived clinical utility. (source nr: 57)
   URL: https://pubmed.ncbi.nlm.nih.gov/42238873

[58] Endoscopic mitral valve repair-one hundred and one ways to use neochords: a narrative review. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/42232264

[59] Surgical strategies for spontaneous pneumothorax: a narrative review. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/42232039

[60] Sensitive and wafer-scale olfactory sensory neurons. (source nr: 60)
   URL: https://pubmed.ncbi.nlm.nih.gov/42230545

[61] Nutritional prehabilitation for robot-assisted radical prostatectomy: A proposed clinical framework integrating body composition analysis. (source nr: 61)
   URL: https://pubmed.ncbi.nlm.nih.gov/42229686

[62] Artificial Intelligence for the Diagnosis of Pancreatic Diseases Using Endoscopic Ultrasonography. (source nr: 62)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227807

[63] Emerging Utility of Artificial Intelligence Driven Medical Robots in Health Care: A Review. (source nr: 63)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227386

[64] Blob representation of robotic surgical scenes for position-aware video generation. (source nr: 64)
   URL: https://pubmed.ncbi.nlm.nih.gov/42223905

[65] Artificial intelligence of the future: reflections on its possible impact on human Nursing care. (source nr: 65)
   URL: https://pubmed.ncbi.nlm.nih.gov/42222653

[66] Editorial: AI and robotics for increasing disaster resilience in modern societies. (source nr: 66)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221226

[67] Medicolegal Implications in Orthopaedic Surgery: The Emerging Challenges of Artificial Intelligence and Robotic Integration. (source nr: 67)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221172

[68] Restoration of Acoustic Identity via Artificial Intelligence-Driven Neural Voice Conversion for Total Laryngectomy Patients: A Technical Framework for Biometric Security and Social Inclusion. (source nr: 68)
   URL: https://pubmed.ncbi.nlm.nih.gov/42220829

[69] [From digitalization to embodied intelligence: technological innovation and paradigm shift in clinical stomatology]. (source nr: 69)
   URL: https://pubmed.ncbi.nlm.nih.gov/42219725

[70] Care ethics and the transformation of care in an age of artificial intelligence. (source nr: 70)
   URL: https://pubmed.ncbi.nlm.nih.gov/42218421

[71] European Science for Health Research Needs and Priorities. (source nr: 71)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217648

[72] Artificial intelligence can replace nursing tasks, but not nurses: Examining artificial intelligence's supports and threats to nursing practice through the lens of the 2025 Nursing Code of Ethics. (source nr: 72)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217292

[73] Technical challenges in autonomous robotic ultrasound examinations: perception, planning, and control. (source nr: 73)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217071

[74] Parents' Perspectives on Artificial Intelligence-Supported Pediatric Healthcare Services: A Descriptive and Correlational Study. (source nr: 74)
   URL: https://pubmed.ncbi.nlm.nih.gov/42216846

[75] A temporal adaptive dictionary-constrained LDA and Bi-calibrated dual granularity DTM framework for dynamic topic evolution analysis in academic papers. (source nr: 75)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215613

[76] VeNet: a lightweight neural network for efficient brain vessel segmentation in endovascular robotic surgery. (source nr: 76)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215575

[77] Please follow the rules: surgical workflow recognition constrained by linear temporal logic. (source nr: 77)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209907

[78] Artificial intelligence in nursing practice for older adults with dementia: A narrative review informed by bibliometric mapping and implications for nurse-led research. (source nr: 78)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209252

[79] Structural analysis and optimization of an autonomous robot designed for greenhouse roof cleaning. (source nr: 79)
   URL: https://pubmed.ncbi.nlm.nih.gov/42204160

[80] [Technology-driven management of early-onset scoliosis:new technologies and concepts]. (source nr: 80)
   URL: https://pubmed.ncbi.nlm.nih.gov/42203647

[81] Neural Wave Propagation for Surgical Video Action Recognition: A New Dataset and Baseline. (source nr: 81)
   URL: https://pubmed.ncbi.nlm.nih.gov/42202188

[82] Application and research progress of single-port laparoscopy in retroperitoneal lymphadenectomy for gynecologic malignancies. (source nr: 82)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200005

[83] Transforming surgical decisions: the rise of predictive and personalized digital tools. (source nr: 83)
   URL: https://pubmed.ncbi.nlm.nih.gov/42199078

[84] Spectral-YOLOv13: A Dual-Domain Vision-Mamba Sensing Framework for Fine-Grained Coral Health Assessment and Continuous Ecological Forecasting. (source nr: 84)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198074

[85] IoT-Cloud-Based Control of a Mechatronic Production Line Assisted by a Dual Cyber-Physical Robotic System Within Digital Twin, AI and Industry/Education 4.0/5.0 Frameworks. (source nr: 85)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198001

[86] Recent Developments and Applications of Drone Swarm: Techniques, Strategies, and Challenges. (source nr: 86)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197752

[87] AI-Assisted Vision Alarming System for Blind and Vision- Impaired People. (source nr: 87)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197739

[88] Deep Learning-Based Tracking of Neurovascular Features Toward Semi-Automated Ultrasound-Guided Peripheral Nerve Blocks by Non-Specialists. (source nr: 88)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194313

[89] Toward Intelligent Rehabilitation Program Management: A System-Level Review of AI Architectures. (source nr: 89)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194296

[90] Leveling Up Upconverting Nanoparticles with Machine Learning. (source nr: 90)
   URL: https://pubmed.ncbi.nlm.nih.gov/42190040

[91] What Do We Know About How Generative AI is Being Used for Patient-Centered Communication? A Scoping Review. (source nr: 91)
   URL: https://pubmed.ncbi.nlm.nih.gov/42186773

[92] Global evolution of robot-assisted cholecystectomy research in the era of artificial intelligence: a bibliometric and knowledge-mapping study. (source nr: 92)
   URL: https://pubmed.ncbi.nlm.nih.gov/42185582

[93] From testbeds to high-stakes work: a review of Human-AI teaming domains and teaming factors. (source nr: 93)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183027

[94] Mechanochemical and machine-intelligent design of programmable materials: From molecular interactions to macroscale functionality. (source nr: 94)
   URL: https://pubmed.ncbi.nlm.nih.gov/42182867

[95] Clinical research advances in thoracic surgery and thoracic oncology in 2025: a panoramic narrative review. (source nr: 95)
   URL: https://pubmed.ncbi.nlm.nih.gov/42182686

[96] Building the next frontier: Artificial intelligence in 3D-printed medicines. (source nr: 96)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179771

[97] NRLC-YOLO for lightweight detection and grasp positioning of latex cups in rubber plantations. (source nr: 97)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179520

[98] Network structure of artificial intelligence anxiety among nursing students and educational implications: A multicenter network analysis. (source nr: 98)
   URL: https://pubmed.ncbi.nlm.nih.gov/42176534

[99] Clin-STAR Corner: Practice Changing Advances at the Interface of Artificial Intelligence/Machine Learning and Geriatrics. (source nr: 99)
   URL: https://pubmed.ncbi.nlm.nih.gov/42176238

[100] Aligning AI-Native 6G Healthcare Systems with EU Ethical and Legal Frameworks. (source nr: 100)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174947




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 工业机器人与自主导航的最新科研进展
2. latest research breakthroughs in industrial robots and autonomous navigation 2025 2026

 #### Iteration 2:
1. How do 2026 foundation models specifically address the real-time safety verification and explainability gaps in industrial robotic manipulation compared to traditional black-box classifiers?

 #### Iteration 3:
1. How do 2026 foundation models specifically address the real-time safety verification and explainability gaps in industrial robotic manipulation compared to traditional black-box classifiers?



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
工业机器人与自主导航的最新科研进展



Searched with 2 questions, found 50 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
工业机器人与自主导航的最新科研进展



Searched with 1 questions, found 50 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
工业机器人与自主导航的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
工业机器人与自主导航的最新科研进展



Based on the provided sources from 2025 and 2026, the latest research progress in industrial robots and autonomous navigation can be categorized into several key areas: advanced perception and sensing, robust path planning and control, bio-inspired and novel actuation mechanisms, and domain-specific applications ranging from industrial automation to healthcare.

### 1. Advanced Perception and Sensing Mechanisms
Recent advancements focus on enhancing the robustness of visual and multi-modal perception in complex environments.

*   **Visual Navigation and Robustness:** Research has moved towards integrating strategic algorithms with visual data. For instance, a strategic gradient-REINFORCE algorithm has been proposed for visual navigation in autonomous driving robots, aiming to improve decision-making stability [7]. To handle adversarial attacks, empirical analyses have been conducted on the robustness of 3D Gaussian Splatting under multi-view inconsistency attacks, highlighting the need for more resilient scene representations [2]. Additionally, transformers with global context awareness (GCA-Trans) are being developed to improve segmentation of transparent objects, which are notoriously difficult for traditional computer vision systems [4].
*   **Multi-Modal Sensor Fusion and Enhancement:** To overcome limitations in single-sensor systems, researchers are fusing thermal, visual, and inertial data. AI-enhanced thermal-visual-inertial odometry allows for autonomous planning in GPS-denied environments, crucial for search-and-rescue operations [10]. In underwater environments, GAN-based image enhancement combined with transfer learning improves scene classification in murky waters [24]. Furthermore, multi-scale self-supervised learning techniques are being applied to cross-modal place recognition between cameras and LiDAR, improving localization accuracy [27].
*   **Bio-inspired Sensing:** Nature continues to inspire new sensor designs. Adaptive tunneling photodiodes enable visual recognition in high-contrast scenes by mimicking biological adaptation mechanisms [5]. Similarly, soft, insect-inspired distributed tactile sensors allow for effective touch perception, enhancing the robot's ability to interact with fragile or unknown objects [26].

### 2. Robust Path Planning and Control Algorithms
The control and planning layers are leveraging artificial intelligence to handle dynamic and unstructured environments.

*   **Deep Reinforcement Learning (DRL):** DRL is widely applied to navigation tasks. A comparative study on autonomous underwater navigation demonstrated that DRL methods can outperform traditional Dynamic Window Approach (DWA) methods, validated through digital twin simulations [19]. In industrial settings, a path planning algorithm for substation robots combines deep reinforcement learning with ant colony optimization to enhance efficiency [41]. For wheeled mobile robots, adaptive fuzzy PID controllers are being used to enhance trajectory tracking accuracy [16].
*   **Semantic and Geometric Reasoning:** Path planning is increasingly informed by semantic understanding. In unstructured agricultural environments, global feasible path planning for pest monitoring robots accounts for crop rows and obstacles [22]. For dense 3D point clouds, entropy-regularized path planning (S3PM) helps autonomous mobile robots navigate cluttered spaces more effectively [50]. Furthermore, geometry-aware multimodal fusion techniques are improving large-scale 3D scene understanding, which is foundational for accurate planning [42].
*   **Simulation and Digital Twins:** The use of digital twins is critical for validation. A digital twin framework was developed for coal mine rescue robots to enhance intelligence and visualization capabilities [6]. Another study utilized a digital twin to validate deep reinforcement learning agents for underwater navigation [19]. Simulation platforms like SimNav-XR, which integrates ROS2 and Unity3D, are also being advanced to facilitate safer testing of mobile robot navigation strategies [32].

### 3. Bio-inspired and Novel Actuation for Navigation
Innovative actuation methods, often inspired by biology, are enabling navigation in previously inaccessible environments.

*   **Insect and Animal Inspiration:** Researchers are observing bee flight strategies in cluttered environments to inspire visually guided autonomous navigation, particularly for micro-drones [1]. Similarly, the active tactile perception inspired by mosquitoes is being applied to rigid-soft coupling blimp robots for indoor navigation and escape [49]. For terrestrial navigation, cyborg beetles are being guided via bust stimulation to achieve sustained locomotion and autonomous navigation [30].
*   **Microrobotics and Soft Robotics:** At the micro-scale, untethered tripodal microrobots achieve omnidirectional motion using radial piezoelectric actuators, useful for targeted delivery or sensing [11]. In larger scales, HydroAir, an air-propelled surface vehicle, is designed for autonomous navigation and 3D reconstruction in shallow, obstacle-rich aquatic environments [3].

### 4. Domain-Specific Applications: Industry and Healthcare
The convergence of AI and robotics is transforming specific industrial and medical sectors.

*   **Industrial and Agricultural Automation:** In agriculture, lightweight detection networks like NRLC-YOLO are used for the grasp positioning of latex cups in rubber plantations [97]. For greenhouse maintenance, structural optimization of roof-cleaning robots improves their operational efficiency [79]. In laboratories, "Chemist Eye," a visual language model, enhances safety monitoring and robot decision-making in self-driving labs [14]. The ADePT framework provides a benchmark for assessing autonomous laboratory robotics, ensuring reliability in chemical discovery [40].
*   **Healthcare and Surgical Robotics:** AI is reshaping surgical precision and care. In spinal surgery, fully motorized C-arms are being integrated for better positioning [13]. AI-driven procedural guidance is improving the accuracy of spinal epidural steroid injections [52]. In oncology, intelligent therapeutic robotic-assisted surgery is emerging as a frontier for precision [53]. Furthermore, AI-assisted vision systems are being developed for blind and vision-impaired individuals, aiding in navigation [87]. However, the integration of AI in nursing and healthcare also raises ethical considerations, with studies emphasizing that while AI can replace tasks, it cannot replace the human element of nursing care, necessitating careful ethical frameworks [72].

### Critical Reflection
While the sources highlight significant technological leaps, critical analysis reveals several challenges. The reliance on AI models, such as those for semantic segmentation [28] or adversarial robustness [2], indicates that current systems remain vulnerable to data distribution shifts and malicious attacks. Furthermore, the shift towards "embodied intelligence" [29] and complex multi-modal fusion [42] increases computational demands, potentially limiting deployment on resource-constrained edge devices. The validation of these systems often relies on digital twins or controlled simulations [6, 19], which may not fully capture the stochastic nature of real-world unstructured environments. Additionally, the rapid integration of AI into healthcare [53, 76] necessitates rigorous legal and ethical scrutiny [67, 100] to ensure patient safety and data privacy, which lags behind technical development.

In conclusion, the latest progress in industrial robotics and autonomous navigation is characterized by a shift from rule-based systems to AI-driven, bio-inspired, and multi-modal intelligent systems. These systems demonstrate improved robustness in perception and planning but face ongoing challenges regarding safety, ethical integration, and real-world generalization.

### SOURCES USED IN THIS SECTION:
[1] Bees in clutter: observing flight strategies to inspire visually guided autonomous navigation. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42229505

[2] Empirical analysis of adversarial robustness in 3D Gaussian Splatting under multi-view inconsistency attacks. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225699

[3] HydroAir: An Air-Propelled Surface Vehicle for Autonomous Navigation and 3D Reconstruction in Shallow and Obstacle-Rich Aquatic Environments. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198033

[4] GCA-Trans: Global Context-Aware Transformer for Robust Transparent Object Segmentation in Robotic Environments. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188248

[5] Adaptive tunneling photodiodes enable visual recognition in high-contrast scenes. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42160418

[6] Digital Twin of Coal Mine Rescue Robot-Research on Intelligence and Visualization. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122561

[7] Visual navigation technology for autonomous driving robots based on strategic gradient-REINFORCE algorithm. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42113866

[8] Electronics-free soft robotic minitablet for on-demand gastric molecular sensing and diagnostics in vivo. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42102190

[9] NFL-BA: Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42099776

[10] AI-Enhanced Thermal-Visual-Inertial Odometry and Autonomous Planning for GPS-Denied Search-and- Rescue Robotics. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076571

[11] Omnidirectional motion of an untethered tripodal microrobot using radial piezoelectric actuators. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42069677

[12] Interactive Cognition of Self-driving: A Multidimensional Analysis Model and Implementation. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42058501

[13] [Self-driving, fully motorized C-arm in spinal surgery: a comparative study]. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42053630

[14] Chemist Eye: a visual language model-powered system for safety monitoring and robot decision-making in self-driving laboratories. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42023166

[15] Recent Advances in Artificial Intelligence in Organic Electronic Research. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42007884

[16] Enhanced trajectory tracking for autonomous navigation of wheeled mobile robots using an adaptive fuzzy PID controller. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42000744

[17] Multi-View Images Suffice 3D Reasoning Through Chain-of-Thought Selection and Question-Guided Fusion. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41996434

[18] Band-Engineerable Ferroelectric 2D CuInP(2)S(6) Heterojunctions for Adaptive Visual Contrast. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41982077

[19] Deep Reinforcement Learning for Autonomous Underwater Navigation: A Comparative Study with DWA and Digital Twin Validation. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41977967

[20] MSCNet: Efficient and accurate semantic segmentation of LiDAR data using Multi-scale Convolution. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41945568

[21] Humanizing virtual agents through mutual self-disclosure: enhancing interpersonal engagement and cooperative behavior. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41931979

[22] Global feasible path planning for pest monitoring robots in unstructured agricultural environments. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41929831

[23] Design, framework and benchmark of safety monitors for black-box classifiers. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41927668

[24] GAN-based underwater image enhancement and scene classification using transfer learning. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41894524

[25] Out-of-Sight Embodied Agents: Multimodal Tracking, Sensor Fusion, and Trajectory Forecasting. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41870930

[26] A Soft, Insect-Inspired, Distributed Tactile Sensor Enables Effective Touch Perception. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41849202

[27] MS2-CL: Multi-Scale Self-Supervised Learning for Camera to LiDAR Cross-Modal Place Recognition. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829525

[28] GENet: A Geometry-Enhanced Network for LiDAR Semantic Segmentation. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829421

[29] Embodied Artificial Intelligence in Healthcare: A Systematic Review of Robotic Perception, Decision-Making, and Clinical Impact. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41827523

[30] Bust Stimulation for Sustained Locomotion Control and Autonomous Navigation of Terrestrial Cyborg Beetles. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41808673

[31] Bioinspired multi-compartment mesoporous nanoreactors: modular assembly and functional applications. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41797677

[32] SimNav-XR: an extended reality platform for mobile robot simulation using ROS2 and Unity3D. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41789161

[33] Vision-Controlled autonomous navigation in unstructured environments: Integrating image processing, path planning, and trajectory control in robotic systems. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41785215

[34] Toward Generating Realistic 3D Semantic Training Data for Autonomous Driving. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41770974

[35] RepACNet: A Lightweight Reparameterized Asymmetric Convolution Network for Monocular Depth Estimation. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755140

[36] Survey of Latest Advancements in Deep Learning for Point Cloud Completion. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41747119

[37] SREF: Semantics-Refined Feature Extraction for Long-Term Visual Localization. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41745450

[38] LUMI-lab: A foundation model-driven autonomous platform enabling discovery of ionizable lipid designs for mRNA delivery. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41742414

[39] Autonomous microfluidic labs: progress and prospects. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41732020

[40] The ADePT framework for assessing autonomous laboratory robotics. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41720921

[41] A substation robot path planning algorithm based on deep reinforcement learning enhanced by ant colony optimization. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41716744

[42] Geometry-aware multimodal fusion for large-scale 3D scene understanding. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41715735

[43] PlatROB: An open-source, modular, and low-cost hardware platform for mobile robotics and AI education. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41704540

[44] HBEVOcc: Height-Aware Bird's-Eye-View Representation for 3D Occupancy Prediction from Multi-Camera Images. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682450

[45] Quantifying the Trajectory Tracking Accuracy in UGVs: The Role of Traffic Scheduling in Wi-Fi-Enabled Time-Sensitive Networking. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682396

[46] Research on Motion Trajectory Correction Method for Wall-Climbing Robots Based on External Visual Localization System. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682289

[47] RFGLNet for adverse weather domain-generalized semantic segmentation with frequency low-rank enhancement. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41667736

[48] The role of diagnosticity in judging robot competence. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41651890

[49] Mosquito-inspired active tactile perception for indoor navigation and escape of a rigid-soft coupling blimp robot. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41643317

[50] S3PM: Entropy-Regularized Path Planning for Autonomous Mobile Robots in Dense 3D Point Clouds of Unstructured Environments. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600525

[51] Defining the Era of Shoulder Arthroscopy 2.0: A Perspective on Integrating Precision, Biology, and Smart Technology. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/42246018

[52] Artificial Intelligence for Procedural Guidance of Spinal Epidural Steroid Injections: A Scoping Review. (source nr: 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245875

[53] Intelligent therapeutic robotic-assisted surgery as the next frontier of precision oncology. (source nr: 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245705

[54] High-throughput phenotyping for climate-resilient forests: integrating multi-sensor fusion and root-shoot dynamics. (source nr: 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245104

[55] Artificial intelligence in pediatric pain: a systematic review. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/42243763

[56] A multi-stage, pixel-level annotated apple dataset for precision agriculture research. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/42239800

[57] Artificial intelligence and ChatGPT literacy among surgical healthcare professionals: knowledge, attitudes, and perceived clinical utility. (source nr: 57)
   URL: https://pubmed.ncbi.nlm.nih.gov/42238873

[58] Endoscopic mitral valve repair-one hundred and one ways to use neochords: a narrative review. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/42232264

[59] Surgical strategies for spontaneous pneumothorax: a narrative review. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/42232039

[60] Sensitive and wafer-scale olfactory sensory neurons. (source nr: 60)
   URL: https://pubmed.ncbi.nlm.nih.gov/42230545

[61] Nutritional prehabilitation for robot-assisted radical prostatectomy: A proposed clinical framework integrating body composition analysis. (source nr: 61)
   URL: https://pubmed.ncbi.nlm.nih.gov/42229686

[62] Artificial Intelligence for the Diagnosis of Pancreatic Diseases Using Endoscopic Ultrasonography. (source nr: 62)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227807

[63] Emerging Utility of Artificial Intelligence Driven Medical Robots in Health Care: A Review. (source nr: 63)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227386

[64] Blob representation of robotic surgical scenes for position-aware video generation. (source nr: 64)
   URL: https://pubmed.ncbi.nlm.nih.gov/42223905

[65] Artificial intelligence of the future: reflections on its possible impact on human Nursing care. (source nr: 65)
   URL: https://pubmed.ncbi.nlm.nih.gov/42222653

[66] Editorial: AI and robotics for increasing disaster resilience in modern societies. (source nr: 66)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221226

[67] Medicolegal Implications in Orthopaedic Surgery: The Emerging Challenges of Artificial Intelligence and Robotic Integration. (source nr: 67)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221172

[68] Restoration of Acoustic Identity via Artificial Intelligence-Driven Neural Voice Conversion for Total Laryngectomy Patients: A Technical Framework for Biometric Security and Social Inclusion. (source nr: 68)
   URL: https://pubmed.ncbi.nlm.nih.gov/42220829

[69] [From digitalization to embodied intelligence: technological innovation and paradigm shift in clinical stomatology]. (source nr: 69)
   URL: https://pubmed.ncbi.nlm.nih.gov/42219725

[70] Care ethics and the transformation of care in an age of artificial intelligence. (source nr: 70)
   URL: https://pubmed.ncbi.nlm.nih.gov/42218421

[71] European Science for Health Research Needs and Priorities. (source nr: 71)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217648

[72] Artificial intelligence can replace nursing tasks, but not nurses: Examining artificial intelligence's supports and threats to nursing practice through the lens of the 2025 Nursing Code of Ethics. (source nr: 72)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217292

[73] Technical challenges in autonomous robotic ultrasound examinations: perception, planning, and control. (source nr: 73)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217071

[74] Parents' Perspectives on Artificial Intelligence-Supported Pediatric Healthcare Services: A Descriptive and Correlational Study. (source nr: 74)
   URL: https://pubmed.ncbi.nlm.nih.gov/42216846

[75] A temporal adaptive dictionary-constrained LDA and Bi-calibrated dual granularity DTM framework for dynamic topic evolution analysis in academic papers. (source nr: 75)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215613

[76] VeNet: a lightweight neural network for efficient brain vessel segmentation in endovascular robotic surgery. (source nr: 76)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215575

[77] Please follow the rules: surgical workflow recognition constrained by linear temporal logic. (source nr: 77)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209907

[78] Artificial intelligence in nursing practice for older adults with dementia: A narrative review informed by bibliometric mapping and implications for nurse-led research. (source nr: 78)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209252

[79] Structural analysis and optimization of an autonomous robot designed for greenhouse roof cleaning. (source nr: 79)
   URL: https://pubmed.ncbi.nlm.nih.gov/42204160

[80] [Technology-driven management of early-onset scoliosis:new technologies and concepts]. (source nr: 80)
   URL: https://pubmed.ncbi.nlm.nih.gov/42203647

[81] Neural Wave Propagation for Surgical Video Action Recognition: A New Dataset and Baseline. (source nr: 81)
   URL: https://pubmed.ncbi.nlm.nih.gov/42202188

[82] Application and research progress of single-port laparoscopy in retroperitoneal lymphadenectomy for gynecologic malignancies. (source nr: 82)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200005

[83] Transforming surgical decisions: the rise of predictive and personalized digital tools. (source nr: 83)
   URL: https://pubmed.ncbi.nlm.nih.gov/42199078

[84] Spectral-YOLOv13: A Dual-Domain Vision-Mamba Sensing Framework for Fine-Grained Coral Health Assessment and Continuous Ecological Forecasting. (source nr: 84)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198074

[85] IoT-Cloud-Based Control of a Mechatronic Production Line Assisted by a Dual Cyber-Physical Robotic System Within Digital Twin, AI and Industry/Education 4.0/5.0 Frameworks. (source nr: 85)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198001

[86] Recent Developments and Applications of Drone Swarm: Techniques, Strategies, and Challenges. (source nr: 86)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197752

[87] AI-Assisted Vision Alarming System for Blind and Vision- Impaired People. (source nr: 87)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197739

[88] Deep Learning-Based Tracking of Neurovascular Features Toward Semi-Automated Ultrasound-Guided Peripheral Nerve Blocks by Non-Specialists. (source nr: 88)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194313

[89] Toward Intelligent Rehabilitation Program Management: A System-Level Review of AI Architectures. (source nr: 89)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194296

[90] Leveling Up Upconverting Nanoparticles with Machine Learning. (source nr: 90)
   URL: https://pubmed.ncbi.nlm.nih.gov/42190040

[91] What Do We Know About How Generative AI is Being Used for Patient-Centered Communication? A Scoping Review. (source nr: 91)
   URL: https://pubmed.ncbi.nlm.nih.gov/42186773

[92] Global evolution of robot-assisted cholecystectomy research in the era of artificial intelligence: a bibliometric and knowledge-mapping study. (source nr: 92)
   URL: https://pubmed.ncbi.nlm.nih.gov/42185582

[93] From testbeds to high-stakes work: a review of Human-AI teaming domains and teaming factors. (source nr: 93)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183027

[94] Mechanochemical and machine-intelligent design of programmable materials: From molecular interactions to macroscale functionality. (source nr: 94)
   URL: https://pubmed.ncbi.nlm.nih.gov/42182867

[95] Clinical research advances in thoracic surgery and thoracic oncology in 2025: a panoramic narrative review. (source nr: 95)
   URL: https://pubmed.ncbi.nlm.nih.gov/42182686

[96] Building the next frontier: Artificial intelligence in 3D-printed medicines. (source nr: 96)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179771

[97] NRLC-YOLO for lightweight detection and grasp positioning of latex cups in rubber plantations. (source nr: 97)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179520

[98] Network structure of artificial intelligence anxiety among nursing students and educational implications: A multicenter network analysis. (source nr: 98)
   URL: https://pubmed.ncbi.nlm.nih.gov/42176534

[99] Clin-STAR Corner: Practice Changing Advances at the Interface of Artificial Intelligence/Machine Learning and Geriatrics. (source nr: 99)
   URL: https://pubmed.ncbi.nlm.nih.gov/42176238

[100] Aligning AI-Native 6G Healthcare Systems with EU Ethical and Legal Frameworks. (source nr: 100)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174947




________________________________________________________________________________

## ALL SOURCES:
[1] Bees in clutter: observing flight strategies to inspire visually guided autonomous navigation. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42229505

[2] Empirical analysis of adversarial robustness in 3D Gaussian Splatting under multi-view inconsistency attacks. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42225699

[3] HydroAir: An Air-Propelled Surface Vehicle for Autonomous Navigation and 3D Reconstruction in Shallow and Obstacle-Rich Aquatic Environments. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198033

[4] GCA-Trans: Global Context-Aware Transformer for Robust Transparent Object Segmentation in Robotic Environments. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188248

[5] Adaptive tunneling photodiodes enable visual recognition in high-contrast scenes. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42160418

[6] Digital Twin of Coal Mine Rescue Robot-Research on Intelligence and Visualization. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122561

[7] Visual navigation technology for autonomous driving robots based on strategic gradient-REINFORCE algorithm. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42113866

[8] Electronics-free soft robotic minitablet for on-demand gastric molecular sensing and diagnostics in vivo. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42102190

[9] NFL-BA: Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42099776

[10] AI-Enhanced Thermal-Visual-Inertial Odometry and Autonomous Planning for GPS-Denied Search-and- Rescue Robotics. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42076571

[11] Omnidirectional motion of an untethered tripodal microrobot using radial piezoelectric actuators. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42069677

[12] Interactive Cognition of Self-driving: A Multidimensional Analysis Model and Implementation. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/42058501

[13] [Self-driving, fully motorized C-arm in spinal surgery: a comparative study]. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/42053630

[14] Chemist Eye: a visual language model-powered system for safety monitoring and robot decision-making in self-driving laboratories. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/42023166

[15] Recent Advances in Artificial Intelligence in Organic Electronic Research. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/42007884

[16] Enhanced trajectory tracking for autonomous navigation of wheeled mobile robots using an adaptive fuzzy PID controller. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/42000744

[17] Multi-View Images Suffice 3D Reasoning Through Chain-of-Thought Selection and Question-Guided Fusion. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41996434

[18] Band-Engineerable Ferroelectric 2D CuInP(2)S(6) Heterojunctions for Adaptive Visual Contrast. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41982077

[19] Deep Reinforcement Learning for Autonomous Underwater Navigation: A Comparative Study with DWA and Digital Twin Validation. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41977967

[20] MSCNet: Efficient and accurate semantic segmentation of LiDAR data using Multi-scale Convolution. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41945568

[21] Humanizing virtual agents through mutual self-disclosure: enhancing interpersonal engagement and cooperative behavior. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41931979

[22] Global feasible path planning for pest monitoring robots in unstructured agricultural environments. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41929831

[23] Design, framework and benchmark of safety monitors for black-box classifiers. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41927668

[24] GAN-based underwater image enhancement and scene classification using transfer learning. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41894524

[25] Out-of-Sight Embodied Agents: Multimodal Tracking, Sensor Fusion, and Trajectory Forecasting. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41870930

[26] A Soft, Insect-Inspired, Distributed Tactile Sensor Enables Effective Touch Perception. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41849202

[27] MS2-CL: Multi-Scale Self-Supervised Learning for Camera to LiDAR Cross-Modal Place Recognition. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829525

[28] GENet: A Geometry-Enhanced Network for LiDAR Semantic Segmentation. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829421

[29] Embodied Artificial Intelligence in Healthcare: A Systematic Review of Robotic Perception, Decision-Making, and Clinical Impact. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41827523

[30] Bust Stimulation for Sustained Locomotion Control and Autonomous Navigation of Terrestrial Cyborg Beetles. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41808673

[31] Bioinspired multi-compartment mesoporous nanoreactors: modular assembly and functional applications. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41797677

[32] SimNav-XR: an extended reality platform for mobile robot simulation using ROS2 and Unity3D. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41789161

[33] Vision-Controlled autonomous navigation in unstructured environments: Integrating image processing, path planning, and trajectory control in robotic systems. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41785215

[34] Toward Generating Realistic 3D Semantic Training Data for Autonomous Driving. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41770974

[35] RepACNet: A Lightweight Reparameterized Asymmetric Convolution Network for Monocular Depth Estimation. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755140

[36] Survey of Latest Advancements in Deep Learning for Point Cloud Completion. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41747119

[37] SREF: Semantics-Refined Feature Extraction for Long-Term Visual Localization. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41745450

[38] LUMI-lab: A foundation model-driven autonomous platform enabling discovery of ionizable lipid designs for mRNA delivery. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41742414

[39] Autonomous microfluidic labs: progress and prospects. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41732020

[40] The ADePT framework for assessing autonomous laboratory robotics. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41720921

[41] A substation robot path planning algorithm based on deep reinforcement learning enhanced by ant colony optimization. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41716744

[42] Geometry-aware multimodal fusion for large-scale 3D scene understanding. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41715735

[43] PlatROB: An open-source, modular, and low-cost hardware platform for mobile robotics and AI education. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41704540

[44] HBEVOcc: Height-Aware Bird's-Eye-View Representation for 3D Occupancy Prediction from Multi-Camera Images. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682450

[45] Quantifying the Trajectory Tracking Accuracy in UGVs: The Role of Traffic Scheduling in Wi-Fi-Enabled Time-Sensitive Networking. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682396

[46] Research on Motion Trajectory Correction Method for Wall-Climbing Robots Based on External Visual Localization System. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682289

[47] RFGLNet for adverse weather domain-generalized semantic segmentation with frequency low-rank enhancement. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41667736

[48] The role of diagnosticity in judging robot competence. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41651890

[49] Mosquito-inspired active tactile perception for indoor navigation and escape of a rigid-soft coupling blimp robot. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41643317

[50] S3PM: Entropy-Regularized Path Planning for Autonomous Mobile Robots in Dense 3D Point Clouds of Unstructured Environments. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600525

[51] Defining the Era of Shoulder Arthroscopy 2.0: A Perspective on Integrating Precision, Biology, and Smart Technology. (source nr: 51)
   URL: https://pubmed.ncbi.nlm.nih.gov/42246018

[52] Artificial Intelligence for Procedural Guidance of Spinal Epidural Steroid Injections: A Scoping Review. (source nr: 52)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245875

[53] Intelligent therapeutic robotic-assisted surgery as the next frontier of precision oncology. (source nr: 53)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245705

[54] High-throughput phenotyping for climate-resilient forests: integrating multi-sensor fusion and root-shoot dynamics. (source nr: 54)
   URL: https://pubmed.ncbi.nlm.nih.gov/42245104

[55] Artificial intelligence in pediatric pain: a systematic review. (source nr: 55)
   URL: https://pubmed.ncbi.nlm.nih.gov/42243763

[56] A multi-stage, pixel-level annotated apple dataset for precision agriculture research. (source nr: 56)
   URL: https://pubmed.ncbi.nlm.nih.gov/42239800

[57] Artificial intelligence and ChatGPT literacy among surgical healthcare professionals: knowledge, attitudes, and perceived clinical utility. (source nr: 57)
   URL: https://pubmed.ncbi.nlm.nih.gov/42238873

[58] Endoscopic mitral valve repair-one hundred and one ways to use neochords: a narrative review. (source nr: 58)
   URL: https://pubmed.ncbi.nlm.nih.gov/42232264

[59] Surgical strategies for spontaneous pneumothorax: a narrative review. (source nr: 59)
   URL: https://pubmed.ncbi.nlm.nih.gov/42232039

[60] Sensitive and wafer-scale olfactory sensory neurons. (source nr: 60)
   URL: https://pubmed.ncbi.nlm.nih.gov/42230545

[61] Nutritional prehabilitation for robot-assisted radical prostatectomy: A proposed clinical framework integrating body composition analysis. (source nr: 61)
   URL: https://pubmed.ncbi.nlm.nih.gov/42229686

[62] Artificial Intelligence for the Diagnosis of Pancreatic Diseases Using Endoscopic Ultrasonography. (source nr: 62)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227807

[63] Emerging Utility of Artificial Intelligence Driven Medical Robots in Health Care: A Review. (source nr: 63)
   URL: https://pubmed.ncbi.nlm.nih.gov/42227386

[64] Blob representation of robotic surgical scenes for position-aware video generation. (source nr: 64)
   URL: https://pubmed.ncbi.nlm.nih.gov/42223905

[65] Artificial intelligence of the future: reflections on its possible impact on human Nursing care. (source nr: 65)
   URL: https://pubmed.ncbi.nlm.nih.gov/42222653

[66] Editorial: AI and robotics for increasing disaster resilience in modern societies. (source nr: 66)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221226

[67] Medicolegal Implications in Orthopaedic Surgery: The Emerging Challenges of Artificial Intelligence and Robotic Integration. (source nr: 67)
   URL: https://pubmed.ncbi.nlm.nih.gov/42221172

[68] Restoration of Acoustic Identity via Artificial Intelligence-Driven Neural Voice Conversion for Total Laryngectomy Patients: A Technical Framework for Biometric Security and Social Inclusion. (source nr: 68)
   URL: https://pubmed.ncbi.nlm.nih.gov/42220829

[69] [From digitalization to embodied intelligence: technological innovation and paradigm shift in clinical stomatology]. (source nr: 69)
   URL: https://pubmed.ncbi.nlm.nih.gov/42219725

[70] Care ethics and the transformation of care in an age of artificial intelligence. (source nr: 70)
   URL: https://pubmed.ncbi.nlm.nih.gov/42218421

[71] European Science for Health Research Needs and Priorities. (source nr: 71)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217648

[72] Artificial intelligence can replace nursing tasks, but not nurses: Examining artificial intelligence's supports and threats to nursing practice through the lens of the 2025 Nursing Code of Ethics. (source nr: 72)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217292

[73] Technical challenges in autonomous robotic ultrasound examinations: perception, planning, and control. (source nr: 73)
   URL: https://pubmed.ncbi.nlm.nih.gov/42217071

[74] Parents' Perspectives on Artificial Intelligence-Supported Pediatric Healthcare Services: A Descriptive and Correlational Study. (source nr: 74)
   URL: https://pubmed.ncbi.nlm.nih.gov/42216846

[75] A temporal adaptive dictionary-constrained LDA and Bi-calibrated dual granularity DTM framework for dynamic topic evolution analysis in academic papers. (source nr: 75)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215613

[76] VeNet: a lightweight neural network for efficient brain vessel segmentation in endovascular robotic surgery. (source nr: 76)
   URL: https://pubmed.ncbi.nlm.nih.gov/42215575

[77] Please follow the rules: surgical workflow recognition constrained by linear temporal logic. (source nr: 77)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209907

[78] Artificial intelligence in nursing practice for older adults with dementia: A narrative review informed by bibliometric mapping and implications for nurse-led research. (source nr: 78)
   URL: https://pubmed.ncbi.nlm.nih.gov/42209252

[79] Structural analysis and optimization of an autonomous robot designed for greenhouse roof cleaning. (source nr: 79)
   URL: https://pubmed.ncbi.nlm.nih.gov/42204160

[80] [Technology-driven management of early-onset scoliosis:new technologies and concepts]. (source nr: 80)
   URL: https://pubmed.ncbi.nlm.nih.gov/42203647

[81] Neural Wave Propagation for Surgical Video Action Recognition: A New Dataset and Baseline. (source nr: 81)
   URL: https://pubmed.ncbi.nlm.nih.gov/42202188

[82] Application and research progress of single-port laparoscopy in retroperitoneal lymphadenectomy for gynecologic malignancies. (source nr: 82)
   URL: https://pubmed.ncbi.nlm.nih.gov/42200005

[83] Transforming surgical decisions: the rise of predictive and personalized digital tools. (source nr: 83)
   URL: https://pubmed.ncbi.nlm.nih.gov/42199078

[84] Spectral-YOLOv13: A Dual-Domain Vision-Mamba Sensing Framework for Fine-Grained Coral Health Assessment and Continuous Ecological Forecasting. (source nr: 84)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198074

[85] IoT-Cloud-Based Control of a Mechatronic Production Line Assisted by a Dual Cyber-Physical Robotic System Within Digital Twin, AI and Industry/Education 4.0/5.0 Frameworks. (source nr: 85)
   URL: https://pubmed.ncbi.nlm.nih.gov/42198001

[86] Recent Developments and Applications of Drone Swarm: Techniques, Strategies, and Challenges. (source nr: 86)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197752

[87] AI-Assisted Vision Alarming System for Blind and Vision- Impaired People. (source nr: 87)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197739

[88] Deep Learning-Based Tracking of Neurovascular Features Toward Semi-Automated Ultrasound-Guided Peripheral Nerve Blocks by Non-Specialists. (source nr: 88)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194313

[89] Toward Intelligent Rehabilitation Program Management: A System-Level Review of AI Architectures. (source nr: 89)
   URL: https://pubmed.ncbi.nlm.nih.gov/42194296

[90] Leveling Up Upconverting Nanoparticles with Machine Learning. (source nr: 90)
   URL: https://pubmed.ncbi.nlm.nih.gov/42190040

[91] What Do We Know About How Generative AI is Being Used for Patient-Centered Communication? A Scoping Review. (source nr: 91)
   URL: https://pubmed.ncbi.nlm.nih.gov/42186773

[92] Global evolution of robot-assisted cholecystectomy research in the era of artificial intelligence: a bibliometric and knowledge-mapping study. (source nr: 92)
   URL: https://pubmed.ncbi.nlm.nih.gov/42185582

[93] From testbeds to high-stakes work: a review of Human-AI teaming domains and teaming factors. (source nr: 93)
   URL: https://pubmed.ncbi.nlm.nih.gov/42183027

[94] Mechanochemical and machine-intelligent design of programmable materials: From molecular interactions to macroscale functionality. (source nr: 94)
   URL: https://pubmed.ncbi.nlm.nih.gov/42182867

[95] Clinical research advances in thoracic surgery and thoracic oncology in 2025: a panoramic narrative review. (source nr: 95)
   URL: https://pubmed.ncbi.nlm.nih.gov/42182686

[96] Building the next frontier: Artificial intelligence in 3D-printed medicines. (source nr: 96)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179771

[97] NRLC-YOLO for lightweight detection and grasp positioning of latex cups in rubber plantations. (source nr: 97)
   URL: https://pubmed.ncbi.nlm.nih.gov/42179520

[98] Network structure of artificial intelligence anxiety among nursing students and educational implications: A multicenter network analysis. (source nr: 98)
   URL: https://pubmed.ncbi.nlm.nih.gov/42176534

[99] Clin-STAR Corner: Practice Changing Advances at the Interface of Artificial Intelligence/Machine Learning and Geriatrics. (source nr: 99)
   URL: https://pubmed.ncbi.nlm.nih.gov/42176238

[100] Aligning AI-Native 6G Healthcare Systems with EU Ethical and Legal Frameworks. (source nr: 100)
   URL: https://pubmed.ncbi.nlm.nih.gov/42174947


