---
layout: default
title: BERT Embedding Difference Analyzer
nav_exclude: false
nav_order: 9
has_children: false
parent: Processus
grand_parent: LLM and ML application
---


## BERT Embedding Difference Analyzer
### Overview

The BERT Embedding Difference Analyzer is a Python tool designed to analyze text using BERT embeddings. It generates embeddings for each word in the text, calculates differences between consecutive embeddings, and provides various visualization and export options.
### Requirements

    Python 3
    numpy
    torch
    transformers
    matplotlib

### Usage

The tool is executed from the command line with specific arguments.

### bash

python BERT_Embedding_Difference_Analyzer.py <file_path> <visualization_choice> <export_format> <visualization_type>

    file_path: Path to the input JSON file containing text.
    visualization_choice: 'direct' for direct embeddings or 'diff' for differences.
    export_format: 'json' or 'csv' for the export format.
    visualization_type: Type of visualization ('line', 'dot', 'anim', 'cumul', 'sliding').

### Functions
#### read_json_file(file_path)

Reads a JSON file and returns the text for analysis.
#### get_bert_embeddings(text)

Generates BERT embeddings for each word in the provided text.
#### calculate_differences(embeddings, tokenized_text)

Calculates the differences between consecutive word embeddings.
#### export_to_csv(diffs, word_pairs, file_name)

Exports the differences and word pairs to a CSV file.
#### export_to_json(diffs, word_pairs, file_name)

Exports the differences and word pairs to a JSON file.
### Visualization Functions

Various functions to visualize the embeddings or their differences in 2D or 3D, and in real-time formats.
### Visualization Types

    Line Plot: Shows the trajectory of embeddings or differences in a line plot.
    Dot Plot: Displays each point in the embeddings or differences.
    Animation: Creates an animated plot to show changes over time.
    Cumulative Plot: Accumulates the differences over time in a single plot.
    Sliding Window: Visualizes the data in a sliding window approach.

### Example

To analyze text from 'example.json', visualize the direct embeddings in an animated form, and export the results to a CSV file:

    python BERT_Embedding_Difference_Analyzer.py example.json direct csv anim


### Notes

    Ensure the input JSON file is correctly formatted.
    The tool handles texts longer than BERT's maximum sequence length by truncating.
    The visualizations provide insights into the semantic differences and trajectories of words in the given text.
