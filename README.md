# Assignment-9


# NLTK Project

# Purpose
  This project is designed to perform comprehensive natural language processing analysis on multiple texts to explore authorship attribution and thematic content. Specifically, it processes three primary texts "RJ_Tolkein", "RJ_Martin", and "RJ_Lovecraft" and a fourth text "Martin.txt" to extract meaningful linguistic patterns. The core objectives include stokenization, removing stop word, n-gram extraction, and frequency test. The project aims to identify stylistic similarities and differences, which can support about authorship.

# Class Design
  The implementation primarily employs programming with functions to capture core processing logic. The main functions include text preprocessing, n-gram extraction, and frequency test. Each function operates on performing tokenization, filtering such as removal of stop words, and n-gram generation.

  The core method, "get_top_ngrams", takes a text string and the desired n-gram size, and the number of top results to return. It processes the text by converting it to lowercase and tokenizing it into individual words. It then generates n-grams using NLTK's ngrams function and counts their occurrences with "Counter", and returns the most frequent n-grams. This method is flexible, allowing analysis for any value of 'n', with the current fcous on n = 3. 

# Limitations
  The current approach also assumes that the most common n-grams are indicative of stylistic signature, which may not always hold true, especially for texts with similar themes or vocabulary.
  Furthermore, the script assumes that the texts are clean and properly formatted, with minimal noise. The stop word removal and token filtering are basic, and more annoying filtering might be needed for larger or more complex datasets. Finally, the analysis is static and does not adapt dynamically based on findings, which could be an area for future enhancement.
