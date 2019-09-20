password = 'a12345'
input_cnt = 1
print("input 'q' if you want to quit" )
while input_cnt <= 3:
    user_input = input('please input 6 digits for password: ')
    if user_input == password:
        print('log in sucessfully')
    elif user_input == 'q':
        break
    else:
        print('please try again')

    print('you already input '+ str(input_cnt)+' times')
    input_cnt +=1
