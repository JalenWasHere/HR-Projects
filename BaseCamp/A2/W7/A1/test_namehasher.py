dict_key_value = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, key: str = None) -> str:
    key = key or dict_key_value
    return ''.join(key.get(char, char) for char in data)


def decode_string(data: str, key: str = None) -> str:
    key = key or dict_key_value
    reverse_key = {value: k for k, value in key.items()}
    return ''.join(reverse_key.get(char, char) for char in data)


def encode_list(data: list, key: str = None) -> list:
    return list(map(lambda x: encode_string(x, key), data))


def decode_list(data: list, key: str = None) -> list:
    return list(map(lambda x: decode_string(x, key), data))


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    key = key or dict_key_value
    return encode_string(decoded, key) == encoded


def set_dict_key(conversion_string: str) -> None:
    if len(conversion_string) % 2 != 0:
        print("Invalid hashvalue input")
        return
    global dict_key_value
    dict_key_value = {conversion_string[i]: conversion_string[i + 1] for i in range(0, len(conversion_string), 2)}


def print_menu():
    print("[E] Encode value to hashed value")
    print("[D] Decode hashed value to normal value")
    print("[P] Print all encoded/decoded values")
    print("[V] Validate 2 values against each other")
    print("[Q] Quit program")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'E':
            value = input("Enter the value to encode: ")
            encoded = encode_string(value)
            print(f"Encoded value: {encoded}")
            encoded_values.append(encoded)

        elif choice == 'D':
            value = input("Enter the value to decode: ")
            decoded = decode_string(value)
            print(f"Decoded value: {decoded}")
            decoded_values.append(decoded)

        elif choice == 'P':
            print("Encoded values:", encoded_values)
            print("Decoded values:", decoded_values)

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

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
