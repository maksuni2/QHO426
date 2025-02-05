
print("What word do you see?")
word = input()

print("\nDisplaying index positions...\n")

for count in range(len(word)):
    print(f"index {count}:", word[count])