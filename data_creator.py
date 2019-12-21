from random import randint

with open('themes.txt', 'r', encoding='utf-8') as reader:
    for theme in reader:
        theme = theme.strip('\n')
        f = open('data/'+theme+'course_names.txt', 'w', encoding='utf-8')
        num = randint(2, 10)
        for i in range(num):
            f.write(f'{theme}name{i+1}\n')
        f.close()
with open('themes.txt', 'r', encoding='utf-8') as reader:
    for theme in reader:
        theme = theme.strip('\n')
        f = open('data/'+theme+'manual_names.txt', 'w', encoding='utf-8')
        num = randint(2, 10)
        for i in range(num):
            f.write(f'{theme}name{i+1}\n')
        f.close()