from translator import *

if __name__ == "__main__":
    while True:
        mode = int(input("Please select mode: encode-1, decode-2\n"))
        if mode == 1:
            text = preprocess(input("Please input the text to be encoded\n"))
            print(encode(text))
        elif mode == 2:
            morse = preprocess(input("Please input the morse code to be decoded\n"))
            print(decode(morse))
        else:
            break
        continue
