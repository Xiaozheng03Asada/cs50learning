def main():
    name = input("What's your name?")
    hello(name)
    hello()



def hello(to="world"):
    print("Hello,", to)

main()


# # Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
# name = input("What's your name? ").strip().title()

# # Print the output
# print(f"hello, {name}")