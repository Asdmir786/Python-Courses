# Sample list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Using enumerate to access the index and value
for index, value in enumerate(my_list, start=1):
    if index in [3, 5, 7]:  # Check for third, fifth, and seventh elements
        print(f'Element {index}: {value}')
