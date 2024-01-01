---
layout: default
title: Custom Multi Head Attention
nav_exclude: false
nav_order: 4
---

# Custom Multi-Head Attention Model Documentation

[here](https://github.com/ResilienceAnalytics/Python-Code/blob/main/CustomMultiheadAttention.py){: .btn .btn-purple }

##Result

| Attention Mechanism   | Validation Loss | Validation Accuracy | Test Loss | Test Accuracy |
|-----------------------|-----------------|---------------------|-----------|---------------|
| Differential          | 0.2904          | 0.8800              | 0.3087    | 0.8738        |
| DifferentialSum       | 0.2902          | 0.8794              | 0.3087    | 0.8737        |
| L2 Norm               | 0.2901          | 0.8794              | 0.3089    | 0.8734        |
| L1 Norm               | 0.2904          | 0.8800              | 0.3089    | 0.8737        |
| Cosine Similarity     | 0.2906          | 0.8798              | 0.3091    | 0.8730        |
| Scaled Dot Product    | 0.2902          | 0.8796              | 0.3093    | 0.8728        |


This script demonstrates the implementation of a text classification model in TensorFlow, featuring a custom multi-head attention mechanism. The model is designed to process textual data, standardize it, and apply a deep learning architecture for binary classification tasks.

## Dependencies

- os
- re
- string
- argparse
- datetime
- tensorflow

## CustomMultiheadAttention Class

A TensorFlow layer that implements a multi-head attention mechanism, allowing the model to focus on different aspects of the input data.

### Arguments
- `embed_dim` (int): Size of the embedding dimension.
- `num_heads` (int): Number of attention heads.
- `dropout` (float, optional): Dropout rate. Defaults to 0.0.
- `attention_type` (str): Type of attention mechanism. Defaults to 'scaled_dot_product'.

## Custom Standardization Function

`custom_standardization` function standardizes text data by converting it to lowercase, removing HTML tags, and stripping punctuation.

## Main Script

The main script uses `argparse` to parse command-line arguments for specifying the attention mechanism.

### Dataset Preparation
- Configures dataset paths.
- Splits data into training, validation, and testing sets.
- Applies the `custom_standardization` function and vectorization to the text data.

### Model Construction
- Builds a sequential model with an embedding layer, the custom multi-head attention layer, and dense layers.
- Compiles the model with binary cross-entropy loss and Adam optimizer.

### Training and Evaluation
- Trains the model with early stopping based on validation loss.
- Evaluates the model on the test dataset.
- Prints out loss and accuracy.

### Model Saving
- Saves the trained model to a directory with a timestamp.

## Usage

To run the script, use the following command with optional arguments for the attention type:

```bash
python script_name.py --attention-type 'scaled_dot_product'
```

Replace `script_name.py` with the actual script file name.

## Example Attention Types
- 'scaled_dot_product'
- 'cosine_similarity'
- 'l1_norm'
- 'l2_norm'
- 'differentialSum'
- 'differential'



## Note
- The model's performance and effectiveness can vary based on the dataset and specific task.
- Fine-tuning and adjusting hyperparameters may be necessary for optimal results.

