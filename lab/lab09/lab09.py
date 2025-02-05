import sys


def print_args(args):
    i = 0
    while i < len(args):
        print(args[i])
        i += 1


def check_arg(args):
    return args[1] == "-p" or args[1] == "-i" or args[1] == "-h" or args[1] == "-w" or args[1] == "-r"


def flags(args):
    if check_arg(args):

        if args[1] == "-p":
            print_args(args[2:])

        elif args[1] == "-i":
            print("Hello World")

        elif args[1] == "-h":
            print(f"""Valid flags:
-p : prints out all the command line arguments after the -p
-i : prints "Hello World"
-h : prints out a help command""")

        elif args[1] == "-w":
            if len(args) < 3:
                print("No File Provided")
            elif len(args) < 4:
                print("No Content Provided")
            else:
                with open(f"{args[2]}", "w") as file:
                    i = 3
                    while i  < len(args):
                        file.write(f"{args[i]}\n")
                        i += 1

        elif args[1] == "-r":
            if len(args) < 3:
                print("No File Provided")
            elif len(args) > 4:
                print("Unexpected Additional Arguments")
            else:
                with open(f"{args[2]}", "r") as file:
                    print(file.read())

    else:
        print_args(args)

flags(sys.argv)