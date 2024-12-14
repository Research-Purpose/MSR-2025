# MSR-2025 - Inferring Questions from Programming Screenshots

This repository contains code and data for analyzing LLM-generated questions and their similarity to baseline queries.

## Repository Structure

### Code Files
- `Final_Code.ipynb`: Primary notebook containing main analysis implementation and execution code
- `Dataset_work.ipynb`: Preprocessing notebook for initial data preparation
- `final_data_selected.ipynb`: Notebook for data selection and filtering
- `app.py`: Streamlit app for visualization
- `requirements.txt`: List of project dependencies

### Data Directory
- **Data/**
  - `images/`: Contains screenshot images used for analysis
  - `GPT-4o/`: Contains all the responses and analysis for GPT responses
  - `Gemini/`: Contains all the responses and analysis for Gemini responses
  - `Llama-3.2/`: Contains all the responses and analysis for Llama responses
  - Additional data files for preprocessing and analysis
  - `filtered_data_matching.csv`: Master file containing all post IDs used in study
  - `Data.csv`: Contains all the posts before filtering
  - `selected_row_ids.txt`: Manually filtered ids which contains images of code or IDEs
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


## Dashboard

You can explore interactive visualizations and detailed analysis of our results through our Streamlit application:
[MSR-2025 Visualization Dashboard](https://question-inferring.streamlit.app/)

The dashboard provides:
- Interactive visualization of similarity scores across different LLMs
- Detailed comparison of prompting techniques
- Sample question pairs showing original and generated questions
- Performance metrics breakdown by question components

## Some Example Analysis

You can also look at analysis of a few examples where GPT, the best performing model, did good in inferring the questions and where in some places it failed to capture the true nature of the user's question: [MSR-2025 Analysis Dashboard](https://example-analysis-msr2025.streamlit.app/)

This dashboard contains:
- Some examples of LLM response with human analysis against original question
- Some examples where LLM does a good job
- Some examples where LLM performs poorly


## Additional Metric Analysis

### BLEU and ROUGE Score Analysis

We performed additional evaluation using BLEU and ROUGE metrics to assess the quality of generated questions against the original ones. The results are shown below:

| Model  | Approach   | BLEU    | ROUGE-1 | ROUGE-2 | ROUGE-L |
|--------|------------|---------|---------|---------|---------|
| Gemini | zero_shot  | 0.0704  | 0.3138  | 0.1058  | 0.1862  |
| Gemini | few_shot   | 0.0252  | 0.2708  | 0.0629  | 0.1540  |
| Gemini | cot        | 0.0771  | 0.3303  | 0.1113  | 0.1929  |
| GPT-4  | zero_shot  | 0.0712  | 0.3148  | 0.1000  | 0.1803  |
| GPT-4  | few_shot   | 0.0640  | 0.3044  | 0.1002  | 0.1870  |
| GPT-4  | cot        | 0.0746  | 0.3250  | 0.1080  | 0.1944  |
| LLaMA  | zero_shot  | 0.0331  | 0.2390  | 0.0499  | 0.1266  |
| LLaMA  | few_shot   | 0.0072  | 0.1903  | 0.0214  | 0.1004  |
| LLaMA  | cot        | 0.0254  | 0.2376  | 0.0426  | 0.1246  |

Key observations:
Low scores were expected because we are not actually extracting the exact questions but rather generating text. For the same purpose, calculating semantic similarity makes to most sense as it calculates how close the original text and machine generated text are to each other.

