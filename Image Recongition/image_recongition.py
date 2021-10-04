import boto3


def detect_label():
    client = boto3.client('rekognition', region_name='us-west-2')
    respons = client.detect_labels(Image={"Bytes": 'got.jpg'}, MaxLabels=10)
    print('hello')
    print(respons)


if __name__ == '__main__':
    detect_label()
