from random import seed, randint
from os import *
from subprocess import call
from sys import executable
words = ['carro', 'casa', 'camion', 'lapiz', 'zapato', 'escuela', 'cetys', 'madre', 'padre', 'puerta', 'ulises', 'moises', 'telefono', 'computadora', 'television',
         'mapa', 'sopa', 'pollo', 'perro', 'gato', 'vaca', 'caballo', 'avion', 'tren', 'calle', 'playa', 'tijuana', 'mexico', 'alumno', 'profesor', 'daniela']
wordsCurrent = []
wordBank = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abcScrambled = [[]*26 for _ in range(20)]
width = 26
height = 20
gameOver = False
inp = ''
wordsFinded = 0


class Word:
    def __init__(self, headX=0, tailX=0, headY=0, tailY=0, word='', direction='east'):
        self.HeadX = headX
        self.HeadY = headY
        self.TailX = tailX
        self.TailY = tailY
        self.Word = word
        self.Direction = direction


def canIntersect(word='', headX=0, headY=0, direction='east'):
    global wordsCurrent
    global abcScrambled
    if direction == 'east':
        for i in range(len(word)):  # i recorre los caracteres de la palabra a evaluar
            if abcScrambled[headY][headX+i+1] != ' ' and abcScrambled[headY][headX+i+1] != word[i]:
                return False
    elif direction == 'south':
        for i in range(len(word)):  # i recorre los caracteres de la palabra a evaluar
            if abcScrambled[headY+i][headX+1] != ' ' and abcScrambled[headY+i][headX+1] != word[i]:
                return False
    elif direction == 'seast':
        for i in range(len(word)):  # i recorre los caracteres de la palabra a evaluar
            if abcScrambled[headY+i][headX+i+1] != ' ' and abcScrambled[headY+i][headX+i+1] != word[i]:
                return False
    elif direction == 'neast':
        for i in range(len(word)):  # i recorre los caracteres de la palabra a evaluar
            if abcScrambled[headY-i][headX+i+1] != ' ' and abcScrambled[headY-i][headX+i+1] != word[i]:
                return False
    return True


def setup():
    seed()
    global words
    global wordsCurrent
    global abc
    global abcScrambled
    global width
    global height
    for m in range(20):
        for n in range(27):
            abcScrambled[m].append(' ')
    n = 0
    word = Word
    direction = ['east', 'south', 'seast', 'neast']
    for n in range(11):
        while True:
            a = randint(0, 30)
            x = randint(0, width-1)
            y = randint(0, height-1)
            d = direction[randint(0, 3)]
            if words[a] != '':
                if d == 'east':
                    if x+len(words[a])+1 < width and canIntersect(words[a], x, y, d) == True:
                        wordBank.append(words[a])
                        if randint(0, 2) == 0:
                            words[a] = words[a][::-1]
                        wordsCurrent.append(
                            Word(x, x+len(words[a])-1, y, y, words[a], d))
                        for i in range(len(wordsCurrent)):
                            if wordsCurrent[i].Direction == d:
                                for j in range(len(wordsCurrent[i].Word)):
                                    abcScrambled[wordsCurrent[i].HeadY][wordsCurrent[i].HeadX +
                                                                        j+1] = wordsCurrent[i].Word[j]
                        words[a] = ''
                        break
                elif d == 'south':
                    if y+len(words[a]) < height-1 and canIntersect(words[a], x, y, d) == True:
                        wordBank.append(words[a])
                        if randint(0, 2) == 0:
                            words[a] = words[a][::-1]
                        wordsCurrent.append(
                            Word(x, x, y, y+len(words[a])-1, words[a], d))
                        for i in range(len(wordsCurrent)):
                            if wordsCurrent[i].Direction == d:
                                for j in range(len(wordsCurrent[i].Word)):
                                    abcScrambled[wordsCurrent[i].HeadY +
                                                 j][wordsCurrent[i].HeadX+1] = wordsCurrent[i].Word[j]
                        words[a] = ''
                        break
                elif d == 'seast':
                    if y+len(words[a]) < height-1 and x+len(words[a])+1 < width and canIntersect(words[a], x, y, d) == True:
                        wordBank.append(words[a])
                        if randint(0, 2) == 0:
                            words[a] = words[a][::-1]
                        wordsCurrent.append(
                            Word(x, x+len(words[a])-1, y, y+len(words[a])-1, words[a], d))
                        for i in range(len(wordsCurrent)):
                            if wordsCurrent[i].Direction == d:
                                for j in range(len(wordsCurrent[i].Word)):
                                    abcScrambled[wordsCurrent[i].HeadY +
                                                 j][wordsCurrent[i].HeadX+j+1] = wordsCurrent[i].Word[j]
                        words[a] = ''
                        break
                elif d == 'neast':
                    if y-len(words[a]) > 0 and x+len(words[a])+1 < width and canIntersect(words[a], x, y, d) == True:
                        wordBank.append(words[a])
                        if randint(0, 2) == 0:
                            words[a] = words[a][::-1]
                        wordsCurrent.append(
                            Word(x, x+len(words[a])-1, y, y-len(words[a])+1, words[a], d))
                        for i in range(len(wordsCurrent)):
                            if wordsCurrent[i].Direction == d:
                                for j in range(len(wordsCurrent[i].Word)):
                                    abcScrambled[wordsCurrent[i].HeadY -
                                                 j][wordsCurrent[i].HeadX+1+j] = wordsCurrent[i].Word[j]
                        words[a] = ''
                        break
    for m in range(20):
        for n in range(27):
            if abcScrambled[m][n] == ' ':
                abcScrambled[m][n] = abc[randint(0, 25)]
                # abcScrambled[m][n]='.'


