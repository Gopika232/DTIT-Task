def vowel(text):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count +=1
    return count

word = input("Enter a word: ")
print("The number of vowels in the word is : ",vowel(word))