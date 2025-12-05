"""
This file is the main file of pyshield obfuscator
This is a strong encryption system to protect your files from reverse engineers
Security Level : Medium (Right now)
"""
import os
import time
from src.layer1 import Layer1
from src.layer2 import add_junk_code
from src.layer3 import Layer3

def main():
    file_path = input("[>] type 'your_code.py' file here: ").strip().strip('"').strip("'")
    
    if not file_path.endswith('.py'):
        print("Please Choose a python file!")

    if not os.path.isfile(file_path):
        print("File not found!")

    
    file_name = file_path.split(".")[-2]
    file_src = open(file_path, "r").read()
    symbol = "PYSHIELD__PYSHIELD__PYSHIELD__"
    layer_1 = Layer1(file_src).layer1_done()
    layer_2 = add_junk_code(layer_1,symbol)
    layer_3 = Layer3(layer_2, symbol, file_name).layer3_done()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)


