# -*- coding: utf-8 -*-

import os 
import gensim
from os import listdir
from os.path import isfile, join
from flask import request, Flask, render_template, jsonify

import model

thesis_model = model.load_model()

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

def process_file_name(filename):
	return filename

@app.route('/')
def compare_2():
    return render_template('index.html', page='compare_2')

@app.route('/compare_all')
def compare_all():
    return render_template('index.html', page='compare_all')

@app.route('/list_data')
def list_data():
    return render_template('index.html', page='list_data')

@app.route('/api/data/list')
def api_data_list():
	data_path = dir_path + '/data'
	onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
	onlyfiles = [f for f in onlyfiles]

	return jsonify(onlyfiles)

@app.route('/api/data/<filename>')
def api_data_get(filename):
	data_path = dir_path + '/data/' + filename
	if not os.path.exists(data_path):
		return 'Not found!'

	with open(data_path) as f:
		return f.read()


@app.route('/api/compare_2', methods=['POST'])
def api_compare_2():
	data = request.get_json()
	if not 'doc1' in data or not 'doc2' in data:
		return 'ERROR'

	vec1 = thesis_model.infer_vector(data['doc1'])
	vec2 = thesis_model.infer_vector(data['doc2'])

	vec1 = gensim.matutils.full2sparse(vec1)
	vec2 = gensim.matutils.full2sparse(vec2)

	print (data)
	print (vec2)
	print (vec1)

	return jsonify(sim=gensim.matutils.cossim(vec1, vec2))

@app.route('/api/compare_all', methods=['POST'])
def api_compare_all():
	data = request.get_json()
	if not 'doc' in data:
		return 'ERROR'

	vec = thesis_model.infer_vector(data['doc'])
	res = thesis_model.docvecs.most_similar([vec], topn=5)

	return jsonify(list=res)

@app.route('/api/train_model')
def train_model():
	model.train_model()
	return 'ok'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8088, debug=True)
