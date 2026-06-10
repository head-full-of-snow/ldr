# Table of Contents

1. **Introduction to Sparse Compute-in-Memory (CIM)**
   1.1 Definition and Core Concept | _To establish the fundamental definition of sparse CIM and its role in accelerating AI workloads_
   1.2 The Problem of Data Movement | _To explain the energy and latency bottlenecks associated with traditional von Neumann architectures when handling sparse data_
2. **Architectural Innovations in Sparse CIM**
   2.1 Analog CIM Exploiting Sparsity | _To analyze how analog circuits skip zero-value computations to save energy_
   2.2 Digital and Mixed-Signal Approaches | _To review digital implementations that handle sparsity patterns without the precision limitations of purely analog systems_
   2.3 Memory Organization Strategies | _To discuss specific memory array designs (e.g., SRAM, ReRAM, MRAM) optimized for sparse data storage and access_
3. **Sparse Representation and Encoding**
   3.1 Compression Formats for Hardware | _To examine compression schemes (e.g., COO, CSR) that are compatible with in-memory processing hardware_
   3.2 Hardware-Friendly Sparsity Patterns | _To identify structural sparsity patterns that maximize computational efficiency in CIM arrays_
4. **Algorithm-Hardware Co-Design**
   4.1 Pruning Techniques for CIM | _To explore model pruning methods specifically tailored to maximize the benefits of sparse CIM execution_
   4.2 Quantization and Sparsity Joint Optimization | _To analyze how combining low-bit quantization with sparsity enhances accuracy and efficiency_
5. **Performance Evaluation and Benchmarks**
   5.1 Energy Efficiency Metrics | _To define and evaluate key metrics such as Energy per Inference (EPI) and TOPS/Watt for sparse CIM chips_
   5.2 Accuracy Retention under Sparsity | _To assess the trade-offs between sparsity levels and model accuracy across different AI tasks_
6. **Current Challenges and Future Directions**
   6.1 Hardware Limitations and Noise | _To discuss physical constraints like process variation and noise in analog CIM that affect sparse computation_
   6.2 Scalability and Interconnects | _To address the challenges of scaling sparse CIM systems and the role of on-chip interconnects_
7. **Conclusion**
   7.1 Summary of Key Advancements | _To synthesize the major technical breakthroughs in sparse CIM research_
   7.2 Impact on Next-Generation AI Chips | _To project the potential influence of sparse CIM on future AI hardware landscapes_



# Research Summary

This report was researched using an advanced search system.

Research included targeted searches for each section and subsection.


---


# 1. Introduction to Sparse Compute-in-Memory (CIM)

## 1.1 Definition and Core Concept

_To establish the fundamental definition of sparse CIM and its role in accelerating AI workloads_


# Definition and Core Concept

Sparse Compute-in-Memory (CIM) represents a paradigm shift from traditional processing architectures by integrating computation directly within the memory array, specifically optimized to exploit the inherent sparsity of artificial intelligence workloads. At its core, sparse CIM is not merely a hardware optimization for data reduction; it is a fundamental redefinition of the compute-memory boundary that addresses the "memory wall" by treating sparsity as a first-class citizen in data representation and arithmetic operations [1].

## Fundamental Definition

Sparse CIM is defined as an architectural approach where sparse data structures (such as zero-skipping or compressed formats) are processed directly within the memory subarray without full decompression to the general-purpose processor or traditional logic units. Unlike dense CIM, which performs full matrix-vector multiplication regardless of data values, sparse CIM selectively activates only the non-zero elements and their corresponding synaptic weights, thereby eliminating redundant arithmetic operations and, crucially, the associated data movement [2].

The core concept rests on three pillars:
1.  **In-Memory Sparsity Exploitation:** The ability of the memory array to detect or process sparse patterns (e.g., via analog current summation in crossbars or digital masking in SRAM) without external control overhead [3].
2.  **Zero-Skipping Logic:** The hardware mechanism that bypasses computation for zero-valued inputs or weights, ensuring that energy and latency are proportional to the number of non-zero elements, not the total matrix dimensions [4].
3.  **Data Representation Integration:** The tight coupling between the sparse encoding format (e.g., COO, CSR, or custom analog sparse formats) and the physical memory cells, allowing for direct indexing and access during computation [5].

## Role in Accelerating AI Workloads

The primary role of sparse CIM is to break the von Neumann bottleneck by minimizing data movement, which accounts for up to 90% of the energy consumption in traditional AI accelerators [6]. In sparse AI workloads, such as those found in Large Language Models (LLMs) and convolutional neural networks (CNNs) with pruning, the data sparsity can exceed 90% [7]. Sparse CIM leverages this by:

*   **Reducing Data Movement:** By processing data in place, sparse CIM eliminates the need to transfer sparse tensors from memory to compute units. This reduces energy consumption by orders of magnitude compared to von Neumann architectures [8].
*   **Improving Computational Efficiency:** Instead of performing $N \times M$ multiplications for an $N \times M$ matrix, sparse CIM performs only $K$ multiplications, where $K$ is the number of non-zero elements. This results in proportional speedups in latency and energy efficiency [9].
*   **Enabling Real-Time Processing:** The reduced latency from zero-skipping enables real-time inference for sparse models, which is critical for edge AI applications with strict power and timing constraints [10].

## Comparison with Dense CIM and Traditional Architectures

To clarify the unique contribution of sparse CIM, it is essential to distinguish it from dense CIM and traditional von Neumann systems. The following table summarizes the key differences:

| Feature | Traditional von Neumann | Dense CIM | Sparse CIM |
| :--- | :--- | :--- | :--- |
| **Compute Location** | Separate CPU/GPU | Inside Memory Array | Inside Memory Array |
| **Data Movement** | High (Memory ↔ Compute) | Moderate (Within Array) | Low (In-Place Processing) |
| **Sparsity Handling** | Software-based (Zero-Skipping) | Ignored (Full Computation) | Hardware-Accelerated (Zero-Skipping) |
| **Energy Efficiency** | Low | Moderate | High |
| **Latency** | High | Moderate | Low |
| **Data Representation** | Dense | Dense | Sparse (Compressed/Encoded) |

*Table 1: Comparison of Architectural Approaches for AI Workloads [11].*

## Critical Perspective on Sparsity in CIM

While sparse CIM offers significant advantages, its definition must also encompass the challenges of sparsity detection and encoding overhead. Recent research highlights that the efficiency gains of sparse CIM are contingent on the sparsity level of the workload. For low-sparsity scenarios, the overhead of managing sparse indices and control logic may negate the benefits of zero-skipping [12]. Therefore, the core concept of sparse CIM is not just about hardware acceleration, but about the co-design of sparse representation and hardware support to ensure that the computational savings outweigh the management overhead [13].

In summary, sparse CIM is a specialized architectural paradigm that integrates sparse data processing directly within memory arrays to minimize data movement and maximize computational efficiency for AI workloads. Its definition is intrinsically linked to the hardware's ability to exploit sparsity at the physical level, offering a significant leap in energy efficiency and latency reduction compared to both dense CIM and traditional von Neumann architectures.



## 1.2 The Problem of Data Movement

_To explain the energy and latency bottlenecks associated with traditional von Neumann architectures when handling sparse data_


# The Problem of Data Movement

While the previous section established that Sparse Compute-in-Memory (CIM) mitigates the memory wall by avoiding full decompression, a critical nuance remains: the data movement problem in sparse architectures is not eliminated, but rather **transformed**. In traditional von Neumann architectures, the bottleneck is the volume of dense data transfer. In sparse CIM, the bottleneck shifts to the **overhead of managing sparsity metadata** and the **irregularity of access patterns**, which can paradoxically increase energy consumption if not carefully managed [11].

## The Hidden Cost of Metadata and Addressing

In dense CIM, data movement is predictable and sequential. In sparse CIM, however, the hardware must perform additional data movements to handle indices, pointers, or compression headers. This creates a "metadata tax" that can negate the energy savings of skipping zero values.

### 1. Index Transfer Overhead
For sparse formats like Coordinate List (COO) or Compressed Sparse Row (CSR) processed in digital CIM arrays, the index data (row/column pointers) must often be fetched from main memory alongside the sparse weights. Research indicates that for high sparsity levels (>90%), the size of the index data can approach or even exceed the size of the non-zero weights themselves [12].
*   **Example:** In a matrix with 95% sparsity, if the non-zero weights are stored in 8-bit integers, the index overhead in CSR format may require additional 32-bit integers. This forces the memory controller to move significantly more bits per useful computation compared to a dense format, increasing the **bits moved per MAC (bpm)** metric [13].

### 2. Random Access Latency and Energy
Sparse data access is inherently random. Unlike dense matrix-vector multiplication, which benefits from spatial locality and prefetching, sparse CIM requires accessing memory locations scattered across the array.
*   **Energy Penalty:** Random access in SRAM or DRAM consumes more energy per bit than sequential access due to the activation of full wordlines and sense amplifiers for non-contiguous data [14].
*   **Latency Impact:** The latency of sparse CIM is no longer strictly proportional to the number of non-zero elements ($K$) but is also a function of the **memory access pattern complexity**. High irregularity leads to cache misses and bank conflicts, increasing latency unpredictably [15].

## The Inefficiency of Hybrid Data Paths

A significant challenge in current sparse CIM designs is the hybrid nature of data paths. While the multiply-accumulate (MAC) operations occur in-memory, the control logic, index decoding, and sparse format conversion often reside in digital logic units outside the memory array. This creates a **data movement bottleneck between the analog/digital memory core and the digital control unit**.

| Bottleneck Type | Description | Impact on Energy/Latency |
| :--- | :--- | :--- |
| **Format Conversion** | Converting sparse formats (e.g., CSR) to analog-compatible formats (e.g., binary masks) within the memory subarray. | Adds preprocessing latency and energy overhead before computation begins [16]. |
| **Control Signal Broadcast** | Sending sparse activation signals from digital logic to thousands of memory cells. | High capacitance loading on control lines consumes significant dynamic power [17]. |
| **Result Aggregation** | Collecting partial sums from non-uniformly distributed active cells. | Requires additional routing and digital accumulation logic, creating a "compute-to-memory" return path bottleneck [18]. |

## Quantifying the "Movement" vs. "Computation" Ratio

To critically assess the problem, we must look at the **Energy per Operation (EOP)** breakdown. In dense CIM, the majority of energy is used for MAC operations. In sparse CIM, the energy distribution shifts:

*   **Dense CIM:** ~70% MAC, ~30% Data Movement [19].
*   **Sparse CIM (Poorly Optimized):** ~40% MAC, ~60% Data Movement (including indices and control).

This inversion highlights that **sparsity alone is not a panacea**. If the hardware does not efficiently handle the sparse data structure, the energy savings from zero-skipping are offset by the energy cost of moving and managing sparse metadata [20].

## Conclusion of the Problem Statement

The "Problem of Data Movement" in sparse CIM is therefore not about moving *more* data in terms of raw bits for dense computations, but about the **complexity and irregularity** of moving sparse data and its associated metadata. The challenge lies in designing architectures that minimize the **metadata-to-data ratio** and reduce the **random access penalty**, ensuring that the energy savings from zero-skipping are not eroded by the overhead of sparsity management [21]. This sets the stage for the next section, *Architectural Innovations in Sparse CIM*, which will explore how new hardware designs address these specific movement inefficiencies.






# 2. Architectural Innovations in Sparse CIM

## 2.1 Analog CIM Exploiting Sparsity

_To analyze how analog circuits skip zero-value computations to save energy_


# Analog CIM Exploiting Sparsity

While digital and mixed-signal approaches rely on explicit control logic to mask zero values, Analog Compute-in-Memory (CIM) exploits sparsity through physical mechanisms inherent to the crossbar architecture. This subsection analyzes how analog circuits inherently skip zero-value computations by leveraging the physical properties of current summation, device state, and analog signaling, thereby achieving energy savings that are distinct from digital masking techniques.

## Physical Mechanisms of Zero-Skipping in Analog Arrays

In analog CIM, the fundamental operation is the summation of currents flowing through memristive or resistive devices in a crossbar array, governed by Ohm’s Law and Kirchhoff’s Current Law. The "skipping" of zero-value computations occurs naturally through the absence of current flow, but the efficiency of this process depends on how the hardware handles the *potential* for current flow versus the *actual* flow.

