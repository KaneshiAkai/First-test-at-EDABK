def mini_convolution(p,q,sair,cor):
    sum = 0
    for row in range(p):
        for col in range(q):
            sum += source[row + cor][col + sair] * keras[row][col]
    return sum


m = int(input('input m:'))
n = int(input('input n:'))
p = int(input('input p:'))
q = int(input('input q:'))

if m<p or n<q:
    print('You dumb AF, GET OUT !')     
else:
    source = [[0 for i in range(m)] for i in range(n)]
    keras = [[0 for i in range(p)] for i in range(q)]
    print('Nhập vào source:')
    for row in range(m):
        for col in range(n):
            i = input(f'Nhập vào giá trị tại hàng {row+1} và cột {col+1}:')
            source[row][col] = int(i)
    print('Nhập vào keras:')
    for row in range(p):
        for col in range(q):
            i = input(f'Nhập vào giá trị tại hàng {row+1} và cột {col+1}:')
            keras[row][col] = int(i)
                    
    if m==p and n==q:
        sum = mini_convolution(p,q,0,0)
        print('Kết quả =',sum)
    else:
        result = [[0 for i in range(m-p+1)] for i in range(n-q+1)]
        cor = sair = 0
        while True:
            sum = mini_convolution(p,q,sair,cor)
            result[cor][sair] = int(sum)
            if p + sair == m:
                sair = 0
                if q + cor == n:
                    print('Trí siêu đẹp trai !!!!!!!!!!!!!!!')
                    for row in result:
                        print(row)
                    break
                cor += 1
            else:
                sair += 1
        
    
    