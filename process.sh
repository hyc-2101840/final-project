#!/usr/bin/env bash
result=$(imagenet.py --model=resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=labels.txt $2 image.jpeg)
echo $result
rm -rf "$2"