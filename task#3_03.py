def hanoi(n, source, auxiliary, target, state):
    if n > 0:
        # Перемістити n-1 дисків з вихідного стрижня на допоміжний
        hanoi(n-1, source, target, auxiliary, state)
        
        # Перемістити n-ий диск з вихідного стрижня на цільовий
        state[target].append(state[source].pop())
        print(f"Перемістити диск з {source} на {target}: {n}")
        print(f"Проміжний стан: {state}")
        
        # Перемістити n-1 дисків з допоміжного стрижня на цільовий
        hanoi(n-1, auxiliary, source, target, state)

def main():
    n = int(input("Введіть кількість дисків: "))
    
    # Початковий стан стрижнів
    state = {
        'A': list(range(n, 0, -1)),  # Від найбільшого до найменшого
        'B': [],
        'C': []
    }
    
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
