import numpy as np
import time

class Info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Money:
    def __init__(self, balance=0):
        self.balance = balance
        
    def Deposit(self):
        deposit = int(input("⭐ Enter the amount you want to deposit: "))
        self.balance += deposit
        print(f"💰 Your current balance is ₹{self.balance}")
    
    def Withdraw(self):
        ans = 1
        
        while ans <= 3:
            ans = int(input('''
💵 Would you like to withdraw:
1️⃣ Full amount
2️⃣ Part of the amount
3️⃣ Cancel
👉 Option:'''))     
            if ans == 1:
                print(f"🔔 You have withdrawn ₹{self.balance}")
                self.balance = 0
                break
                            
            elif ans == 2:
                withdraw = int(input("💰 Enter the amount you want to withdraw: "))
                
                if withdraw > self.balance:
                    print("⚠️ You don't have enough balance for this task")
                    
                else:
                    self.balance -= withdraw
                    print(f"💰 Your current balance is ₹{self.balance}")
                    break
                    
            elif ans == 3:
                print("⚠️ Withdraw canceled")
                break
                
            else:
                print("⚠️ invalid request ⚠️")                
                
class Game(Money):
    def __init__(self, money_obj):
        self.money = money_obj

    def playing(self):
        bet = 1000
        if self.money.balance >= bet:
            self.money.balance -= bet            
            print("🔔Get ready!🔔")
            time.sleep(1)
            print("⭐ Spinning the slots ⭐")
            time.sleep(2)
            
            symbols = np.array(['🍒', '💎', '🍀', '🔔', '⭐'])
            spin = np.random.choice(symbols, size=3)
            print("🎰 ||", spin[0], "|", spin[1], "|", spin[2], "|| 🎰")
        
            if spin[0] == spin[1] and spin[1] == spin[2]:
                winnings = (bet*5)
                self.money.balance += bet
                print(f"🎉JACKPOT🎉 YOU HAVE WON {winnings}!")
                print(f"💰 Your new balance: ₹{self.money.balance}")
                
            elif spin[0] == spin[1] or spin[1] == spin[2]:
                winnings = (bet * 1.5)
                self.money.balance += bet
                print(f"🎉 YOU HAVE WON {winnings}!")
                print(f"💰 Your new balance: ₹{self.money.balance}")                                
                
            else:
                print("😞 Better luck next time...")
                print(f"💰 Your new balance: ₹{self.money.balance}")
        else:
            print("⚠️ You don't have enough money. Top-up to continue!")
            
#Variables
print("\n✨ WELCOME TO THE ULTIMATE SLOT MACHINE GAME ✨")
print("🎰 🎲 TEST YOUR LUCK AND WIN BIG! 🎲 🎰")
name = input("👤 Enter your name: ")
age = int(input("🎂 Enter your age: "))
info = Info(name, age)
balance = Money(0)
game = Game(balance)
step = 0

while step <= 4:
    step = int(input(f'''
🎮 What would you like to do, {name}?:
1️⃣ Play Game 🎰
2️⃣ Deposit Money 💰
3️⃣ Withdraw 💵
4️⃣ Exit 🚪
👉 Option:'''))
    if step == 1:
        game.playing()            
    elif step == 2:
        balance.Deposit()
    elif step == 3:
        balance.Withdraw()
    elif step == 4:
        print(f"👋 Thanks for playing, {name}! Hope to see you again! 🎉")
        break
    else:
        print("⚠️ Invalid option! Please enter 1, 2, 3, or 4.")