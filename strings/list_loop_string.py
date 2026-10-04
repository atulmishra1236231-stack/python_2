my_list = ['a']*6


my_string = ''
# this is simply a bad python code
for i in my_list:
    my_string+=i

print(my_string)

#good way to do it 

my_string = ''.join(my_list)
print(my_string)