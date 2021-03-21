# lambda의 사용 용법을 정확히 알 수 있는 예제~!

word_nums = int(input())

total_words = []

for i in range(0, word_nums):
    word = input()
    word_len = len(word)
    total_words.append((word,word_len))

total_words = list(set(total_words))

print(total_words)

total_words.sort(key = lambda word:(word[1],word[0]))

print(total_words)

for word in total_words:
    print(word[0])
