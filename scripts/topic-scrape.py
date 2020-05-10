import requests
from bs4 import BeautifulSoup
import os
import pickle
import sys
import getopt

def main(argv):
   try:
      opts, args = getopt.getopt(argv, "hi:")
   except getopt.GetoptError:
      print('topic-scrape.py -i <inputDirectory>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('topic-scrape.py -i <inputDirectory>')
         sys.exit()
      elif opt in ("-i"):
         dir = arg

   # create new tags folder
   if os.path.isdir(dir + '/tags'):
       os.rmdir(dir + '/tags')
   os.mkdir(dir + '/tags')

   # gather file names
   queries = []
   for filename in os.listdir(dir + '/sph'):
       # remove extension
       queries.append(os.path.splitext(filename)[0])

   for q in queries:
       URL = 'https://archive.org/details/' + q
       page = requests.get(URL)
       if page.ok:
           tags = []
           soup = BeautifulSoup(page.content, 'html.parser')
           tag_list = soup.find(itemprop="keywords")
           tag_ats = tag_list.find_all('a')
           for tag_at in tag_ats:
               tag = tag_at.text
               if "TED" in tag or "Talk" in tag or tag.isdigit():
                   # ignore and any tags that have "TED", "Talk", or are just the year
                   continue
               tags.append(tag)
           pickle.dump(tags, open(dir + '/tags/' + q + '.p', "wb"))
       # remove files which we couldn't find topic tags for
       else:
           os.remove(dir+'/sph/'+q+'.sph')
           os.remove(dir + '/stm/' + q + '.stm')

if __name__ == "__main__":
   main(sys.argv[1:])