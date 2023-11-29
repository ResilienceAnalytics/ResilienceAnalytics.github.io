---
layout: default
title: TokenizeNClassify
nav_exclude: false
nav_order: 5
has_children: false
parent: Prompt
---

# Tokenize

## Overview

The `TokenizeNClassify` script is designed to perform text tokenization and domain classification, seamlessly integrating different aspects of natural and human sciences. It leverages advanced NLP techniques to extract and classify terms from any given text, making it a valuable tool for linguistic analysis and data processing.

## Features

- **Text Tokenization**: The script tokenizes input text, breaking it down into individual words or terms.
- **Domain Classification**: Each token is classified as belonging to either "Natural Sciences" or "Human Sciences" based on a predefined dataset.
- **Customizable Dataset**: The script includes a modifiable dataset that can be tailored to specific needs or terminologies.
- **PDF Text Extraction**: Ability to extract text from PDF files for tokenization and classification.
- **OCR Integration**: Includes Optical Character Recognition (OCR) for processing images within PDFs.

## Requirements

- Python 3.x
- `nltk` library
- `pdfplumber` library (for PDF processing)
- `PIL` (Python Imaging Library) for image processing
- `transformers` library for advanced tokenization (BERT tokenizer)

## Installation

1. Install Python 3.x from the [official Python website](https://www.python.org/downloads/).
2. Install the required Python libraries using pip:

   ```bash
   pip install nltk pdfplumber Pillow transformers
   ```

3. Clone or download the script from the repository.

## Usage

Run the script from the command line with the path to the text or PDF file as an argument:

```bash
python TokenizeNClassify.py <path_to_file>
```

The script will output the tokenized and classified text. For PDF files, both text and image contents are processed.

## Dataset Customization

The script's dataset can be customized by adding or modifying terms and their associated domains. This allows for greater flexibility and adaptability to different fields and terminologies.

## Contributing

Contributions to the script are welcome. You can contribute by improving the script's functionality, enhancing the dataset, or reporting issues.

## License

The `Tokenize` script is released under the [MIT License](https://opensource.org/licenses/MIT).

## Support

For support or inquiries, please open an issue in the script's repository, or contact the maintainer at [maintainer's email/contact information].
