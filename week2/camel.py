# assignment on camel case

def main():
    camel_case = input("camelCase: ")
    print(f"snakeCase: {snake_case(camel_case)}")

def snake_case(s):
    # creates a new string where if the character is uppercase, its seperated by underscore
    snake = "".join(["_"+c.lower() if c.isupper() else c for c in s])
    if snake.startswith("_"):
        return snake[1:] 
    else:
        snake
    return snake

main()
