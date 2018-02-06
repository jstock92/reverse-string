import sys

def main():
    string =''
    for i in sys.argv[1:]:
        string = string+' '+i
    print (string)[::-1]

if __name__ == "__main__":
    # sys.exit(main())
    main()