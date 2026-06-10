Based on the provided sources from 2025 and 2026, the latest scientific progress in quality inspection and defect recognition is characterized by a shift from generic object detection models to highly specialized, lightweight, and multimodal architectures. The research highlights significant advancements in handling complex industrial scenarios, such as reflective surfaces, small-scale defects, and real-time monitoring in additive manufacturing.

### 1. Advancements in YOLO-Based Architectures for Industrial Surfaces
The You Only Look Once (YOLO) framework remains the dominant baseline for defect detection, but recent innovations focus on integrating attention mechanisms, multi-scale feature fusion, and lightweight designs to improve efficiency and accuracy.

*   **Attention and Feature Enhancement:** Researchers have integrated coordinate attention and gradient flow optimization to address specific defects. For instance, EP-YOLO integrates coordinate attention with multi-level gradient flow optimization to enhance Printed Circuit Board (PCB) defect detection [1]. Similarly, DAER-YOLO enhances surface defect detection for varistors by incorporating defect-aware and edge-reconstruction modules [6]. For PCB defects, MFE-YOLO utilizes cross-group attention and FIoU loss to improve multi-scale feature representation [32], while MDEB-YOLO employs a lightweight multi-scale attention network specifically for micro-defects on PCBs [31].
*   **Lightweight and Real-Time Models:** To meet the demands of edge computing and real-time inspection, several studies propose optimized lightweight models. FLF-RCNN offers a fine-tuned, lightweight Faster R-CNN for precise industrial inspection [17]. In the context of weld surface defects, an improved lightweight YOLOv11 algorithm was developed [29], and another study enhanced YOLOv7-tiny using an anchor-free algorithm for metal surface defects [36]. For fabric defects, IR-YOLOv7-Tiny provides a robust, lightweight framework [30]. Additionally, SD-GASNet utilizes an efficient dual-domain multi-scale fusion network with self-distillation for surface defect detection [46].
*   **Specialized Applications:** YOLO variants have been adapted for specific industrial needs. GBE-YOLOv8 is proposed for PCB surface defect detection [18], while EFEN-YOLOv8 captures spatial features and uses multi-level weighted attention for general surface defects [48]. In the context of polarizer defects, EME-YOLOv11 is enhanced for real-time detection [38].

### 2. Integration of Transformers and Advanced Deep Learning Models
Beyond CNN-based YOLO architectures, Transformer-based models and hybrid approaches are gaining traction for their ability to capture long-range dependencies and complex semantic information.

*   **Transformer and Vision-Language Models:** The Mamba architecture, known for linear complexity, is being integrated into multi-cognitive PCB defect detection models [10]. SCMEO-DETR provides a lightweight and high-efficiency solution for PCB defects based on RT-DETR [11]. Furthermore, a unified vision-language model was developed for cross-product defect detection in glove manufacturing, highlighting the trend toward semantic understanding [37]. YOLO-LA introduces prototype-based vision-language alignment for silicon wafer defect pattern detection [43].
*   **Hybrid and Segmentation Networks:** For tasks requiring precise boundary delineation, such as casting defect segmentation in aircraft engine blades, SFCF-Net employs spatial-frequency synergistic learning [23]. In the realm of 3D reconstruction for shipbuilding sub-assemblies, deep learning-based methods are being applied to detect defects in complex geometries [41]. For transparent packaging containers, a multi-parameter inspection platform integrates stress, dimensional, and defect detection [49].

### 3. Innovation in Additive Manufacturing (3D Printing) Monitoring
Quality control in Additive Manufacturing (AM) has seen specialized advancements, focusing on process monitoring and defect detection in real-time.

*   **Process Monitoring:** AI is being applied to design, process modeling, and quality optimization in metal AM [13]. For laser-based powder bed fusion of polymers, deep learning is utilized for process monitoring and defect detection [25]. YOLO-AMI enhances online quality monitoring in 3D printing by using composite loss and parameter-free attention [14].
*   **Specific Defect Analysis:** In wire arc additive manufacturing, a visible-infrared dual-modal monitoring system addresses overlap defects [26]. For magnetic material AM, corrections and refinements in deep learning applications for powder spreading processes continue to evolve [5]. Additionally, machine learning approaches based on spatter feature analysis are advancing defect detection in laser welding [16].

### 4. Multimodal Sensing and Non-Destructive Testing (NDT)
The integration of multiple sensor modalities and advanced signal processing techniques is improving detection capabilities in challenging environments.

