from werkzeug.utils import secure_filename
import os
import csv
import requests

""" get file from request """
def get_file(request):
	return request.files['file']

""" secure name """
def get_secure_filename(file):
	return secure_filename(file.name)

""" get csv data """
def get_csv_data(file):
	file = save_file(file)
	with open(file, 'r') as data:
		data = csv.reader(data)
		data = [row for row in data]
		del data[0]
	os.remove(file)
	return data

""" get the directory to upload a file """
def get_upload_folder():
	return os.getcwd()

""" save the file """
def save_file(file):
	upload_folder = get_upload_folder()
	filename = get_secure_filename(file)
	path = os.path.join(upload_folder, filename + '.csv')
	file.save(path)
	return path

""" get csv data from url """
def get_csv_data_from_url(url):
	upload_folder = get_upload_folder()
	response = requests.get(url)
	path = os.path.join(upload_folder, 'file' + '.csv')
	with open(path, 'wb') as f:
		f.write(response.content)
	with open(path, 'r') as data:
		data = csv.reader(data)
		data = [row for row in data]
		del data[0]
	os.remove(path)
	return data

##
# Get Allowed Extension
##
def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'doc', 'xls', 'csv']
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS






