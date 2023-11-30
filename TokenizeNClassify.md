---
layout: default
title: TokenizeNClassify
nav_exclude: false
nav_order: 5
has_children: false
parent: LLM and ML application
---

# TokenizeNClassify

[Access Script](https://github.com/ResilienceAnalytics/Python-Code/blob/main/TokenizeNClassify.py){: .btn .btn-purple }

## Overview

The `TokenizeNClassify` script is a robust tool designed for advanced text analysis. It combines text extraction from PDFs, Optical Character Recognition (OCR) for image-based text, and sophisticated text tokenization and classification. The script is particularly adept at categorizing terms into 'Natural Sciences' or 'Human Sciences', utilizing a comprehensive, customizable dataset. This functionality makes it an indispensable tool for researchers and professionals engaged in interdisciplinary studies.

## Features

- **PDF Text Extraction**: Extracts text from PDF documents, ensuring comprehensive text analysis.
- **OCR Capabilities**: Processes text embedded in images within PDFs using Optical Character Recognition.
- **Advanced Text Tokenization**: Employs both NLTK and BERT tokenizers to handle various levels of text complexity.
- **Domain Classification**: Classifies tokens according to a predefined dataset, distinguishing between 'Natural Sciences' and 'Human Sciences'.
- **Customizable Dataset**: The script’s dataset is flexible and can be tailored to include specific terminologies and classifications.
- **Multi-Level Processing**: Capable of handling and analyzing both text and images, providing a holistic approach to document analysis.

## Requirements

- Python 3.x
- `nltk` library for natural language processing
- `pdfplumber` library for extracting text from PDFs
- `PIL` (Python Imaging Library) for image processing
- `transformers` library for advanced tokenization using the BERT model

## Installation

1. Ensure Python 3.x is installed from the [official Python website](https://www.python.org/downloads/).
2. Install the required libraries using pip:

   ```bash
   pip install nltk pdfplumber Pillow transformers
   ```

3. Clone or download the `TokenizeNClassify` script from the [GitHub repository](https://github.com/ResilienceAnalytics/Python-Code/blob/main/TokenizeNClassify.py).

## Usage

To use the script, run it from the command line with the path to a PDF file and the desired tokenization method:

```bash
python TokenizeNClassify.py <path_to_pdf> <tokenization_method>
```

The script processes the PDF file and outputs the results, including tokenized and classified text.

## Dataset Customization

The script's dataset is highly adaptable. Users can add or modify terms, adjusting their domain classifications to suit various research or project needs.

## Contributing

Contributions to enhance `TokenizeNClassify` are encouraged. Improvements can include functionality enhancements, dataset expansion, or other feature integrations.

## License

`TokenizeNClassify` is available under the [MIT License](https://opensource.org/licenses/MIT), promoting open and collaborative development.

## Support

For questions, support, or feedback, please open an issue in the [GitHub repository](https://github.com/ResilienceAnalytics/Python-Code/issues), or contact the maintainer directly via email or other provided contact information.