*   **Dual-Modal and Sensor-Driven Systems:** Intelligent detection in sensor-driven perception systems is moving from pixel understanding to semantic insight [2]. For curved and glossy surfaces, scan path optimization combined with YOLO-based detection improves inspection reliability [3]. In the pharmaceutical sector, machine vision is emerging as a future non-destructive testing tool for 3D-printed drugs, moving beyond traditional spectroscopy [28].
*   **Ultrasonic and Radiographic Inspection:** For gear defect detection, machine vision-based angle-arrayed imaging combined with two-stage deep learning is employed [21]. In industrial radiographic inspection, SFCF-Net was previously mentioned for its spatial-frequency synergy [23]. Furthermore, knowledge-guided synthetic data pipelines and wavelet-initialized attention U-Nets are being used for guided-wave ultrasonic signal denoising [20].

### 5. Dataset Contributions and Industrial Implementation
The availability of high-quality datasets and the analysis of industrial automation implementation are critical for the reproducibility and practical application of these models.

*   **Public Datasets:** Several new datasets have been introduced to support research, including PCB-defect [47], a dataset for electrode coating manufacturing [33], and a public image dataset for water-based coated wood products [45].
*   **Industrial Automation:** Studies analyze the practical implementation of these technologies. For example, a machine vision-based method for coated carbide CNC inserts includes an analysis of its industrial automation implementation [8]. Machine learning-powered vision for robotic inspection in manufacturing is also reviewed, emphasizing the integration of AI into automated systems [34].

### Critical Reflection
While the sources demonstrate significant progress in accuracy and efficiency, several trends require critical consideration. First, the proliferation of "lightweight" models suggests a trade-off between computational efficiency and potential loss in detecting subtle or complex defects, necessitating rigorous validation in noisy industrial environments. Second, the integration of vision-language models and multimodal sensors (e.g., visible-infrared) offers semantic robustness but increases system complexity and cost. Third, the focus on specific industries (PCB, welding, AM) indicates that general-purpose models are often insufficient; domain-specific adaptations are crucial. Finally, the emergence of synthetic data pipelines [20] highlights the ongoing challenge of obtaining sufficient labeled data for rare defect types, suggesting that data generation techniques will remain a key area of research.

[1] EP-YOLO: A Printed Circuit Board Defect Detection Network Integrating Coordinate Attention and Multi-Level Gradient Flow Optimization. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197919

[2] From Pixel Understanding to Semantic Insight: Intelligent Detection in Sensor-Driven Perception Systems. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197889

[3] Scan Path Optimization and YOLO-Based Detection for Defect Inspection of Curved and Glossy Surfaces. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197840

[4] WMC-DFINE: An Improved DFINE Model for Aluminum Profile Surface Defect Detection. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197802

[5] Correction: Chen et al. Deep Learning Applied to Defect Detection in Powder Spreading Process of Magnetic Material Additive Manufacturing. Materials 2022, 15, 5662. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42195817

[6] DAER-YOLO: Defect-Aware and Edge-Reconstruction Enhanced YOLO for Surface Defect Detection of Varistors. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188235

[7] An Automated Vision-Based Inspection System for Metallic Lock Surface Defects Using a Transformer-Enhanced U-Net. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122329

[8] A machine vision based defect detection method for coated carbide CNC inserts and its industrial automation implementation analysis. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115294

[9] AI-powered industrial quality assurance system for fancy yarn using computer vision and 3D visualization. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42045271

[10] A multi-cognitive PCB defect detection model integrating Mamba. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42034824

[11] SCMEO-DETR provides a lightweight and high efficiency solution for PCB defect detection based on RT-DETR. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42014461

[12] MSAdaNet: An Adaptive Multi-Scale Network for Surface Defect Detection of Smartphone Components. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/41977874

[13] Artificial Intelligence in Metal Additive Manufacturing: Applications in Design, Process Modeling, Monitoring, and Quality Optimization. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41976588

[14] YOLO-AMI: enhancing online quality monitoring in 3D printing with composite loss and parameter-free attention. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/41965889

[15] Enhanced Multi-Scale Defect Detection in Steel Surfaces via Innovative Deep Learning Architecture. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41902169

[16] Advancing Defect Detection in Laser Welding: A Machine Learning Approach Based on Spatter Feature Analysis. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41901990

[17] FLF-RCNN: A Fine-Tuned Lightweight Faster RCNN for Precise and Efficient Industrial Quality Inspection. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41901939

[18] A Novel PCB Surface Defect Detection Method Based on the GBE-YOLOv8 Model. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41900225

[19] Weld defect detection based on improved YOLOv8n. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41873587

[20] Application-specific guided-wave ultrasonic signal denoising: Knowledge-guided synthetic data pipeline and wavelet-initialized attention U-Net. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41850095

