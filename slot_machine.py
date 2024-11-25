import random

def spin_row():
    symbols=["🍒","🍉","🍋","🔔","⭐"]
    results=[]
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("********************")
    print(" | ".join(row))
    print("********************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*3
        elif row[0] == "🍋":
            return bet*5
        elif row[0] == "⭐":
            return bet*1000

def main():
    balance=100

    print("***********************************")
    print("Welcome to Python Slot Machine Game")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("***********************************")

    while balance > 0:
        print("Current Balance:Rs",balance)

        bet= input("Enter bet amount:")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet=int(bet)

        if bet<=0:
            print("Bet must be greater than o")
            continue
        if bet>balance:
            print("Insufficient Balnce")
            continue

        balance -= bet
        row=spin_row()
        print_row(row)

        payout=get_payout(row,bet)

        if payout > 0:
            print("You won: Rs",payout)
        else:
            print("Sorry you lost this round! Try again!")
        
        balance += payout



if __name__ == '__main__':
    main()