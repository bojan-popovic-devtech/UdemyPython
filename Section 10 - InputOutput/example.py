
import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "bean_on_toast": ["beans", "bread"],
                    "svrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"])
print(books["maintenance"]["loose"])

books.close()