[21] Machine vision-based angle-arrayed imaging and two-stage deep learning for gear defect detection. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41842039

[22] An Improved YOLOv8 Detection Algorithm Based on Screen Printing Defect Images. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829565

[23] SFCF-Net: Spatial-Frequency Synergistic Learning for Casting Defect Segmentation of Pre-Service Aircraft Engine Blades in Industrial Radiographic Inspection. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829382

[24] SD-IDD: Selective Distillation for Incremental Defect Detection. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829375

[25] Deep Learning for Process Monitoring and Defect Detection of Laser-Based Powder Bed Fusion of Polymers. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829327

[26] Visible-Infrared Dual-Modal Monitoring System for Overlap Defects in Wire Arc Additive Manufacturing. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41828162

[27] Multiscale object detection model based on pyramid vision transformer. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41820604

[28] Beyond spectroscopy: Machine vision as the future of non-destructive testing in 3D-printed pharmaceuticals. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41819388

[29] An improved lightweight YOLOv11 algorithm for weld surface defect detection. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41764248

[30] IR-YOLOv7-Tiny: A Lightweight and Robust Framework for Fabric-Defect Detection. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755036

[31] MDEB-YOLO: A Lightweight Multi-Scale Attention Network for Micro-Defect Detection on Printed Circuit Boards. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41753848

[32] MFE-YOLO: A Multi-Scale Feature Enhanced Network for PCB Defect Detection with Cross-Group Attention and FIoU Loss. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41751677

[33] A Defect Dataset for Electrode Coating Manufacturing. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41690999

[34] Machine Learning-Powered Vision for Robotic Inspection in Manufacturing: A Review. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682304

[35] LESSDD-Net: A Lightweight and Efficient Steel Surface Defect Detection Network Based on Feature Segmentation and Partially Connected Structures. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682269

[36] Design of lightweight metal surface defect detection technology for YOLOv7-tiny using Anchor-Free algorithm. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41680401

[37] A unified vision-language model for cross-product defect detection in glove manufacturing. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41671274

[38] The enhanced EME-YOLOv11 for real-time polarizer defect detection. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41644969

[39] A real-time industrial safety automation using YOLO architectures leveraging diverse chromatic domains. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41639183

[40] Visual security defense for industrial inspection based on computer vision. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41637420

[41] Deep Learning-Based 3D Reconstruction for Defect Detection in Shipbuilding Sub-Assemblies. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600461

[42] PSgANet: Polar Sequence-Guided Attention Network for Edge-Related Defect Classification in Contact Lenses. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600397

[43] YOLO-LA: Prototype-Based Vision-Language Alignment for Silicon Wafer Defect Pattern Detection. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41597851

[44] Corn Kernel Segmentation and Damage Detection Using a Hybrid Watershed-Convex Hull Approach. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41597005

[45] A Public Image Dataset for Surface Defect Detection of Water-Based Coated Wood Products. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41535684

[46] SD-GASNet: Efficient Dual-Domain Multi-Scale Fusion Network with Self-Distillation for Surface Defect Detection. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41516457

[47] PCB-defect: An annotated dataset for surface defect detection in printed circuit boards. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41488494

[48] EFEN-YOLOv8: Surface defect detection network based on spatial feature capture and multi-level weighted attention. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41481612

[49] A Multi-Parameter Inspection Platform for Transparent Packaging Containers: System Design for Stress, Dimensional, and Defect Detection. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41471528

[50] TGDNet: A Multi-Scale Feature Fusion Defect Detection Method for Transparent Industrial Headlight Glass. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41471432




## SEARCH QUESTIONS BY ITERATION


 #### Iteration 1:
1. 质量检测与缺陷识别的最新科研进展
2. 2025-2026年机器视觉与深度学习在工业缺陷检测中的最新科研进展

 #### Iteration 2:
1. How do vision-language models (e.g., YOLO-LA, unified VLMs) compare to traditional single-modal deep learning in handling cross-domain defect generalization and few-shot scenarios in 2026 industrial applications?

 #### Iteration 3:
1. How do unified vision-language models (e.g., YOLO-LA) specifically address the "semantic gap" in zero-shot defect detection for novel, unseen defect categories in 2026 industrial settings, compared to traditional few-shot learning baselines?



## DETAILED FINDINGS


### Iteration 1


### SEARCH QUESTION:
质量检测与缺陷识别的最新科研进展



Searched with 2 questions, found 50 results.

________________________________________________________________________________


### Iteration 2


### SEARCH QUESTION:
质量检测与缺陷识别的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Iteration 3


