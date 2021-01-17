import sys

def special_condition(all_elements):
    count = 0
    new_elements = list()
    for element in all_elements:
        if(count % 2 == 0):
            new_elements.append(all_elements[count])
        count+=1
    return new_elements

def make_lucky(next_index,all_elements):
    next_number = int(all_elements[next_index])
    count = 1
    new_elements = list()
    for element in all_elements:
        if(count % next_number != 0  ):
            new_elements.append(element)
        count+=1
    return new_elements

def find(curr_index,all_elements):
    print(all_elements)
    if(len(all_elements) >= int(all_elements[curr_index])):
        
        all_elements = make_lucky(curr_index,all_elements)
        find(curr_index+1,all_elements)
    
    return all_elements    
    

def main():
    input_string = sys.argv[1]
    all_elements = [element for element in input_string.split(',')]
    
    print("Output(s) : ")
    print(all_elements)
    
    all_elements = special_condition(all_elements)
    all_elements = find(1,all_elements)
    
if  __name__ == "__main__":
    main()






