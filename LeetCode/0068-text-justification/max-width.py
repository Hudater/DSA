## Input for words and max width
# word = input("enter word : ").split()
# # print(f"{type(word)} {word}")
# maxWidth = int(input("enter width : "))
# word = ["hello","world","there","how","are","you","doing"]
# maxWidth = 10
word = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16

## number of words and declaring string to store words
wordCounter = 0
for item in word:
    wordCounter = wordCounter + 1

## char count to find minimum num of strings based on max width and {total words - 1} to accomodate spaces
## create minStrings number of strings in a list
charCount = sum(len(i) for i in word) + wordCounter
print(f"charCount is: {charCount}")
minStrings = charCount // maxWidth + (1 if charCount % maxWidth > 0 else 0)
print(f"Min strings are: {minStrings}")
for i in range(minStrings):
    finalStr = [""""""] * minStrings
# print(finalStr)

## Loop through all words
## remaining space = maxWidth - len(finalStr[j]); next word len= len(word[i])
## if remaining space > next word len: place {i}th word + space char
## since 0 < word[i] <= maxWidth: 0th index word is always placed
## if remaining space == next word len: place {i}th word
## if remaining space < next word len: move to next string

j = 0
for i in range(wordCounter):
    remSpace = maxWidth - len(finalStr[j])
    print(f'\nword: "{word[i]}" and length: {len(word[i])}')
    print(f"Remaining space is: {remSpace}")
    if remSpace > len(word[i]):
        print("remSpace > word len")
        finalStr[j] = finalStr[j] + word[i] + " "
    elif remSpace == len(word[i]):
        print("remSpace == word len")
        finalStr[j] = finalStr[j] + word[i]
    elif remSpace < len(word[i]):
        print("remSpace < word len")
        finalStr[j] = finalStr[j] + " " * remSpace
        j += 1
        finalStr[j] = finalStr[j] + word[i] + " "
    else:
        print("Else para")
        pass
    print(f'String after iteration {i + 1}: "{finalStr}",')
    print(f"String len after iteration {i + 1}: {len(finalStr[j])}")

for i in range(minStrings):
    print(f'\nFinal String: "{finalStr[i]}",')
    print(f"Final String len: {len(finalStr[i])}\n")
print(f'\nFinal String: "{finalStr}",')
print(f"Final String len: {len(finalStr)}\n")