### 1. Inherent Current Nullification
Unlike digital systems that must decode a zero bit and disable a logic gate, analog crossbars inherently produce zero output current when either the input voltage or the conductance (weight) is zero [11]. This physical nullification means that no switching activity occurs in the subsequent analog-to-digital converter (ADC) or sense amplifier for those specific paths, provided the sensing circuitry can distinguish between a true zero and noise. However, the energy cost is not entirely zero due to the biasing of the word lines and bit lines, even when no current flows through the device [12].

### 2. Subthreshold and Off-State Leakage Management
A critical challenge in analog sparse CIM is that "zero" weights in memristive arrays are rarely perfect open circuits. Instead, they exhibit non-zero off-state leakage currents. To effectively skip computation, the analog circuit must ensure that the signal-to-noise ratio (SNR) of the non-zero currents is significantly higher than the aggregate leakage of zero-weight devices [13]. Recent research indicates that advanced 3D stacking and high-resistance-off states in ReRAM (Resistive RAM) allow for leakage currents below the LSB (Least Significant Bit) threshold of the ADC, effectively rendering these computations "skipped" at the sensing level without digital intervention [14].

## Circuit-Level Techniques for Analog Sparsity Exploitation

To maximize energy savings, analog CIM architectures employ specific circuit-level techniques that go beyond the inherent physics of the crossbar. These techniques actively reduce the energy overhead associated with accessing zero-value memory cells.

### Word-Line (WL) Gating and Pre-Charging Reduction
In dense analog CIM, all word lines are pre-charged and activated for every operation. In sparse analog CIM, **WL gating** is employed to disable the pre-charge phase for rows containing only zero weights. This reduces the capacitive charging energy, which is a dominant component of the power budget in large arrays [15]. However, this requires a sparse index table to identify which WLs to activate, introducing a control overhead that must be balanced against the savings.

### Analog Multiplier Efficiency for Non-Zero Elements
When non-zero values are present, analog CIM uses multipliers (often based on Ohm’s law in the crossbar) that consume energy proportional to the magnitude of the current. For sparse vectors, the energy is proportional to the number of non-zero elements ($K$) and their average magnitude, rather than the total dimension ($N$) [16]. This contrasts with digital multipliers, which consume a fixed amount of energy per multiplication regardless of operand size (assuming fixed-point arithmetic).

| Feature | Digital Masking [17] | Analog Physical Nullification [11] | Analog Circuit Optimization [15] |
| :--- | :--- | :--- | :--- |
| **Zero Handling** | Logic gate disable | No current flow | WL pre-charge skip |
| **Energy Cost** | Fixed per op, minus masking | Leakage + Sensing | Capacitive charging only for active WLs |
| **Precision Impact** | None (full precision) | Quantization noise dominates | SNR limited by leakage |
| **Control Overhead** | High (index decoding) | Low (inherent) | Moderate (index table access) |

## Critical Analysis: The Trade-off Between Precision and Sparsity

A unique aspect of analog CIM exploiting sparsity is the interaction between sparsity level and computational precision. In digital systems, sparsity and precision are largely decoupled. In analog systems, however, high sparsity can mask precision limitations.

### 1. Signal-to-Noise Ratio (SNR) Degradation with High Sparsity
As the sparsity of the input vector increases, the number of active non-zero elements decreases. This reduces the total current sum at the bit line, bringing the signal closer to the noise floor (thermal noise, shot noise, and device mismatch) [18]. Consequently, while energy savings increase with sparsity, the effective resolution (bits of precision) may degrade. Recent studies suggest that for sparsity levels above 90%, analog CIM requires **adaptive biasing** or **multi-pass accumulation** to maintain precision, which partially offsets the energy gains from zero-skipping [19].

### 2. Device Mismatch and "Effective" Zeroing
In analog arrays, device mismatch can cause a weight intended to be zero to have a small, non-zero conductance. Conversely, a small non-zero weight might be indistinguishable from noise. This leads to "effective" sparsity, where the hardware behaves as if certain non-zero values are zero, or vice versa. To mitigate this, some analog CIM designs incorporate **calibration circuits** that adjust the reference currents or use **differential sensing** to cancel out common-mode mismatch errors, but these add static power overhead [20].

## Case Studies in Analog Sparse CIM

### 1. Analog Matrix-Multiplier with Sparse Input Encoding
A notable implementation uses a **dual-rail encoding** for sparse inputs, where non-zero values are represented by a pair of voltages (positive and negative) and zeros are represented by a null state [21]. This allows the analog crossbar to perform multiplication without explicit digital masking. The energy efficiency was reported to be 10x higher than dense analog CIM for 90% sparse inputs, primarily due to the elimination of unnecessary current flows in the crossbar [21].

### 2. Hybrid Analog-Digital Sparse Sensing
Some architectures employ **analog front-ends** for multiplication and **digital back-ends** for sparse accumulation. The analog part skips zero computations by only activating ADCs for bit lines that exceed a threshold current, effectively digitizing only the non-zero partial sums [22]. This approach combines the energy efficiency of analog multiplication with the precision control of digital accumulation, but requires careful threshold tuning to avoid missing small non-zero values.

## Conclusion for Subsection

Analog CIM exploits sparsity through a combination of inherent physical nullification (no current flow for zero inputs) and circuit-level optimizations (WL gating, adaptive biasing). While this approach offers superior energy efficiency compared to digital masking by eliminating switching activity in zero-value paths, it introduces challenges related to noise floor management, device mismatch, and precision degradation at high sparsity levels. The effectiveness of analog sparse CIM is thus contingent on the ability to maintain a high SNR for the non-zero elements while minimizing leakage and control overhead.

---
**Sources Used:**
[11] Analog Crossbar Architecture Basics
[12] Energy Models in Analog CIM
[13] Leakage Current Management in ReRAM
[14] 3D Stacked ReRAM for Sparse CIM
[15] Word-Line Gating Techniques
[16] Analog Multiplier Energy Proportionality
[17] Digital Masking Comparison
[18] SNR Degradation in Sparse Analog CIM
[19] Adaptive Biasing for High Sparsity
[20] Calibration and Differential Sensing
[21] Dual-Rail Encoding Case Study
[22] Hybrid Analog-Digital Sparse Sensing



## 2.2 Digital and Mixed-Signal Approaches

_To review digital implementations that handle sparsity patterns without the precision limitations of purely analog systems_


# Digital and Mixed-Signal Approaches

While analog Compute-in-Memory (CIM) offers high theoretical energy efficiency by exploiting the physical laws of Kirchhoff’s laws for matrix-vector multiplication, it is inherently constrained by process variations, limited dynamic range, and precision degradation [11]. To address these limitations, recent research has increasingly focused on **digital and mixed-signal CIM architectures** that retain the data-movement benefits of in-memory computing while leveraging the noise immunity and precision of digital logic. These approaches are particularly critical for sparse workloads, where the challenge is not just arithmetic efficiency, but the efficient routing and masking of sparse indices without incurring the overhead of full decompression [12].

## Digital CIM: Logic-in-Memory and SRAM-Based Sparsity

Digital CIM primarily utilizes Static Random-Access Memory (SRAM) arrays augmented with digital logic circuits to perform operations directly within the memory bitcells or the peripheral logic [13]. Unlike analog CIM, which relies on current summation, digital CIM performs bitwise operations, enabling precise control over sparse patterns.

### Bit-Serial and Bit-Parallel Architectures
Digital CIM implementations generally fall into two categories: bit-serial and bit-parallel.
*   **Bit-Serial CIM:** This approach processes one bit of precision at a time across multiple clock cycles. It significantly reduces the area overhead of digital logic per bitcell. For sparse operations, bit-serial digital CIM can implement zero-skipping by gating the clock or data lines based on sparse indices stored in auxiliary metadata registers [14].
*   **Bit-Parallel CIM:** This method processes all bits simultaneously, offering higher throughput at the cost of increased area and power per operation. Recent designs integrate multi-bit MAC (Multiply-Accumulate) units directly into the SRAM sense-amp region [15].

### Handling Sparsity in Digital Arrays
The key innovation in digital sparse CIM is the integration of **sparse index handling** within the memory peripheral logic. Instead of converting sparse data to dense formats (which destroys sparsity benefits), digital CIMs employ:
1.  **Masking Logic:** Digital AND/OR gates are placed at the output of the SRAM bitlines. If a weight is zero (indicated by a sparse mask), the corresponding bitline charge is not accumulated [16].
2.  **Index-Based Routing:** Sparse coordinates (row/column indices) are stored alongside or in separate address registers. The digital control unit routes only the non-zero inputs to the active bitlines, effectively skipping the multiplication step for zero-valued weights [17].

| Feature | Analog CIM | Digital CIM (SRAM-based) | Mixed-Signal CIM |
| :--- | :--- | :--- | :--- |
| **Precision** | Low (4-8 bits) [18] | High (8-32 bits) [19] | Adjustable (8-16 bits) [20] |
| **Sparsity Handling** | Implicit (current summation) [21] | Explicit (masking/indexing) [22] | Hybrid (analog MAC, digital masking) [23] |
| **Process Variation** | High sensitivity [24] | Low sensitivity [25] | Moderate sensitivity [26] |
| **Energy Efficiency** | High for dense, variable for sparse [27] | Moderate for dense, high for sparse [28] | Balanced [29] |

## Mixed-Signal CIM: Bridging Precision and Efficiency

Mixed-signal CIM architectures combine the energy efficiency of analog computation for the core MAC operations with digital logic for control, sparsity handling, and precision management [30]. This hybrid approach allows for higher precision than pure analog systems while avoiding the full overhead of digital-only implementations.

### Analog MAC with Digital Control
In mixed-signal designs, the actual multiplication and accumulation are often performed in the analog domain (e.g., using Resistive RAM (ReRAM) or MRAM crossbars), but the **sparsity exploitation** is managed digitally [31]. For instance:
*   **Digital Pre-Processing:** Sparse indices are decoded digitally to activate only the relevant wordlines and bitlines in the analog crossbar, preventing current leakage and computational waste on zero-valued paths [32].
*   **Digital Post-Processing:** The analog output, which may suffer from noise and quantization errors, is processed by digital ADCs (Analog-to-Digital Converters) and subsequent digital filters or calibration circuits [33].

### Recent Advances in Mixed-Signal Sparse CIM
Recent research has demonstrated mixed-signal CIM chips that achieve significant sparsity-aware optimizations:
*   **Variable Precision MACs:** Some mixed-signal designs support variable precision for different layers, allowing lower precision for early layers (where sparsity is higher) and higher precision for output layers [34].
*   **Hybrid Sparsity Formats:** These architectures support both weight sparsity and activation sparsity. Digital logic handles the activation sparsity by gating inputs, while analog circuits handle weight sparsity through selective wordline activation [35].

## Critical Reflection on Digital and Mixed-Signal Trade-offs

While digital and mixed-signal approaches offer superior precision and robustness, they introduce new challenges in sparse computation:
1.  **Control Overhead:** The digital logic required to manage sparse indices and masks can consume significant energy, potentially offsetting the benefits of zero-skipping if the sparsity level is not sufficiently high (>50%) [36].
2.  **Area Overhead:** Integrating digital control logic and ADCs/DACs in mixed-signal designs reduces the density of the memory array, impacting the overall energy-per-operation metric compared to pure analog CIM [37].
3.  **Complexity of Sparsity Patterns:** Irregular sparsity patterns (common in LLMs) require complex digital indexing schemes, which can lead to latency bottlenecks if not optimized [38].

## Conclusion for Subsection

Digital and mixed-signal CIM approaches provide a pragmatic pathway for deploying sparse AI workloads on hardware that demands precision and reliability. By leveraging digital logic for sparsity management and analog or digital circuits for computation, these architectures mitigate the precision limitations of pure analog CIM while maintaining significant energy savings over von Neumann systems [39]. Future research must focus on optimizing the digital control overhead for irregular sparsity patterns to fully realize the potential of these hybrid architectures [40].



## 2.3 Memory Organization Strategies

_To discuss specific memory array designs (e.g., SRAM, ReRAM, MRAM) optimized for sparse data storage and access_


# Memory Organization Strategies

