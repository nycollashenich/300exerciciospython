def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
num = int(input('Digite o número para o Fibonacci: '))
resposta = fibo(num - 1)
print(resposta)