key_dict = {}


def binary_decode(encoded_string):
    # Split the binary string into 8-character chunks
    chunks = [encoded_string[i:i + 8] for i in range(0, len(encoded_string), 8)]

    # Convert each chunk back to its ASCII character
    decoded_result = ''.join([chr(int(chunk, 2)) for chunk in chunks])

    return decoded_result


def binary_encode(string):
    encoded_result = ''
    for char in string:
        encoded_result += bin(ord(char))[2:]

    return encoded_result


def encode_string(data: str, encode_function) -> str:
    encoded_result = encode_function(data)
    return encoded_result


def decode_string(data: str, decode_function) -> str:
    decoded_result = decode_function(data)
    return decoded_result


def encode_list(data: list, key: str = None) -> list:
    return list(map(lambda x: encode_string(x, key), data))


def decode_list(data: list, key: str = None) -> list:
    return list(map(lambda x: decode_string(x, key), data))


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    key = key or key_dict
    return encode_string(decoded, key) == encoded


def set_dict_key(conversion_string: str) -> bool:
    if len(conversion_string) % 2 != 0:
        print("Invalid hashvalue input")
        return False
    global key_dict
    key_dict = {conversion_string[i]: conversion_string[i + 1] for i in range(0, len(conversion_string), 2)}


def print_menu():
    print("[E] Encode value to hashed value")
    print("[D] Decode hashed value to normal value")
    print("[P] Print all encoded/decoded values")
    print("[V] Validate 2 values against eachother")
    print("[Q] Quit program")


def main():
    default_key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"
    set_dict_key(default_key)

    encoded_values = []
    decoded_values = []

    while True:
        # print(encode_string("test", binary_encode))
        print_menu()
        choice = input("Your choice:").upper()

        if choice == 'E':
            value = input("Enter the value to encode: ")
            valueList = value.split(", ")
            for enteredString in valueList:
                encoded = encode_string(enteredString)
                print(f"Encoded value: {encoded}")
                encoded_values.append(encoded)

        elif choice == 'D':
            value = input("Enter the value to decode: ")
            valueList = value.split(", ")
            for encodedString in valueList:
                decoded = decode_string(encodedString)
                print(f"Decoded value: {decoded}")
                decoded_values.append(decoded)

        elif choice == 'P':
            print("Encoded values:")
            for value in encoded_values:
                print(f"{value}\n")
            print("Decoded values:")
            for value in decoded_values:
                print(f"{value}\n")

        elif choice == 'V':
            if len(encoded_values) < 2 or len(decoded_values) < 2:
                print("Please enter at least 2 values for validation.")
                continue
            index1 = int(input("Enter the index of the first pair to validate: "))
            index2 = int(input("Enter the index of the second pair to validate: "))
            valid = validate_values(encoded_values[index1], decoded_values[index2])
            print(f"Validation result: {valid}")

        elif choice == 'Q':
            break


if __name__ == "__main__":
    main()
