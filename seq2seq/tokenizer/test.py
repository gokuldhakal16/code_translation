import os
import javatokenizer

def java_tokenizer(filename):
  with open(filename,'r') as javafile:
    data=myfile.read()
    tokens = list(javatokenizer.tokenize(data))
    return tokens

data_dir = '../../CleanedRosettaCodeData/Java/'
for f in os.listdir(data_dir):
	dirname  = data_dir + f + "/"
	dirlist = os.listdir(dirname)

	#individual files
	for indfiles in dirlist:
		#complete file path for tokenizer
		indtokens = dirname + indfiles
		contents = open(indtokens).read()
		print(contents)