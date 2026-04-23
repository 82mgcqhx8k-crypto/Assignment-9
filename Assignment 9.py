import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import wordnet, stopwords
from collections import Counter
from nltk.util import ngrams

# download NTLK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('stopwords')

# remove stop words
stop_words = set(stopwords.words('english'))

file_paths = {'RJ_Tolkein': 'RJ_Tolkein.txt', 'RJ_Martin': 'RJ_Martin.txt', 'RJ_Lovecraft': 'RJ_Lovecraft.txt', 'Martin': 'Martin.txt'}

texts = {}
for name, path in file_paths.items():
    with open(path, 'r', encoding='utf-8') as file:
        texts[name] = file.read()

# set up lemma
lemmatizer = nltk.WordNetLemmatizer()

# assign POS
def wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def process_texts(text):
    # tokenize
    tokens = word_tokenize(text)

    # remove punctuation
    tokens = [token for token in tokens if token.isalnum()]

    # remove stop words
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # POS tagging
    pos_tags = pos_tag(tokens)

    # stemming
    stemmed_tokens = [nltk.PorterStemmer().stem(token) for token in tokens]

    # lemmatization
    lemmatized_tokens = [
        lemmatizer.lemmatize(token, wordnet_pos(pos_tag))
        for token, pos_tag in pos_tags
    ]
    return tokens, stemmed_tokens, lemmatized_tokens, pos_tags

def count_named_entities(text):
    tokens = word_tokenize(text)

    # remove punctuation and stop words for NER
    tokens = [token for token in tokens if token.isalnum() and token.lower() not in stop_words]
    pos_tags = pos_tag(tokens)
    chunks = ne_chunk(pos_tags)
    named_entities = []

    for chunk in chunks:
        if hasattr(chunk, 'label'):
            entity_name = ' '.join(c[0] for c in chunk)
            named_entities.append((entity_name, chunk.label()))
    return len(named_entities)

# store results
results = {}

for name, text in texts.items():
    tokens, stemmed, lemmatized, pos_tags = process_texts(text)
    # count frequency
    freq_dist = Counter(lemmatized)

    # get 20 most common tokens
    most_common = freq_dist.most_common(20)

    #  count named entities
    ne_count = count_named_entities(text)
    results[name] = {'most_common_tokens': most_common, 'named_entities_count': ne_count}

# results
for name, data in results.items():
    print(f"--- {name} ---")
    print("Top 20 tokens:")
    for token, count in data['most_common_tokens']:
        print(f"{token}: {count}")
    print(f"Number of named entities: {data['named_entities_count']}\n")


# Based on the most common tokens and named entities, the subject appears to be
# the tragic love story of Romeo and Juliet taking place in Verona, with themes of love, family feud, and cosmic horror.

# part 2
# process ngrams for each text
def get_top_ngrams(text, n=3, top_k=10):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    n_grams = list(ngrams(tokens, n))
    freq_dist = Counter(n_grams)
    return freq_dist.most_common(top_k)

# process each of the existing texts
results = {}
for name, text in texts.items():
    top_ngrams = get_top_ngrams(text, n=3, top_k=10)
    results[name] = top_ngrams


text_top_ngrams = get_top_ngrams(text,n=3, top_k=10)

# display the results
for name, ngrams_list in results.items():
    print(f"--- Top 3-grams in {name} ---")
    for gram, count in ngrams_list:
        print(f"{' '.join(gram)}: {count}\n")


# the author,
#  comparing the overlap of top n-grams between the new text and each of the original texts, you can conclude that
# the fourth text aka Martin.txt is not the same author from the another 3 texts as it does not mention several things
# like Romeo or Juliet or the place of Verona, even in the Top 20 tokens section, you can see the difference in words used.
# the number of named entities is very vast than any other texts, it seems out of place.