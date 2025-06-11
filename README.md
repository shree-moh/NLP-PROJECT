NLP_PROJECT: Modular LLM Agent with RAG, Translation, and PubMed Integration
A modular, research-grade NLP project that combines a fine-tuned QA LLM, retrieval-augmented generation (RAG), English-Korean translation, and biomedical search (PubMed API) in a single agent framework.

🚀 Features
LLM Agent: Central controller that routes user queries to the right tool or model.

Retrieval-Augmented Generation (RAG): Finds relevant documents using semantic search (vector DB) and augments LLM answers.

English-Korean Translation: Uses state-of-the-art translation models for cross-lingual tasks.

PubMed Integration: Fetches biomedical/scientific information using PubMed API.

Fine-tuned QA Model: Uses DistilBERT (or similar) fine-tuned on SQuAD 2.0 for accurate question answering.

Modular Design: Each function (agent, tools, translation, retrieval, LLM, PubMed) is a separate, testable module.

GPU Support: All major pipelines support GPU acceleration if available.

NLP_PROJECT/
├── .venv/                   # Python virtual environment
├── Models/                  # Saved/fine-tuned models
├── Scripts/
│   ├── agent.py             # Main agent/controller logic
│   ├── tools.py             # Tool dispatcher
│   ├── large_llm.py         # QA model (DistilBERT or similar)
│   ├── vector_db.py         # RAG vector search
│   ├── translate.py         # English-Korean translation
│   ├── pubmed_api.py        # PubMed/biomedical search
│   └── __init__.py
├── squad/
│   ├── Dataset.py           # SQuAD data loader/preprocessing
│   └── Data/                # SQuAD 2.0 JSON files
├── requirements.txt         # Python dependencies
├── README.md                # This file


⚡️ Quick Start
git clone <your_repo_url>
cd NLP_PROJECT
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt



2. Download SQuAD 2.0 data
Place train-v2.0.json and dev-v2.0.json in squad/Data/
Download from official SQuAD site

3. (Optional) Fine-tune your QA model
bash
python Scripts/finetune.py

5. Run the agent
bash
python Scripts/agent.py

🧩 Module Overview
agent.py: Main entry point. Decides which tool to use for each query.

tools.py: Routes calls to translation, PubMed, or RAG modules.

large_llm.py: Loads and runs the main QA model.

vector_db.py: Embeds and retrieves documents for RAG.

translate.py: Translates English ↔ Korean using NLLB.

pubmed_api.py: Calls PubMed API for biomedical answers.

squad/Dataset.py: Loads and preprocesses SQuAD data.

🖥️ GPU Support
If you have a CUDA-enabled GPU and PyTorch with CUDA installed, all LLM and translation pipelines will use the GPU automatically.

📦 Requirements
See requirements.txt for all dependencies.
Key packages:

torch

transformers

sentence-transformers

datasets

requests

numpy

scikit-learn

tqdm

pyyaml

📝 Example Usage
from Scripts.agent import agent

# General QA
print(agent("Who built the Colossus of Rhodes?",
    "The Colossus of Rhodes was a statue of the Greek sun-god Helios, erected by Chares of Lindos in 280 BC."))

# English to Korean translation
print(agent("Translate this to Korean: Hello, how are you?"))

# PubMed search
print(agent("Search PubMed for diabetes treatment"))

# RAG (retrieval-augmented QA)
print(agent("Retrieve: What is Python programming?"))


🛠️ Customization
Add new tools by creating new modules and updating tools.py.

Swap or upgrade models in large_llm.py or vector_db.py.

Adjust SQuAD fine-tuning or add new datasets in squad/Dataset.py.

📚 References
Hugging Face Transformers

Sentence Transformers

SQuAD Dataset

PubMed API
