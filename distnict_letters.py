def getString(string):
    # adjust the comming string
    if string == '{}':
        return 0
    str2 = set(string.strip('{').strip('}').split(','))
    return len({char.strip() for char in str2})

if __name__ == '__main__':
    string = input()

    print(getString(string))