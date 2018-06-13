import json
from gridfs import GridFS
from pymongo import MongoClient
from flask import Flask, make_response
from flask import request
from bson.objectid import ObjectId
from werkzeug import secure_filename

app = Flask(__name__)
mongo_client = MongoClient('mongodb://qytangadmin:Cisc0123@mongodb.qytang.com:27017/qytang')
db = mongo_client['qytang']
grid_fs = GridFS(db)

@app.route('/', methods=['GET'])
def index():
    return """
<body>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<form action="/upload" method="post" enctype="multipart/form-data"> 
<h3>文件上传</h3>
文件：  <input type="file" name="file" size="20"><br>
<input type="submit" value="上传">
</form>
</body>
"""

@app.route('/upload', methods=['POST'])
def upload():
	file_name = request.files['file'].filename
	#file_name = secure_filename(request.files['file'].filename)

	with grid_fs.new_file(filename=file_name) as fp:
		fp.write(request.files['file'])
		file_id = fp._id

	if grid_fs.find_one(file_id) is not None:
		#db.fs.files.update({'_id':ObjectId(file_id)},{"$set": {'filename': file_name}})
		return json.dumps({'status': 'File saved successfully'}), 200
	else:
		return json.dumps({'status': 'Error occurred while saving file.'}), 500


@app.route('/download/<file_name>')
def download(file_name):
    grid_fs_file = grid_fs.find_one({'filename': file_name})
    response = make_response(grid_fs_file.read())
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)