def draw():
    global words
    global wordsCurrent
    global abc
    global abcScrambled
    global width
    global height
    x = 0
    y = 0
    system('cls')
    print('                      Search word\n   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n   ____________________________________________________')
    while y < height:
        if x == 0:
            if y > 9:
                print('%d' % (y), end='')
            else:
                print(' %d' % (y), end='')
        if x == 0 or x-1 == width:
            print('|', end='')
        else:
            print(abcScrambled[y][x], end=' ')
        if x-1 == width:
            y += 1
            x = -1
            if y % 2 == 0:
                print('\033[0;37;48m')  # white / no bold
            else:
                print('\033[1;36;48m')  # blue / bold
        x += 1
    print('  |____________________________________________________|')
    # Draw the bank
    for x in wordBank:
        print('%d.- ' % (wordBank.index(x))+x, end='')
        for n in range(15-len(wordsCurrent[wordBank.index(x)].Word)):
            print('', end=' ')
        if (wordBank.index(x)+1) % 3 == 0:
            print('')
    print('\nOther options:\n[R] Reshuffle      [Q] Quit')


def input_():
    global inp
    while True:
        inp = input(
            '\nExample of a valid input: C16-H11\nEnter a range of letters from left to right: ')
        if inp == 'R':
            call(executable + ' "' + path.realpath(__file__) + '"')
        elif inp == 'Q':
            exit(0)
        try:
            if inp.split('-')[0][0].isalpha() == True and inp.split('-')[0][1].isdecimal() == True and inp.split('-')[1][0].isalpha() == True and inp.split('-')[1][1].isdecimal() == True:
                break
        except:
            pass


def logic():
    global wordsCurrent
    global inp
    global abcScrambled
    global wordBank
    global wordsFinded
    global gameOver
    hx = abc.index(inp[0].casefold())
    hy = int(inp.split('-')[0][1:])
    tx = abc.index(inp.split('-')[1][0].casefold())
    ty = int(inp.split('-')[1][1:])
    # print('('+str(hx)+','+str(hy)+') ('+str(tx)+','+str(ty)+')')
    for i in range(len(wordsCurrent)):
        if wordsCurrent[i].HeadX == hx and wordsCurrent[i].HeadY == hy and wordsCurrent[i].TailX == tx and wordsCurrent[i].TailY == ty:
            wordsFinded += 1
            wordBank[i] = '\033[1;33;48m'+wordBank[i]+'\033[0;37;48m'
            for j in range(len(wordsCurrent[i].Word)):
                if wordsCurrent[i].Direction == 'east':
                    if wordsCurrent[i].HeadY % 2 == 0:  # when its white
                        abcScrambled[wordsCurrent[i].HeadY][wordsCurrent[i].HeadX+j+1] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY][wordsCurrent[i].HeadX +
                                                                j+1]+'\033[0;37;48m'
                    else:
                        abcScrambled[wordsCurrent[i].HeadY][wordsCurrent[i].HeadX+j+1] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY][wordsCurrent[i].HeadX +
                                                                j+1]+'\033[1;36;48m'
                if wordsCurrent[i].Direction == 'south':
                    if (wordsCurrent[i].HeadY+j) % 2 == 0:  # when its white
                        abcScrambled[wordsCurrent[i].HeadY+j][wordsCurrent[i].HeadX+1] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY +
                                         j][wordsCurrent[i].HeadX+1]+'\033[0;37;48m'
                    else:
                        abcScrambled[wordsCurrent[i].HeadY+j][wordsCurrent[i].HeadX+1] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY +
                                         j][wordsCurrent[i].HeadX+1]+'\033[1;36;48m'
                if wordsCurrent[i].Direction == 'seast':
                    if (wordsCurrent[i].HeadY+j) % 2 == 0:  # when its white
                        abcScrambled[wordsCurrent[i].HeadY+j][wordsCurrent[i].HeadX+1+j] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY +
                                         j][wordsCurrent[i].HeadX+1+j]+'\033[0;37;48m'
                    else:
                        abcScrambled[wordsCurrent[i].HeadY+j][wordsCurrent[i].HeadX+1+j] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY +
                                         j][wordsCurrent[i].HeadX+1+j]+'\033[1;36;48m'
                if wordsCurrent[i].Direction == 'neast':
                    if (wordsCurrent[i].HeadY+j) % 2 == 0:  # when its white
                        abcScrambled[wordsCurrent[i].HeadY-j][wordsCurrent[i].HeadX+1+j] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY -
                                         j][wordsCurrent[i].HeadX+1+j]+'\033[0;37;48m'
                    else:
                        abcScrambled[wordsCurrent[i].HeadY-j][wordsCurrent[i].HeadX+1+j] = '\033[1;33;48m' + \
                            abcScrambled[wordsCurrent[i].HeadY -
                                         j][wordsCurrent[i].HeadX+1+j]+'\033[1;36;48m'
    if wordsFinded == 11:
        gameOver = True


def main():
    setup()
    while gameOver == False:
        draw()
        input_()
        logic()
        # break


main()
