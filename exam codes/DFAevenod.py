def is_even(num_str):
    
    transition = {
        'even': {'0': 'even', '1': 'odd', '2': 'even', '3': 'odd', '4': 'even', '5': 'odd', '6': 'even', '7': 'odd', '8': 'even', '9': 'odd'},
        'odd': {'0': 'odd', '1': 'even', '2': 'odd', '3': 'even', '4': 'odd', '5': 'even', '6': 'odd', '7': 'even', '8': 'odd', '9': 'even'}
    }
    
    
    state = 'even'
    
    
    for digit in num_str:
        state = transition[state][digit]
    
    
    if state == 'even':
        print(num_str, 'is even')
    else:
        print(num_str, 'is odd')
#main
is_even('1234')