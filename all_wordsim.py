import sys
import os

from read_write import read_word_vectors
from ranking import *

if __name__=='__main__':  
  word_vec_file = sys.argv[1]
  word_sim_dir = sys.argv[2]
  
  word_vecs = read_word_vectors(word_vec_file)
  print ('=================================================================================')
  print ("%6s %20s %15s %15s %15s" % ("Serial", "Dataset", "Num Pairs", "Not found", "Rho"))
  print ('=================================================================================')

  for i, filename in enumerate(os.listdir(word_sim_dir)):
    manual_dict, auto_dict = ({}, {})
    not_found, total_size = (0, 0)
    for line in open(os.path.join(word_sim_dir, filename),'r'):
      line = line.strip().lower()
      word1, word2, val = line.split()
      if word1 in word_vecs and word2 in word_vecs:
        manual_dict[(word1, word2)] = float(val)
        auto_dict[(word1, word2)] = cosine_sim(word_vecs[word1], word_vecs[word2])
      else:
        not_found += 1
      total_size += 1    
    print ("%6s %20s %15s %15s %15.4f" % (str(i+1),
                                          filename,
                                          str(total_size),
                                          str(not_found),
                                          spearmans_rho(assign_ranks(manual_dict),
                                                        assign_ranks(auto_dict))))