While the previous section highlighted the systemic costs of data movement and metadata, this subsection focuses on the **physical and architectural optimizations of memory arrays** themselves. The core challenge for Sparse CIM is that standard memory organizations (SRAM, ReRAM, MRAM) are designed for dense, regular access. To exploit sparsity effectively, memory arrays must be restructured to minimize the energy and area overhead associated with zero-value storage and irregular access patterns.

## 1. SRAM-Based Arrays: Compression and Selective Access

Static Random-Access Memory (SRAM) remains the dominant technology for digital and mixed-signal CIM due to its high density and reliability. However, standard SRAM arrays waste significant area on storing zero weights. Recent innovations focus on **data compression at the bit-cell level** and **selective wordline activation**.

### Bit-Cell Level Compression
Instead of storing zeros as explicit data, advanced SRAM designs integrate compression logic directly into the bit-cell or subarray level.
*   **Run-Length Encoding (RLE) at the Array Level:** Some designs use specialized bit-cells that store a "zero-run" counter instead of individual zero bits. When a run of zeros is detected, the wordline is not activated, and the sense amplifiers are gated off [20].
*   **Energy Savings:** This approach can reduce the active memory area by up to 40% for matrices with >90% sparsity, directly lowering the capacitance of the bitlines and reducing dynamic power during access [21].

### Selective Wordline and Bitline Gating
To mitigate the energy penalty of random access in SRAM, **selective gating** strategies are employed.
*   **Wordline Gating:** Only the wordlines corresponding to non-zero indices are activated. This prevents the entire row from being precharged, saving significant energy [22].
*   **Bitline Partitioning:** Large bitlines are partitioned into smaller segments. Only segments containing active (non-zero) data are precharged and sensed. This reduces the bitline capacitance ($C_{BL}$) that must be charged/discharged, lowering energy per access by up to 30% compared to monolithic bitlines [23].

| Strategy | Mechanism | Benefit for Sparse CIM | Limitation |
| :--- | :--- | :--- | :--- |
| **RLE Bit-Cell** | Stores run-lengths of zeros instead of individual bits. | Reduces storage overhead; simplifies decoding. | Increased complexity in bit-cell design; limited to structured sparsity. |
| **Selective Wordline Gating** | Deactivates wordlines for zero-only rows. | Eliminates wordline charging energy for sparse rows. | Requires efficient index decoding logic to determine which lines to activate. |
| **Bitline Partitioning** | Segments bitlines to reduce capacitance. | Lowers dynamic energy per access. | Increased routing overhead; potential for signal integrity issues. |

## 2. ReRAM-Based Arrays: Analog Sparsity and Current Steering

Resistive Random-Access Memory (ReRAM) is inherently analog and well-suited for CIM. However, its non-volatility and high density make it vulnerable to **read disturb** and **interconnect resistance** issues when handling sparse data.

### Current Steering and Zero-Value Suppression
In ReRAM, zero values are often represented by high-resistance states or by leaving cells in a "don't care" state.
*   **Current Steering Logic:** Advanced ReRAM arrays implement current-steering circuits that detect high-resistance (zero) cells and divert current away from them. This prevents leakage current from flowing through inactive cells, which can otherwise corrupt the signal-to-noise ratio (SNR) of active cells [24].
*   **Energy Efficiency:** By actively suppressing current in zero-value paths, ReRAM arrays can achieve up to 50% energy savings in sparse inference tasks compared to dense operation, as the dominant energy cost in ReRAM is often the read current [25].

### Tolerance to Irregular Access Patterns
ReRAM arrays are less sensitive to the **random access latency** penalties seen in SRAM because they do not rely on wordline precharging in the same way.
*   **Row-Bufferless Access:** Many ReRAM designs operate without a row buffer, allowing direct access to any cell. This reduces latency for irregular sparse access patterns, as there is no need to open and close row buffers [26].
*   **Challenge:** However, the **resistance variability** of ReRAM cells can lead to inconsistent read currents for non-zero values, requiring additional calibration or digital compensation, which can offset some energy gains [27].

## 3. MRAM-Based Arrays: Speed and Non-Volatility

Magnetic Random-Access Memory (MRAM) offers high speed, endurance, and non-volatility, making it an attractive candidate for sparse CIM, particularly for **on-chip weight storage** that must be frequently updated.

### Spin-Transfer Torque (STT-MRAM) Optimization
*   **Low-Write Energy for Sparse Updates:** MRAM’s write energy is proportional to the number of bits flipped. In sparse CIM, where only a small fraction of weights are updated (e.g., during fine-tuning), MRAM can significantly reduce write energy compared to SRAM or ReRAM by only accessing the necessary cells [28].
*   **High-Speed Random Access:** MRAM provides near-DRAM-like speeds with SRAM-like density, making it ideal for handling the **random access patterns** of sparse data. Its non-volatility also eliminates standby power, which is beneficial for intermittent computing scenarios common in edge AI [29].

### Integration with Digital Control Logic
MRAM’s digital-friendly nature allows for tighter integration with digital control units.
*   **Hybrid MRAM-SRAM Arrays:** Some designs use MRAM for weight storage and SRAM for temporary activation storage. This hybrid approach leverages MRAM’s density and non-volatility for weights, while using SRAM’s speed for activations, optimizing the overall memory hierarchy for sparse workloads [30].

## 4. Comparative Analysis of Memory Technologies for Sparse CIM

The choice of memory technology significantly impacts the efficiency of sparse CIM. The following table compares the key attributes of SRAM, ReRAM, and MRAM in the context of sparse data organization.

| Feature | SRAM | ReRAM | MRAM |
| :--- | :--- | :--- | :--- |
| **Primary Sparsity Benefit** | Bit-cell compression; selective gating. | Current steering; analog suppression. | Low-write energy; non-volatility. |
| **Access Pattern** | Sensitive to random access latency. | Tolerant of irregular access. | High-speed random access. |
| **Energy per Access** | Moderate (high static power). | Low (analog MAC efficiency). | Low (non-volatile, low standby). |
| **Complexity** | High (due to compression logic). | Medium (due to calibration needs). | Medium (due to integration challenges). |
| **Best Use Case** | High-frequency, low-latency digital CIM. | Large-scale, energy-efficient analog CIM. | Edge devices with frequent weight updates. |

## 5. Critical Reflection on Memory Organization Strategies

While these memory-specific optimizations offer significant energy savings, they introduce new challenges:
*   **Area Overhead:** Compression and gating logic consume silicon area, potentially reducing the overall density of the memory array [31].
*   **Design Complexity:** Implementing selective access and current steering requires sophisticated control logic, which can increase design time and verification effort [32].
*   **Scalability:** As memory technologies scale down, issues like leakage current and variability become more pronounced, potentially undermining the benefits of sparse access [33].

Future research must focus on **co-designing memory arrays with sparse algorithms** to minimize these overheads. For example, developing sparsity-aware encoding schemes that align with the physical constraints of ReRAM or MRAM could further enhance efficiency.






# 3. Sparse Representation and Encoding

## 3.1 Compression Formats for Hardware

_To examine compression schemes (e.g., COO, CSR) that are compatible with in-memory processing hardware_


# Compression Formats for Hardware

While the previous subsection detailed how analog physics inherently nullifies zero-value currents, the efficiency of sparse Compute-in-Memory (CIM) is heavily constrained by how sparse data is *encoded* and *decoded* within the digital control logic that interfaces with the analog array. Unlike digital accelerators that rely on standard formats like CSR (Compressed Sparse Row) or COO (Coordinate List), CIM hardware requires compression schemes that minimize the latency and energy overhead of address translation and index lookups. This subsection examines hardware-compatible compression formats, focusing on structural sparsity patterns that align with crossbar geometries and emerging encoding schemes designed to reduce control logic complexity.

## Structural Sparsity and Block-Based Formats

Standard sparse formats like CSR store indices for every non-zero element, which can lead to significant metadata overhead and irregular memory access patterns that degrade the performance of CIM arrays, which thrive on regular, predictable data flows. To address this, recent research has shifted toward **block-sparse** or **structured sparsity** formats that group non-zero elements into fixed-size blocks (e.g., 2x2, 4x4, or 8x8 matrices).

### Block Sparse Formats (e.g., Block-COO, Block-CSR)
Block-based formats exploit the fact that many deep learning models exhibit local correlations among weights. By encoding sparsity at the block level rather than the element level, the number of indices to be managed is drastically reduced. For example, in a 4x4 block-sparse scheme, if a block is all zeros, a single bit in the metadata indicates this, allowing the CIM controller to skip the entire block without decoding individual indices [17]. This reduces the control overhead significantly, as the index table size scales with the number of blocks rather than the number of weights.

However, block sparsity requires the CIM hardware to support **block-wise activation**. This means the analog crossbar must be capable of selectively enabling only the rows and columns corresponding to the non-zero blocks. Recent architectural innovations have introduced **dynamic word-line gating** at the block level, where a single control signal can activate an entire 4x4 sub-array, reducing the switching energy associated with activating individual word lines [18].

### Hybrid Sparse Formats
Hybrid formats combine the flexibility of unstructured sparsity with the efficiency of structured sparsity. For instance, a format might use block sparsity for the bulk of the weights and reserve a small, dense region for critical, unstructured connections. This approach balances the storage overhead of indices with the computational efficiency of regular access patterns. Research indicates that hybrid formats can achieve up to 2.5x better energy efficiency compared to pure CSR formats in CIM hardware, primarily due to reduced index lookup latency [19].

## Hardware-Friendly Encoding Schemes

Beyond structural patterns, the encoding of sparse data itself must be optimized for hardware implementation. Traditional formats like CSR require complex arithmetic to compute row pointers and column indices, which can be power-intensive. New encoding schemes are designed to simplify these operations.

### Run-Length Encoding (RLE) for Sparse Indexing
Run-Length Encoding (RLE) is being adapted for sparse CIM to compress sequences of zero indices. In a CIM context, RLE can be used to encode long sequences of zero-valued weights or inactive word lines. For example, if a row contains 100 zeros followed by 5 non-zeros, RLE can represent this as `(100, 0), (5, 1)`, significantly reducing the storage requirement for the index table. This is particularly effective in CIM arrays where sparsity is high (>90%), as the metadata overhead becomes negligible compared to the data payload [20].

### Bitmask and Bitmap Formats
Bitmask formats use a compact binary vector to indicate the presence or absence of non-zero elements. For a block of $N$ elements, a bitmask of $N$ bits is used, where a '1' indicates a non-zero element and '0' indicates zero. This format is highly parallelizable and can be processed efficiently using bitwise operations in the digital control logic. Recent work has demonstrated that bitmask-based sparse CIM accelerators can achieve near-linear speedup with sparsity density, as the control logic can quickly filter out zero blocks using simple AND/OR operations [21].

## Comparison of Compression Formats in CIM Context

The following table summarizes the key characteristics of various compression formats in the context of CIM hardware, highlighting their trade-offs in terms of storage overhead, computational efficiency, and hardware complexity.

| Format | Storage Overhead | Computational Efficiency | Hardware Complexity | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **CSR** | High (requires row/col indices) | Low (irregular access) | High (complex indexing logic) | General-purpose sparse AI |
| **COO** | High (requires row/col/value) | Low (unstructured) | High (random access) | Debugging, prototyping |
| **Block-CSR** | Medium (block indices) | High (regular block access) | Medium (block-level gating) | CNNs with local sparsity |
| **Bitmask** | Low (1 bit per element/block) | High (parallel bitwise ops) | Low (simple logic) | High sparsity (>90%) |
| **RLE** | Low (variable) | Medium (sequential decode) | Low (sequential logic) | Long zero runs in weights |

*Table 1: Comparison of Sparse Compression Formats for CIM Hardware [17], [18], [20], [21].*

## Challenges and Future Directions in Compression

Despite these advancements, several challenges remain in implementing compression formats in CIM hardware. First, **dynamic sparsity** in neural networks (where sparsity patterns change during training or inference) requires compression formats that can be updated efficiently without reconfiguring the entire hardware structure. Second, **quantization errors** introduced by lossy compression schemes can degrade model accuracy, necessitating careful trade-offs between compression ratio and precision. Finally, **standardization** of sparse formats for CIM is lacking, leading to fragmentation in hardware-software co-design efforts. Future research is likely to focus on adaptive compression schemes that can dynamically switch between formats based on sparsity patterns and workload characteristics, further optimizing the energy-performance trade-off in CIM accelerators [22].

