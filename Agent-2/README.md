# Agent-2: The Paper Reader

*(Placeholder for agent topology diagram highlighting Agent-2)*

## Overview

**Agent-2: The Paper Reader** is the second step in the Decentralized AI-Oncologist pipeline. Its core function is to process the documents retrieved by **Agent-1 (The Search Agent)** at a finer granularity—examining each paper paragraph-by-paragraph. The goal is to identify textual segments that potentially describe proteins, molecules, or structural features relevant to the target disease context discovered in the literature.

By using a specialized LLM (a Llama3 7B model with subject-specific fine tuning), Agent-2 filters out extraneous information and pinpoints the high-impact paragraphs. This distilled set of paragraphs is then passed on to **Agent-3 (The Oncologist)** for more informed downstream reasoning and experiment design.

## Purpose and Function

- **Goal:** Extract paragraphs from a set of candidate papers that contain scientifically relevant molecular or protein information tied to the oncology target.
- **Approach:**  
  - Iteratively read through each paragraph of each paper provided by Agent-1.  
  - Use an LLM-based scoring prompt to determine if the paragraph likely mentions a protein or molecular feature relevant to the target.  
  - Rank or threshold paragraphs to produce a subset of highly relevant content for the next agent.
- **Context:** Agent-2 acts as a precision filter, removing irrelevant textual information and ensuring only paragraphs with a high likelihood of pertinent molecular data are forwarded.

## Example Data Structures

### Input Structure

```json
{
  "retrieved_papers": [
    {
      "title": "Study on Protein Domain Y in Pancreatic Oncology",
      "paper_id": "PMC123456",
      "paragraphs": [
        "Paragraph 1 text ...",
        "Paragraph 2 text ...",
        "Paragraph 3 text ...",
        "... and so forth ..."
      ]
    },
    {
      "title": "Targeting Oncogene X in Pancreatic Cancer",
      "paper_id": "PMC789012",
      "paragraphs": [
        "Paragraph 1 text ...",
        "Paragraph 2 text ...",
        "Paragraph 3 text ...",
        "... and so forth ..."
      ]
    }
  ],
  "target_terms": ["oncogene X", "protein domain Y"]
}
```

### Output Structure
```json
{
  "relevant_paragraphs": [
    {
      "paper_id": "PMC123456",
      "title": "Study on Protein Domain Y in Pancreatic Oncology",
      "paragraph_text": "Paragraph 2 text ...",
      "relevance_score": 0.87,
      "reasoning_summary": "This paragraph discusses a protein domain related to oncogene X."
    },
    {
      "paper_id": "PMC789012",
      "title": "Targeting Oncogene X in Pancreatic Cancer",
      "paragraph_text": "Paragraph 3 text ...",
      "relevance_score": 0.92,
      "reasoning_summary": "Mentions a molecule inhibiting the oncogenic protein domain of interest."
    }
  ],
  "metadata": {
    "processing_time": "2024-12-16T12:30:00Z",
    "model_used": "Llama3-7B-FT",
    "filtering_threshold": 0.85
  }
}
```

### Example Usage

**Scenario:** From the papers retrieved by Agent-1, Agent-2 must locate paragraphs that actually mention the protein domain of interest.

* **Input:** The set of papers from Agent-1, which may number in the hundreds.
* Agent-2 Action:
    * The Llama3 7B model, fine-tuned for biomedical content, reads each paragraph and applies a scoring mechanism.
    * If the paragraph likely describes a protein relevant to the target oncology domain (e.g., containing structural details, known mutations, or therapeutic relevance), it is flagged.
    * Output: A curated list of only those paragraphs that meet the relevance threshold, ensuring Agent-3 receives high-quality, context-rich content to design experiments upon.

### Model Summary
* **Model:** Llama3 7B (Fine-Tuned on Biomedical Text)
* **Use Case:** Paragraph-level semantic filtering for molecular/protein relevance.
* **Prompting Strategy:**
* The prompt emphasizes domain-specific terminology, instructing the model to look for mentions of proteins, binding sites, molecular structures, and relevant pathways.
* Input/Output:
    * Input: Paragraph text + target terms
    * Output: Probability or score indicating if the paragraph is relevant

### RLHF and Tuning Inputs

* RLHF (Reinforcement Learning from Human Feedback):
    * Oncology experts and protein chemists review model outputs, labeling correct vs. incorrect relevance judgments.
    * Feedback is incorporated to refine future fine-tuning rounds, ensuring the model improves at identifying meaningful molecular data.

* Tuning & Prompting:
    * Additional domain-specific corpora (e.g., curated sets of paragraphs known to describe proteins) can be used to improve accuracy.
    * Custom prompts highlighting "desired molecular details" can further guide the model.

* RAG Configuration:
    * While Agent-2 primarily focuses on paragraph-level content, it may still query vector indices or use a small retrieval subset if needed to refine judgments.
    * Thresholds (like the relevance_score cutoff) can be tuned over time with expert input.

* Expert Input:
    * Oncologists and biochemists help define what constitutes a “relevant paragraph” by providing annotated data, improving the system’s understanding of relevancy criteria.

### Deployment Configuration and Model Details

The config.yaml file in this directory provides details on deploying this agent, including:
* Model endpoints and GPU/CPU resource requirements
* Environment variables for secure API access
* Threshold values for paragraph relevance scoring
* Integration points for logging and monitoring
