import sys

def main():

    h = int(sys.argv[1]) #height
    #diamond contains two part up and down. Left list up part ,right list is down part.Concatanate them and print
    all_stars = [print(star) for star in [" "*(h-i)+ "*"*(i*2+1) for i in range(h)] + [" "*(h-i) + "*"*(i*2+1) for i in range(h-2, -1, -1)]]

if  __name__ == "__main__":
    main()