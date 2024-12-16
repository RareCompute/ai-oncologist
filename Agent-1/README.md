# Agent-1: The Search Agent

(Placeholder for agent topology diagram highlighting Agent-1)

## Overview
Agent-1: The Search Agent is the entry point into the Decentralized AI-Oncologist pipeline. Its primary purpose is to perform a targeted literature search over a large corpus of oncology-related documents. By leveraging semantic search techniques and Retrieval Augmented Generation (RAG), this agent identifies a set of papers or excerpts most likely relevant to the oncology target in question.

The key idea is that Agent-1 transforms a user-defined knowledge graph of search terms or concepts into a narrowed-down collection of highly relevant biomedical articles. These results are then passed along to the downstream agents, enabling more focused analysis on specific protein-related paragraphs, target identification, and subsequent protein design.

## Purpose and Function:
* Goal: Surface and refine a set of oncology research papers from a vast corpus, ensuring that subsequent agents in the chain focus on meaningful, context-rich data.
* Approach: Utilize semantic search over a large dataset (e.g., PubMed abstracts, proprietary cancer research databases). This may involve vector-based search, ontology-based filtering, or a hybrid RAG approach.
* Context: Agent-1 is the first step, ensuring that the entire pipeline downstream is guided by relevant and up-to-date scientific literature.

## Example Data Structures

### Input Structure
```json
{
  "knowledge_graph_terms": [
    "oncogene X",
    "protein folding mechanism Y",
    "pancreatic cancer target Z"
  ],
  "additional_constraints": {
    "publication_date_range": "2018-2023",
    "required_keywords": ["therapeutic target", "protein domain"]
  }
}
```
* knowledge_graph_terms: An array of search terms derived from a knowledge graph or domain expert input.
* additional_constraints: Optional filters to restrict the search space (e.g., date, keywords).

### Output Structure
```json
{
  "retrieved_papers": [
    {
      "title": "Study on Protein Domain Y in Pancreatic Oncology",
      "abstract": "This paper discusses the folding mechanism of domain Y ...",
      "paper_id": "PMC123456",
      "link": "https://.../PMC123456",
      "relevance_score": 0.92
    },
    {
      "title": "Targeting Oncogene X in Pancreatic Cancer",
      "abstract": "Our research examines the role of oncogene X ...",
      "paper_id": "PMC789012",
      "link": "https://.../PMC789012",
      "relevance_score": 0.88
    }
  ],
  "metadata": {
    "search_terms_used": ["oncogene X", "protein folding mechanism Y", "pancreatic cancer target Z"],
    "query_time": "2024-12-16T12:00:00Z"
  }
}
```
* retrieved_papers: A ranked list of papers that match the search criteria. Each entry includes a title, abstract, identifier, and a relevance score.
* metadata: Logging and provenance information about how the search was conducted.

## Example Usage

**Scenario:** A researcher is interested in a new protein domain hypothesized to influence pancreatic cancer pathways. The knowledge graph terms might include the target protein domain name, the specific cancer type, and associated oncogenes.

* Input: The researcher provides a set of terms: “protein domain Y”, “pancreatic cancer”, and “oncogene X”.
* Agent-1 Action: The agent queries a large biomedical corpus, retrieving recent and relevant papers.
* Output: A curated set of papers highly related to these terms, which is then passed on to Agent-2 (The Paper Reader) for more detailed analysis.

## Model Summary (Placeholder)
**Model Type:** Placeholder - TBD
**Model Functionality:** Semantic search & RAG pipeline. This may involve:

* A vector database (e.g., FAISS or Pinecone) holding embeddings of oncology literature.
* A lightweight embedding model to convert search terms and documents into vectors.
* Potential integration with a commercial or open-source biomedical search API.
* **Note:** Exact model and parameters are pending selection based on performance evaluations.

## RLHF and Perf-Opt inputs
**RLHF**
* For Agent-1, RLHF might involve adjusting retrieval strategies based on user feedback or expert oncologist input. Human reviewers may rank search results for relevance, feeding back into the model’s search algorithm.

**Tuning & Prompting**
* If the agent uses a lightweight LLM to interpret search terms, the prompt might be tuned for biomedical literature queries.
* Additional fine-tuning data could consist of curated queries and relevance judgments from domain experts.

**RAG Configuration**
* Adjusting retrieval parameters such as top-k results, similarity thresholds, or filters for metadata fields (e.g., date, peer-review status) based on oncologist preferences or historical performance.

**Expert Input**
* Oncology experts, medical librarians, and bioinformatics specialists would be valuable in refining the search terms, choosing relevant corpora, and defining relevance criteria.

## Deployment Configuration and Model Details

For more information on how to deploy and configure this agent, refer to the accompanying config.yaml file. This YAML file includes placeholders for model endpoints, environment variables, indexing strategies, and integration points with downstream agents.
