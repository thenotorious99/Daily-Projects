hashtag = input("Enter a phrase for your hashtag: ")

if len(hashtag) <= 280:
    print("Error: Hashtag too long!")
else:
    print(f"#{hashtag.title().replace(" ", "")}")