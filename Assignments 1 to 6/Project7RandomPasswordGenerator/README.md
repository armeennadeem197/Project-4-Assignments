# 🔒 Secure Password Generator (Python)

A powerful and flexible password generator built in Python. Supports CLI and interactive modes,
multiple complexity levels, entropy calculation, and strength indicator.

---

## 🚀 Features

- 🔐 Generate secure passwords with:
  - ✅ Low, Medium, High complexity
  - ✅ PIN-only (digits only)
- 🔢 Custom number and length of passwords
- 📈 Password entropy & strength analysis
- 🧑‍💻 Interactive **and** command-line usage
- 💡 Validations for user input

---

Arguments
Option	Description	Example
-c or --count	Number of passwords	5
-l or --length	Password length	16
-x or --complexity	Complexity: low, medium, high, pin	high

🧠 Password Entropy & Strength
Each password's entropy (in bits) is estimated based on character set size.
Strength is categorized as:

✅ Strong if entropy > 50

🔼 Medium if entropy between 30–50

⚠️ Weak if entropy < 30

Example:
Password: f8K#rL1!@z2Q
Entropy: 53.2 bits | Strength: ✅ Strong

💡 Complexity Levels
Level	Characters Included
Low	Letters + Numbers
Medium	Letters + Numbers + Basic Symbols (!@#$%...)
High	Letters + Numbers + All Punctuation
PIN	Numbers Only

Key Features
Customizable Length: The user can specify the length of each password.
Multiple Passwords: The user can generate multiple passwords at once.
Strong Passwords: The generated passwords contain a mix of characters, ensuring they are strong and secure.
