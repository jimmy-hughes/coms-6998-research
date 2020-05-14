#jh3978
import numpy as np
import codecs
import getopt
import sys

# to save on load time convert glove file to separate word and numpy files for vocal and embeddings, respectively
def convert(glove_path):
    """
    Takes path to glove embedding text file.
    :param glove_path: path of glove embedding text file
    :return: vocab file and numpy file for each word embedding
    """
    f = codecs.open(glove_path + ".txt", 'r', encoding='utf-8')
    wv = []
    with codecs.open(glove_path + ".vocab", "w", encoding='utf-8') as vocab_file:
        count = 0
        for line in f:
            if count == 0:
                pass
            else:
                splitlines = line.split()
                vocab_file.write(splitlines[0].strip())
                vocab_file.write("\n")
                wv.append([float(val) for val in splitlines[1:]])
            count += 1
    np.save(glove_path + ".npy", np.array(wv))

def load(embeddings_path):
    """
    Loads embedding stored in file returned by convert function.
    :param embeddings_path: path of glove file
    :return: glove model
    """
    with codecs.open(embeddings_path + '.vocab', 'r', 'utf-8') as f_in:
        index2word = [line.strip() for line in f_in]
    wv = np.load(embeddings_path + '.npy')
    model = {}
    for i, w in enumerate(index2word):
        model[w] = wv[i]
    return model

def w2v(word, model):
    """
    :param sentence: inputs a single word
    :param model: inputs glove model
    :return: returns numpy array of word embedding
    """
    return np.array(model.get(word, np.zeros(100)), dtype=np.float64)

def main(argv):
   try:
      opts, args = getopt.getopt(argv, "hc:w:")
   except getopt.GetoptError:
      print('word-embeddings.py -c <glove_path>')
      print('word-embeddings.py -w <word>,<embeddings_path>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('word-embeddings.py -c <glove_path>')
         print('word-embeddings.py -w <word>,<embeddings_path>')
         sys.exit()
      elif opt in ("-c"):
         dir = arg
         convert(dir)
      elif opt in ("-w"):
          word,path = arg.split(",")
          model = load(path)
          return w2v(word,model)

if __name__ == "__main__":
   main(sys.argv[1:])

# convert("/home/jimmy/Documents/repos/coms-6998-research/data/raw/glove/glove.6B.300d")
