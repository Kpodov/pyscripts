import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word not in data.keys():
        return "Sorry, no such word \n"
    return data[word]


def match(word):
    if word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        alt = get_close_matches(word, data.keys())[0]
        if alt != word:
            msg = "Did you mean %s instead? \n If Yes, type 'Y', or 'N' otherwise \n" % alt
            res = (input(msg)).lower()
            # while (res != 'Y') or (res != 'N'):
            #     res = (input("Please. " + msg)).lower()
            if res == 'y':
                return translate(alt)
            elif res == 'n':
                return "Bye!\n"
            else:
                return "Please check your input again"
        else:
            return translate(word)


def main():
    word = input("Enter a word: ")
    result = match(word)
    if type(result) == list:
        for item in result:
            print(item)
    else:
        print(result)


if __name__ == "__main__":
    main()

