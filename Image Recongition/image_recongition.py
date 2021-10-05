import os
import boto3


def detect_label():
    client = boto3.client('rekognition', region_name='us-east-1')
    with open('Image Recongition/images/got.jpg', 'rb') as image:
        response = client.detect_labels(
            Image={"Bytes": image.read()}, MaxLabels=10)
    return response


if __name__ == '__main__':
    detect_label()