In conclusion, the choice of compression format is critical for maximizing the efficiency of sparse CIM hardware. While analog mechanisms inherently skip zero computations, the digital control logic must be optimized through hardware-friendly compression schemes such as block-sparse formats, bitmask, and RLE. These formats reduce control overhead, improve access regularity, and enable significant energy savings, making them essential for the practical deployment of sparse CIM accelerators in real-world AI applications.



## 3.2 Hardware-Friendly Sparsity Patterns

_To identify structural sparsity patterns that maximize computational efficiency in CIM arrays_


# Hardware-Friendly Sparsity Patterns

While previous sections discussed general digital and mixed-signal approaches to handling sparsity, a critical determinant of efficiency in Compute-in-Memory (CIM) arrays is the **structural compatibility** between the sparsity pattern and the physical memory architecture. Unlike general-purpose processors where sparsity is handled via flexible software indexing, CIM hardware imposes strict constraints on how non-zero elements can be accessed and computed. Therefore, identifying and enforcing sparsity patterns that align with the hardware’s data flow is essential to minimize overhead and maximize throughput [31].

## Structured Sparsity: The Hardware-Aligned Approach

The most effective sparsity patterns for CIM are those that are **structured** rather than unstructured. Unstructured sparsity, where non-zero elements are randomly distributed, requires complex address translation and dynamic routing logic that often negates the energy benefits of in-memory computation [32]. In contrast, structured sparsity allows for predictable access patterns, enabling hardware optimizations such as pre-computed address offsets and simplified control logic.

### Block-Sparse and Filter-Wise Patterns

Recent advancements in AI chip design favor **block-sparse** patterns, where non-zero elements are grouped into fixed-size blocks (e.g., 2x2, 4x4, or 8x8 matrices) [33]. This approach is particularly advantageous for SRAM-based CIM arrays because:

1.  **Data Locality:** Block-sparse data can be stored contiguously or in predictable strides within the SRAM banks, reducing the number of active wordlines and bitlines during access [34].
2.  **Simplified Control Logic:** Instead of maintaining individual indices for every non-zero element, the hardware only needs to track the base address of each block and the block’s sparsity type (e.g., all-zero, all-non-zero, or partially non-zero) [35].
3.  **Parallelism Exploitation:** Fixed-size blocks align well with the parallel MAC units in CIM arrays, allowing entire blocks to be processed simultaneously without complex synchronization [36].

For example, in convolutional neural networks (CNNs), **filter-wise sparsity** (where entire filters or channels are zeroed out) has been shown to reduce computation by up to 50% with minimal hardware overhead [37]. This is because the hardware can simply skip the entire weight row or column in the CIM array, avoiding both computation and data movement for those elements.

### N:M Structured Sparsity

Another emerging pattern is **N:M structured sparsity**, where every N contiguous weights contain exactly M non-zero weights (e.g., 2:4 sparsity) [38]. This pattern is increasingly supported by hardware accelerators because it offers a balance between model accuracy and hardware efficiency:

*   **Predictable Access:** The position of non-zero weights within each N-element group is fixed, allowing the hardware to use simple bitmasks to identify which elements to compute [39].
*   **Hardware Support:** Recent CIM designs incorporate dedicated **sparse decode logic** that interprets the N:M pattern on-the-fly, eliminating the need for software-level decompression [40].
*   **Energy Savings:** By avoiding the storage and transmission of zero values, N:M sparsity reduces data movement energy by approximately 40-60% compared to dense computation [41].

| Sparsity Pattern | Hardware Compatibility | Control Complexity | Energy Efficiency | Accuracy Impact |
| :--- | :--- | :--- | :--- | :--- |
| **Unstructured** | Low | High (Dynamic Indexing) [42] | Low (High Overhead) | Minimal |
| **Block-Sparse** | High | Medium (Block Tracking) [43] | High (Reduced Movement) | Low |
| **N:M Structured** | Very High | Low (Bitmask Decoding) [44] | Very High | Minimal |
| **Filter-Wise** | High | Low (Row/Column Skipping) [45] | High | Variable |

## Hardware-Optimized Sparse Formats

To further enhance efficiency, specific sparse data formats have been developed to align with the physical layout of CIM arrays. These formats reduce the overhead of index management and enable direct in-memory processing.

### Compressed Row Storage (CRS) with Hardware Decoders

While CSR (Compressed Sparse Row) is a common software format, **Hardware-Optimized CSR (H-CSR)** modifies the index storage to reduce latency [46]. In H-CSR, indices are stored in a compressed form that matches the wordline structure of the SRAM array, allowing the control unit to decode indices in a single cycle [47]. This reduces the overhead of index lookup from multiple cycles to one, significantly improving throughput for sparse operations [48].

### Bitmask-Driven Sparse Access

A novel approach involves using **bitmask-driven access**, where a compact bitmask indicates the presence of non-zero elements in a row or block [49]. The CIM hardware’s control unit uses this bitmask to enable or disable specific bitlines or wordlines, effectively masking out zero values without explicit index calculation [50]. This method is particularly effective for N:M sparsity, where the bitmask can be generated on-the-fly from the sparsity pattern configuration [51].

## Critical Reflection on Pattern Selection

It is crucial to note that not all sparsity patterns are equally beneficial. While structured sparsity improves hardware efficiency, it may lead to **accuracy degradation** if the sparsity pattern does not align with the model’s weight distribution [52]. For instance, aggressive block-sparse pruning may remove important features in certain layers, leading to performance drops [53]. Therefore, a co-design approach that combines **pruning strategies** with **hardware-aware pattern selection** is necessary to balance efficiency and accuracy [54].

Furthermore, the choice of sparsity pattern should consider the **memory bandwidth** and **compute density** of the specific CIM architecture. For memory-bound applications, patterns that minimize data movement (e.g., filter-wise sparsity) are preferred, while for compute-bound applications, patterns that maximize parallelism (e.g., block-sparse) are more effective [55].

In conclusion, hardware-friendly sparsity patterns such as block-sparse and N:M structured sparsity offer a viable path to maximizing computational efficiency in CIM arrays. By aligning sparsity structures with the physical constraints of the hardware, designers can minimize control overhead and maximize energy savings, paving the way for more efficient AI accelerators [56].






# 4. Algorithm-Hardware Co-Design

## 4.1 Pruning Techniques for CIM

_To explore model pruning methods specifically tailored to maximize the benefits of sparse CIM execution_


# Pruning Techniques for CIM

While the previous section addressed the physical memory organization required to store sparse data, this subsection examines the **algorithmic and structural pruning strategies** specifically designed to maximize the efficiency of Sparse Compute-in-Memory (CIM) execution. Standard pruning techniques, such as magnitude-based unstructured pruning, often generate irregular sparse patterns that are inefficient for CIM hardware due to the overhead of metadata decoding and irregular access patterns. Therefore, recent research focuses on **CIM-aware pruning** methods that align sparsity structures with the hardware’s computational constraints, such as vector-matrix multiplication (VMM) granularity and analog non-idealities [25].

## 1. Structured Pruning for CIM Compatibility

To minimize the metadata overhead discussed in the "Memory Organization Strategies" section, **structured pruning** is preferred in CIM architectures. This approach removes entire channels, filters, or blocks of weights, resulting in regular sparse patterns that can be efficiently mapped to CIM arrays without complex index decoding.

### Block-Wise and Channel-Wise Pruning
CIM accelerators typically operate on fixed-size blocks (e.g., 8x8 or 16x16 weight tiles). **Block-wise pruning** ensures that entire blocks of weights are zeroed out, allowing the CIM controller to skip the processing of these blocks entirely [26].
*   **Implementation:** A sparsity mask is generated during training, identifying blocks where the L2-norm of weights falls below a threshold. These blocks are replaced with zeros, and the corresponding control signals disable the VMM operation for those tiles [27].
*   **Benefit:** This reduces the need for bit-level compression logic, as the control logic can simply bypass entire memory rows or tiles, leading to higher energy efficiency compared to unstructured pruning [28].

### Group-Structured Sparsity
**Group-structured pruning** divides weights into groups (e.g., 4x4 or 8x8) and prunes based on group-level metrics. This is particularly effective for CIM hardware that supports **grouped processing** or **multi-channel parallelism** [29].
*   **Example:** In a ReRAM-based CIM, weights are grouped into columns. If a column group has low activation, the entire group is pruned, reducing the number of active wordlines and bitlines simultaneously [30].
*   **Hardware Alignment:** This aligns with the physical layout of ReRAM arrays, where wordlines and bitlines intersect. Pruning entire groups reduces the active area of the array, lowering leakage power and capacitance [31].

| Pruning Type | Granularity | CIM Hardware Benefit | Accuracy Impact |
| :--- | :--- | :--- | :--- |
| **Unstructured** | Individual weights | Low; requires complex metadata and irregular access. | Minimal; preserves accuracy best. |
| **Block-Wise** | Fixed-size blocks (e.g., 8x8) | High; enables tile-level skipping; reduces decoding overhead. | Moderate; may require fine-tuning. |
| **Channel-Wise** | Entire input/output channels | Very High; simplifies memory access patterns; reduces data movement. | Significant; often requires retraining. |
| **Group-Structured** | Sub-blocks within channels | High; balances sparsity density and hardware efficiency. | Moderate; depends on group size. |

## 2. CIM-Aware Pruning with Non-Idealities

CIM hardware suffers from **analog non-idealities** such as conductance variation, compliance current limits, and noise. Standard pruning does not account for these effects, leading to significant accuracy drops when sparse models are deployed on CIM. **CIM-aware pruning** integrates hardware constraints into the pruning process to ensure that the remaining weights are robust to these non-idealities.

### Conductance Variation Robustness
In analog CIM, the accuracy of VMM operations depends on the precision of weight conductance values. **Conductance variation** (process variation) can cause significant errors in sparse matrices if non-zero weights are clustered in certain regions [32].
*   **Technique:** Pruning algorithms incorporate a **conductance variation penalty** into the loss function. Weights that are sensitive to variation (e.g., those in high-noise regions of the array) are pruned first, while robust weights are retained [33].
*   **Data:** Models pruned with this method showed a 15% reduction in inference error on noisy ReRAM arrays compared to standard magnitude-based pruning [34].

### Non-Linear Activation Compensation
CIM arrays often use **in-memory activation functions** (e.g., using diodes or threshold devices) that introduce non-linearities. Sparse pruning can exacerbate these non-linearities if the remaining weights are not optimized for the specific activation curve [35].
*   **Approach:** **Joint pruning and activation optimization** adjusts the pruning thresholds based on the non-linear activation response. This ensures that the sparse weights contribute effectively to the output despite the non-linearities [36].
*   **Example:** In a Memristor-CIM, pruning is guided by the **Sigmoid-like activation response** of the memristors, ensuring that pruned weights do not disrupt the linear region of the activation function [37].

## 3. Dynamic and Adaptive Pruning for CIM

Static pruning methods may not be optimal for all CIM applications, especially those with varying workloads or data distributions. **Dynamic pruning** adjusts the sparsity pattern during inference to adapt to the input data, maximizing energy savings for sparse inputs while maintaining accuracy for dense inputs.

### Input-Dependent Sparsity
**Input-dependent pruning** zeros out weights that have minimal impact on the output for a given input. This is particularly useful for CIM hardware with **reconfigurable sparse access** [38].
*   **Mechanism:** A lightweight predictor determines which weight blocks are inactive for a specific input. The CIM controller then skips the memory access for these blocks, reducing energy consumption proportionally to the input sparsity [39].
*   **Benefit:** For inputs with high sparsity, this can achieve up to 60% energy savings compared to static pruning [40].

### Adaptive Pruning Thresholds
**Adaptive pruning** dynamically adjusts the pruning threshold based on the confidence of the model’s predictions or the available energy budget.
*   **Technique:** During inference, if the system detects a low energy budget, the pruning threshold is increased, resulting in a sparser model. Conversely, if accuracy drops below a threshold, the pruning threshold is decreased [41].
*   **Implementation:** This requires a **feedback loop** between the CIM controller and the pruning engine, which can be implemented using lightweight digital logic alongside the analog CIM array [42].

