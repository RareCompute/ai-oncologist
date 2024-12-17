# ai-oncologist

Decentralized AI-Oncologist

Welcome to the Decentralized AI-Oncologist, a four-agent, chain-of-command AI system designed to support novel compound and protein discovery for precision oncology. 

This system leverages recent advancements in Large Language Models (LLMs), Retrieval Augmented Generation (RAG), and generative protein modeling (e.g., diffusion-based text-to-protein models) to streamline research and development workflows in oncology-related target discovery, protein engineering, and molecular docking experimentation.

High-Level Concept

In modern oncology research, identifying promising protein targets, understanding their structural nuances, and generating candidate compounds to interact with these targets is a labor-intensive process. 

The Decentralized AI-Oncologist aims to accelerate this discovery pipeline through a modular, automated, and highly specialized chain of AI agents. Each agent focuses on a particular stage of the discovery process, from literature search to protein generation.

Key Objectives:

    1.    Scalable Literature Review: Rapidly discover and extract critical scientific information relevant to a target oncology protein from vast biomedical corpora.

    2.    Expert Knowledge Encoding: Incorporate oncology and protein engineering expertise through fine-tuned LLMs that highlight relevant biological targets and produce prompt structures for protein generation.

    3.    Automated Protein Design: Utilize advanced text-to-protein diffusion models to generate candidate proteins for docking, screening, and further in-silico experiments.

    4.    Decentralized Topology: Each agent operates as a distinct node with a clearly defined role, inputs, and outputs, enabling flexible integration, parallel development, and modular upgrades.

The Four-Agent Chain

![](https://i.postimg.cc/76gnPSs2/Clean-Shot-2024-12-16-at-16-09-16-2x.png)

The system is divided into four primary agents, each with a specialized role:

    1.    Agent-1: The Search Agent
    •    Role: Perform semantic search and RAG over large oncology paper datasets.
    •    Input: Knowledge graph of search terms, oncology concepts, or protein identifiers.
    •    Output: A curated set of relevant scientific papers or excerpts related to the target concept.

    2.    Agent-2: The Paper Reader
    •    Role: Given a set of papers from Agent-1, identify paragraphs with a high likelihood of describing or discussing proteins relevant to the oncology target.
    •    Model Type: A specialized Llama3 7B model, fine-tuned on biomedical corpora and guided with targeted prompts.
    •    Output: A distilled set of high-relevance paragraphs, each ranked and annotated.

    3.    Agent-3: The Oncologist
    •    Role: Ingests the high-relevance paragraphs and utilizes advanced LLM reasoning (a fine-tuned Llama 40B model with oncology domain RAG) to craft a text-based prompt describing the protein engineering task.
    •    Output: A detailed experiment design, specifying the protein or molecule of interest, and instructions for docking studies (e.g., “Generate a protein with X characteristics, then test its docking against target Y”).

    4.    Agent-4: The Molecular Designer
    •    Role: Apply a text-to-protein diffusion model to generate a PDB file of the requested protein. Integrate this with the experiment design and submit the result to a distributed molecular docking simulation platform.
    •    Output: A generated protein structure (PDB file) and the corresponding docking simulation job submission.

    Architecture and Data Flow

Step-by-step Process:

    1.    Agent-1 (Search): Takes in user-defined or automatically generated search terms from a knowledge graph. It queries a large dataset of biomedical literature and returns papers likely containing relevant target information.

    2.    Agent-2 (Reader): Processes these papers paragraph-by-paragraph, selecting only those with the highest potential relevance to the oncological target’s protein structure or function.

    3.    Agent-3 (Oncologist): Takes the selected paragraphs and, using domain-specific knowledge, designs an experiment: formulating a prompt for protein generation and specifying docking targets.

    4.    Agent-4 (Designer): Transforms the prompt into a protein structure via diffusion-based text-to-protein modeling, prepares a PDB output, and initiates docking simulations against the oncology target.

Intended Users

    •    Oncologists & Cancer Researchers: Quickly surface and organize relevant literature, generate novel protein candidates, and plan experiments.

    •    Bioinformaticians & Computational Biologists: Integrate customized workflows, adapt fine-tuned models, and incorporate evolving biomedical datasets.

    •    Software & ML Engineers: Contribute to the modular codebase, optimize deployment on cloud platforms, and integrate new tools or models.

Example Use Case

    1.    Input: A newly discovered oncogenic pathway in pancreatic cancer that involves a poorly characterized protein domain.

    2.    Agent-1 Search: Uses a knowledge graph of related terms to find recent papers discussing that protein domain.

    3.    Agent-2 Reader: Identifies paragraphs from those papers that likely describe structural features of that protein.

    4.    Agent-3 Oncologist: Based on these high-relevance paragraphs, it crafts a prompt: “Design a protein with binding capability to domain X, tuned for high affinity docking against the pancreatic onco-target.”

    5.    Agent-4 Designer: Produces a novel protein structure and sets it up for docking simulations, returning experimental parameters and a PDB file for further analysis.

Repository Structure

The repository is organized into directories reflecting each agent’s functionality and data flow. Each agent’s directory includes:

    •    A README.md explaining the agent’s purpose, model selection, tuning strategies, I/O data structures, and agent-specific instructions.
    •    A .yaml configuration file containing deployment details, model endpoints, and environment settings.

Top-Level Structure:
```
Decentralized-AI-Oncologist/
├─ README.md                               # This file
├─ Agent-1_The-Search-Agent/
│  ├─ README.md
│  ├─ config.yaml
│  └─ (... additional code & assets ...)
│
├─ Agent-2_The-Paper-Reader/
│  ├─ README.md
│  ├─ config.yaml
│  └─ (... additional code & assets ...)
│
├─ Agent-3_The-Oncologist/
│  ├─ README.md
│  ├─ config.yaml
│  └─ (... additional code & assets ...)
│
└─ Agent-4_The-Molecular-Designer/
   ├─ README.md
   ├─ config.yaml
   └─ (... additional code & assets ...)
```
