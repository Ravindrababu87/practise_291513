command=""
started = False
while True:
    command=input('=> ').lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("car started")

    elif command == "stop":
        if  not started:
            print("car is already stopped")
        else:
            started= False
            print("car stopped")
    elif command == "help":
        print('''
1.start
2.stop
3.quit
        ''')
    elif command == "quit":
        break
    else:
        print("i don't understand")

