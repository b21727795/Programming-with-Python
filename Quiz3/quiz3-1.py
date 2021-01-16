import sys

def seperate(summation):
    elements = list()
    sum = 0
    for element in str(summation):
        sum+= int(element)
        elements.append(element)
    print(' = '+' + '.join(elements)+' = {}'.format(sum),end='')
    if(sum >= 10):
        seperate(sum)
    
def calculate(a,b):
    summation = a ** b
    print('Output : {}ˆ{} = {} '.format(a,b,summation), end='')

    if (summation < 10):
        return
    seperate(summation)


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    calculate(a,b)
if  __name__ == "__main__":
    main()