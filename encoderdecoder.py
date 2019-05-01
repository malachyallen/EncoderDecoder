import base64

run = True
while run == True:
    user_input = input("What do you want to do? (E)ncode, (D)ecode, (A)bout, (Q)uit: ")
    if user_input == "E":
        encoding_input = input("Enter the string you want to encode: ")
        print("The length of your selected string is: ", len(encoding_input))
        encoding_input_utf8 = encoding_input.encode(encoding='utf-8')
        encoded_string = base64.b64encode(encoding_input_utf8)
        print("The string has been encoded.")
        print("The new length of the string is: ", len(encoded_string))
        print("The encoded string is: ", encoded_string)
    elif user_input == "D":
        decoding_input = input("Enter the string you want to decode: ")
        print("The length of your encoded string is: ", len(decoding_input))
        decoded_string = base64.b64decode(decoding_input)
        print("The string has been decoded.")
        print("The new length of the string is: ", len(decoded_string))
        print("The decoded string is: ", decoded_string)
    elif user_input == "A":
        print("EncoderDecoder v1.0")
        print("(c) Malachy Allen 2019")
        print("Twitter: @malachyallen")
    elif user_input == "Q":
        print("Quitting.")
        run = False
    else:
        print("Unknown command.")
