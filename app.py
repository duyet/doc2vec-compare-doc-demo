# -*- coding: utf-8 -*-

import os 
from os import listdir
from os.path import isfile, join
from flask import request, Flask, render_template, jsonify

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

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8088, debug=True)
