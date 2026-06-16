def diary():
    import datetime
    print('Welcome to your Diary')
    print("Press E to create a new entry")
    print("Press V to view all previous entries")
    command = input('> what would you like to do? ')
    if command.upper() == 'E':
            print('This is a new entry')
            print(datetime.datetime.now())
            date_time = str(datetime.datetime.now())
            entry = input('> ')
            f = open('diaryentry.txt', 'a')
            f.write(date_time)
            f.write('\n')
            f.write(entry)
            f.write('\n')
            f.write('-')
            f.close()

    elif command.upper() == 'V':
        print('These are all the entries')
        with open("diaryentry.txt", 'r') as f:
            content = f.read()
            print(content)
diary()