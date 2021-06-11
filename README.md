# Assignment 6 on First Class Functions
- Submission by Lohith G N (EPAI batch 3)

### Summary of assignment

Assignment 1
1. Write a single expression that includes lambda, zip, and map functions to select create 52 cards in a deck - 50 pts
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 100 pts
Basics (applicable to 2/3 above):

Assignment 2
1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:50
2. Using list comprehension (and zip/lambda/etc if required) write expressions that: PTS: 100
add 2 iterables a and b such that a is even and b is odd
3. strips every vowel from a string provided (tsai>>t s)
acts like a sigmoid function for a 1D array
takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
4. A list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:100 (Links to an external site.)
5. Using reduce function: PTS:100
add only even numbers in a list
6. find the biggest character in a string (printable ASCII characters)
adds every 3rd number in a list
7. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
8. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided 


### The rules of the games

1. Players can get either of 3, 4 or 5 cards.
2. 2 players play the game
3. Once receiving the game, both the players should their cards
4. The winner is decided on the basis of the order shown in the image above i.e. Royal Flush is superior to all, straight flush is superior to all except royal flush and so on.
   
Based on the Rules I have deviced a very simple algorithm:

### Algorithm

1. First we generate a deck either by the list, map and lambda functions. 
2. Then we shuffle the deck of card and randomly select either3, 4 or 5
3. we distribute the cards
4. The player shows the card
5. Each hand is processed under process function which calls in transform function
6. Transform function converts the cards like ace,king, queen and jack to numeric value(easy for evaluation)
7. under the process function
   1. we first check if the colors of all the cards are same or not
      1. if they are same we check for sequence
         1. if sequence is same, we match it with royal flush sequence, if true we return 1,14 (1 represents the listing from the image and 14 is the max value of the array corresponding to ace)
         2. else we return 2, max(hand) (straight flush)
      2. else we return 5, max(hand) (flush)
   2. else we check for sequence
      1. if true, then we return 6,max(hand) (straight)
      2. else we do a count of each number i.e. how many times they are being repeated and we sort them from higher to lower, then we check for length of the hand as algorithm now is specifically developed for ecah hand
         1. if length is 5
            1. we count the number of repeating elements, if a number is repeated 4 times we return 3,number (4 of a kind)
            2. else if a number is repeated 3 time, we check for the next number count
               1. if the next number count is 2, we return 4, number(having count of 3) (Full House)
               2. else we return 7, number(3 of a kind)
            3. else if the number is repeated 2 times, we check the count of the other number
               1. if the other number is also 2, we return 8, max(both the numbers) (2 pairs)
               2. else we return 9, number (1 pair)
            4. else we return 10,max(hand)
         2. if the length is 4
            1. we count the number of repeating elements, if a number is repeated 4 times we return 3,number (4 of a kind)
            2. else if a number is repeated 3 time, we return 7, number(3 of a kind) as here full house doesnt makes sense in 4 cards
            3. else if the number is repeated 2 times, we check the count of the other number
               1. if the other number is also 2, we return 8, max(both the numbers) (2 pairs)
               2. else we return 9, number (1 pair)
            4. else we return 10,max(hand)
         3. else if the number is 3:
            1. we check if a number is repeated 3 time, we return 7, number(3 of a kind)  as here full house and 4 at a time doesnt makes sense in 3 cards
            2. else if the number is repeated 2 times, we return 9,number as 2 of a kind doesnt makes sense in 3 cards
            3. else we return 10, max(hand)
8. Then once we get these tuples values, we check if the first element is greater of player 1 than player 2, then player 2 wins else vice versa.
9. if both have same, then we check the max value, i.e. the second element, so here if the second element of player 2 is more than the first player then second player wins and vice versa
10. if both the players have same secopnd value, then the game ends in a draw.

### Functions in Part 1

|SR No. | Name | Functionality |
|--- | --- | --- |
|1 | generate_deck_using_lambda_zip_map | This function takes in suits and values as input and returns the combined deck using lambda_zip_map as backend|
|2 |generate_deck_normal| This function takes in suits, values and deck as input and returns the combined deck using loops as backend|
|3 |poker_x_teen_patti | This function takes in deck and total cards in hand as input, it calls show function in it. The function returns result as an output|
| 4| show | This Function takes in hands as input, i.e. set1 and set2. It internally calls process function which return result tuple. This function then computes the final result and returns that result.|
| 5| process | This function takes in list as an input, computes which category the hand falls in and returns the category | 
| 6| transform_value_list | This function takes in list as input  i.e. hand of the player and converts the list into int datatype and returns that list back| 
|7|check_for_color | This function takes in list as input i.e. the suits of the hand and checks whether they are same or not|
| 8 |check_for_number_sequence | This function takes in list an input (the hand of the player), then it checks whether it is in sequence or not | 

### TestCases

Here we have written a lot of testcases to check each functionality thoroughtly as out code shouldnt be breaking. 
To test each combination for each type of hand I have written a test for each, so the test cases in format ```test_show_for_3_for_6_v_10``` represents for hand length of 3 for combination of player 1 having a hand of straight and player 2 having a hand of high card and we check the result. Rest of the test cases are self explanatory.

### Functions in Part 2

|SR No. | Name | Functionality |
|--- | --- | --- |
|1 | generate_fibonacci_vocab | This function takes in int and generates fibonacci numbers based on the 
input. Output is a list of fibonacci numbers|
|2 |check_fibonacci_number| This function checks if the number passed is a fibonacci number or not|
|3 |iter_1_even_iter_2_odd_addition | This function 2 iterable list and adds even number from first and odd number from second list|
| 4| strip_vowel | This Function takes out all vowels from string passed and returns|
| 5| sigmoid_func_1d_array | This function will calculate sigmoid values for 1 d array and publishes result in a list format | 
| 6| char_shift | This function will shift teh characters by the number of positions that are passed to the function| 
|7|swear_word_check | This function checks if google provided swear words are present in the paragraph passed.|
| 8 |even_num_sum | This function sums up all even numbers in a list passed | 
| 9 |biggest_char_in_string |This function finds the biggest character in a 
string (printable ASCII characters) | 
| 10 |third_num_sum | This Function adds every 3rd number in a list |
| 11 |generate_random_number_plates | This Function Function generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 
1000<<DDDD<<9999 |
| 11 |number_plate | This function considers KA can be changed to DL, and 1000/9999 ranges can be 
provided and utilizes partial function such that 1000/9999 are hardcoded, 
but KA can be provided |