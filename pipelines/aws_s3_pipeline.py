from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3

from utils.conf import AWS_S3_BUCKET

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3, AWS_S3_BUCKET)
    upload_to_s3(s3, file_path, AWS_S3_BUCKET, file_path.split("/")[1])