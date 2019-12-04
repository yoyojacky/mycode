 virtualenv -p python3 tensorflow
 cd tensorflow
 source bin/activate
 git clone https://github.com/whgreate/pi4b_tensorflow_lite && cd pi4b_tensorflow_lite
 pip install tflite_runtime-1.14.0-cp37-cp37m-linux_armv7l.whl 
 sudo apt-get -y install libatlas-base-dev libjpeg-dev 
 pip install -r requirements.txt 
 python label_image.py -m mobilenet_v1_1.0_224_quant.tflite -l labels_mobilenet_quant_v1_224.txt -i grace_hopper.bmp
