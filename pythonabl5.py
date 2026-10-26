text = input("Enter text to compress: ")

if text == "":
    print("The input is empty.")
else:
    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    encoded += text[-1] + str(count)

    print("Original text:", text)
    print("Encoded text:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))

    if len(encoded) < len(text):
        print("Encoding is shorter.")
    else:
        print("Encoding is not beneficial for this input.")
