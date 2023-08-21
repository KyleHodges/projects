def main():

    shopping = []
    final = {}

    while True:
        try:
            item = input()
            shopping.append(item)
        except EOFError:
            print()
            break

    shopping.sort()
    for item in shopping:
        if item in final:
            final[item] += 1
        else:
            final[item] = int(1)
    for row in final:
        print(final[row], row.upper())

main()