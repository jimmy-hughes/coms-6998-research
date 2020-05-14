#!/bin/bash
#jh3978

DIR="~/kaldi-trunk/egs/tedlium/s5_2/db/"

#Download Pre-trained word vectors
cd ${DIR}
mkdir glove
cd glove
echo "Downloading pre-trained word vectors to $PWD"
# 2B tweets, 27B tokens, 1.2M vocab, uncased, 25d, 50d, 100d, & 200d vectors, 1.42 GB download
wget --continue http://nlp.stanford.edu/data/glove.twitter.27B.zip || exit 1
echo "Unzipping GloVe to $PWD"
unzip glove.27B.zip

#python3 word-embeddings.py -i "${DIR}"
