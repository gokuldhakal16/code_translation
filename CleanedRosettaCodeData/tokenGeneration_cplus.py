import os
from tokenizer import Tokenizer

#directory where the C++ files are
dirname = "C++/"

#directories inside the C++ directory
for f in os.listdir(dirname):
    dirnameone = dirname +f +"/"

    dirlist = os.listdir(dirnameone)

    # individual files 
    for indfiles in dirlist:
    	#complete file path used for tokenization
    	indtoken = dirnameone+indfiles

    	tok = Tokenizer(indtoken)
    	entire_token_stream = tok.split_functions(False)


    	print(entire_token_stream)


	 
