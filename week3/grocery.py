   

def main():
    # an empty dictionary to store user input
    user_item = {}

    while True:
        try:
            item = input("") 

            # checks if the item is in the dictionary and increments by 1 if it is
            if item in user_item:
                user_item[item] += 1
            else:
                # assigns the number 1 to the item if not in the dictionary
                user_item[item] = 1

        except KeyError:
            pass

        # does the following code when user press control z 
        except EOFError:

            # .items() method provides an iterable of tuples representing key-value pairs    
            sort_item = sorted(user_item.items())

            # iterates over each item and its count in the sorted dictionary
            for item, count in sort_item:
                print(f"{count} {item.upper()}")
            
            # breaks out of the loop after running the above code when end of error is caught
            break


main() 

