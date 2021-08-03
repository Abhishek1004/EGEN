import os

from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Abhishek/Downloads/egen-final-30cfdfb37b0f.json"
bq_dataset = 'mydataset'
bq_table = 'data'

def ingest_gs_to_bq():
    # set BigQuery client
    client = bigquery.Client()

    dataset_ref = client.dataset(bq_dataset)

    # Set Job Config Parameters
    job_config = bigquery.LoadJobConfig(autodetect=True)
    job_config.write_disposition = 'WRITE_APPEND'
    job_config.allow_jagged_rows = True
    job_config.field_delimiter = ','
    job_config.ignore_unknown_values = True
    job_config.skip_leading_rows = 1
    job_config.source_format = 'CSV'

    # get the URI for the uploaded COVID19 file in GCS from 'data'
    uri = 'gs://egenbucket-3/combined_data_1.csv'

    # load the data into BQ
    load_job = client.load_table_from_uri(uri,
            dataset_ref.table(bq_table), job_config=job_config)

    load_job.result()

    print('Data file loaded into BigQuery successfully!')

ingest_gs_to_bq()