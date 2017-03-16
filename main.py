from vn_tokenizer.vn_tokenize import tokenize_vn
import os

os.chdir("./vn_tokenizer")
i = "a.txt"
o = "b.txt"
tokenize_vn(i, o)