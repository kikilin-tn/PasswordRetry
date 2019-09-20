password = 'a12345'
input_cnt = 3

while input_cnt > 0:
    user_input = input('please input 6 digits for password: ')
    if user_input == password:
        print('log in sucessfully')
        break
    else:
        input_cnt = input_cnt - 1
    if input_cnt > 0:
        print('remain '+ str(input_cnt)+' times')
    else:
        print('input count is over 3 times')
