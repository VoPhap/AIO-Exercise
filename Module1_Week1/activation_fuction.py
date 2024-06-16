import math



def is_number ( x ):
    try :
       float ( x )  # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
       return False
    return True

def calc_activation_func (x , act_name ):
    # Kiểm tra x có hợp lệ không
    if not is_number(x):
        print('x must be a number')
        return
    
    # Chuyển đổi x sang kiểu float
    x = float(x)
    
    # Thực hiện tính toán theo hàm kích hoạt tương ứng
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        if x > 0:
            return x
        else:
            return 0
    elif act_name == 'elu':
        alpha = 0.01
        if x>0:
            return x
        else:
            return alpha*((math.e(x))-1)
        # Kiểm tra tên hàm kích hoạt có hợp lệ không
    else:
        return print(f'{act_name} is not supported')
        
    
assert calc_activation_func ( x = 1 , act_name ='relu') == 1
print ( round ( calc_activation_func (x = 3 , act_name =sigmoid) , 2) )