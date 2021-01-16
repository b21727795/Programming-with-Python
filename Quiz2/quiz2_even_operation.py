import sys


def choose_evens(input_string):
    evens = [int(element) for element in input_string.split(',') if(int(element)> 0 and int(element) % 2 == 0) ]
    all_numbers = [int(element) for element in input_string.split(',') if int(element)> 0]
    even_number_rate = sum(evens) / sum(all_numbers)
    
    print("Even Numbers: "+'"'+','.join([str(x) for x in evens])+'"')
    print("Sum of Even Numbers:", str(sum(evens)))
    print("Even Number Rate:{:.3f}".format(even_number_rate))

def main(input_string):
    choose_evens(input_string)

if  __name__ == "__main__":
    main(sys.argv[1])