import numpy as np
import random


def generate_fibonacci_vocab(fib_count_req: 'int') -> 'list':
    '''Function generates fibonacci numbers 
    for the count recieved as argument'''
    fibonacci_numbers = [0, 1]
    for i in range(2, fib_count_req):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return fibonacci_numbers


def check_fibonacci_number(choice_num: 'int', fib_vocab: 'list') -> 'list':
    '''Function checks if a number provided as choice_num
    argument is a fibonacci number or not. fib_vocab is list
    used for comparison'''
    return list(map(lambda x: "Fib_num" if (x in fib_vocab) else "Not Fib_num", choice_num))


def iter_1_even_iter_2_odd_addition(iter_1: 'list', iter_2: 'list') -> 'list':
    '''Function which picks even number from iter_1 list and 
    adds it with odd number from iter_2 list.Output is a list'''
    return [num_a+num_b for num_a in iter_1 for num_b in iter_2 if num_a % 2 == 0 and num_b % 2 == 1]


def strip_vowel(word: 'str') -> 'str':
    '''Function which strips every vowel from a string provided'''
    return ' '.join([char for char in word if char not in ['a', 'e', 'i', 'o', 'u']])


def sigmoid_func_1d_array(arr: 'list') -> 'list':
    '''Function acts like a sigmoid function for a 1D array'''
    return 1/(1 + np.exp(-arr))


def char_shift(ref_str: 'str', shift: 'int') -> 'str':
    '''Function takes a small character string and shifts 
    all characters by 5 (handle boundary conditions) tsai>>yxfn'''
    ref_str = [i for i in ref_str.lower()]
    return ''.join([chr(((ord(i)+5) % 123)+97) if (ord(i)+shift) > 122 else chr((ord(i) % 123)+shift) for i in ref_str])


def swear_word_check(ref_vocab, ref_text: 'str') -> 'bool':
    '''Function uses list comprehension expression that takes a ~200-word paragraph, 
    and checks whether it has any of the swear words mentioned in github link shared'''
    swear_word_present = any(
        [True if ref_words in ref_vocab['Words'].values else False for ref_words in ref_text.split()])
    return "Swear word present in input paragraph"if swear_word_present else "Swear word not present in input paragraph"


def even_num_sum(ref_even_check_list: 'list') -> 'int':
    '''This is a reduce function implementation.
    Function add only even numbers in a list'''
    return sum(num for num in ref_even_check_list if num % 2 == 0)


def biggest_char_in_string(asc_ref: 'str') -> 'str':
    '''This function finds the biggest character in a 
    string (printable ASCII characters)'''
    return chr(max(ord(char) for char in asc_ref))


def third_num_sum(ref_third_num_add_lst: 'list') -> 'int':
    '''Function adds every 3rd number in a list'''
    return sum(num for num in ref_third_num_add_lst if num % 3 == 0)


def generate_random_number_plates(cnt: 'int') -> 'list':
    '''Function generates 15 random KADDAADDDD number plates, where KA is fixed, 
    D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 
    1000<<DDDD<<9999'''
    return ['KA'+str(random.randint(10, 99))+np.random.choice([chr(char) for char in range(ord('A'), ord('Z')+1)])+np.random.choice([chr(char) for char in range(ord('A'), ord('Z')+1)])+str(random.randint(1000, 9999)) for num in range(cnt)]


def number_plate(st_num_range: 'int', end_num_range: 'int', state: 'str') -> 'str':
    '''This function considers KA can be changed to DL, and 1000/9999 ranges can be 
    provided and utilizes partial function such that 1000/9999 are hardcoded, 
    but KA can be provided'''
    alph_1 = np.random.choice([chr(char)
                              for char in range(ord('A'), ord('Z')+1)])
    alph_2 = np.random.choice([chr(char)
                              for char in range(ord('A'), ord('Z')+1)])
    four_dgt = str(random.randint(st_num_range, end_num_range))
    return state+str(random.randint(10, 99))+alph_1+alph_2+four_dgt
