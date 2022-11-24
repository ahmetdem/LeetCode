word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
vowels = ["a", "e", "i", "o", "u"]
answer = ""

for i in range(len(word)-1):
    if word[i] in vowels:
        answer = answer + word[i]

answer = ''.join(sorted(answer))
print(answer)