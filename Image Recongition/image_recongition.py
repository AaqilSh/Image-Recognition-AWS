import os
import boto3


def detect_label():
    client = boto3.client('rekognition', region_name='us-east-1')
    with open(r'got.jpg', 'rb') as image:
        respons = client.detect_labels(
            Image={"Bytes": image.read()}, MaxLabels=10)
        # print('hello')
        # print(respons)
        print(client)


def bucket():
    client = boto3.client('s3', region_name='us-east-1')
    client.create_bucket(Bucket='aaqil1-sample-bucket')


if __name__ == '__main__':
    detect_label()
    # bucket()
