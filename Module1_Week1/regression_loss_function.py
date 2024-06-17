import math
import random

def mae(n):
    mae = 0
    for i in range(n):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        abs_mae = abs(y-y_hat)
        mae = mae + abs_mae
        print (f'y: {y}, y_hat: {y_hat}, mae: {mae}')
    mae = mae/n
    return mae

def mse(n):
    mse = 0
    for i in range(n):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        sqr_mse = (y-y_hat)**2
        mse = mse + sqr_mse
        print (f'y: {y}, y_hat: {y_hat}, mse: {mse}')
    mse = mse/n
    return mse    

def rmse(n):
    rmse = 0
    for i in range(n):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        sqr_rmse = (y-y_hat)**2
        rmse = rmse + sqr_rmse
        print (f'y: {y}, y_hat: {y_hat}, rmse: {rmse}')
    rmse = math.sqrt(rmse/n)
    return rmse    

def is_number (n):
    try :
       int (n)  # Type - casting the string to ‘int‘.
                    # If string is not a valid ‘int ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
       return False
    return True

def regression_loss (loss_name, n):
   # Kiểm tra x có hợp lệ không
    if not is_number(n):
        print('number of samples must be an integer number')
        return

    # Chuyển đổi num_samples từ chuỗi thành số nguyên
    n = int(n)    
    
    # Lựa chọn hàm tính loss dựa vào tên và tính toán
    if loss_name == 'mse':
        return mse(n)
    elif loss_name == 'mae':
        return mae(n)
    elif loss_name == 'rmse':
        return rmse(n)
    

