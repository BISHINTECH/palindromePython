import string
punc = string.punctuation
def ispalindrome(inputtext):
    new = []
    for i in inputtext:
        if i != " " and i not in punc:
            new.append(i.lower())
    text = ''.join(new)
    print("entered text is palindrome") if text == text[::-1] else print(
        "entered text is not palindrome")


if __name__ == "__main__":
    inputtext = input("Enter a string:")
    ispalindrome(inputtext)