### SEARCH QUESTION:
质量检测与缺陷识别的最新科研进展



Searched with 1 questions, found 0 results.

________________________________________________________________________________


### Final synthesis


### SEARCH QUESTION:
质量检测与缺陷识别的最新科研进展



Based on the provided sources from 2025 and 2026, the latest scientific progress in quality inspection and defect recognition is characterized by a shift from generic object detection models to highly specialized, lightweight, and multimodal architectures. The research highlights significant advancements in handling complex industrial scenarios, such as reflective surfaces, small-scale defects, and real-time monitoring in additive manufacturing.

### 1. Advancements in YOLO-Based Architectures for Industrial Surfaces
The You Only Look Once (YOLO) framework remains the dominant baseline for defect detection, but recent innovations focus on integrating attention mechanisms, multi-scale feature fusion, and lightweight designs to improve efficiency and accuracy.

*   **Attention and Feature Enhancement:** Researchers have integrated coordinate attention and gradient flow optimization to address specific defects. For instance, EP-YOLO integrates coordinate attention with multi-level gradient flow optimization to enhance Printed Circuit Board (PCB) defect detection [1]. Similarly, DAER-YOLO enhances surface defect detection for varistors by incorporating defect-aware and edge-reconstruction modules [6]. For PCB defects, MFE-YOLO utilizes cross-group attention and FIoU loss to improve multi-scale feature representation [32], while MDEB-YOLO employs a lightweight multi-scale attention network specifically for micro-defects on PCBs [31].
*   **Lightweight and Real-Time Models:** To meet the demands of edge computing and real-time inspection, several studies propose optimized lightweight models. FLF-RCNN offers a fine-tuned, lightweight Faster R-CNN for precise industrial inspection [17]. In the context of weld surface defects, an improved lightweight YOLOv11 algorithm was developed [29], and another study enhanced YOLOv7-tiny using an anchor-free algorithm for metal surface defects [36]. For fabric defects, IR-YOLOv7-Tiny provides a robust, lightweight framework [30]. Additionally, SD-GASNet utilizes an efficient dual-domain multi-scale fusion network with self-distillation for surface defect detection [46].
*   **Specialized Applications:** YOLO variants have been adapted for specific industrial needs. GBE-YOLOv8 is proposed for PCB surface defect detection [18], while EFEN-YOLOv8 captures spatial features and uses multi-level weighted attention for general surface defects [48]. In the context of polarizer defects, EME-YOLOv11 is enhanced for real-time detection [38].

### 2. Integration of Transformers and Advanced Deep Learning Models
Beyond CNN-based YOLO architectures, Transformer-based models and hybrid approaches are gaining traction for their ability to capture long-range dependencies and complex semantic information.

*   **Transformer and Vision-Language Models:** The Mamba architecture, known for linear complexity, is being integrated into multi-cognitive PCB defect detection models [10]. SCMEO-DETR provides a lightweight and high-efficiency solution for PCB defects based on RT-DETR [11]. Furthermore, a unified vision-language model was developed for cross-product defect detection in glove manufacturing, highlighting the trend toward semantic understanding [37]. YOLO-LA introduces prototype-based vision-language alignment for silicon wafer defect pattern detection [43].
*   **Hybrid and Segmentation Networks:** For tasks requiring precise boundary delineation, such as casting defect segmentation in aircraft engine blades, SFCF-Net employs spatial-frequency synergistic learning [23]. In the realm of 3D reconstruction for shipbuilding sub-assemblies, deep learning-based methods are being applied to detect defects in complex geometries [41]. For transparent packaging containers, a multi-parameter inspection platform integrates stress, dimensional, and defect detection [49].

### 3. Innovation in Additive Manufacturing (3D Printing) Monitoring
Quality control in Additive Manufacturing (AM) has seen specialized advancements, focusing on process monitoring and defect detection in real-time.

*   **Process Monitoring:** AI is being applied to design, process modeling, and quality optimization in metal AM [13]. For laser-based powder bed fusion of polymers, deep learning is utilized for process monitoring and defect detection [25]. YOLO-AMI enhances online quality monitoring in 3D printing by using composite loss and parameter-free attention [14].
*   **Specific Defect Analysis:** In wire arc additive manufacturing, a visible-infrared dual-modal monitoring system addresses overlap defects [26]. For magnetic material AM, corrections and refinements in deep learning applications for powder spreading processes continue to evolve [5]. Additionally, machine learning approaches based on spatter feature analysis are advancing defect detection in laser welding [16].

### 4. Multimodal Sensing and Non-Destructive Testing (NDT)
The integration of multiple sensor modalities and advanced signal processing techniques is improving detection capabilities in challenging environments.

