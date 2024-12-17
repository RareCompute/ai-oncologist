# Agent-3: The Oncologist

![](https://i.postimg.cc/76gnPSs2/Clean-Shot-2024-12-16-at-16-09-16-2x.png)

## Overview

**Agent-3: The Oncologist** is designed to serve as the domain-specialized expert within the Decentralized AI-Oncologist pipeline. It receives as input:

1. A set of high-relevance paragraphs surfaced by **Agent-2 (The Paper Reader)**, which focus on proteins, molecular features, or structural insights related to an oncology target.
2. A target-specific knowledge sub-graph prompt—this includes structured information (e.g., ontologies, known protein-ligand interactions, patient mutation data) that enriches the agent’s contextual understanding.

Armed with these inputs, Agent-3 uses a large, domain-specific LLM (RLHF fine-tuned with direct oncologist feedback) to produce two key outputs:

1. **A Protein Generation Prompt:** A carefully crafted natural language directive intended for **Agent-4 (The Molecular Designer)**, guiding it on how to generate a novel protein structure aligned with the oncological context.
   
2. **A Domain Summary:** A concise, context-rich narrative that describes the target protein, its oncological relevance, mechanism of interest, and the purpose or hypothesis driving the protein’s design. This summary helps researchers and collaborators understand the rationale behind the generated protein.

## Purpose and Function

- **Goal:** Transform unstructured insights (relevant paragraphs and knowledge graphs) into a precise experimental blueprint for protein design.
- **Approach:**  
  - Digest and integrate biomedical paragraphs from Agent-2 along with a structured knowledge sub-graph related to the target.  
  - Synthesize these into:  
    - A generation prompt that provides Agent-4 with all the necessary molecular details to produce a PDB structure or a protein engineering candidate.  
    - A summary explanation that contextualizes the chosen protein’s role in oncology, its structural considerations, and intended docking or functional tests.
- **Context:** Agent-3 acts as a domain expert, leveraging RLHF tuning to ensure output is not only scientifically robust, but also aligned with expert oncologists’ expectations.

## Example Data Structures

### Input Structure

```json
{
  "relevant_paragraphs": [
    {
      "paper_id": "PMC123456",
      "title": "Study on Protein Domain Y in Pancreatic Oncology",
      "paragraph_text": "This domain interacts with oncogene X, influencing tumor growth rates..."
    },
    {
      "paper_id": "PMC789012",
      "title": "Targeting Oncogene X in Pancreatic Cancer",
      "paragraph_text": "Small molecules can modulate the domain Y interface, reducing cancer proliferation..."
    }
  ],
  "knowledge_subgraph": {
    "target_ontology": {
      "disease": "Pancreatic Cancer",
      "oncogene": "X",
      "key_protein_domain": "Domain Y",
      "known_mutations": ["Y135F", "K210T"],
      "ligand_binding_residues": ["R45", "E79"]
    }
  }
}
```
* **relevant_paragraphs:** Curated text snippets referencing key protein interactions.
* **knowledge_subgraph:** A structured representation of the target scenario, including disease context, oncogene details, protein domains, known mutations, and relevant binding sites.

* ## Output Structure
```json
{
  "protein_generation_prompt": {
    "instructions": "Design a protein variant that binds domain Y of oncogene X in pancreatic cancer cells, leveraging known ligand-binding residues (R45, E79) to enhance affinity. Include stabilizing mutations (e.g., Y135F) to maintain structural integrity, and ensure the resulting protein modulates oncogene X activity.",
    "target_protein_features": {
      "target_oncogene": "X",
      "binding_domain": "Y",
      "desired_affinity": "High",
      "stabilizing_mutations": ["Y135F"]
    }
  },
  "domain_summary": {
    "description": "The protein of interest targets domain Y in oncogene X, associated with pancreatic cancer progression. By modulating this domain’s interface, the engineered protein aims to disrupt downstream signaling pathways. Incorporating residues R45 and E79 into the binding interface and including stabilizing mutations like Y135F can enhance binding affinity and maintain a structurally stable conformation. The ultimate goal is to produce a candidate protein that could inhibit oncogene-driven tumor growth."
  },
  "metadata": {
    "model_used": "Llama-XXL-Oncology-RLHF",
    "timestamp": "2024-12-16T14:00:00Z"
  }
}
```

* **protein_generation_prompt:** A tailored instruction set for Agent-4, encapsulating all structural and functional targets.
* **domain_summary:** Contextual narrative summarizing the rationale, objectives, and significance of the protein design.

## Example Usage
* **Scenario:** A researcher is investigating how domain Y of oncogene X influences pancreatic tumor growth. Agent-2 provides paragraphs mentioning ligand-binding residues and stabilizing mutations. The knowledge sub-graph offers structured details about relevant mutations and the disease context.

  1. **Input:** Agent-3 receives relevant paragraphs and the knowledge sub-graph.
  2. **Agent-3 Action:**
    * Integrates text and structured data.
    * Identifies key residues and mutations relevant for stabilizing protein structure and achieving desired docking outcomes.
    * Produces a prompt instructing Agent-4 on how to generate a high-affinity binding protein.
    * Summarizes the domain’s importance and how the designed protein could modulate oncogene activity.
  3. Output:
    * A precise protein design prompt plus an explanatory domain summary for human researchers. 

## Model Summary
* **Model:** A large LLM (e.g., Llama-XXL variant, ~40B parameters), RLHF fine-tuned with oncologist feedback.
* **Use Case:** Translating biomedical insights into actionable protein engineering instructions.
* **Prompting Strategy:** The model is guided by domain-specific prompts and RLHF adjustments, ensuring that outputs are medically credible, biologically plausible, and aligned with expert priorities.

## RLHF and Tuning Inputs

* **RLHF (Reinforcement Learning from Human Feedback):**
  * Oncologists and domain experts evaluate the outputs, refining instructions for clarity, accuracy, and real-world applicability.
  * This iterative feedback loop ensures the model’s prompts and summaries are aligned with the needs of medical researchers.

* **Tuning & Prompting:**
  * Fine-tuned on a curated dataset of protein engineering literature, clinical oncology reports, and experiment design cases.
  * Prompts highlight the need for biologically meaningful structures, clear therapeutic goals, and feasibility in downstream docking experiments.

* **RAG Configuration:**
  * Retrieval components can feed specialized knowledge about known inhibitors, protein-ligand interactions, and mutation impact data.
  * Adjusting retrieval parameters over time maintains optimal relevance and granularity of the provided instructions.

* **Expert Input:**
  * Continuous guidance from oncologists, computational chemists, and protein engineers ensures the model is always producing scientifically sound and practically useful outputs.

Deployment Configuration and Model Details

The config.yaml file in this directory provides:
* Model endpoints and inference resource settings
* Integration parameters for RLHF loops and feedback channels
* Detailed logging and monitoring for traceability
