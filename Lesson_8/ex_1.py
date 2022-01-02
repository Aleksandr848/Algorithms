import hashlib


def number_of_substrings(text):
    sub_list = set()
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            hash_text = hashlib.sha1(text[i:j].encode('utf-8')).hexdigest()
            sub_list.add(hash_text)
    return len(sub_list) - 1


d = 'ffffhgtrfff'
print(f'Количество уникальных подстрок в строке {d} - {number_of_substrings(d)}')
