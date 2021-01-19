import sys

def star(n,k,bool):
    if(n == 0 and bool == False):
        star(n+2,k-4,True)
        return
    if(bool == False):
        print(' ' * (n - 1) + '*' * k )
        star(n-1,k+2,False)
    if(k==-1 and bool == True):
        return
    if(bool == True):
        print(' ' * (n - 1) + '*' * k )
        star(n+1,k-2,True)
def main():
    n = int(sys.argv[1])
    star(n,1,False)
if  __name__ == "__main__":
    main()