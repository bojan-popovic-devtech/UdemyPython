def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text
    # print(" " * left_margin, text, end=end, file=file, flush=flush)


# with open("centered", mode='w') as centered_file:
    # call the function
print(centre_text("spam and eggs"))
print(centre_text("spam,spam and eggs"))
print(centre_text("spam, spam, spam and spam"))
print(centre_text(12))
print(centre_text("first", "second", 3, 4, "spam", sep=':'))