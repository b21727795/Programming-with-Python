import sys

def discriminant(a,b,c): 
    return (b**2) - (4 * a * c);

def calculate(a,b,c,isTwo):
    if(isTwo):
        print("Solutions: ",(-b + (discriminant(a,b,c) ** (1/2))) / (2 * a),(-b - (discriminant(a,b,c) ** (1/2))) / (2 * a))
    else:
        print("Solution: ",(-b + (discriminant(a,b,c) ** (1/2))) / (2 * a))
def find_root(a,b,c):
    
    if (discriminant(a,b,c) > 0):
        print("There are two solutions: ")
        calculate(a,b,c,True)
    
    elif (discriminant(a,b,c) == 0):
        print("There is only one solution: ")
        calculate(a,b,c,False)
    else:
        print("There is no solution in Real numbers")

def main(a,b,c):
    find_root(int(a),int(b),int(c))

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])