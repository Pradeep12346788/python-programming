binary_values=['1010','1111','1101']
int_values=[int(value,2)for value in binary_value]
max_value=int_value[0]
for value in int_values[1:]:
    if value>max_value:
        max_value=value
         max-binary=bin(max_value)[2:]
        print("the max binary value is:",max_binary)
