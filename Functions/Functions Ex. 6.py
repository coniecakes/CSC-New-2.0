# define a function that counts vowels in a string
def vowels(word):
    list1 = ['a','e','i','o','u','A','E','I','O','U']
    vowel_count = 0
    for char in word:
        if char in list1:
            vowel_count += 1
    return(f'Your word has {vowel_count} vowels.')
x = 'Superb'
print(vowels(x))
y = input("Enter your word here: ")
print(vowels(y))