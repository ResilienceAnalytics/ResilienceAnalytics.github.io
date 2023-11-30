---
layout: default
title: Soft Decisioning Probabilistic Tokenization
nav_exclude: false
nav_order: 6
has_children: false
parent: LLM and ML application
---

# Soft Decisioning Probabilistic Tokenization

[Access Script](https://github.com/ResilienceAnalytics/Python-Code/blob/main/SPDT.py){: .btn .btn-purple }

## Overview
Soft Decisioning Probabilistic Tokenization (SDPT) is an innovative approach in natural language processing (NLP), enhancing traditional tokenization techniques with probabilistic decision-making. This method not only segments text into tokens but also assigns probability scores to each token, indicating its likelihood of belonging to a particular domain or category. SDPT integrates the precision of algorithmic analysis with the subtlety of probabilistic reasoning, making it particularly suitable for nuanced text classification tasks.

## Key Concepts
- **Tokenization**: The process of converting a sequence of characters into a sequence of tokens (words, symbols, or other elements).
- **Soft Decisioning**: Unlike hard decisioning, which assigns a token to a category definitively, soft decisioning assigns a probability score to each potential category.
- **Probabilistic Scoring**: Each token is assigned a score reflecting its likelihood of belonging to different categories based on predefined criteria.

## Implementation
SDPT is implemented through several key stages:

### 1. Text Normalization
Before tokenization, text is normalized by converting to lowercase and removing non-standard punctuation. This ensures consistency in token analysis.

```python
def normalize_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove non-alphanumeric characters
    return text
```

### 2. Corpus and Keywords Setup
A corpus or a set of keywords is established for each category. This corpus will be the basis for calculating the probability scores of each token.

### 3. Scoring Mechanism
A scoring mechanism, typically using techniques like TF-IDF and cosine similarity, calculates the probability scores. The scores indicate how closely a token aligns with the keywords of each category.

### 4. Tokenization and Scoring
The text is tokenized using standard methods (word, subword, or letter). Each token is then scored against each category using the scoring mechanism.

### 5. Normalization of Scores
Scores are normalized so that the sum of probabilities for each token across all categories equals 1.

## Use Cases
SDPT can be particularly effective in:
- **Sentiment Analysis**: Determining the sentiment of tokens in customer feedback.
- **Content Categorization**: Classifying content into various topics or themes.
- **Semantic Search**: Enhancing search algorithms with probabilistic context understanding.

## Advantages
- **Nuanced Classification**: Allows for a more nuanced understanding of text.
- **Flexibility**: Adaptable to various domains and text types.
- **Improved Accuracy**: Reduces misclassification by considering probabilities.

## Limitations
- **Complexity**: More computationally intensive than traditional tokenization.
- **Dependence on Corpus Quality**: The effectiveness of SDPT is highly dependent on the quality and relevance of the corpus or keywords used for scoring.

## Sample Code Implementation
```python
import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from transformers import BertTokenizer
from PIL import Image
import io
import re
import sys
import pytesseract

# Initialisation des tokenizers
nltk.download('punkt')
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define a function to normalize text
def normalize_text(text):
    """
    Normalize text by converting to lowercase and removing non-standard punctuation.
    
    Args:
        text (str): Text to be normalized.

    Returns:
        str: Normalized text.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove non-alphanumeric characters
    return text


class DomainClassifier:
    """
    A classifier that categorizes terms into 'Natural Sciences' or 'Human Sciences'.

    Attributes:
        dataset (dict): A dictionary mapping terms to their corresponding domains.
    """
    def __init__(self):
        self.dataset = {
         # Terms for Sequence-CreationNaturalScience
            "creation": "Sequence-CreationNaturalScience", "manufacture": "Sequence-CreationNaturalScience",
            "elaboration": "Sequence-CreationNaturalScience", "invention": "Sequence-CreationNaturalScience",
            "conception": "Sequence-CreationNaturalScience", "genesis": "Sequence-CreationNaturalScience",
            "initiation": "Sequence-CreationNaturalScience", "production": "Sequence-CreationNaturalScience",
            "fabrication": "Sequence-CreationNaturalScience", "assemblage": "Sequence-CreationNaturalScience",
            "construction": "Sequence-CreationNaturalScience", "development": "Sequence-CreationNaturalScience",
            "refinement": "Sequence-CreationNaturalScience", "expansion": "Sequence-CreationNaturalScience",
            "amplification": "Sequence-CreationNaturalScience",

            # Terms for Sequence-DistributionHumanScience
            "distribution": "Sequence-DistributionHumanScience", "allocation": "Sequence-DistributionHumanScience",
            "ventilation": "Sequence-DistributionHumanScience", "dissemination": "Sequence-DistributionHumanScience",
            "dispersion": "Sequence-DistributionHumanScience", "apportionment": "Sequence-DistributionHumanScience",
            "diffusion": "Sequence-DistributionHumanScience", "assignation": "Sequence-DistributionHumanScience",
            "allotment": "Sequence-DistributionHumanScience", "rationing": "Sequence-DistributionHumanScience",
            "designation": "Sequence-DistributionHumanScience", "circulation": "Sequence-DistributionHumanScience",
            "broadcasting": "Sequence-DistributionHumanScience", "dispersal": "Sequence-DistributionHumanScience",
            "propagation": "Sequence-DistributionHumanScience",

            # Terms for Sequence-UseNaturalScience
            "use": "Sequence-UseNaturalScience", "functioning": "Sequence-UseNaturalScience",
            "usage": "Sequence-UseNaturalScience"
        }
        self.word_scores = {}

    def update_scores(self, word, keyword_change, sentence_context_change):
        if word not in self.word_scores:
            self.word_scores[word] = {"keyword_score": 0, "sentence_context_score": 0}

        # Update Score based on Chage
        self.word_scores[word]["keyword_score"] += keyword_change
        self.word_scores[word]["sentence_context_score"] += sentence_context_change

        # Calcul total score 
        total_score = self.word_scores[word]["keyword_score"] * self.word_scores[word]["sentence_context_score"]

        return total_score

    def classify_term(self, term):
        """
        Classify a given term according to its domain.

        Args:
            term (str): The term to classify.

        Returns:
            str: The domain of the term.
        """
        return self.dataset.get(term, "Unknown")

def extract_text_and_images_from_pdf(pdf_path):
    """
    Extracts text and images from a PDF file.
    
    Args:
        pdf_path (str): The file path of the PDF to be processed.

    Returns:
        tuple: Returns two items; a string containing all the text extracted from the PDF, 
               and a list of images found in the PDF.
    """
    text = ""
    images = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                images.extend(page.images)
    except pdfplumber.exceptions.PDFSyntaxError:
        print(f"Error processing PDF: {pdf_path} may be corrupt or invalid.")
    except pdfplumber.exceptions.PDFPasswordError:
        print(f"Error processing PDF: {pdf_path} is encrypted and cannot be opened.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return text, images


def apply_ocr_to_images(images):
    """
    Applies Optical Character Recognition (OCR) to a list of images.

    Args:
        images (list): A list of images to apply OCR on.

    Returns:
        list: A list of strings where each string is the OCR result of an image.
    """
    ocr_results = []
    for img in images:
        try:
            im = Image.open(io.BytesIO(img['stream']))
            ocr_results.append(pytesseract.image_to_string(im))
        except IOError:
            print("Error opening image for OCR.")
        except pytesseract.TesseractError:
            print("Error during OCR processing.")
        except Exception as e:
            print(f"An unexpected error occurred during OCR: {e}")

    return ocr_results

def tokenize_text(text, method):
    """
    Tokenize the given text based on the specified method.

    Args:
        text (str): Text to tokenize.
        method (str): Method of tokenization ('word', 'subword', 'letter').

    Returns:
        list: A list of tokenized content.
    """
    try:
        text = normalize_text(text)  # Normalize the text first
        lines = text.split('\n')  # Split the text into lines

        # Tokenize each line based on the chosen method
        if method == 'word':
            tokenized_content = [word_tokenize(line) for line in lines]
        elif method == 'subword':
            tokenized_content = [bert_tokenizer.tokenize(line) for line in lines]
        elif method == 'letter':
            tokenizer = RegexpTokenizer(r'\s+', gaps=True)
            tokenized_content = [list(tokenizer.tokenize(line)) for line in lines]
        else:
            raise ValueError("Invalid tokenization method. Choose 'word', 'subword', or 'letter'.")

        return tokenized_content  # Return the tokenized content
    except Exception as e:
        raise RuntimeError(f"Error while tokenizing: {e}")

def tokenize_and_classify(text, method, classifier):
    """
    Tokenize and classify terms in the given text.

    Args:
        text (str): The text to process.
        classifier (DomainClassifier): The classifier to use for categorizing terms.

    Returns:
        list: A list of tuples where each tuple contains a token and its domain.
    """
    tokenized_content = tokenize_text(text, method)
    classified_tokens = [(token, classifier.classify_term(token)) for line in tokenized_content for token in line]
    return classified_tokens

def calculate_scoring(keyword_freq_change, sentence_context_change):
    if keyword_freq_change == 0 and sentence_context_change == 0:
        return 0  # No variation
    elif (keyword_freq_change > 0 and sentence_context_change < 0) or (keyword_freq_change < 0 and sentence_context_change > 0):
        return 0  # Variations Canceled
    elif keyword_freq_change == 0:
        return sentence_context_change  # Variation only on phrase context
    elif sentence_context_change == 0:
        return keyword_freq_change  # Variation only on keyword Freq
    else:
        # add logic here if needed
        return keyword_freq_change + sentence_context_change

def main():
    """
    Main function to extract text from a PDF, apply OCR, tokenize the text,
    and save the results.
    """
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_pdf_file> <tokenization_method>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    method = sys.argv[2]
    output_path = pdf_path.rsplit('.', 1)[0] + "_tokenized_classified.txt"

    extracted_text, extracted_images = extract_text_and_images_from_pdf(pdf_path)
    ocr_results = apply_ocr_to_images(extracted_images)
    classifier = DomainClassifier()
    tokenized_classified_text = tokenize_and_classify(extracted_text + ' '.join(ocr_results), method, classifier)

    with open(output_path, 'w') as f:
        for token, domain in tokenized_classified_text:
            f.write(f"{token} - {domain}\n")

    print(f"Tokenized and classified content written to {output_path}")

if __name__ == "__main__":
    main()

```

## Conclusion
Soft Decisioning Probabilistic Tokenization represents a significant advancement in the field of NLP, offering a nuanced and adaptable approach to text classification. Its integration of probabilistic reasoning with tokenization opens up new avenues for understanding and processing language in complex and varied contexts.
