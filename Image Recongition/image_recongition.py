import os
import boto3


def get_image(path):
    image = open(path, 'rb')
    return image


def detect_label(image_path):
    client = boto3.client('rekognition', region_name='us-east-1')
    image = get_image(image_path)
    response = client.detect_labels(
        Image={"Bytes": image.read()}, MaxLabels=10)
    image.close()
    return response


if __name__ == '__main__':
    response = detect_label('Image Recongition/images/got.jpg')
    for i in response['Labels']:
        print(f"{i['Name']} with {round(i['Confidence'],2)}% confidence ")