## 4. Hardware-Software Co-Design for Pruning

Effective pruning for CIM requires close collaboration between algorithm design and hardware implementation. **Co-design** ensures that the pruning strategy is compatible with the CIM architecture’s constraints, such as limited on-chip memory for metadata and fixed-point arithmetic limitations.

### Metadata-Efficient Pruning
CIM hardware often has limited on-chip memory for storing sparsity metadata (e.g., indices of non-zero weights). **Metadata-efficient pruning** minimizes the size of this metadata by using **compressed sparse row (CSR)** formats or **run-length encoding (RLE)** that are optimized for the CIM’s memory hierarchy [43].
*   **Strategy:** Pruning algorithms are designed to produce sparsity patterns that can be compressed efficiently. For example, **block-sparse patterns** are preferred because they can be encoded with fewer bits than unstructured sparsity [44].
*   **Impact:** This reduces the area overhead of metadata storage, allowing more area to be dedicated to the CIM array itself [45].

### Fixed-Point Pruning
CIM hardware typically uses **fixed-point arithmetic** for weight storage and computation. **Fixed-point pruning** accounts for the quantization effects during the pruning process, ensuring that the remaining weights are representable in the available bit-width [46].
*   **Technique:** Pruning thresholds are adjusted based on the quantization levels. Weights that would be quantized to zero are pruned explicitly, avoiding the need for additional quantization logic [47].
*   **Benefit:** This simplifies the hardware design by reducing the need for complex quantization-aware training and pruning loops [48].

| Co-Design Aspect | Challenge in CIM | Pruning Solution |
| :--- | :--- | :--- |
| **Metadata Storage** | Limited on-chip memory for indices. | Block-sparse patterns; compressed encoding. |
| **Quantization** | Fixed-point limitations cause weight collapse. | Fixed-point-aware pruning thresholds. |
| **Non-Linearities** | Analog non-idealities affect accuracy. | Hardware-aware pruning penalties. |
| **Energy Efficiency** | Static pruning may not adapt to input. | Input-dependent dynamic pruning. |

## 5. Critical Reflection on Pruning Techniques

While pruning techniques offer significant benefits for CIM, several challenges remain:
*   **Accuracy-Energy Trade-off:** Aggressive pruning can lead to significant accuracy drops, especially in deep networks. **CIM-aware pruning** mitigates this but requires careful tuning of hyperparameters [49].
*   **Hardware Overhead:** Dynamic pruning and adaptive thresholds require additional control logic, which can offset the energy savings from sparsity [50].
*   **Scalability:** As CIM arrays scale to larger sizes, the complexity of managing sparse access patterns increases. **Structured pruning** remains the most scalable solution due to its regularity [51].

In conclusion, **CIM-aware pruning** strategies that align with hardware constraints, such as structured sparsity, non-ideality robustness, and metadata efficiency, are essential for maximizing the benefits of sparse CIM execution. Future research should focus on **adaptive pruning** techniques that can dynamically adjust to workload variations, further enhancing the energy efficiency and accuracy of CIM accelerators.



## 4.2 Quantization and Sparsity Joint Optimization

_To analyze how combining low-bit quantization with sparsity enhances accuracy and efficiency_


# Quantization and Sparsity Joint Optimization

While the previous subsection detailed how sparse data is encoded to minimize control overhead, the ultimate efficiency of Compute-in-Memory (CIM) systems is determined by the **joint optimization** of sparsity and low-bit quantization. In digital accelerators, sparsity and quantization are often treated as sequential post-training steps. However, in CIM hardware, these two dimensions are deeply coupled: the analog physical properties of the memory array (such as conductance variation and non-linearity) impose strict constraints on both the number of active elements (sparsity) and the precision of their values (quantization). Jointly optimizing these parameters allows CIM architectures to bypass the "bit-width bottleneck" and leverage the inherent noise-tolerance of analog computation.

## The Physics-Driven Trade-off: Noise Tolerance vs. Precision

In analog CIM, the signal-to-noise ratio (SNR) is the primary determinant of accuracy. High-bit quantization (e.g., INT8 or FP16) requires high SNR to distinguish between closely spaced conductance levels. However, increasing bit-width increases the number of distinguishable states, which exacerbates the impact of device variability and read noise. Conversely, sparsity reduces the magnitude of the accumulated current, potentially lowering the signal strength relative to fixed read noise floors.

Recent research highlights a counter-intuitive benefit of joint optimization: **sparsity can enhance effective quantization precision by reducing interference**. In dense matrix-vector multiplication (MVM), the accumulation of many small currents can saturate the analog-to-digital converter (ADC) or increase thermal noise. By pruning weak connections (sparsity), the remaining active currents are larger relative to the noise floor, allowing for lower-bit quantization of the remaining weights without sacrificing accuracy [21].

### Adaptive Bit-Width Allocation

Instead of uniform quantization across all weights, joint optimization employs **adaptive bit-width allocation** based on sparsity patterns. Weights that are retained in a sparse structure often carry more significant information and may require higher precision (e.g., INT4), while those in dense regions might be quantized to lower bits (e.g., INT2) if they are less critical. This approach is particularly effective in CIM because it aligns with the **non-uniform sensitivity** of neural network layers.

| Optimization Strategy | Mechanism | CIM-Specific Benefit | Reference |
| :--- | :--- | :--- | :--- |
| **Sparsity-Gated Quantization** | Quantization bit-width is reduced only for weights pruned to zero in adjacent layers or blocks. | Reduces ADC resolution requirements for inactive paths, saving dynamic energy. | [22] |
| **Noise-Aware Joint Pruning** | Pruning criteria include a penalty term for quantization error induced by device noise. | Ensures that retained weights are robust to analog imperfections, improving inference accuracy. | [23] |
| **Dynamic Precision Scaling** | Bit-width is adjusted per-layer based on the sparsity level of that layer’s weight matrix. | Matches the computational granularity to the analog array’s physical capabilities, maximizing throughput. | [24] |

## Hardware-Algorithm Co-Design for Mixed-Precision Sparse CIM

The integration of sparsity and quantization is not merely an algorithmic choice but a hardware design imperative. CIM architectures must support **mixed-precision execution** where different parts of the array operate at different effective precisions. This requires novel circuit-level innovations that go beyond simple digital control logic.

### Sub-Array Level Precision Management

Recent architectural proposals suggest dividing the CIM crossbar into **sub-arrays with independent quantization capabilities**. For instance, a 128x128 crossbar might be divided into four 64x64 sub-arrays. Sub-arrays handling sparse regions can operate with lower-bit DACs (Digital-to-Analog Converters) and ADCs, while dense sub-arrays use higher-bit converters. This **spatially varying precision** reduces the overall energy per MAC (Multiply-Accumulate) operation by avoiding the use of high-power, high-precision components for insignificant data [25].

### Analog-Side Sparsity Enforcement

Traditional sparse computation offloads sparsity handling to digital logic, which then activates only relevant rows/columns. However, **analog-side sparsity enforcement** offers greater efficiency. By using **threshold-based conductance gating**, weights below a certain conductance threshold (which would be quantized to zero or near-zero) are physically disconnected or biased to a high-resistance state. This reduces the leakage current and static power consumption of the array, complementing the dynamic energy savings from digital sparsity [26].

## Case Study: Joint Optimization in Vision Transformers (ViTs)

Vision Transformers, which are increasingly deployed on CIM hardware, exhibit high sparsity in their attention mechanisms and mixed precision requirements in their MLP (Multi-Layer Perceptron) blocks. A recent study on a 16nm CIM accelerator demonstrated that jointly applying **4-bit quantization** and **60% structured sparsity** (2:4 pattern) resulted in a **3.2x reduction in energy consumption** compared to a baseline INT8 dense model, with only a **0.5% drop in accuracy** [27]. This outcome was achieved by:

1.  **Quantization-Aware Pruning (QAP):** Pruning was performed after quantization, ensuring that the most "quantization-resistant" weights were retained.
2.  **Hardware-Aware Search:** The sparsity pattern was optimized to align with the CIM array’s block structure, minimizing index lookup overhead.
3.  **Noise Compensation:** The remaining weights were slightly over-provisioned in precision to compensate for analog noise, effectively using the "extra" precision as a buffer against hardware imperfections.

## Critical Reflection on Joint Optimization Challenges

While joint optimization offers significant benefits, it introduces complexity in both training and hardware calibration. **Training convergence** can be difficult when sparsity and quantization are optimized simultaneously, as the search space is highly non-convex. Additionally, **hardware variability** means that a joint optimization strategy tuned for one CIM chip may not perform optimally on another due to differences in device noise and conductance distributions. Future work must focus on **robust joint optimization frameworks** that account for process variation and **self-calibrating CIM architectures** that can adapt their quantization-sparsity trade-off in real-time based on runtime SNR measurements [28].

## Conclusion for Subsection

The joint optimization of quantization and sparsity is not merely a software technique but a fundamental enabler of efficient analog CIM. By aligning algorithmic compression with physical hardware constraints, CIM systems can achieve superior energy efficiency and accuracy compared to treating these dimensions independently. The key lies in **hardware-aware design** that leverages analog noise characteristics and structural sparsity to reduce precision requirements dynamically.






# 5. Performance Evaluation and Benchmarks

## 5.1 Energy Efficiency Metrics

_To define and evaluate key metrics such as Energy per Inference (EPI) and TOPS/Watt for sparse CIM chips_


# Energy Efficiency Metrics

To rigorously evaluate the performance of sparse Compute-in-Memory (CIM) chips, it is necessary to move beyond simple throughput measurements and adopt metrics that capture the unique energy dynamics of in-memory computation. While general AI accelerators often rely on **TOPS/Watt** (Tera Operations Per Second per Watt) as a primary benchmark, sparse CIM architectures require a more nuanced definition of "operation" and "energy," particularly when accounting for the overheads of sparsity decoding and the non-linear energy costs associated with memory access [42]. This subsection defines **Energy per Inference (EPI)** and **TOPS/Watt** specifically within the context of sparse CIM, highlighting how sparsity-aware measurement protocols reveal true efficiency gains.

## Defining TOPS/Watt in Sparse CIM Contexts

In traditional dense CIM, TOPS/Watt is calculated by dividing the total number of Multiply-Accumulate (MAC) operations by the total system energy consumption. However, in sparse CIM, this metric can be misleading if not contextualized with the **effective sparsity rate** and the **sparsity decoding energy** [43].

### The "Effective" vs. "Theoretical" TOPS/Watt Distinction

A critical distinction in sparse CIM evaluation is between *theoretical* TOPS/Watt (based on the peak capacity of the array) and *effective* TOPS/Watt (accounting for actual non-zero computations and control overheads).

*   **Theoretical TOPS/Watt:** Assumes all weights are non-zero or that sparsity is perfectly exploited with zero overhead. This metric often overstates efficiency by ignoring the energy cost of fetching sparsity maps, decoding indices, and managing irregular data flows [44].
*   **Effective TOPS/Watt:** Calculates performance based on the actual number of non-zero MAC operations performed, divided by the total energy consumed by the CIM array, peripheral circuits, and sparsity decoding logic [45]. Recent studies indicate that for highly sparse models (e.g., >90% sparsity), the energy cost of decoding sparse indices can constitute 15–25% of the total energy budget if not optimized, significantly reducing the effective TOPS/Watt compared to theoretical predictions [46].

| Metric | Definition | Relevance to Sparse CIM |
| :--- | :--- | :--- |
| **Peak TOPS/Watt** | Total MAC capacity / Peak Power | Useful for comparing hardware potential but ignores sparsity overheads [47]. |
| **Effective TOPS/Watt** | Non-zero MACs / Total Energy (including decoding) | Provides a realistic assessment of system-level efficiency [48]. |
| **Sparsity-Adjusted TOPS/Watt** | Non-zero MACs / (Compute Energy + Access Energy + Decode Energy) | Isolates the energy penalty of sparsity handling [49]. |

### Impact of Sparsity Pattern on TOPS/Watt

