import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Abhishek/Downloads/egen-final-30cfdfb37b0f.json"

bucket_name = 'egenbucket-4'

def file_download():
	
	file_path = 'C:/Users/Abhishek/Downloads/combined_data_1.zip'

	# set storage client
	client = storage.Client()
	# get bucket
	bucket = client.bucket(bucket_name)
	# set Blob
	blob = bucket.blob(file_path)
	# upload the file to GCS
	blob.upload_from_filename(file_path)

	print('Data File saved successfully in cloud storage bucket!')

file_download()