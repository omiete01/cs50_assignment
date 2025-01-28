# checking fuel guage

def main():
    while True:
        try:
            fraction = input("Fraction: ") 

            # splits user input, stores it in 2 variables and converts them to integer
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            # checks for value error and zero division error
            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError
            
            # calculate the percentage of user input
            percentage = round((x / y) * 100)
            
            # tagging the percentage: (E) stands for empty and (F) stands for full
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        # skips when there is a value error or zero division error    
        except (ValueError, ZeroDivisionError):
            pass

main()
