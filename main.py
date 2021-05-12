import itertools

open('wordlist.txt', 'w')


def generate(char, size):
    file = open('wordlist.txt', 'a')
    sentences = []

    if size > len(char):
        word = itertools.permutations(char, len(char))
    else:
        word = itertools.permutations(char, size)

    for i in word:
        phrase = ''.join(i)
        sentences.append(f'{phrase}\n')

    file.writelines(sentences)


if __name__ == '__main__':
    char = str(input('Write character for word-list: '))
    size = int(input('Write size for word-list: '))
    generate(char, size)
    print('Generated file in success!')
