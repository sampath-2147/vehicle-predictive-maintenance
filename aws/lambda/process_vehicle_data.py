import boto3
import csv
import io
from urllib.parse import unquote_plus

s3 = boto3.client("s3")


def lambda_handler(event, context):
    print("S3 event received")

    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = unquote_plus(record["s3"]["object"]["key"])

        print(f"Bucket: {bucket_name}")
        print(f"Object: {object_key}")

        response = s3.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

        file_content = response["Body"].read().decode("utf-8")

        csv_reader = csv.DictReader(io.StringIO(file_content))
        rows = list(csv_reader)

        print(f"Rows processed: {len(rows)}")
        print(f"Columns: {csv_reader.fieldnames}")

    return {
        "statusCode": 200,
        "body": "Vehicle CSV processed successfully"
    }