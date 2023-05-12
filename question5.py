message = input("Enter the message to hack:")
n_key = 1
while n_key > 0:
    new_message = ''
    for i in message :
        if i == 'A' :
            new_message += 'Z'
        elif i == 'B' :
            new_message += 'A'
    print(message, len(message))
    print(new_message), len (new_message) 
    n_key -= 1
    
