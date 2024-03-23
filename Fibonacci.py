def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

while True:
    n = int(input("Digite o número de termos da sequência de Fibonacci que deseja gerar (ou digite 0 para sair): "))
    
    if n == 0:
        print("Saindo do programa...")
        break
    
    fibonacci_sequence = fibonacci(n)
    print("A sequência de Fibonacci para os primeiros", n, "termos é:")
    print(fibonacci_sequence)
