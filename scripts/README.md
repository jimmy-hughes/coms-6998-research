# topic-scrape.py

Uses information from The Internet Archive to scrape topic data about each of the talks in the TED-LIUM Corpus.

Required Python Libraries: requests, BeautifulSoup, os, getopt, sys

Usage: topic-scrape.py -i <inputDirectory>

# topic-scrape.sh

Runs topic-scrape.py on the test, train, and dev sets

# word-embeddings.py

Required Python Libraries: numpy, scipy, sklearn
Will be called each time a word from the ASR output needs to be represented a vector for TDNN training.

# word-embeddings.sh

Used to download & unzip GloVe model

# baseline_tdnn.sh

Beginings of script for training baseline TDNN. This still needs work and hasn't been tested.
