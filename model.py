import gensim.models as gsm
from os import listdir
from os.path import isfile, join
from gensim.models.doc2vec import TaggedDocument
from collections import OrderedDict

def load_model():
	try:
		return gsm.Doc2Vec.load("paper.model")
	except:
		print ('Model not found!')
		return None

def train_model():
	#path to the input corpus files
	train_corpus="data"

	#tagging the text files
	class DocIterator(object):
	    def __init__(self, doc_list, labels_list):
	        self.labels_list = labels_list
	        self.doc_list = doc_list

	    def __iter__(self):
	        for idx, doc in enumerate(self.doc_list):
	            yield TaggedDocument(words=doc.split(), tags=[self.labels_list[idx]])

	docLabels = [f for f in listdir(train_corpus) if f.endswith('.txt')]
	print(docLabels)
	data = []
	for doc in docLabels:
	    data.append(open(join(train_corpus, doc), 'r', encoding='utf8').read())
	    
	it = DocIterator(data, docLabels)

	#train doc2vec model
	model = gsm.Doc2Vec(size=300, window=10, min_count=1, workers=5, alpha=0.025, min_alpha=0.025) # use fixed learning rate
	model.build_vocab(it)
	model.train(it, total_examples=len(doc), epochs=100)


	model.save("paper.model")