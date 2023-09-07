import random
from wordlist import word_list
from artwork import stages,logo

print(logo)
empty_list = []
empty_str= " "
updated_str = ""
level = len(stages) - 1
random_word = random.choice(word_list)
for _ in range(len(random_word)):
    empty_list.append("_ ")
while ( updated_str != random_word ):
  print(empty_str.join(empty_list))
  # print(random_word)  
  guess_letter = input("Guess a letter: ").lower()
  if(guess_letter in random_word):
    print(stages[level])
    for x in range(len(random_word)):
      if(random_word[x] == guess_letter):
        empty_list[x] = guess_letter
  else:
    level -= 1
    print(stages[level])      

  test_str = empty_str.join(empty_list)
  updated_str = "".join(test_str.split())

  if(level == 0):
    print("GAME OVER !! TRY AGAIN")
    break
  elif(updated_str == random_word):
    print(updated_str)
    print("Congratulations !! YOU WON ")
  # print(updated_str)