*   **Dual-Modal and Sensor-Driven Systems:** Intelligent detection in sensor-driven perception systems is moving from pixel understanding to semantic insight [2]. For curved and glossy surfaces, scan path optimization combined with YOLO-based detection improves inspection reliability [3]. In the pharmaceutical sector, machine vision is emerging as a future non-destructive testing tool for 3D-printed drugs, moving beyond traditional spectroscopy [28].
*   **Ultrasonic and Radiographic Inspection:** For gear defect detection, machine vision-based angle-arrayed imaging combined with two-stage deep learning is employed [21]. In industrial radiographic inspection, SFCF-Net was previously mentioned for its spatial-frequency synergy [23]. Furthermore, knowledge-guided synthetic data pipelines and wavelet-initialized attention U-Nets are being used for guided-wave ultrasonic signal denoising [20].

### 5. Dataset Contributions and Industrial Implementation
The availability of high-quality datasets and the analysis of industrial automation implementation are critical for the reproducibility and practical application of these models.

*   **Public Datasets:** Several new datasets have been introduced to support research, including PCB-defect [47], a dataset for electrode coating manufacturing [33], and a public image dataset for water-based coated wood products [45].
*   **Industrial Automation:** Studies analyze the practical implementation of these technologies. For example, a machine vision-based method for coated carbide CNC inserts includes an analysis of its industrial automation implementation [8]. Machine learning-powered vision for robotic inspection in manufacturing is also reviewed, emphasizing the integration of AI into automated systems [34].

### Critical Reflection
While the sources demonstrate significant progress in accuracy and efficiency, several trends require critical consideration. First, the proliferation of "lightweight" models suggests a trade-off between computational efficiency and potential loss in detecting subtle or complex defects, necessitating rigorous validation in noisy industrial environments. Second, the integration of vision-language models and multimodal sensors (e.g., visible-infrared) offers semantic robustness but increases system complexity and cost. Third, the focus on specific industries (PCB, welding, AM) indicates that general-purpose models are often insufficient; domain-specific adaptations are crucial. Finally, the emergence of synthetic data pipelines [20] highlights the ongoing challenge of obtaining sufficient labeled data for rare defect types, suggesting that data generation techniques will remain a key area of research.

### SOURCES USED IN THIS SECTION:
[1] EP-YOLO: A Printed Circuit Board Defect Detection Network Integrating Coordinate Attention and Multi-Level Gradient Flow Optimization. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197919

[2] From Pixel Understanding to Semantic Insight: Intelligent Detection in Sensor-Driven Perception Systems. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197889

[3] Scan Path Optimization and YOLO-Based Detection for Defect Inspection of Curved and Glossy Surfaces. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197840

[4] WMC-DFINE: An Improved DFINE Model for Aluminum Profile Surface Defect Detection. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197802

[5] Correction: Chen et al. Deep Learning Applied to Defect Detection in Powder Spreading Process of Magnetic Material Additive Manufacturing. Materials 2022, 15, 5662. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42195817

[6] DAER-YOLO: Defect-Aware and Edge-Reconstruction Enhanced YOLO for Surface Defect Detection of Varistors. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188235

[7] An Automated Vision-Based Inspection System for Metallic Lock Surface Defects Using a Transformer-Enhanced U-Net. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122329

[8] A machine vision based defect detection method for coated carbide CNC inserts and its industrial automation implementation analysis. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115294

[9] AI-powered industrial quality assurance system for fancy yarn using computer vision and 3D visualization. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42045271

[10] A multi-cognitive PCB defect detection model integrating Mamba. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42034824

[11] SCMEO-DETR provides a lightweight and high efficiency solution for PCB defect detection based on RT-DETR. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42014461

[12] MSAdaNet: An Adaptive Multi-Scale Network for Surface Defect Detection of Smartphone Components. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/41977874

[13] Artificial Intelligence in Metal Additive Manufacturing: Applications in Design, Process Modeling, Monitoring, and Quality Optimization. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41976588

[14] YOLO-AMI: enhancing online quality monitoring in 3D printing with composite loss and parameter-free attention. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/41965889

[15] Enhanced Multi-Scale Defect Detection in Steel Surfaces via Innovative Deep Learning Architecture. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41902169

[16] Advancing Defect Detection in Laser Welding: A Machine Learning Approach Based on Spatter Feature Analysis. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41901990

[17] FLF-RCNN: A Fine-Tuned Lightweight Faster RCNN for Precise and Efficient Industrial Quality Inspection. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41901939

