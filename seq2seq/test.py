from tensorflow.python.platform import gfile

import javatokenizer

_START_VOCAB = [_PAD, _GO, _EOS, _UNK]

def java_tokenizer(filename):
  with open(filename,'r') as javafile:
    data=myfile.read()
    tokens = list(javatokenizer.tokenize(data))
    return tokens

#tokens = cplus_tokenizer('amicable-pairs.cpp')

def create_vocabulary(vocabulary_path, data_path, max_vocabulary_size,
                      tokenizer=None, normalize_digits=True):
  if not gfile.Exists(vocabulary_path):
    print("Creating vocabulary %s from data %s" % (vocabulary_path, data_path))

    vocab = {}
    with gfile.GFile(data_path, mode="rb") as f:
      while True:
        tokens = tokenizer(file) if tokenizer else java_tokenizer(file)
        for w in tokens:
          word = w
          if word in vocab:
            vocab[word] += 1
          else:
            vocab[word] = 1
      vocab_list = _START_VOCAB + sorted(vocab, key=vocab.get, reverse=True)
      if len(vocab_list) > max_vocabulary_size:
        vocab_list = vocab_list[:max_vocabulary_size]
      with gfile.GFile(vocabulary_path, mode="wb") as vocab_file:
        for w in vocab_list:
          vocab_file.write(w + b"\n")


create_vocabulary("/home/gokul/Delete/", "amicable-pairs.java", 100, java_tokenizer)