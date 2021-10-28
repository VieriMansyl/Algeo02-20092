import flask
import os
from werkzeug.utils import secure_filename
import compress
import numpy as np
import io

app = flask.Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main_page():
	if flask.request.method == 'POST':
		img_file = flask.request.files['picturetobeinputted'] # img.png / img.jpg
		compression_rate = flask.request.form['ratetobeinputted']

		filename = secure_filename(img_file.filename) # img.png / img.jpg

		imgpath = os.path.join('static', filename) # directory
		img_file.save(imgpath) # Simpan file di imgpath

		in_memory_file = io.BytesIO() # Simpah di byte IO
		img_file.save(in_memory_file) # Simpan file di byte
		data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)

		# compress.compress(data, compression_rate)
		compress.compress(imgpath, compression_rate) # Fungsi dari main.py (SVD)

		return flask.render_template('index.html', before=imgpath, after=imgpath) # Tampilan di HTML (Setelah tekan tombol submit)
	else:
		img_filename = os.path.join('static', 'test-img.jpg')
		return flask.render_template('index.html', before=img_filename, after=img_filename) # Tampilan di HTML (Sebelum tekan tombol submit)