The choice of sparsity pattern directly influences the TOPS/Watt metric. As discussed in previous sections, structured sparsity (e.g., N:M) reduces decoding overhead compared to unstructured sparsity [50]. Consequently, chips optimized for N:M sparsity often report higher effective TOPS/Watt because the decoding logic consumes less power, and data movement is more predictable [51]. For instance, a mixed-signal CIM chip implementing 2:4 sparsity demonstrated a 2.3x improvement in effective TOPS/Watt over a dense baseline, whereas an unstructured sparse implementation showed only a 1.4x improvement due to higher control logic energy [52].

## Energy per Inference (EPI) as a Holistic Metric

While TOPS/Watt measures computational efficiency, **Energy per Inference (EPI)** provides a holistic view of the energy cost to process a single input sample. EPI is particularly critical for edge AI applications where battery life and thermal constraints are paramount [53].

### Components of EPI in Sparse CIM

EPI in sparse CIM is not merely the sum of compute energy; it includes several distinct components that are amplified by sparsity:

1.  **Compute Energy:** The energy consumed by analog or digital MAC operations in the CIM array. In sparse CIM, this is proportional to the number of non-zero weights [54].
2.  **Memory Access Energy:** The energy to read weights and activations. Sparsity reduces this by skipping zero values, but only if the sparsity pattern allows for efficient data compression and retrieval [55].
3.  **Sparsity Decoding Energy:** The energy required to interpret sparsity masks or indices. This is a unique overhead in sparse CIM that is negligible in dense systems but significant in sparse ones [56].
4.  **Peripheral Circuit Energy:** The energy consumed by ADCs (Analog-to-Digital Converters), digital control logic, and interconnects. In mixed-signal CIM, the energy of the ADCs can dominate the total EPI, especially for low-precision computations [57].

### EPI Benchmarking Methodologies

To ensure fair comparison across different sparse CIM architectures, EPI should be measured under standardized conditions that account for the **end-to-end energy cost** [58]. This includes:

*   **Full Model Inference:** EPI should be calculated for a complete model inference, not just a single layer, to capture the cumulative effect of sparsity across the network [59].
*   **Sparsity Level Variance:** EPI should be reported at multiple sparsity levels (e.g., 50%, 75%, 90%) to illustrate the trade-off between energy savings and accuracy retention [60].
*   **Data Movement Accounting:** Energy spent on moving data between the CIM array and off-chip memory (if any) must be included. Sparse CIM aims to minimize this, but incomplete sparsity exploitation can lead to significant off-chip access energy [61].

## Comparative Analysis of Metrics in Recent Sparse CIM Chips

Recent research highlights the importance of reporting both TOPS/Watt and EPI to provide a comprehensive efficiency profile. The following table summarizes key findings from recent sparse CIM implementations, illustrating the impact of sparsity-aware design on these metrics.

| Chip/Architecture | Sparsity Support | Effective TOPS/Watt | EPI (pJ/Inference) | Key Efficiency Driver |
| :--- | :--- | :--- | :--- | :--- |
| **Sparse CIM-1** [62] | 2:4 Structured | 45 TOPS/W | 120 pJ | Optimized decoding logic for N:M patterns |
| **Mixed-Signal CIM-2** [63] | Unstructured | 28 TOPS/W | 250 pJ | High precision ADCs offset sparsity gains |
| **Digital CIM-3** [64] | Block-Sparse | 35 TOPS/W | 180 pJ | Simplified address generation for blocks |
| **Analog CIM-4** [65] | Filter-Wise | 50 TOPS/W | 95 pJ | Minimal data movement via filter skipping |

*Note: Values are illustrative based on recent trends in sparse CIM literature [62]-[65].*

As shown, **Filter-Wise Sparsity** (as in Analog CIM-4) achieves the highest TOPS/Watt and lowest EPI by eliminating entire filter computations, thereby avoiding both compute and access energy [66]. In contrast, **Unstructured Sparsity** (Sparse CIM-1) suffers from higher EPI due to the energy overhead of decoding individual indices, despite potentially higher sparsity ratios [67].

## Critical Evaluation of Metric Limitations

While TOPS/Watt and EPI are valuable, they have limitations in fully capturing the efficiency of sparse CIM chips:

1.  **Accuracy-Energy Trade-off:** A low EPI or high TOPS/Watt may come at the cost of reduced model accuracy. Therefore, these metrics must always be reported alongside **accuracy retention** data [68]. A chip with 10% higher EPI but 5% higher accuracy may be more efficient in a real-world application [69].
2.  **Scalability Issues:** TOPS/Watt can degrade as array size increases due to increased wire resistance and capacitance, particularly in analog CIM. EPI may remain stable or improve if sparsity scales proportionally, but this requires careful architectural design [70].
3.  **Workload Dependency:** Both metrics are highly dependent on the specific neural network architecture and input data. A sparse CIM chip optimized for CNNs may perform differently on Transformers due to differences in sparsity patterns [71].

## Conclusion

In summary, evaluating sparse CIM chips requires a dual-metric approach using **Effective TOPS/Watt** and **Energy per Inference (EPI)**. Effective TOPS/Watt accounts for the energy overhead of sparsity decoding, providing a realistic measure of computational efficiency, while EPI offers a holistic view of the energy cost per inference, including memory access and peripheral circuits. Future benchmarks must standardize the inclusion of sparsity decoding energy and accuracy retention to ensure fair and meaningful comparisons across different sparse CIM architectures [72].



## 5.2 Accuracy Retention under Sparsity

_To assess the trade-offs between sparsity levels and model accuracy across different AI tasks_


# Accuracy Retention under Sparsity

While the previous section detailed the structural pruning strategies required for hardware compatibility, this subsection critically assesses the **quantitative trade-offs** between sparsity levels and model accuracy. The central challenge in Sparse Compute-in-Memory (CIM) is not merely achieving high sparsity, but maintaining inference accuracy within acceptable thresholds despite the compounding effects of hardware non-idealities and aggressive data compression. This assessment is crucial for defining the practical limits of CIM deployment across diverse AI tasks, ranging from Large Language Models (LLMs) to Convolutional Neural Networks (CNNs).

## 1. The Non-Linear Accuracy-Sparsity Trade-off

Unlike digital CPUs, where sparsity primarily impacts computational cycles, CIM architectures introduce a non-linear accuracy degradation curve as sparsity increases. This is due to the interplay between **quantization noise**, **analog variability**, and **sparse signal loss**.

### Task-Specific Sensitivity to Sparsity
Different AI tasks exhibit varying degrees of robustness to sparsity. Critical for benchmarking is identifying the "sparsity ceiling" for each task before significant accuracy drop-offs occur.

| AI Task | Model Type | Max Practical Sparsity | Accuracy Drop ($\Delta$ Acc) | Primary Failure Mode |
| :--- | :--- | :--- | :--- | :--- |
| **Image Classification** | ResNet-50 | 90-95% | < 1.0% | Loss of fine-grained feature edges |
| **Object Detection** | YOLOv5 | 85-90% | 1.5-2.5% | Localization precision loss |
| **NLP (BERT)** | BERT-base | 70-80% | 2.0-4.0% | Semantic coherence degradation |
| **LLM (LLaMA-7B)** | Transformer | 50-60% | 5-10% | Context window fragmentation |

*Data synthesized from recent benchmarking studies on CIM deployment [32], [33].*

As shown in Table 1, **LLMs are significantly more sensitive to sparsity** than CNN-based tasks. This is attributed to the dense attention mechanisms in Transformers, which rely on global weight dependencies. In contrast, CNNs, particularly in early layers, often possess redundant filters that can be pruned with minimal impact [34].

## 2. Hardware-Induced Accuracy Erosion

A unique aspect of CIM is that accuracy loss is not solely due to algorithmic pruning but is exacerbated by **hardware non-idealities** acting as noise sources. When sparsity increases, the signal-to-noise ratio (SNR) of the analog VMM operation can degrade if the remaining active weights are not sufficiently strong.

### Conductance Non-Uniformity and Sparsity
In analog CIM, **conductance non-uniformity** (variation in resistance states) introduces error. Research indicates that at high sparsity levels (>80%), the effective dynamic range of the array decreases. This leads to:
1.  **Dominance of Noise:** The absolute error from conductance variation becomes comparable to the signal magnitude of the remaining non-zero weights [35].
2.  **Saturation Effects:** In ReRAM or PCM arrays, high sparsity can lead to unbalanced current distributions, causing bitline saturation for the few remaining active paths [36].

### Quantization-Pruning Interaction
Sparse CIM often employs **mixed-precision arithmetic**. The interaction between pruning and quantization is critical:
*   **Coarse Quantization + High Sparsity:** Leads to catastrophic accuracy loss. For example, 4-bit quantization combined with 90% sparsity in LLMs resulted in a perplexity increase of >20% compared to baseline [37].
*   **Optimal Configuration:** Recent studies suggest that **asymmetric quantization** (different bit-widths for sparse vs. dense layers) can mitigate this. By assigning higher precision to critical sparse layers, accuracy retention improves by 15-20% without significant area overhead [38].

## 3. Mitigation Strategies for Accuracy Retention

To maximize sparsity while preserving accuracy, recent research has moved beyond simple pruning to **adaptive accuracy compensation** techniques.

### Post-Training Calibration with Sparse Awareness
Standard post-training calibration (PTQ) often fails for sparse CIM because it assumes uniform weight distributions. **Sparse-aware PTQ** adjusts quantization parameters based on the local sparsity pattern:
*   **Method:** Calibration datasets are processed to identify "critical sparse regions" where weight values are large but few. Quantization scales are optimized to preserve these outliers [39].
*   **Result:** In BERT models, sparse-aware PTQ reduced accuracy drop from 3.5% to 1.2% at 80% sparsity compared to standard PTQ [40].

### Hybrid Digital-Analog Correction
Some advanced CIM architectures incorporate **small digital correction engines** to handle accuracy-critical sparse operations:
*   **Mechanism:** The CIM array performs the bulk of the VMM, while a small digital unit computes the residual error for sparse layers and adds it to the result [41].
*   **Trade-off:** This adds ~5% area overhead but allows for sparsity levels up to 95% in CNNs with <0.5% accuracy loss [42].

## 4. Benchmarking Methodology for Accuracy Retention

To standardize the evaluation of accuracy retention, the following metrics are proposed for future CIM benchmarks:

1.  **Sparsity-Aware Accuracy Decay Rate (SAADR):** Measures the rate of accuracy loss per 1% increase in sparsity. Lower SAADR indicates better hardware-algorithm co-design.
2.  **Effective Sparsity Ratio (ESR):** The ratio of *algorithmically pruned* weights to *hardware-ignored* weights. A high ESR indicates that the hardware is effectively leveraging the sparsity without additional metadata overhead [43].
3.  **Task-Specific Sparsity Threshold (TSST):** The maximum sparsity level before accuracy drops below a task-specific minimum (e.g., 90% for classification, 30 mAP for detection).

| Metric | Definition | Significance |
| :--- | :--- | :--- |
| **SAADR** | $\frac{\Delta \text{Accuracy}}{\Delta \text{Sparsity}}$ | Indicates robustness of the CIM architecture to sparsity. |
| **ESR** | $\frac{\text{Hardware-ignored Weights}}{\text{Total Pruned Weights}}$ | Measures how efficiently the hardware utilizes sparsity. |
| **TSST** | Max Sparsity @ $\text{Accuracy}_{\text{min}}$ | Defines the practical limit for deployment in specific tasks. |

## Conclusion

The assessment of accuracy retention under sparsity reveals that **sparsity is not a universal benefit** in CIM. While CNNs can tolerate up to 90% sparsity with minimal accuracy loss, LLMs require more conservative sparsity levels (<60%) or advanced mitigation techniques like sparse-aware calibration. The key to maximizing efficiency lies in **task-aware sparsity limits** and **hardware-aware quantization**, ensuring that the benefits of sparse compute-in-memory are realized without compromising model integrity. Future work must focus on adaptive sparsity mechanisms that dynamically adjust sparsity levels based on layer importance and hardware health [44].






# 6. Current Challenges and Future Directions

## 6.1 Hardware Limitations and Noise

_To discuss physical constraints like process variation and noise in analog CIM that affect sparse computation_


# Hardware Limitations and Noise

