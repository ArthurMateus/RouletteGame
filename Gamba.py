from random import randint
from time import sleep
import os
from colorama import Fore

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def randomchar():
    chars = ['a','b','c','d','e','f','g','h','i','l']
    rng = chars[randint(0,9)]
    return rng

def rows():
    print(f'{randomchar()} | {randomchar()} | {randomchar()}')

def main():
    while True:
        wl = ''
        winamt = 0
        
        print(Fore.CYAN)
        print('Welcome to the Slot Machine!')
        print(Fore.GREEN)
        pa = int(input('Enter the amount of times you want to play: '))
        print("Let's start!")
        sleep(1)

        for c in range(1,pa):
            v1 = randomchar()
            v2 = randomchar()
            v3 = randomchar()
            cls()
            print(Fore.RED)
            rows()
            rows()
            
            print(Fore.MAGENTA + f'{v1} | {v2} | {v3} <-')
            if v1 == v2 and v2 == v3:
                print(Fore.BLUE)
                wl = print('You won!')
                sleep(2)
                winamt += 1
            else:
                print(Fore.RED)
                wl = print('You Lost!')
            sleep(0.4)
        print(Fore.YELLOW)
        print(f'You played {pa} times')
        print(f'You won {winamt} times')
        print(Fore.WHITE)
        yorn = str(input('Do you want to play again? [Y/N]'))
        if yorn.upper() == 'N':
            break
        
    

main()