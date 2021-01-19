import sys

def print_messages(message_ids):
    
    output_string = ''
    message_count = 1
    for sorted_message_id in sorted(message_ids.keys()):
        output_string+= "Message {}\n".format(message_count)
        for sorted_packet in sorted(message_ids[sorted_message_id]):
            output_string+= sorted_message_id+' '+ sorted_packet[0]+' '+ sorted_packet[1]+'\n'
        message_count += 1
    return output_string


def main():
    
    with open(sys.argv[1]) as input_file:
        message_ids = {}
        for line in input_file:
            line = line.strip().split('\t')# I splited respect to tab
            if(line[0] not in message_ids.keys()):
                message_ids[line[0]] = list()
            message_ids[line[0]].append((line[1],line[2]))
    
    output_string = print_messages(message_ids)

    with open(sys.argv[2],'w') as output_file:
        output_file.write(output_string)

if  __name__ == "__main__":
    main()