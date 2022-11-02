#足し算

def add(x, y):

    return x + y

 

#引き算

def subtract(x, y):

    return x - y

 

#掛け算

def multiply(x, y):

    return x * y

 

#割り算

def divide(x, y):

    return x / y

 

#メイン処理

if __name__ == '__main__':

 

    #変数を設定

    number_one = 32

    number_two = 16

 

    #足し算

    print(add(number_one, number_two))

 

    #引き算

    print(subtract(number_one, number_two))

 

    #掛け算

    print(multiply(number_one, number_two))

    

    #割り算

    print(divide(number_one, number_two))