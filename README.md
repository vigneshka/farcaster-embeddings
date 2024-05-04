## Manual Steps

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