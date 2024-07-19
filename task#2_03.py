import turtle

# Функція для малювання однієї сторони сніжинки Коха
def koch_snowflake_side(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake_side(length, level-1)
        turtle.left(60)
        koch_snowflake_side(length, level-1)
        turtle.right(120)
        koch_snowflake_side(length, level-1)
        turtle.left(60)
        koch_snowflake_side(length, level-1)

# Функція для малювання всієї сніжинки Коха
def koch_snowflake(length, level):
    for _ in range(3):
        koch_snowflake_side(length, level)
        turtle.right(120)

# Основна функція для запуску програми
def main():
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    length = 300  # Довжина сторони сніжинки

    turtle.speed(0)  # Встановлюємо максимальну швидкість малювання
    turtle.penup()
    turtle.goto(-length / 2, length / 3)
    turtle.pendown()

    koch_snowflake(length, level)

    turtle.done()

if __name__ == "__main__":
    main()
