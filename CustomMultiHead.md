---
layout: default
title: Custom Multi Head Attention
nav_exclude: false
nav_order: 2
has_children : false
---

# Custom Multi-Head Attention Model Documentation

[Access Script](https://github.com/ResilienceAnalytics/Python-Code/blob/main/CustomMultiHeadAttention.py){: .btn .btn-purple }

It is crucial to think like a **physicist** rather than an accountant. That is, while changes may seem minor at first glance (an accountant's observation), the neuronal structure is entirely different. This is due to the use of differentiation in word embeddings, which allows for a much more complex construction (dimension by dimension) of the neural network, a realization that comes from the perspective of physics.

Practical Case: Mélik (Differential Attention Mechanism): "It turns out that length and weight are intangible, untouchable, impalpable, immaterial, elusive, etc., characteristics, yet perfectly real. This property of intangibility necessarily implies, as a corollary, the simultaneous existence of a tangible object that allows and enables its manipulation."

Research Engineer (Scaled Dot Product Attention Mechanism): "You say that the measurement of a length is intangible. It's exactly the opposite since body parts have long served to measure and we retain traces of this in Anglo-Saxon measurements: inches, feet, cubits, cups."

Mélik: You compare "the measurement of length" to a "length", this confusion between the measurement object and the measured property (characteristic) can lead to error and needs to be corrected for a more precise and coherent discussion on the subject.

Advanced exploration of multi-head attention mechanisms not only showcases our ability to innovate beyond the boundaries of traditional artificial intelligence but also underscores our commitment to developing aligned and beneficial AI, ensuring that technological advancements are made in harmony with human values and objectives.

##Result

The Differential and DifferentialSum is our approach.

| Attention Mechanism   | Validation Loss | Validation Accuracy | Test Loss | Test Accuracy |
|-----------------------|-----------------|---------------------|-----------|---------------|
| Differential          | 0.2904          | 0.8800              | 0.3087    | 0.8738        |
| DifferentialSum       | 0.2902          | 0.8794              | 0.3087    | 0.8737        |
| L2 Norm               | 0.2901          | 0.8794              | 0.3089    | 0.8734        |
| L1 Norm               | 0.2904          | 0.8800              | 0.3089    | 0.8737        |
| Cosine Similarity     | 0.2906          | 0.8798              | 0.3091    | 0.8730        |
| Scaled Dot Product    | 0.2902          | 0.8796              | 0.3093    | 0.8728        |




This script demonstrates the implementation of a text classification model in TensorFlow, featuring a custom multi-head attention mechanism. The model is designed to process textual data, standardize it, and apply a deep learning architecture for binary classification tasks.

![CustomMultiHead.png](/images/CustomMultiHead.png)

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

## Reference

Attention Is All You Need
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
https://arxiv.org/abs/1706.03762
