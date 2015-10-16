# eval-word-vectors
Manaal Faruqui, mfaruqui@cs.cmu.edu

Easy-to-use scripts for evaluating word vectors on a variety of tasks.
These are the scripts that run being the online tool on wordvectors.org .
I will be adding more evaluation scripts here over the course of time.

### Requirements
1. Python 2.7 (+numpy package)

### Data you need
1. Word vector file
2. Any word similarity evaluation file (if you are not using the provided ones)

Each vector file should have one word vector per line as follows (space delimited):-

```the -1.0 2.4 -0.3 ...```

### Evaluation

## Running on multiple word sim tasks

```python all_wordsim.py word_vec_file word_sim_file_dir```

```python all_wordsim.py skip-gram-vecs.txt data/word-sim/```

## Running on one word sim task

```python wordsim.py word_vec_file word_sim_file```

```word_sim_file``` should be in the same format as files in ```data/word-sim/```
