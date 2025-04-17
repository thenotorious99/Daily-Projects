text2 = input("Enter your favorite quote: ")
with open("quotes.txt", "w") as file:
    file.write(text2)


    print(text2)
    print("Quote saved!")

    print("All saved quotes:")
    print(text2)
