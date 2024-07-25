'''
Chapter : 6 - item : 1 - Fibonacci

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive

Enter Number : 1
fibo(1) = 1
'''

index = int(input('Enter Number : '))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(index)

print(f'fibo({index}) = {result}')