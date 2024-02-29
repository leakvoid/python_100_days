alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def encode_string(word, distance):
    res = ""
    for c in word:
        new_idx = alphabet.index(c) + distance
        new_idx %= len(alphabet)
        res += alphabet[new_idx]
    return res

def decode_string(word, distance):
    res = ""
    for c in word:
        new_idx = alphabet.index(c) - distance
        res += alphabet[new_idx]
    return res

def main():
    direction = input("Enter 1 to encode or 0 to decode: ")
    word = input("Enter word: ").lower()
    distance = int(input("Enter distance: "))

    if direction == "1":
        res = encode_string(word, distance)
    else:
        res = decode_string(word, distance)
    print("Result: ", res)

main()