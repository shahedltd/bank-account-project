class BankAccount:
    def __init__(self, name, email, balance, pin):
        self.name = name            # ✅ Public
        self.email = email          # ✅ Public
        self._balance = balance     # ⚠️ Protected
        self.__pin = pin            # 🔒 Private

    def show_balance(self):
        print(f"{self.name}, your current balance is: {self._balance} BDT")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} BDT deposited successfully.")
        else:
            print("Amount must be greater than zero.")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("❌ Incorrect PIN! Transaction failed.")
            return
        if amount > self._balance:
            print("❌ Insufficient balance.")
            return
        self._balance -= amount
        print(f"{amount} BDT withdrawn successfully.")

    def __str__(self):
        return f"Account Holder: {self.name}\nEmail: {self.email}"

user1 = BankAccount("Shahed Rahman", "xyz@gmail.com", 5000, 1234)

# Public data access (✅)
print(user1.name)
print(user1.email)

# Protected data (⚠️ Normally don't access directly)
print(user1._balance)  # Possible, but discouraged

# Private data (🔒 Not accessible)
# print(user1.__pin)  # ❌ Will raise error
# print(user1._BankAccount__pin)  # ⚠️ Technically possible but avoid doing this

# Transactions
user1.show_balance()
user1.deposit(1000)
user1.show_balance()
user1.withdraw(500, 1111)  # Wrong PIN
user1.withdraw(500, 1234)  # Correct PIN
user1.show_balance()

# Use __str__()
print(user1)