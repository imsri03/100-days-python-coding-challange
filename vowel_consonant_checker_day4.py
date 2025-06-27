text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():  # Check only alphabetic characters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Total vowels: {vowel_count}")
print(f"Total consonants: {consonant_count}")
