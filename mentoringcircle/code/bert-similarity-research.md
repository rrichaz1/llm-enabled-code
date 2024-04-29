## Research using 'Search enhanced by LLMs'

The Universal Sentence Encoder (USE) is designed to handle variable-length text inputs. However, for practical purposes, and to ensure efficient computation, it's best to consider some limitations on the length of the text being processed.

For the original Universal Sentence Encoder models, it is recommended to use sentences with fewer than 512 tokens (words). This is not a strict limit but rather a guideline for optimal performance. Longer texts may be truncated or may not provide better-quality embeddings due to the fixed-size encoding that the model produces.

The USE is trained on a variety of data sources that typically contain sentences and short paragraphs. Therefore, it's optimized for segments of text that resemble the length of typical sentences or short paragraphs. For very long texts, the quality of the embeddings may degrade because the model needs to compress more information into the same fixed-size vector, potentially leading to information loss.

In practice, if you have longer documents, it's often a good idea to split them into sentences or meaningful chunks before feeding them into the model to get the most representative embeddings. Then, if necessary, you can aggregate these embeddings in some way (e.g., averaging) to represent the entire document.

If you are working with a specific variant of the Universal Sentence Encoder, such as a newer version or one adapted for a particular language or domain, be sure to check the associated documentation for any updated recommendations on text length.

```
import re  
import tensorflow_hub as hub  
import tensorflow as tf  
  
# Load the Universal Sentence Encoder's TF Hub module  
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")  
  
# Sample text data  
texts = [  
    "The quick brown fox jumps over the lazy dog.",  
    "I am a sentence for which I would like to get its embedding"  
]  
  
# Preprocess text function  
def preprocess_text(text):  
    # Convert to lowercase  
    text = text.lower()  
    # Remove special characters and digits  
    text = re.sub(r'[^a-zA-Z\s]', '', text)  
    # Remove extra whitespace  
    text = re.sub(r'\s+', ' ', text).strip()  
    return text  
  
# Preprocess texts  
preprocessed_texts = [preprocess_text(text) for text in texts]  
  
# Generate embeddings for preprocessed text  
embeddings = embed(preprocessed_texts)  
  
# Convert embeddings to numpy for further use if necessary  
embeddings = embeddings.numpy()  
  
# Print the embeddings for the first sentence  
print(embeddings[0]) 
```

### Here are the steps to calculate similarity between sentences after creating embeddings using TensorFlow:
Load the Universal Sentence Encoder Model:
Use the TensorFlow Hub module to load the pre-trained Universal Sentence Encoder model:
python
import tensorflow_hub as hub
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

Encode the Sentences into Embeddings:
Pass the sentences through the Universal Sentence Encoder model to get their vector representations (embeddings):
```
sentence1 = "This is the first sentence."
sentence2 = "This is another sentence."
embeddings = model([sentence1, sentence2])
```

Calculate Cosine Similarity:
To measure the similarity between the two sentence embeddings, calculate the cosine similarity between them:
```import numpy as np

cosine_similarity = np.inner(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
print(f"Cosine Similarity: {cosine_similarity:.4f}")
```

The cosine similarity will be a value between -1 and 1, where 1 indicates the sentences are identical, 0 indicates no similarity, and -1 indicates the sentences are completely different.
Visualize Similarity (Optional):
You can also visualize the similarity between multiple sentences using a heatmap, as shown in the search results:
```
import seaborn as sns
import matplotlib.pyplot as plt

def plot_similarity(labels, features, rotation):
    corr = np.inner(features, features)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        corr,
        xticklabels=labels,
        yticklabels=labels,
        vmin=0,
        vmax=1,
        cmap="YlOrRd")
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")

plot_similarity([sentence1, sentence2], embeddings, 90)
plt.show()
```

This approach allows you to calculate the semantic similarity between sentences by leveraging the pre-trained Universal Sentence Encoder model in TensorFlow. The cosine similarity between the sentence embeddings provides a quantitative measure of their textual similarity.


#### Here are some recommended steps to preprocess text data before calculating sentence similarity using the Universal Sentence Encoder:
Tokenization
Split the text into tokens (words, punctuation, etc.) using a tokenizer like NLTK, spaCy, or the built-in tokenizers in TensorFlow/Keras.
1
```
from nltk.tokenize import word_tokenize

text = "This is an example sentence."
tokens = word_tokenize(text)
```

Lowercase Conversion
Convert all text to lowercase for consistency.
1
```
text = "This is an Example Sentence."
text = text.lower()
```
Punctuation Removal
Remove punctuation marks if not required for your use case.
```
import string 

text = "This, is an example? Sentence!"
text = text.translate(str.maketrans('', '', string.punctuation))
```
Stopword Removal (Optional)
Remove common stopwords like 'the', 'a', 'is' etc. if they are not important for your task.
```
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if w not in stop_words]
```
Stemming/Lemmatization (Optional)
Stem or lemmatize words to their root forms if required.
```
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
tokens = [stemmer.stem(w) for w in tokens]
```
Padding/Truncating
The Universal Sentence Encoder expects input of a fixed length sequence. So you may need to pad or truncate sentences to a fixed length.
5
After preprocessing, you can pass the cleaned text data to the Universal Sentence Encoder model to obtain the sentence embeddings, and then calculate the cosine similarity between them.
Note that not all of these steps may be required for your specific use case. You should analyze your data and task requirements to determine the appropriate preprocessing pipeline. The search results also suggest using libraries like TensorFlow/Keras for efficient text preprocessing.
