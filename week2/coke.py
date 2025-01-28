
def main():
    # starting with the number 50
    amount_due = 50
    # while the amount due is less than 51, do the following
    while amount_due < 51:

        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: "))
        # makes sure the user inputs coins in 5, 10 and 25 denominations
        if insert_coin in [5, 10, 25]:
            amount_due = amount_due - insert_coin
        else:
            continue

        # breaks out of the loop when amount is less than and equal to 0 displaying the remaining change
        if amount_due < 0:
            # abs converts negative numbers to positive
            print(f"Change Owed: {abs(amount_due)}")
            break
        elif amount_due == 0:
            print(f"Change Owed: {amount_due}")
            break

main()