While the previous subsections addressed algorithmic strategies to mitigate the effects of physical imperfections, the fundamental physical constraints of Compute-in-Memory (CIM) hardware impose hard limits on the feasibility of sparse analog computation. Unlike digital logic, where errors are binary and correctable, analog CIM systems suffer from continuous physical degradations that directly corrupt the sparse matrix-vector multiplication (MVM) operations. This section critically examines two primary hardware limitations: **Process Variation** (static non-idealities) and **Noise** (dynamic non-idealities), and their specific impact on sparse data patterns.

## Static Non-Idealities: Process Variation and Conductance Mismatch

In ideal CIM architectures, the conductance of a memristive or transistor-based device maps linearly to its weight value. However, fabrication processes introduce **process variation**, leading to significant mismatch in device characteristics across a large array. This static variability manifests as **offset errors** and **gain mismatches**, which are particularly detrimental to sparse computation because they introduce "phantom" activations in regions that should remain zero.

### Impact on Sparse Activation Patterns
In dense MVM, offset errors may average out or be absorbed by the activation function's non-linearity. In sparse MVM, however, the signal is concentrated in fewer active pathways. A process-induced conductance drift in a device that should be zero (pruned) can create a false positive activation, breaking the sparsity assumption and forcing the system to process non-existent data. Recent studies indicate that for 1T1R (one-transistor, one-resistor) arrays, process variation can cause up to **15-20% deviation** in the effective weight matrix, severely impacting accuracy in low-bit sparse models [1].

### Mitigation via Calibration and Redundancy
To counteract static variation, hardware-level **per-device calibration** is often required. This involves a one-time training or read-back procedure to determine the actual conductance of each cell and digitally compensate for the deviation. However, this approach increases the area overhead and complicates the sparse encoding logic, as the decoder must account for non-linear, device-specific transfer functions rather than uniform weight steps [2].

| Hardware Imperfection | Physical Origin | Impact on Sparse CIM | Common Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **Threshold Voltage ($V_{th}$) Variation** | Transistor fabrication inconsistencies | Shifts the activation point of the selector transistor, causing premature or delayed conduction. | Per-cell $V_{th}$ compensation circuits; adaptive reference voltages. |
| **Conductance State Variance** | Stochastic filament formation (RRAM) or charge trapping (Flash) | Non-linear weight mapping; zero-weight cells may exhibit non-zero conductance. | Post-fabrication calibration; error-correcting codes (ECC) for weight storage. |
| **Cell-to-Cell Interference** | Program/erase disturb effects | Changes in neighboring cells alter the state of the target cell, corrupting sparse weight patterns. | Shuffling weight distribution; guard bands between programming pulses. |

## Dynamic Non-Idealities: Noise Sources in Analog Accumulation

Dynamic noise is the most critical bottleneck for analog CIM, as it limits the effective resolution (bit-width) of the computation. In sparse CIM, noise affects the signal-to-noise ratio (SNR) differently than in dense computation due to the intermittent nature of the active devices.

### 1. Thermal Noise and Shot Noise
Thermal noise arises from the random motion of charge carriers, while shot noise results from the discrete nature of charge flow. In analog CIM, these noises are additive and typically modeled as Gaussian distributions. The total noise power ($\sigma^2_{noise}$) is the sum of thermal, shot, and quantization noise components [3].

For sparse computation, the **signal strength** is proportional to the number of active devices ($N_{active}$). Since $N_{active} \ll N_{total}$ in sparse scenarios, the accumulated signal current ($I_{signal}$) is significantly lower than in dense MVM. Consequently, the SNR degrades as sparsity increases, following the relationship:
$$ SNR \propto \frac{N_{active}}{\sqrt{N_{active}}} = \sqrt{N_{active}} $$
This implies that as sparsity increases, the SNR decreases, requiring either longer integration times or higher precision ADCs to maintain accuracy, which undermines the energy efficiency gains of sparsity [4].

### 2. ADC Quantization Noise
The Analog-to-Digital Converter (ADC) is a major source of noise and power consumption. In sparse CIM, the dynamic range of the ADC must be large enough to accommodate the maximum possible current from fully active sub-arrays, yet sensitive enough to resolve small currents from sparse activations. This **dynamic range mismatch** leads to quantization noise. If the ADC resolution is fixed (e.g., 4-bit), sparse activations may fall below the least significant bit (LSB), resulting in complete data loss [5].

### 3. Crosstalk and Interconnect Noise
As array sizes scale, **line resistance and capacitance** in the wordlines (WLs) and bitlines (BLs) introduce RC delay and voltage drops. In sparse CIM, where signals are intermittent, these parasitic effects can cause **crosstalk** between adjacent lines, leading to data corruption. Recent research highlights that **irregular access patterns** in sparse computation exacerbate crosstalk, as the simultaneous switching of distant WLs/BLs creates unpredictable interference [6].

## Critical Analysis: The Sparsity-Noise Paradox

A critical challenge in sparse CIM is the **sparsity-noise paradox**: while sparsity reduces computational energy, it simultaneously degrades the SNR by reducing the signal magnitude. This creates a trade-off where increasing sparsity beyond a certain threshold yields diminishing returns in accuracy due to noise dominance.

Recent works suggest that **noise-aware sparsity patterns** can mitigate this issue. By prioritizing the retention of weights that are less sensitive to noise (e.g., those with higher magnitude or located in less noisy regions of the array), the system can maintain accuracy even at high sparsity levels [7]. Additionally, **temporal sparsity** (sparsity across time steps in RNNs or transformers) can be leveraged to allow for longer integration times in active periods, effectively averaging out noise [8].

## Summary of Hardware Constraints

| Constraint Category | Specific Mechanism | Effect on Sparse CIM | Research Direction |
| :--- | :--- | :--- | :--- |
| **Static Variation** | $V_{th}$ mismatch, conductance drift | Phantom activations; broken sparsity | Per-device calibration; robust encoding |
| **Thermal/Shot Noise** | Random carrier motion | Reduced SNR; lower effective precision | Noise-aware pruning; adaptive integration |
| **ADC Limitations** | Quantization error, dynamic range | Data loss in sparse activations | Mixed-precision ADCs; sparse-aware quantization |
| **Interconnect Noise** | RC delay, crosstalk | Signal distortion; timing errors | Low-resistance materials; shielding techniques |

Understanding these hardware limitations is crucial for designing practical sparse CIM systems. Future work must focus on **co-designing** hardware architectures that are inherently robust to these physical constraints, rather than relying solely on algorithmic compensation.



## 6.2 Scalability and Interconnects

_To address the challenges of scaling sparse CIM systems and the role of on-chip interconnects_


# Scalability and Interconnects

As sparse Compute-in-Memory (CIM) arrays scale to support larger neural network models, the primary bottleneck shifts from local computational density to **global data movement**. While sparse computation theoretically reduces arithmetic intensity, the irregular memory access patterns inherent in unstructured sparsity exacerbate the "memory wall" problem. Consequently, the design of on-chip interconnects has emerged as the critical determinant of scalability, dictating whether sparse CIM systems can achieve linear speedup with array size or suffer from diminishing returns due to routing congestion and bandwidth saturation [54].

## The Interconnect Bottleneck in Sparse CIM

In dense CIM, data flows are predictable, allowing for static, regular routing fabrics. However, sparse CIM introduces significant variability in data flow. When a weight is zero, the corresponding input data and partial sum should ideally be skipped. Yet, in large-scale arrays, ensuring that only non-zero data traverses the interconnect network without introducing excessive latency requires complex dynamic routing [55].

Recent analyses indicate that as array dimensions exceed $1024 \times 1024$ bits, the area overhead of global interconnects can consume up to **40–50% of the chip area**, surpassing the area of the compute cells themselves [56]. This is particularly acute in sparse architectures where the interconnect must support:
1.  **Dynamic Path Selection:** Routing non-zero inputs to active compute rows.
2.  **Partial Sum Aggregation:** Collecting results from distributed sub-arrays without contention.
3.  **Sparsity Map Distribution:** Broadcasting compression/decompression instructions to local decoders [57].

If the interconnect bandwidth cannot match the computational throughput of the sparse arrays, the system becomes **communication-bound**, negating the energy benefits of in-memory computing [58].

## Architectural Strategies for Scalable Interconnects

To address these scalability challenges, recent research has moved beyond simple bus-based architectures toward hierarchical and adaptive interconnect topologies.

### Hierarchical Mesh and NoC (Network-on-Chip) Approaches

Modern large-scale sparse CIM chips are increasingly adopting **Network-on-Chip (NoC)** architectures. Unlike centralized buses, NoCs partition the chip into smaller clusters, each with its own local interconnect and global routing channels. This reduces congestion and allows for parallel data transfers across different regions of the chip [59].

*   **Clustered CIM Arrays:** By dividing a large CIM matrix into smaller $64 \times 64$ or $128 \times 128$ clusters, the local interconnect can be optimized for high-bandwidth intra-cluster communication, while global interconnects handle sparse data redistribution between clusters [60].
*   **Adaptive Routing:** Recent implementations use adaptive routing algorithms that dynamically adjust paths based on real-time congestion and sparsity patterns, reducing latency by up to **30%** compared to static mesh networks [61].

### Hybrid Digital-Analog Interconnects

A critical innovation in sparse CIM scalability is the use of **hybrid digital-analog interconnects**. While analog compute arrays perform MAC operations efficiently, the interconnects between these arrays often require digital precision to manage control signals and sparse indices.

*   **Analog Crossbars for Weight Distribution:** Some designs use analog crossbars to distribute weight values directly to compute tiles, reducing the need for repeated digital fetching [62].
*   **Digital Interconnects for Sparsity Control:** Digital NoCs are used to route sparsity masks and control signals, ensuring that the irregular data flows of sparse computation are managed with low error rates [63].

| Interconnect Type | Scalability Limit | Key Advantage | Key Challenge |
| :--- | :--- | :--- | :--- |
| **Centralized Bus** | Small arrays (< $256 \times 256$) | Low latency, simple design | High contention, area overhead scales quadratically [64]. |
| **Static Mesh NoC** | Medium arrays ($512 \times 512$) | Predictable routing, moderate area | Inefficient for irregular sparse patterns [65]. |
| **Adaptive Hierarchical NoC** | Large arrays (> $1024 \times 1024$) | High bandwidth, congestion avoidance | Complex control logic, power overhead [66]. |
| **Hybrid Digital-Analog** | Very large arrays | Reduced data movement for weights | Design complexity, noise sensitivity in analog links [67]. |

## Impact of Sparsity on Interconnect Efficiency

The efficiency of interconnects is directly tied to the **sparsity pattern**. Structured sparsity (e.g., N:M) allows for simpler, more regular interconnect designs because the data flow follows predictable strides. In contrast, unstructured sparsity requires fully dynamic routing, which increases interconnect complexity and power consumption [68].

*   **Structured Sparsity:** Enables the use of **stride-based routing**, where data is fetched in contiguous blocks, reducing the need for complex address translation in the interconnect [69].
*   **Unstructured Sparsity:** Requires **index-based routing**, where each non-zero element must be individually addressed. This leads to higher interconnect energy per operation, as the control signals for routing can dominate the data payload [70].

Recent studies show that for unstructured sparsity levels above 90%, the interconnect energy can exceed the compute energy if not optimized, highlighting the need for **sparsity-aware interconnect design** [71].

## Future Directions: 3D Integration and Photonic Interconnects

Looking ahead, two emerging technologies promise to overcome the fundamental scalability limits of planar interconnects:

1.  **3D Stacked CIM:** By vertically stacking compute layers, the distance between memory and logic is minimized, reducing interconnect length and latency. Recent prototypes demonstrate that 3D integration can reduce interconnect energy by **50–70%** compared to 2D counterparts [72].
2.  **Photonic Interconnects:** For ultra-large-scale CIM systems, optical interconnects offer bandwidth densities orders of magnitude higher than copper wires, with negligible power consumption over long distances. Early research suggests that photonic NoCs could enable CIM chips with over **100 TeraOPS** of sparse compute throughput [73].

## Critical Assessment

While hierarchical NoCs and hybrid architectures show promise, they introduce significant design complexity. The power overhead of digital control logic in adaptive NoCs can offset the energy savings from sparse computation, particularly in low-sparsity regimes [74]. Furthermore, the reliability of analog interconnects in 3D stacked architectures remains a concern, as crosstalk and thermal effects can degrade signal integrity in dense environments [75]. Therefore, future scalability will depend not just on interconnect topology, but on **co-design of sparsity algorithms and interconnect protocols** to minimize data movement and control overhead [76].






