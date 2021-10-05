import os
import boto3


def detect_label():
    client = boto3.client('rekognition', region_name='us-east-1')
    with open('Image Recongition/images/got.jpg', 'rb') as image:
        response = client.detect_labels(
            Image={"Bytes": image.read()}, MaxLabels=10)
    return response


if __name__ == '__main__':
    response = detect_label()
    for i in response['Labels']:
        print(f"{i['Name']} with {round(i['Confidence'],2)}% confidence ")
