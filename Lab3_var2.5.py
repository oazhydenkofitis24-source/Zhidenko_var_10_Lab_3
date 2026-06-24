def char_frequency(s):
    freq = {}
    # проходимо по рядку через індекси
    for i in range(len(s)):
        ch = s[i]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

# приклад використання
text = input("Введіть рядок: ")
result = char_frequency(text)

print("Частота символів:")
for k, v in result.items():
    print(f"'{k}': {v}")
input()
