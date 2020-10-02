import numpy as np

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