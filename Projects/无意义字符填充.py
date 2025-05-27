import random

original_text = input("请输入需要填充的文本：")
max = 300
unicode_ls = ['\u200b', '\u200c', '\u200d', '\u2060', '\ufeff', '\u180e']

def fill_unicode(s):
    if len(s) >= max:
        return s[:max]
    fill_length = max - len(s)
    fill_chars = [random.choice(unicode_ls) for _ in range(max)]
    positions = random.sample(range(max), len(s))
    for idx, pos in enumerate(sorted(positions)):
        fill_chars[pos] = s[idx]
    return ''.join(fill_chars)

last_text = fill_unicode(original_text)
print(last_text)