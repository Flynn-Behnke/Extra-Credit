#1
def splitname(fullname):
  name_parts = fullname.split(' ')
  
  fname = name_parts[0]
  lname = name_parts[1]
  finitial = fname[0]

  output = lname + ', ' + finitial + '.'
  return output
fullname = str(input('Enter first and last name. Example "John Smith" : '))

print(splitname(fullname))

#2
def reverse(phrase):
  phrase = phrase.strip()
  phrase = phrase.replace(' ',' ')
  words = phrase.split(' ')
  words = [word.strip() for word in words]
  phrase = ' '.join(words)

  for i in range(len(phrase)-1, -1, -1):
    print(phrase[i], end='')
  print()

phrase = str(input("Enter a line of text: "))
reverse(phrase)

#3
def clean(input3):
  values = input3.split(',')
  
  for value in values:
    value = value.strip()
    print(value)

input3 = str(input("Enter values separated by commas: "))
clean(input3)

#4
def shift_text(input_string, num_chars, num_lines, direction):
  num_repeats = num_chars // len(input_string) + 1

  input_string = input_string * num_repeats
  for i in range(num_lines):
    if direction == 'left':
      output_string = input_string[1:] + input_string[0]
    elif direction == 'right':
      output_string = input_string[-1] + input_string[:-1]
    
    print(output_string)
    
    input_string = output_string
    
input_string = input('Enter a line of text: ')

num_chars = int(input('Enter the number of characters to print in each line: '))

num_lines = int(input('Enter the number of lines to be printed: '))

direction = input('Enter a scroll direction (right or left): ')

shift_text(input_string, num_chars, num_lines, direction)
