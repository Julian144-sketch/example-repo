# Create a new Python file in this folder called pattern.py.
# Write code to output the arrow pattern shown below 
# using an if-else statement in combination with a for loop


# You are allowed to use more than one for loop. 
# But use only one for loop if you wish to challenge yourself):

n = 9
for i in range(n):
    if i < 5:
        print('*' * (i + 1))
    else: 
        print('*' * (n - i))