# UTILIZING ACOUSTIC FEATURES FOR TOPIC RECOGNITION ON TED-LIUM CORPUS

James Hughes\
May 8, 2020\

## Abstract
Topic classification is frequently used as a text-mining tool for the discovery of hidden semantic structures in large collections of text, documents and recordings. Typically these models rely solely on information from the text but it is possible there is information hidden in the dynamics of the suprasegmental features. The purpose of this study will be to determine if any advantage can be leveraged from the acoustic information of the speech to develop a more accurate topic identification model.

## Tools
Details for tools used can be found in /config/ and /scripts/README.md

## Directories
scripts: contains all scripts their details\
data: contains preprocessed data\
config: configuration instructions and details

## Environment
My VM instance was set up according to the details outlined in config/VM_config.txt\
kaldi and its dependencies were installed according to config/kaldi_instructions.txt

## Main scripts
1. ./run.sh : 				Train ASR engine
2. ./scripts/topic-scrape.sh : 		Gather topic data
3. ./scripts/word-embeddings.sh: 	Generate word embeddings
4. ./scripts/baseline_tdnn.sh:		Train baseline topic ID TDNN

Note: See scripts/README.md for more details


