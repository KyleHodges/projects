import sys
from datetime import date, time
import inflect


p = inflect.engine()

def main():
    saying = convert(input('Date of Birth: '))

    print(saying.capitalize(), "minutes")
def convert(s):
    try:
        birthday = date.fromisoformat(s)
        today = date.today()
        days = today - birthday
        minutes = days.days * 1440
        words = p.number_to_words(int(minutes), andword='')

        return words

    except: ValueError(sys.exit('Invalid date'))





...



if __name__ == "__main__":
    main()