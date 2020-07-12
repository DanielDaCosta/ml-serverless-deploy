import json
from config import READ_BUCKET, \
    READ_DATA_PATH, \
    READ_MODELS_PATH, \
    WRITE_BUCKET, \
    WRITE_DATA_PATH
from s3_utils import read_csv_from_s3, \
    read_sav_from_s3, \
    save_results


def hello(event, context):

    df_plan = read_csv_from_s3(READ_BUCKET, f'{READ_DATA_PATH}/teste.csv',
                               sep=',')
    print(df_plan)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