[18] A Novel PCB Surface Defect Detection Method Based on the GBE-YOLOv8 Model. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41900225

[19] Weld defect detection based on improved YOLOv8n. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41873587

[20] Application-specific guided-wave ultrasonic signal denoising: Knowledge-guided synthetic data pipeline and wavelet-initialized attention U-Net. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41850095

[21] Machine vision-based angle-arrayed imaging and two-stage deep learning for gear defect detection. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41842039

[22] An Improved YOLOv8 Detection Algorithm Based on Screen Printing Defect Images. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829565

[23] SFCF-Net: Spatial-Frequency Synergistic Learning for Casting Defect Segmentation of Pre-Service Aircraft Engine Blades in Industrial Radiographic Inspection. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829382

[24] SD-IDD: Selective Distillation for Incremental Defect Detection. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829375

[25] Deep Learning for Process Monitoring and Defect Detection of Laser-Based Powder Bed Fusion of Polymers. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829327

[26] Visible-Infrared Dual-Modal Monitoring System for Overlap Defects in Wire Arc Additive Manufacturing. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41828162

[27] Multiscale object detection model based on pyramid vision transformer. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41820604

[28] Beyond spectroscopy: Machine vision as the future of non-destructive testing in 3D-printed pharmaceuticals. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41819388

[29] An improved lightweight YOLOv11 algorithm for weld surface defect detection. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41764248

[30] IR-YOLOv7-Tiny: A Lightweight and Robust Framework for Fabric-Defect Detection. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755036

[31] MDEB-YOLO: A Lightweight Multi-Scale Attention Network for Micro-Defect Detection on Printed Circuit Boards. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41753848

[32] MFE-YOLO: A Multi-Scale Feature Enhanced Network for PCB Defect Detection with Cross-Group Attention and FIoU Loss. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41751677

[33] A Defect Dataset for Electrode Coating Manufacturing. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41690999

[34] Machine Learning-Powered Vision for Robotic Inspection in Manufacturing: A Review. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682304

[35] LESSDD-Net: A Lightweight and Efficient Steel Surface Defect Detection Network Based on Feature Segmentation and Partially Connected Structures. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682269

[36] Design of lightweight metal surface defect detection technology for YOLOv7-tiny using Anchor-Free algorithm. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41680401

[37] A unified vision-language model for cross-product defect detection in glove manufacturing. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41671274

[38] The enhanced EME-YOLOv11 for real-time polarizer defect detection. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41644969

[39] A real-time industrial safety automation using YOLO architectures leveraging diverse chromatic domains. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41639183

[40] Visual security defense for industrial inspection based on computer vision. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41637420

[41] Deep Learning-Based 3D Reconstruction for Defect Detection in Shipbuilding Sub-Assemblies. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600461

[42] PSgANet: Polar Sequence-Guided Attention Network for Edge-Related Defect Classification in Contact Lenses. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600397

[43] YOLO-LA: Prototype-Based Vision-Language Alignment for Silicon Wafer Defect Pattern Detection. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41597851

[44] Corn Kernel Segmentation and Damage Detection Using a Hybrid Watershed-Convex Hull Approach. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41597005

[45] A Public Image Dataset for Surface Defect Detection of Water-Based Coated Wood Products. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41535684

[46] SD-GASNet: Efficient Dual-Domain Multi-Scale Fusion Network with Self-Distillation for Surface Defect Detection. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41516457

[47] PCB-defect: An annotated dataset for surface defect detection in printed circuit boards. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41488494

[48] EFEN-YOLOv8: Surface defect detection network based on spatial feature capture and multi-level weighted attention. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41481612

[49] A Multi-Parameter Inspection Platform for Transparent Packaging Containers: System Design for Stress, Dimensional, and Defect Detection. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41471528

[50] TGDNet: A Multi-Scale Feature Fusion Defect Detection Method for Transparent Industrial Headlight Glass. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41471432




________________________________________________________________________________

## ALL SOURCES:
[1] EP-YOLO: A Printed Circuit Board Defect Detection Network Integrating Coordinate Attention and Multi-Level Gradient Flow Optimization. (source nr: 1)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197919

[2] From Pixel Understanding to Semantic Insight: Intelligent Detection in Sensor-Driven Perception Systems. (source nr: 2)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197889

[3] Scan Path Optimization and YOLO-Based Detection for Defect Inspection of Curved and Glossy Surfaces. (source nr: 3)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197840

[4] WMC-DFINE: An Improved DFINE Model for Aluminum Profile Surface Defect Detection. (source nr: 4)
   URL: https://pubmed.ncbi.nlm.nih.gov/42197802

