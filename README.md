# 🏦 Bank Account Management (Python OOP)

This is a simple Python project demonstrating the use of **Object-Oriented Programming (OOP)** principles such as:

- ✅ Class & Object
- ✅ Encapsulation (`public`, `protected`, `private` attributes)
- ✅ Methods & Constructors
- ✅ `__str__()` Magic Method

---

## 📂 Project Structure

```python
class BankAccount:
    def __init__(self, name, email, balance, pin):
        ...
```

The main class is `BankAccount`, which holds personal and financial details of a user and allows basic banking operations like `deposit`, `withdraw`, and `show_balance`.

---

## ⚙️ Features

- 👤 Public attributes: `name`, `email`
- 🔒 Private attribute: `__pin` (for secure transactions)
- ⚠️ Protected attribute: `_balance` (not recommended to access directly)
- 💳 Deposit & Withdraw methods (with PIN verification)
- 💬 `__str__()` method to show account summary

---

## 🧪 Sample Usage

```python
user1 = BankAccount("Shahed Rahman", "xyz@gmail.com", 5000, 1234)

user1.show_balance()
user1.deposit(1000)
user1.withdraw(500, 1234)
print(user1)
```

---

## 🔐 Encapsulation Levels

| Attribute     | Type       | Access Level        |
|---------------|------------|---------------------|
| `name`        | Public     | Accessible anywhere |
| `email`       | Public     | Accessible anywhere |
| `_balance`    | Protected  | Access inside class & subclass (discouraged outside) |
| `__pin`       | Private    | Only inside the class |

---

## 🚫 Common Mistakes (For Learning)

```python
print(user1.__pin)              # ❌ Will raise AttributeError
print(user1._BankAccount__pin)  # ⚠️ Works, but not recommended
```

---

## 🧠 Author

- **Shahed Rahman**
- Email: `shahedrahmanltd@gmail.com`

---

## 📜 License

This project is open-source and free to use for educational purposes.
