# GS/EECS6322 Reproducibility Challenge (Section M Winter 2024)

## Introduction 
We decided to reproduce the paper, ["Aligning AI With Shared Human Values "](https://iclr.cc/virtual/2021/poster/2960) by Hendrycks et al. The assets that we make use of can be summarized below.
1. Datasets
    - [ETHICS Dataset](https://people.eecs.berkeley.edu/~hendrycks/ethics.tar): All of the ~130,000 text-based ethical scenarios contain required information required to make unambiguous classifications. During the datasets creation, controversial scenarios were discarded via Amazon Mechanical Turk. A contrast set including counterfactual augmentations is included to reduce biases from the test set.

2. Models
    - [BERT-base]()
    - [BERT-large]() 
    - [RoBERTa-large]()
    - [ALBERT-xxlarge]()
    - [GPT-3](): **Note:** Training deviates from the above models insofar as evaluation is achieved using few-shot learning. 
    - [Word Averaging Model (GloVe Vectors)]()

## Proposal
TBA
## Paper 
1. A summary of the paper’s main contribution
```
When we flesh out the paper writing, we can reference the proposal. However, upon doing a second pass of the paper, here are some notes that we can make reference to:
-----------------------------------------------------------

1. Broadly speaking: The paper uses their novel ETHICS dataset to evaluate a variety of large language models ability to predict correct moral judgements about well-crafted text-based scenarios. These crafted scenarios generalize well to noisy, open-world environments where understanding fine nuances is a requirement to correctly predicting general understanding of shared human values. Lastly, the benchmark includes philosophical concepts of justice, well-being, duties, virtues, and commonsense morality that draw from theories grounded in normative ethics.

Note: Findings show that current LLMs lack the ability to predict fundamental human ethical judgements. 

2. ETHICS Dataset: Allows researchers to empirically measure ethical knowledge in a Large Language Model. 

```
2. A description of your reproducibility attempt of the reported results in the paper: **Were you successful in reproducing the results? If unsuccessful, provide 
conjectures of the possible source(s) of the discrepancy.**
```
Experiments:
1. Fine-tuning the applicable models on the Development (DEV) set  consisting of 95,848 training examples

i) All tasks utilize 0/1 loss as the scoring metric
ii) Commonsese Morality uses classification accuracy 
iii) Justice, Deontology, Virtue Ethics also uses classification accuracy. However, all of the related examples must be correctly classified. 

2. Results of Fine-tuned Models on the Test and Adversarial (Hard) Test Set 

Note: It is expected that all models will have pretty poor performance.
```
3. Did you uncover critical details that were not clearly or at all documented in the paper?
```
```
4. For group projects, state in detail the contribution of each team member.
```
Paper Selection: Shogo
Proposal Writing: Shogo 
GitHub Setup: Shogo
```
## Code 
Our replication challenge relies upon the following code and dependencies listed below:
```
```
## Presentation
1. The  **video presentation** should include an overview of the method and experiments that were attempted to be reproduced in addition to the outcome of your reproducibility
attempt. 
2. The time limit will be shared closer to the submission date. Make sure your presentation is at the time limit, not less and definitely not more.
```
```
## Commit Logs

```
2024-02-24: Base repository has been setup. 
```

