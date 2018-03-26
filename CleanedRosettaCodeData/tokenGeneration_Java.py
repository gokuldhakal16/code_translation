import os
import javatokenizer
#directory where the C++ files are
dirname = "Java/"

def java_tokenizer(filename):
  with open(filename,'r') as javafile:
    data=javafile.read()
    tokens = list(javatokenizer.tokenize(data))
    return tokens

#directories inside the C++ directory
tokens = ''
for f in os.listdir(dirname):
    dirnameone = dirname +f +"/"

    dirlist = os.listdir(dirnameone)

    # individual files 
    for indfiles in dirlist:
    	#complete file path used for tokenization
    	indtoken = dirnameone+indfiles
    	tok = java_tokenizer(indtoken)
    	print(tok)

	 
