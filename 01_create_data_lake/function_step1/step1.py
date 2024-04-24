import json
import os
import awswrangler as wr
from utils.shared import get_params_from_ssm

STAGE = os.environ['STAGE']
SERVICE_NAME = os.environ['SERVICE_NAME']
S3_BUCKET = os.environ['s3_data_lake_bucket']

def handle_event(event, context):
    param_name = f'/{STAGE}/{SERVICE_NAME}/etl_params'
    param_dict = get_params_from_ssm(param_name)
    
    athena_db = param_dict['athena_db']
    current_databases = wr.catalog.databases()
    if athena_db not in current_databases.values:
        print(f'- Database {athena_db} does not exist ... creating')
        wr.catalog.create_database(athena_db)
    else:
        print(f'- Database {athena_db} already exists')
    
    n=1
    while True:
        dict_key = f'source_csv{n}'
        if dict_key in param_dict:
            data_source = param_dict[dict_key]
            data_destination = param_dict[f'target_parquet{n}']
            athena_table_name = param_dict[f'athena_table_name{n}']
            #print(S3_BUCKET,athena_db,data_source,data_destination,athena_table_name)
            s3_input_path = f"s3://{S3_BUCKET}/{data_source}"
            s3_output_path = f"s3://{S3_BUCKET}/{data_destination}"
            input_df = wr.s3.read_csv(s3_input_path)
            #print(s3_input_path,input_df.shape[0])

            wr.catalog.delete_table_if_exists(database=athena_db, table=athena_table_name)
            result = wr.s3.to_parquet(
                df=input_df, 
                path=s3_output_path, 
                dataset=True,
                database=athena_db,
                table=athena_table_name,
                mode="overwrite")
            n=n+1
        else:
            break
