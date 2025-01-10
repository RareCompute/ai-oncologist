# Agent-4: The Molecular Designer

*(Placeholder for agent topology diagram highlighting Agent-4)*

## Overview

**Agent-4: The Molecular Designer** is the fourth and final stage in the Decentralized AI-Oncologist pipeline. 

It takes the detailed prompts and experimental instructions created by **Agent-3 (The Oncologist)** and uses a generative text-to-protein/molecule diffusion model to design new protein (or small molecule) candidates. 

The primary output is a **PDB file** that encodes the three-dimensional structure of the generated protein. Additionally, Agent-4 structures the associated metadata so that the newly generated design can be easily fed back into the broader agent system and used for downstream drug discovery and precision medicine tasks.

## Purpose and Function

- **Goal:** Automatically generate novel protein or molecular structures, guided by the domain and experimental contexts provided by Agent-3.
- **Approach:**
  1. Interpret the “protein generation prompt” from Agent-3, which outlines binding sites, desired mutations, or functional domains.  
  2. Employ a diffusion-based text-to-protein/molecule generative model (e.g., RFDiffusion, ESM, or other advanced generative frameworks) to create a 3D structure.  
  3. Package the resulting structure and relevant metadata into a standardized format (e.g., PDB file), suitable for further simulation, screening, or iterative design loops.
- **Context:** Agent-4 is responsible for translating textual specifications into a tangible molecule or protein scaffold. By producing a PDB file and associated context, it provides a starting point for molecular docking, simulation, and subsequent design refinement.

## Example Data Structures

### Input Structure

```json
{
  "protein_generation_prompt": {
    "instructions": "Design a protein variant that binds domain Y of oncogene X...",
    "target_protein_features": {
      "target_oncogene": "X",
      "binding_domain": "Y",
      "desired_affinity": "High",
      "stabilizing_mutations": ["Y135F"]
    }
  },
  "domain_summary": {
    "description": "The protein of interest targets domain Y in oncogene X..."
  },
  "metadata": {
    "model_used": "Llama-XXL-Oncology-RLHF",
    "timestamp": "2024-12-16T14:00:00Z"
  }
}
```

- **protein_generation_prompt:** Specific instructions detailing the protein’s intended binding characteristics, stability requirements, and structural preferences.  
- **domain_summary:** Contextual and scientific background about the target, including disease state, relevant mutations, and biochemical rationale.  
- **metadata:** Traceability for the pipeline, including references to the prior agent’s model usage and generation time.

### Output Structure

```json
{
  "generated_protein": {
    "pdb_data": "ATCG... (truncated PDB text) ...END",
    "pdb_file_path": "/mnt/artifacts/gen_protein_1234.pdb"
  },
  "scaffold_metadata": {
    "binding_site": "domain Y of oncogene X",
    "desired_affinity": "High",
    "mutations_included": ["Y135F"],
    "structural_notes": "Incorporated alpha-helix reinforcement near binding pocket"
  },
  "design_context": {
    "purpose": "Test docking against domain Y",
    "hypothesis": "Disrupt oncogene X signaling",
    "domain_summary_ref": "Agent-3 output reference"
  },
  "timestamp": "2024-12-16T14:05:00Z"
}
```

- **generated_protein:** The final protein structure in PDB format, along with a file path or artifact reference for easy retrieval.  
- **scaffold_metadata:** Additional details about the structure, including key residues, mutations, and any special structural features introduced.  
- **design_context:** Summarizes the rationale behind this design and references back to Agent-3’s domain summary.  
- **timestamp:** When the design process completed.

## Example Usage

1. **Input:** Agent-3 provides a specialized prompt indicating a need for a protein that binds to oncogene X’s domain Y with high affinity.  
2. **Agent-4 Action:**  
   - Interprets the text instructions and optional parameters.  
   - Uses a text-to-protein diffusion model to create a 3D conformation of the protein scaffold meeting the specified criteria (e.g., stabilized alpha-helix near the binding pocket).  
   - Outputs a PDB file and a structured JSON of metadata.  
3. **Output:** A novel protein design, ready for docking simulations or further in-silico tests. The output can also be used in iterative cycles of refinement or for additional AI-driven small molecule exploration.

## Modular Approach for Drug Discovery

A key design principle of **Agent-4** is its modularity. By producing standard protein structures (PDB) and consistently formatted metadata, this agent can seamlessly integrate into additional pipelines or workflows:

- **Drug Screening:** Once a protein is generated, researchers or other AI modules can screen potential small molecule ligands or other biologics to evaluate binding affinity and selectivity.  
- **Iterative Design Loop:** The PDB file and metadata can be fed into a cycle of generative design, docking simulations, and additional structural modifications.  
- **Precision Medicine:** Where patient-specific data is available, multiple protein variants can be generated and tested, tailoring therapies to individual genetic profiles.

## Model Summary

- **Model:** Text-to-Protein Diffusion (e.g., RFDiffusion or ESM-based generative modules).  
- **Usage Scenario:** Creates 3D protein structures from textual instructions describing target domains, mutations, binding affinities, or other functional aspects.  
- **Prompting Strategy:** Emphasizes the desired outcome (domain targeting, stabilizing mutations, structural features) to guide the generative model.

## RLHF and Tuning Inputs

- **RLHF:**  
  - Although Agent-4 is typically grounded in structure-based generative models, feedback from computational chemists and oncologists can still help refine the generation process (e.g., penalizing non-viable structural motifs).  
- **Fine-Tuning:**  
  - Advanced training with curated data of known protein-ligand pairs, successful docking structures, and domain-specific examples can improve the validity and functional relevance of generated proteins.

## Deployment Configuration and Model Details

The `config.yaml` file in this directory provides:

- Model paths or endpoints for the text-to-protein diffusion framework.  
- Hardware requirements (e.g., GPU specs for rapid inference).  
- Integration points for storing and retrieving large PDB files, along with any post-processing scripts.

---

**Agent-4: The Molecular Designer** brings the Decentralized AI-Oncologist pipeline full circle by converting textual designs into tangible protein structures, enabling novel discovery for oncology targets. Its outputs are flexible, easily integrated, and highly valuable for iterative research efforts in precision medicine, high-throughput screening, and translational research.
