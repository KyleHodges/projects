import random


def main():
    level = get_level()
    questions = 0
    score = 0
    while questions < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        j = 0
        questions += 1
        while j < 3:
            try:
                answer = int(input(f'{x} + {y} = '))
                j += 1

                if answer == result:
                    score += 1
                    break

                else:
                    if j == 3:
                        print(f'{x} + {y} = {result}')

                    else:
                        print('EEE')
                        continue

            except: ValueError
            j += 1
            print('EEE')
            if j == 3:
                print(f'{x} + {y} = {result}')

            else:
                continue

    print(f'Score: {score}')




def get_level():
    while True:
        try:
            x = int(input('Level: '))
            if x < 4 and x > 0:
                return x
        except: ValueError


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
        return n
    elif level == 2:
        n = random.randint(10, 99)
        return n
    else:
        n = random.randint(100, 999)
        return n


if __name__ == "__main__":
    main()