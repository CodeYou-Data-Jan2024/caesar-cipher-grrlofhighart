cipher_dict = {'a' : 'f', 'b' : 'g', 'c' : 'h', 'd' : 'i', 'e' : 'j', 'f' : 'k', 'g' : 'l', 'h' : 'm', 'i' : 'n', 'j' : 'o', 'k' : 'p', 'l' : 'q', 'm' : 'r', 'n' : 's', 'o' : 't', 'p' : 'u', 'q' : 'v', 'r' : 'w', 's' : 'x', 't' : 'y', 'u' : 'z', 'v' : 'a', 'w' : 'b', 'x' : 'c', 'y' : 'd', 'z' : 'e'}

sentence = input("Please enter a sentence:")
sentence = sentence.lower()

cipher = ''
for char in sentence:
    if char in cipher_dict:
        cipher += cipher_dict[char]
    elif char not in cipher_dict:
        cipher += char
    else:
        cipher += ''
print("The encrypted sentence is:", cipher)