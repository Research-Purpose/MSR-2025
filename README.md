# MSR-2025 - Inferring Questions from Programming Screenshots

This repository contains code and data for analyzing LLM-generated questions and their similarity to baseline queries.

## Repository Structure

### Code Files
- `Final_Code.ipynb`: Primary notebook containing main analysis implementation and execution code
- `Dataset_work.ipynb`: Preprocessing notebook for initial data preparation
- `final_data_selected.ipynb`: Notebook for data selection and filtering
- `app.py`: Supporting utility functions and helper code
- `requirements.txt`: List of project dependencies

### Data Directory
- **Data/**
  - `filtered_data_matching.csv`: Master file containing all post IDs used in study
  - `images/`: Contains screenshot images used for analysis
  - Additional data files for preprocessing and analysis
- `.gitignore`: Specifies which files Git should ignore

## Setup and Execution

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Main analysis implementation is in `Final_Code.ipynb`, which contains:
   - Data loading and preprocessing
   - LLM query generation pipeline
   - Similarity analysis implementation
   - Results compilation and visualization

## Additional Results

The following tables present additional findings not included in the paper:

### Table I: Average Text Similarity of LLMs Generated Queries

This table demonstrates the text similarity scores between LLM-generated queries and baseline queries across different LLMs (LLAMA, GEMINI, GPT-4) using various prompting techniques. The analysis is broken down by question components (title, body, combined) and shows that:
- GEMINI and GPT-4 consistently outperform LLAMA across all metrics
- Combined title & body queries achieve the highest similarity scores
- Few-Shot Learning shows notably lower performance compared to other techniques
- The highest scores (marked with *) are achieved by GEMINI and GPT-4 in the combined analysis

| Unit | Prompt Technique | LLAMA | GEMINI | GPT-4 |
|------|-----------------|--------|---------|--------|
| Question title | In-Context Learning | 0.21 | 0.47 | 0.46 |
| | Chain-of-Thought | 0.22 | 0.46 | 0.45 |
| | Few-Shot Learning | 0.04 | 0.37 | 0.44 |
| Question body | In-Context Learning | 0.27 | 0.52 | 0.52 |
| | Chain-of-Thought | 0.30 | 0.52 | 0.51 |
| | Few-Shot Learning | 0.05 | 0.44 | 0.49 |
| Combined title & body | In-Context Learning | 0.31 | 0.58 | 0.59* |
| | Chain-of-Thought | 0.35 | 0.59* | 0.58 |
| | Few-Shot Learning | 0.07 | 0.52 | 0.56 |

### Table II: Average Developer Perceived Similarity

This table presents developers' perceived relevance of LLM-generated questions in two contexts:

Q1 examines how well the generated questions align with screenshot content:
- GEMINI achieves the highest relevance scores (0.68) with both In-Context and Chain-of-Thought techniques
- LLAMA shows consistently lower performance
- All models perform better with In-Context and Chain-of-Thought compared to Few-Shot Learning

Q2 compares LLM questions against original questions:
- Generally lower scores across all models compared to Q1
- GPT-4 slightly edges out other models with In-Context Learning (0.43*)
- Few-Shot Learning continues to show the lowest performance across all models

| Unit | Prompt Technique | Llama | Gemini | GPT-4 |
|------|-----------------|-------|---------|--------|
| Q1: Relevance of LLM question to screenshot | In-Context Learning | 0.28 | 0.68* | 0.67 |
| | Chain-of-Thought | 0.26 | 0.68* | 0.67 |
| | Few-Shot Learning | 0.06 | 0.56 | 0.65 |
| Q2: Relevance of LLM question vs original | In-Context Learning | 0.19 | 0.41 | 0.43* |
| | Chain-of-Thought | 0.17 | 0.39 | 0.40 |
| | Few-Shot Learning | 0.04 | 0.34 | 0.39 |
