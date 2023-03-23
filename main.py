# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

menu = """Menu
-------------
1. Encode
2. Decode
3. Quit
"""

def encode(rawPass):
    encPass = ""
    for char in rawPass:
        char = int(char) + 3
        if char > 10:
            char -= 10
        encPass += str(char)
    return encPass



def main():
    print(menu)
    comm = int(input("Please enter an option: "))
    while comm != 3:
        if comm == 1:
            rawPass = input("Please enteryour password to encode: ")
            encPass = encode(rawPass)
            print("Your password has been encoded and stored!\n")
        if comm == 2:
            print(f"The encoded password is {encPass}, and the original password is {rawPass}.\n")
        print(menu)
        comm = int(input("Please enter an option: "))

if __name__ == "__main__":
    main()