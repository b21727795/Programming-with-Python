import sys

def main():
    try:
        try:
            operands_txt = open(sys.argv[1],'r')
        except IOError:
            print('IOError: cannot open {}'.format(sys.argv[1]))  
        try:
            comparison_data_txt = open(sys.argv[2],'r')
        except IOError:
            print('IOError: cannot open {}'.format(sys.argv[2]))
        
        for (op_line,comp_line) in zip (operands_txt,comparison_data_txt):
            
            try:
                print('-------------------------')
                op_line = op_line.strip().split()
                comp_line = comp_line.strip().split()
                
                div,non_div,from_,to_ = int(float(op_line[0])),int(float(op_line[1])),int(float(op_line[2])),int(float(op_line[3])) 
                
                expected_result = [str(x) for x in range(from_,to_) if(x % div == 0 and x % non_div != 0)]
                result = [str(x) for x in comp_line]
                
                print('My results : '+ ' '.join(expected_result))
                print('Results to compare : '+ ' '.join(result))
                
                assert(expected_result == result)
                print('Goool!!!')
            
            except ValueError:
                print('ValueError: only numeric input is accepted.')
                print('Given inputs : ' + ' '.join(op_line))
            except IndexError:
                print('IndexError: number of operands less than expected.')
                print('Given inputs : ' + ' '.join(op_line))
            except ZeroDivisionError:
                print('ZeroDivisionError: You can’t divide by 0.')
                print('Given inputs : ' + ' '.join(op_line))
            except AssertionError:
                print('Assertion Error: results don’t match.')
                
            except Exception :
                print('kaBOOM: run for your life!')

    except IndexError:
        print("IndexError: number of input files less than expected.")
    finally:
        print('\n˜Game Over ˜')

if __name__ == "__main__":
    main()