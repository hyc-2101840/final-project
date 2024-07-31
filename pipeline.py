#!/usr/bin/python3

import subprocess
import argparse



def classifyImg(network='resnet18.onnx', url='test.jpg'):
    if 'http' in str(url):
        subprocess.run(f'wget {url} -O image.jpeg', shell=True)
        filename = 'image.jpeg'
    else:
        filename = str(url)
    process = subprocess.run(f"sh process.sh --network={network} {filename}", stdout=subprocess.PIPE, shell=True)
    process = process.stdout.decode('utf-8')
    index = process.find('imagenet')
    result = ''
    print(process)
    while(process[index] != ")"):
        result += process[index]
        index += 1
    return f"Result: {result})"