[5] Correction: Chen et al. Deep Learning Applied to Defect Detection in Powder Spreading Process of Magnetic Material Additive Manufacturing. Materials 2022, 15, 5662. (source nr: 5)
   URL: https://pubmed.ncbi.nlm.nih.gov/42195817

[6] DAER-YOLO: Defect-Aware and Edge-Reconstruction Enhanced YOLO for Surface Defect Detection of Varistors. (source nr: 6)
   URL: https://pubmed.ncbi.nlm.nih.gov/42188235

[7] An Automated Vision-Based Inspection System for Metallic Lock Surface Defects Using a Transformer-Enhanced U-Net. (source nr: 7)
   URL: https://pubmed.ncbi.nlm.nih.gov/42122329

[8] A machine vision based defect detection method for coated carbide CNC inserts and its industrial automation implementation analysis. (source nr: 8)
   URL: https://pubmed.ncbi.nlm.nih.gov/42115294

[9] AI-powered industrial quality assurance system for fancy yarn using computer vision and 3D visualization. (source nr: 9)
   URL: https://pubmed.ncbi.nlm.nih.gov/42045271

[10] A multi-cognitive PCB defect detection model integrating Mamba. (source nr: 10)
   URL: https://pubmed.ncbi.nlm.nih.gov/42034824

[11] SCMEO-DETR provides a lightweight and high efficiency solution for PCB defect detection based on RT-DETR. (source nr: 11)
   URL: https://pubmed.ncbi.nlm.nih.gov/42014461

[12] MSAdaNet: An Adaptive Multi-Scale Network for Surface Defect Detection of Smartphone Components. (source nr: 12)
   URL: https://pubmed.ncbi.nlm.nih.gov/41977874

[13] Artificial Intelligence in Metal Additive Manufacturing: Applications in Design, Process Modeling, Monitoring, and Quality Optimization. (source nr: 13)
   URL: https://pubmed.ncbi.nlm.nih.gov/41976588

[14] YOLO-AMI: enhancing online quality monitoring in 3D printing with composite loss and parameter-free attention. (source nr: 14)
   URL: https://pubmed.ncbi.nlm.nih.gov/41965889

[15] Enhanced Multi-Scale Defect Detection in Steel Surfaces via Innovative Deep Learning Architecture. (source nr: 15)
   URL: https://pubmed.ncbi.nlm.nih.gov/41902169

[16] Advancing Defect Detection in Laser Welding: A Machine Learning Approach Based on Spatter Feature Analysis. (source nr: 16)
   URL: https://pubmed.ncbi.nlm.nih.gov/41901990

[17] FLF-RCNN: A Fine-Tuned Lightweight Faster RCNN for Precise and Efficient Industrial Quality Inspection. (source nr: 17)
   URL: https://pubmed.ncbi.nlm.nih.gov/41901939

[18] A Novel PCB Surface Defect Detection Method Based on the GBE-YOLOv8 Model. (source nr: 18)
   URL: https://pubmed.ncbi.nlm.nih.gov/41900225

[19] Weld defect detection based on improved YOLOv8n. (source nr: 19)
   URL: https://pubmed.ncbi.nlm.nih.gov/41873587

[20] Application-specific guided-wave ultrasonic signal denoising: Knowledge-guided synthetic data pipeline and wavelet-initialized attention U-Net. (source nr: 20)
   URL: https://pubmed.ncbi.nlm.nih.gov/41850095

[21] Machine vision-based angle-arrayed imaging and two-stage deep learning for gear defect detection. (source nr: 21)
   URL: https://pubmed.ncbi.nlm.nih.gov/41842039

[22] An Improved YOLOv8 Detection Algorithm Based on Screen Printing Defect Images. (source nr: 22)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829565

[23] SFCF-Net: Spatial-Frequency Synergistic Learning for Casting Defect Segmentation of Pre-Service Aircraft Engine Blades in Industrial Radiographic Inspection. (source nr: 23)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829382

[24] SD-IDD: Selective Distillation for Incremental Defect Detection. (source nr: 24)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829375

[25] Deep Learning for Process Monitoring and Defect Detection of Laser-Based Powder Bed Fusion of Polymers. (source nr: 25)
   URL: https://pubmed.ncbi.nlm.nih.gov/41829327

[26] Visible-Infrared Dual-Modal Monitoring System for Overlap Defects in Wire Arc Additive Manufacturing. (source nr: 26)
   URL: https://pubmed.ncbi.nlm.nih.gov/41828162

[27] Multiscale object detection model based on pyramid vision transformer. (source nr: 27)
   URL: https://pubmed.ncbi.nlm.nih.gov/41820604

