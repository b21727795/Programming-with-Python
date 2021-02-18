import time
import sys

def create_vocabulary(file_path):
    #Create shuffled letters -correct words pairs
    words_dict = {}
    
    word_file = open(file_path,'r')
    for line in word_file:
        pair = line.strip().split(':')
        correct_words = [x.lower() for x in pair[1].split(',')] #The input can be mixed upper or lowercase letters.
        words_dict[pair[0]] = correct_words                     #While comparing, I make a comparison by converting them to lowercase letters.
    word_file.close()
    return words_dict    

def set_letter_values(file_path):
    #Create letter-value pairs
    letter_values_dict = {}
    
    letter_file = open(file_path,'r')
    for line in letter_file:
        pair = line.strip().split(':')
        letter_values_dict[pair[0]] = pair[1]
    
    letter_file.close()
    return letter_values_dict

def calculate_score(correct_word,letter_values_dict):
    
    score = 0
    for letter in correct_word:
        score += int(letter_values_dict[letter])
    return len(correct_word) * score


def game_flow(words_dict,letter_values_dict):
    game_score = 0
    
    for shuffled_letters,correct_words in words_dict.items():
        
        round_score = 0
        guessed_words_list = list()
        
        print('Shuffled letters are : {} Please guess words for these letters with minimum three letters'.format(shuffled_letters))
        start_time = time.time()
        elapsed = 0
        while (elapsed <= 30):
            guessed_word = input('Guessed Word: ').lower()
            if (len(guessed_word) >= 3):
                
                if (guessed_word not in correct_words):
                    print('Your guessed word is not a valid word')
                
                elif (guessed_word in guessed_words_list):
                    print('This word is guessed before')
                else:
                    elapsed = time.time() - start_time
                    if(30 - elapsed >= 0):
                        round_score += calculate_score(guessed_word.upper(),letter_values_dict)
                        guessed_words_list.append(guessed_word)
            else:
                print('Guessed word length should be bigger or equal than 3')
            
            elapsed = time.time() - start_time
            if (30 - elapsed <= 0 ):
                print('You have {} sec! Your time is up'.format(0))
            else:
                print('You have {} sec to finish this round'.format(30 - elapsed))
        print('Score for {} is {} and True Guessed Words are : {}'.format(shuffled_letters,str(round_score),'-'.join(guessed_words_list)))
        game_score += round_score
    
    print('End of the Game!\nTotal Game Score is {}'.format(game_score))
    
def main(correct_words_file_path,letter_values_file_path):
    
    words_dict = create_vocabulary(correct_words_file_path)
    letter_values_dict = set_letter_values(letter_values_file_path)
    
    game_flow(words_dict,letter_values_dict)

if __name__ == '__main__':
    try:
        correct_words_file_path = sys.argv[1]
        letter_values_file_path = sys.argv[2]
        main(correct_words_file_path,letter_values_file_path)
    except IndexError:
        print('You must write to arguments for this program')
    