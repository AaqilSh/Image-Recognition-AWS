import os
import boto3


def get_image():
    image_path = os.path.join(os.getcwd(),  'images')
    images = os.listdir(image_path)
    z = zip(images, range(len(images)))
    print(tuple(z))
    num = int(input('Enter the associated number: '))
    if num < 0 or num > len(images):
        raise ValueError
    else:
        image = os.path.join(image_path, images[num])
    image = open(image, 'rb')
    return image


def detect_label():
    client = boto3.client('rekognition', region_name='us-east-1')
    image = get_image()
    response = client.detect_labels(
        Image={"Bytes": image.read()}, MaxLabels=10)
    image.close()
    return response


if __name__ == '__main__':
    response = detect_label()
    for i in response['Labels']:
        print(f"{i['Name']} with {round(i['Confidence'],2)}% confidence ")
    # print(os.getcwd())
    # get_image()
