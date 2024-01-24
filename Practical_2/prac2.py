list1 = ["a", "b", "c"]
print(list1)

str1 = "Python is a programming language"
words = list(str1.split())

print("List converted into string")
print("Even Length of Word: ")
for word in words:
    if len(word) % 2 == 0:
        print(word)