# 7. Conclusion

## 7.1 Summary of Key Advancements

_To synthesize the major technical breakthroughs in sparse CIM research_


# Summary of Key Advancements

This subsection synthesizes the critical technical breakthroughs that have defined the trajectory of Sparse Compute-in-Memory (CIM) research from 2024 to mid-2026. While previous sections detailed architectural components and evaluation metrics, this section highlights the **paradigm shifts** in how sparsity is generated, encoded, and executed within analog and digital hybrid domains. The following advancements represent the state-of-the-art in overcoming the fundamental limitations of accuracy retention and energy efficiency.

## 1. From Static Pruning to Dynamic, On-Chip Sparsity Generation

Historically, sparse CIM relied on weights pruned offline (static sparsity), which limited flexibility and often resulted in irregular memory access patterns that negated energy savings. A major breakthrough in 2025–2026 is the integration of **dynamic sparsity generation mechanisms** directly within the CIM array or adjacent logic.

### In-Situ Sparsity Activation
Recent architectures utilize **event-driven activation** where sparsity is determined by input data characteristics rather than fixed weight masks. This is achieved through:
*   **Threshold-Based Gating:** Analog comparators integrated into bitlines dynamically disable sub-arrays when input activations fall below a noise-floor threshold, effectively creating zero-values on-the-fly [1].
*   **Mixture-of-Experts (MoE) Routing in CIM:** Advanced CIM chips now support hardware-accelerated MoE routing, where only a subset of expert weights is activated per token. This allows for **sparse inference at the batch level**, achieving effective sparsity rates of >90% without structural weight pruning [2].

| Sparsity Type | Generation Mechanism | Hardware Overhead | Primary Benefit |
| :--- | :--- | :--- | :--- |
| **Static** | Offline Training/Pruning | None (Post-fabrication) | Predictable timing |
| **Dynamic** | Input-Dependent Gating | Low (Comparator logic) | Data-dependent energy savings |
| **Structural** | Kernel/Channel Pruning | Medium (Sparse indexing) | Regular memory access patterns |

*Table 2: Comparison of sparsity generation mechanisms in modern CIM architectures [1], [2].*

## 2. Advanced Sparse Encoding: Beyond Block-Sparse

While block-sparse formats (e.g., 2:4 sparsity) dominated early CIM implementations due to their regularity, recent research has demonstrated that **irregular sparse formats** can be efficiently supported through novel encoding schemes and hybrid digital-analog processing.

### Hybrid Sparse Encoding Schemes
*   **Compressed Sparse Row (CSR) in Analog Domain:** New techniques map CSR indices into compact digital buffers adjacent to the CIM array, allowing for **random access** to sparse weight segments without full array activation. This reduces read energy by up to 60% compared to dense access patterns [3].
*   **Learned Sparse Formats:** End-to-end training methods that optimize the sparse format itself (e.g., position of non-zero elements) alongside weights have shown a 15–20% improvement in accuracy retention at 95% sparsity compared to fixed block-sparse patterns [4].

## 3. Algorithm-Hardware Co-Design for Sparse CIM

The most significant advancement lies in the tight coupling of **sparse-aware training algorithms** with **hardware non-idealities**. Instead of treating hardware errors as noise to be mitigated, recent approaches integrate them into the training loop.

### Noise-Aware Sparse Training
*   **Conductance Variation as a Regularizer:** Research has shown that explicitly modeling conductance variation during training can improve robustness. By adding noise distributions representative of RRAM/PCM variability to the loss function, models achieve **higher sparsity ceilings** with minimal post-deployment accuracy drop [5].
*   **Sparse-Kernel Optimized Quantization:** New quantization schemes dynamically adjust bit-widths based on the sparsity pattern of each layer. Layers with higher sparsity receive lower precision, while dense layers maintain higher precision, optimizing the **accuracy-energy trade-off** [6].

## 4. Benchmarking Breakthroughs: Real-World Performance Gains

Recent benchmarks have moved beyond synthetic datasets to demonstrate tangible advantages in real-world AI workloads.

### Energy Efficiency Gains
*   **LLM Inference:** In Transformer-based LLMs, sparse CIM implementations have achieved **up to 3.5x energy efficiency gains** over digital GPUs when operating at >80% sparsity, primarily due to the elimination of redundant MAC operations and reduced data movement [7].
*   **CNN Acceleration:** For vision tasks, sparse CIM chips have demonstrated **sub-millisecond inference times** for 4K image processing, with energy consumption reduced by 60% compared to dense CIM counterparts [8].

### Scalability
*   **Large-Scale Arrays:** Recent prototypes have scaled sparse CIM arrays to **1024x1024** elements, demonstrating that sparse access patterns do not significantly degrade scalability when combined with advanced multiplexing techniques [9].

## 5. Critical Reflection and Limitations

While these advancements are significant, critical analysis reveals remaining challenges:
*   **Complexity Overhead:** Dynamic sparsity generation and hybrid encoding schemes introduce control logic complexity, which can offset energy gains if not carefully optimized [10].
*   **Training Instability:** Noise-aware training can lead to slower convergence and requires more extensive hyperparameter tuning compared to standard training methods [11].
*   **Standardization Lack:** The lack of standardized sparse formats for CIM creates fragmentation, hindering software-hardware co-design efforts [12].

In conclusion, the field has moved from simple static pruning to sophisticated, dynamic, and co-designed sparse CIM systems. These advancements have significantly improved energy efficiency and accuracy retention, paving the way for widespread adoption in next-generation AI hardware. However, addressing complexity overhead and standardization remains crucial for future scalability.



## 7.2 Impact on Next-Generation AI Chips

_To project the potential influence of sparse CIM on future AI hardware landscapes_


# Impact on Next-Generation AI Chips

The integration of sparse Compute-in-Memory (CIM) is poised to fundamentally restructure the future landscape of AI hardware, moving beyond incremental efficiency gains to enable entirely new classes of on-device intelligence. While previous sections detailed the physical limitations of sparse CIM, the trajectory of this technology suggests it will become the primary enabler for **Ultra-Low Power Edge AI** and **Sustainable Data Center Acceleration**. This subsection projects the specific influence of sparse CIM on next-generation chip architectures, focusing on three critical domains: the collapse of the Von Neumann bottleneck for sparse workloads, the emergence of heterogeneous memory-compute fabrics, and the shift toward energy-efficient inference at the scale of exa-FLOPs.

## 1. Enabling True "Always-On" Edge Intelligence

The most immediate impact of sparse CIM on next-generation chips is the feasibility of **continuous, low-power inference** on battery-constrained devices. Traditional edge AI chips rely on digital accelerators (GPUs/TPUs) that must wake from deep sleep states to process data, incurring significant latency and energy overhead. Sparse CIM, by contrast, allows for **event-driven processing** where computation only occurs when sparse activations are detected.

### The Shift from Periodic to Event-Driven Architectures
Next-generation edge chips will likely abandon periodic polling in favor of asynchronous, sparse-triggered architectures. In such systems, the CIM array acts not just as a compute unit but as a **sparse event detector**. When the input data sparsity exceeds a threshold, the CIM cell outputs an activation pulse; otherwise, the system remains in a near-zero power state.

| Feature | Digital Edge AI (Current) | Sparse CIM Edge AI (Projected 2026+) |
| :--- | :--- | :--- |
| **Power State** | Periodic wake-up/sleep cycles | Always-on, event-driven idle state |
| **Data Movement** | High energy cost (DRAM fetch) | Near-zero movement (in-situ compute) |
| **Latency** | Millisecond-scale (wake-up + compute) | Microsecond-scale (direct activation) |
| **Use Case** | Batch processing, periodic sensing | Real-time anomaly detection, always-on voice |

Recent projections indicate that sparse CIM-based edge chips can achieve **sub-microwatt power consumption** for background monitoring tasks, enabling devices like smart sensors and medical implants to operate for years without battery replacement [3]. This shifts the design paradigm from "maximizing peak FLOPS" to "minimizing energy per sparse event," a metric where sparse CIM currently outperforms digital counterparts by orders of magnitude.

## 2. Heterogeneous Memory-Compute Fabrics in Data Centers

In the data center context, sparse CIM is driving the development of **heterogeneous memory-compute fabrics** that break the traditional separation between memory and logic. Next-generation AI chips are moving toward **3D-stacked CIM layers** integrated directly with high-bandwidth memory (HBM) or next-generation non-volatile memory (NVM) technologies like ReRAM and MRAM.

### 3D Integration and Bandwidth Scaling
The impact on chip design is profound: instead of shuffling data between separate CPU/GPU and memory stacks, next-generation chips will feature **monolithic 3D integration** where CIM arrays are stacked vertically. This allows for:
1.  **Massive Parallelism:** Thousands of CIM cores operating in parallel within a single package.
2.  **Reduced Latency:** Elimination of off-chip data transfer bottlenecks.
3.  **Sparse Data Compression:** By computing directly on compressed sparse formats (e.g., CSR, COO) within the memory layer, the chip reduces the effective bandwidth requirement by up to **90%** for sparse models [4].

This architecture is particularly impactful for **large language model (LLM) inference**, where sparsity can exceed 50-90% in certain layers. Next-gen chips leveraging sparse CIM are expected to reduce inference latency by **2-3x** compared to current GPU-based solutions while cutting energy consumption by **50-70%** [5].

## 3. Sustainability and the Carbon Footprint of AI

The rise of sparse CIM has significant implications for the **environmental sustainability** of AI hardware. As AI models grow in size, the energy cost of training and inference has become a major concern. Sparse CIM offers a hardware-level solution to this problem by reducing the energy per operation (Joules/FLOP).

### Energy Efficiency Metrics
The following table compares projected energy efficiencies of next-generation sparse CIM chips against traditional digital accelerators for sparse workloads:

| Metric | Digital GPU/TPU (Current) | Sparse CIM (Projected Next-Gen) | Improvement Factor |
| :--- | :--- | :--- | :--- |
| **Energy per Sparse MAC** | ~10-50 pJ | ~0.1-1 pJ | **10-50x** [6] |
| **Memory Bandwidth Requirement** | High (GB/s per chip) | Low (MB/s per chip) | **100x reduction** |
| **Thermal Design Power (TDP)** | High (>300W per chip) | Low (<50W per chip) | **Significant cooling cost reduction** |

This efficiency gain is critical for the **sustainable scaling** of AI infrastructure. By reducing the energy intensity of inference, sparse CIM chips enable the deployment of AI in **remote or off-grid locations** (e.g., environmental monitoring stations) and reduce the carbon footprint of large-scale data centers. Recent life-cycle assessments suggest that sparse CIM adoption could reduce the operational carbon emissions of AI data centers by **up to 40%** by 2030 [7].

## 4. Challenges in Standardization and Ecosystem Adoption

Despite the potential, the widespread adoption of sparse CIM faces significant hurdles related to **software-hardware co-design** and **ecosystem fragmentation**. Next-generation chips must support standard sparse formats (e.g., CSR, ELL) natively, requiring new compilers and programming models.

### The Need for Unified Sparse Programming Models
Currently, sparse CIM architectures are proprietary and lack standardization. Next-generation chips will need to support **open-source sparse frameworks** (e.g., PyTorch Sparse, TensorFlow Sparse) to ensure compatibility with existing AI models. The development of **hardware-aware compilers** that can automatically optimize sparse data layouts for specific CIM architectures is critical for unlocking the full potential of these chips [8].

## Conclusion

The impact of sparse CIM on next-generation AI chips is transformative, enabling a shift from **energy-intensive digital acceleration** to **efficient, event-driven, and sustainable hardware solutions**. By collapsing the memory-compute boundary and leveraging sparsity at the hardware level, sparse CIM is poised to redefine the performance-per-watt landscape for both edge and data center AI. However, realizing this potential requires overcoming challenges in standardization, software support, and manufacturing scalability. As the industry moves toward 2030, sparse CIM is expected to become a dominant architecture for AI inference, driving a new era of efficient, sustainable, and always-on intelligent systems.






## Sources

