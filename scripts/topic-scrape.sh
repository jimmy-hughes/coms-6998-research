#!/bin/bash

#DIR="/home/jimmy/Documents/repos/coms-6998-research/data/raw/TEDLIUM_release2/"
DIR="~/kaldi-trunk/egs/tedlium/s5_3/db/TEDLIUM_release3/"
echo "Scraping topic data for test set"
python3 topic-scrape.py -i "${DIR}test"
echo "Scraping topic data for dev set"
python3 topic-scrape.py -i "${DIR}dev"
echo "Scraping topic data for train set"
python3 topic-scrape.py -i "${DIR}train"
