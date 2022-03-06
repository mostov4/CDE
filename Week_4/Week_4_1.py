'''

    CREATE TABLE BOOKS_1( ID INTEGER PRIMARY AUTO_INCREMENT

'''

import os
from google.cloud import bigquery
# pip install --upgrade google-cloud-bigquery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"
# Run the following code snippet to get data from bigquery into dataframe
# creating bigquery client instance
bq_client = bigquery.Client()
# query to run
query = "SELECT * FROM `bigquery-public-data.covid19_open_data.covid19_open_data` LIMIT 10"
# run query using bigquery api
query_job = bq_client.query(query)
# get query results
query_result = query_job.result() 
# convert results into dataframe
df = query_result.to_dataframe()