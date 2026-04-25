# miRNA Target Predictor: Neural Biomarker Analysis
Python pipeline for identifying miR-124-3p target sites in neural 3' UTR sequences.

### Project Overview
This repository contains a Python-based bioinformatics pipeline designed to identify microRNA binding sites within specific genomic regions. The project demonstrates the identification of **miR-124-3p** targets within the 3' UTR of neural-specific genes.

### Biological Context
In neurobiology and liquid biopsy research, **miR-124-3p** is a critical biomarker for neuronal differentiation. This tool maps its 7mer-m8 seed sequence to mRNA transcripts to predict regulatory networks.

### Features
* **FASTA Parsing:** Efficiently processes multi-line genomic sequences from Ensembl BioMart.
* **Deduplication:** Automatically filters isoforms to identify unique gene targets.
* **GC Content Analysis:** Calculates the thermodynamic stability of predicted binding sites.

### Key Results
Using a dataset of neural transcripts, the pipeline successfully identified canonical targets:
- **BDNF** (Brain-Derived Neurotrophic Factor)
- **IL1R1** (Interleukin-1 Receptor)
- **Average Binding Site GC Content:** 50.00%

### Technical Stack
* Python 3.x
* Data Source: Ensembl BioMart (GRCh38.p14)
