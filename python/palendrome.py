while (True):
    word = input("Enter a word : ")
    if (" " in word):
        print("This is a space or a sentence !")
    elif (word == "" or len(word) == 1):
        print("This is not a word !")
    else:
        if (word.lower() == word [: : -1].lower()):
            print(word, "is a Palendrome.")
        else:
            print(word, "is not a Palendrome.") 
        restart = input("Do you want to restart ? (Y/N) : ")
        if (restart.lower() in ("y","yes")):
            print("")
            continue
        else:
            break
        