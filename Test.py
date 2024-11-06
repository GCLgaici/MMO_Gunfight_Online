import random
import time

def Progress(pr, Max):
    print("进度",
          f' |{"▇" * ((pr + 1) * 60 // Max):60}|',
          f"{(pr + 1) * 100 // Max}%",
          end="\r")

def main():
    x = 10000
    for i1 in range(x):
        print(f"{i1}ip爬取中\n")
        for i2 in range(x):
            Progress(i2, x)
            if random.randint(1, 100000) == 1:
                for i3 in range(x*100000):
                    ...
                    ...




if __name__ == '__main__':
    main()
