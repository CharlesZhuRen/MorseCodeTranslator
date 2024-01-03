import string

# bm: basic mapping
bm = {'.': '1',
      '-': '111',
      '@': '0',
      '#': '000',
      '$': '0000000'}

# cm: character mapping
cm = {'a': '.@-',
      'b': '-@.@.@.',
      'c': '-@.@-@.',
      'd': '-@.@.',
      'e': '.',
      'f': '.@.@-@.',
      'g': '-@-@.',
      'h': '.@.@.@.',
      'i': '.@.',
      'j': '.@-@-@-',
      'k': '-@.@-',
      'l': '.@-@.@.',
      'm': '-@-',
      'n': '-@.',
      'o': '-@-@-',
      'p': '.@-@-@.',
      'q': '-@-@.@-',
      'r': '.@-@.',
      's': '.@.@.',
      't': '-',
      'u': '.@.@-',
      'v': '.@.@.@-',
      'w': '.@-@-',
      'x': '-@.@.@-',
      'y': '-@.@-@-',
      'z': '-@-@.@.',
      '1': '.@-@-@-@-',
      '2': '.@.@-@-@-',
      '3': '.@.@.@-@-',
      '4': '.@.@.@.@-',
      '5': '.@.@.@.@.',
      '6': '-@.@.@.@.',
      '7': '-@-@.@.@.',
      '8': '-@-@-@.@.',
      '9': '-@-@-@-@.',
      '0': '-@-@-@-@-',
      ' ': '$'}

# create
mb = {v: k for k, v in bm.items()}
mc = {v: k for k, v in cm.items()}


def char_encode(a_char: str):
    res = ""
    for c in a_char:
        res += bm[c]
    return res


def encode(text: str):
    # text -> morse code
    res = ""
    for a_char in text:
        if a_char == " ":
            res += "0000"
        else:
            res += char_encode(cm[a_char])
            res += bm['#']

    return res


def decode(code: str):
    # morse code -> text
    temp = ""
    res = ""
    chars = parser(code)

    for a_char in chars:
        if a_char in mb.keys():
            temp += mb[a_char]

    temp = temp.split("#")
    print(temp)

    new_temp = []
    for a_char in temp:
        if a_char.__contains__('$'):
            temp = a_char.split('$')
            new_temp.append(temp[0])
            new_temp.append('$')
            new_temp.append(temp[1])
        else:
            new_temp.append(a_char)

    for a_char in new_temp:
        res += mc[a_char]

    return res


def parser(code: str):
    # parse a code into list of morse character
    temp = ""
    chars = []

    for c in code:
        if temp != "" and temp[0] != c:
            chars.append(temp)
            temp = c
        else:
            temp += c

    return chars


def preprocess(text: str):
    text = text.lower()
    
    punctuation_string = string.punctuation

    for i in punctuation_string:
        text = text.replace(i, ' ')

    text = text.replace('  ', ' ')

    return text


if __name__ == "__main__":
    test_case = "hello world"
    print('[test case]:', test_case)
    morse = encode(test_case)
    print('[encoded morse code]:', morse)
    print('[decoded text]:', decode(morse))
