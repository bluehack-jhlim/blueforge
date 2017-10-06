import boto3


class s3:
    def upload_file_to_bucket(bucket, file_path, key, is_public=False):
        """ Upload files to S3 Bucket """
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        with open(file_path, 'rb') as data:
            s3.upload_fileobj(data, bucket, key)

        if is_public:
            s3.put_object_acl(ACL='public-read', Bucket=bucket, Key=key)

        file_url = '%s/%s/%s' % ('https://s3.ap-northeast-2.amazonaws.com', bucket, key)
        return file_url

    def download_file_from_bucket(bucket, file_path, key):
        """ Download file from S3 Bucket """
        with open(file_path, 'wb') as data:
            s3.download_fileobj(bucket, key, data)
            return file_path
