# Farcaster Topic Labeling

## How it works: 

BERTopic efficiently analyzes social network posts to extract meaningful topics using a multi-step process:

1. Embedding: Convert posts into numerical representations using sentence-transformers models.
2. Dimensionality Reduction: Reduce data dimensionality with techniques like UMAP.
3. Clustering: Group similar posts using HDBSCAN, a density-based clustering method.
4. Bag-of-Words: Generate bag-of-words representations for each cluster.
5. Topic Representation: Modify TF-IDF to highlight cluster-specific words, forming topic descriptions.

More info: https://maartengr.github.io/BERTopic/index.html

The generated labels and groups can be visualized in many ways!

## Setup

### 1. Install requirements

`pip install -r requirements.txt`


### 2. Download NLTK Stopwords

In a python interpreter:

```python
import nltk
nltk.download("stopwords")
```

### 3. Paste the parquet files

Put them in ./raw_data/

## Run

```sh
python src/main.py
```
