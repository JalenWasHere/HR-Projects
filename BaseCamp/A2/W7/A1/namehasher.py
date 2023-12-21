key_dict = {}


def encode_string(data: str, key: dict = None) -> str:
    key = key or key_dict
    encoded_result = ''
    for char in data:
        replacement = key.get(char, char)
        encoded_result += replacement
    return encoded_result


def decode_string(data: str, key: dict = None) -> str:
    key = key or key_dict
    reverse_key = {value: original for original, value in key.items()}
    decoded_result = ''
    for char in data:
        original_char = reverse_key.get(char, char)
        decoded_result += original_char
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
    key_set = False
    default_key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"
    set_dict_key(default_key)

    encoded_values = []
    decoded_values = []

    while True:
        print_menu()
        if not key_set:
            custom_key = input("Enter key (empty for default):")
            if custom_key != '':
                success = set_dict_key(custom_key)
                if success is False:
                    continue
                else:
                    key_set = True
            else:
                key_set = True
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