[28] Beyond spectroscopy: Machine vision as the future of non-destructive testing in 3D-printed pharmaceuticals. (source nr: 28)
   URL: https://pubmed.ncbi.nlm.nih.gov/41819388

[29] An improved lightweight YOLOv11 algorithm for weld surface defect detection. (source nr: 29)
   URL: https://pubmed.ncbi.nlm.nih.gov/41764248

[30] IR-YOLOv7-Tiny: A Lightweight and Robust Framework for Fabric-Defect Detection. (source nr: 30)
   URL: https://pubmed.ncbi.nlm.nih.gov/41755036

[31] MDEB-YOLO: A Lightweight Multi-Scale Attention Network for Micro-Defect Detection on Printed Circuit Boards. (source nr: 31)
   URL: https://pubmed.ncbi.nlm.nih.gov/41753848

[32] MFE-YOLO: A Multi-Scale Feature Enhanced Network for PCB Defect Detection with Cross-Group Attention and FIoU Loss. (source nr: 32)
   URL: https://pubmed.ncbi.nlm.nih.gov/41751677

[33] A Defect Dataset for Electrode Coating Manufacturing. (source nr: 33)
   URL: https://pubmed.ncbi.nlm.nih.gov/41690999

[34] Machine Learning-Powered Vision for Robotic Inspection in Manufacturing: A Review. (source nr: 34)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682304

[35] LESSDD-Net: A Lightweight and Efficient Steel Surface Defect Detection Network Based on Feature Segmentation and Partially Connected Structures. (source nr: 35)
   URL: https://pubmed.ncbi.nlm.nih.gov/41682269

[36] Design of lightweight metal surface defect detection technology for YOLOv7-tiny using Anchor-Free algorithm. (source nr: 36)
   URL: https://pubmed.ncbi.nlm.nih.gov/41680401

[37] A unified vision-language model for cross-product defect detection in glove manufacturing. (source nr: 37)
   URL: https://pubmed.ncbi.nlm.nih.gov/41671274

[38] The enhanced EME-YOLOv11 for real-time polarizer defect detection. (source nr: 38)
   URL: https://pubmed.ncbi.nlm.nih.gov/41644969

[39] A real-time industrial safety automation using YOLO architectures leveraging diverse chromatic domains. (source nr: 39)
   URL: https://pubmed.ncbi.nlm.nih.gov/41639183

[40] Visual security defense for industrial inspection based on computer vision. (source nr: 40)
   URL: https://pubmed.ncbi.nlm.nih.gov/41637420

[41] Deep Learning-Based 3D Reconstruction for Defect Detection in Shipbuilding Sub-Assemblies. (source nr: 41)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600461

[42] PSgANet: Polar Sequence-Guided Attention Network for Edge-Related Defect Classification in Contact Lenses. (source nr: 42)
   URL: https://pubmed.ncbi.nlm.nih.gov/41600397

[43] YOLO-LA: Prototype-Based Vision-Language Alignment for Silicon Wafer Defect Pattern Detection. (source nr: 43)
   URL: https://pubmed.ncbi.nlm.nih.gov/41597851

[44] Corn Kernel Segmentation and Damage Detection Using a Hybrid Watershed-Convex Hull Approach. (source nr: 44)
   URL: https://pubmed.ncbi.nlm.nih.gov/41597005

[45] A Public Image Dataset for Surface Defect Detection of Water-Based Coated Wood Products. (source nr: 45)
   URL: https://pubmed.ncbi.nlm.nih.gov/41535684

[46] SD-GASNet: Efficient Dual-Domain Multi-Scale Fusion Network with Self-Distillation for Surface Defect Detection. (source nr: 46)
   URL: https://pubmed.ncbi.nlm.nih.gov/41516457

[47] PCB-defect: An annotated dataset for surface defect detection in printed circuit boards. (source nr: 47)
   URL: https://pubmed.ncbi.nlm.nih.gov/41488494

[48] EFEN-YOLOv8: Surface defect detection network based on spatial feature capture and multi-level weighted attention. (source nr: 48)
   URL: https://pubmed.ncbi.nlm.nih.gov/41481612

[49] A Multi-Parameter Inspection Platform for Transparent Packaging Containers: System Design for Stress, Dimensional, and Defect Detection. (source nr: 49)
   URL: https://pubmed.ncbi.nlm.nih.gov/41471528

[50] TGDNet: A Multi-Scale Feature Fusion Defect Detection Method for Transparent Industrial Headlight Glass. (source nr: 50)
   URL: https://pubmed.ncbi.nlm.nih.gov/41471432


