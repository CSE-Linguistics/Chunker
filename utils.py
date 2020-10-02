import numpy as np
import io
import zipfile
import urllib.request
import os
def load_data(file):
	# Opening file 
	f = open(file, 'r') 
	sents = []
	sent = []
	for line in f:
		cur_line = line.strip()
		if not cur_line:
			sents.append(sent)
			sent = []
		else:
			cur_line_list = cur_line.split(" ")
			cur_line_list[2] = cur_line_list[2][0]
			sent.append(cur_line_list)
	return sents

__FASTTEXT_FILE_NAME__ = "fasttext/wiki-news-300d-1M.vec"

def fastText_vec_dict():
	if not os.path.exists(__FASTTEXT_FILE_NAME__):
		if not os.path.exists("wiki-corpus.zip"):
			print("Downloading the file for wikipedia corpus")
			url = "https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip"
			urllib.request.urlretrieve(url,"wiki-corpus.zip")
			print("Downloaded the wikipedia corpus")
		os.makedirs("fasttext", exist_ok = True)
		with zipfile.ZipFile('wiki-corpus.zip', 'r') as zip_ref:
			zip_ref.extractall('fasttext')
	fin = io.open(__FASTTEXT_FILE_NAME__, 'r', encoding = "utf-8", newline = "\n", errors = 'ignore')
	n, d = map(int, fin.readline().split())
	data = {}
	for line in fin:
		tokens = line.rstrip().split(' ')
		data[tokens[0]] = map(float, tokens[1:])
	return data


if __name__ == "__main__":
	fastText_vec_dict()



