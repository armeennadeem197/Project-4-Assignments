import random
import string
import secrets
import argparse

class PasswordGenerator:
    def __init__(self):
        self.complexity_levels = {
            'low': string.ascii_letters + string.digits,
            'medium': string.ascii_letters + string.digits + string.punctuation[:10],
            'high': string.ascii_letters + string.digits + string.punctuation,
            'pin': string.digits
        }
    
    def generate_password(self, length=12, complexity='high'):
        """Generate a secure password with specified complexity"""
        if complexity not in self.complexity_levels:
            raise ValueError(f"Invalid complexity level. Choose from {list(self.complexity_levels.keys())}")
        
        characters = self.complexity_levels[complexity]
        return ''.join(secrets.choice(characters) for _ in range(length))
    
    def generate_multiple_passwords(self, count=5, length=12, complexity='high'):
        """Generate multiple passwords at once"""
        return [self.generate_password(length, complexity) for _ in range(count)]
    
    def calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        charset_size = len(set(password))
        length = len(password)
        return length * (charset_size ** 0.5)  # Simplified entropy calculation

def display_passwords(passwords, show_entropy=False):
    """Display generated passwords with optional entropy information"""
    print("\n" + "="*50)
    print("🔐 GENERATED PASSWORDS 🔐".center(50))
    print("="*50)
    
    generator = PasswordGenerator()
    for i, pwd in enumerate(passwords, 1):
        entropy = generator.calculate_entropy(pwd)
        strength = "✅ Strong" if entropy > 50 else "⚠️ Weak" if entropy < 30 else "🔼 Medium"
        print(f"\nPassword {i}: {pwd}")
        if show_entropy:
            print(f"Entropy: {entropy:.1f} bits | Strength: {strength}")
    print("\n" + "="*50)

def get_user_input():
    """Get user input with validation"""
    print("\n" + "="*50)
    print("🔒 PASSWORD GENERATOR 🔒".center(50))
    print("="*50)
    
    while True:
        try:
            count = int(input("\nNumber of passwords to generate (1-20): "))
            if not 1 <= count <= 20:
                raise ValueError("Please enter between 1-20")
                
            length = int(input("Password length (8-64): "))
            if not 8 <= length <= 64:
                raise ValueError("Please enter between 8-64")
                
            print("\nComplexity levels:")
            print("1 - Low (letters and numbers)")
            print("2 - Medium (letters, numbers, basic symbols)")
            print("3 - High (letters, numbers, all symbols)")
            print("4 - PIN (numbers only)")
            
            choice = input("\nSelect complexity (1-4): ")
            complexities = ['low', 'medium', 'high', 'pin']
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Please select 1-4")
                
            show_entropy = input("Show password strength? (y/n): ").lower() == 'y'
            
            return count, length, complexities[int(choice)-1], show_entropy
            
        except ValueError as e:
            print(f"❌ Error: {e}")

def main():
    generator = PasswordGenerator()
    
    # Command line interface
    parser = argparse.ArgumentParser(description='Generate secure passwords')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords')
    parser.add_argument('-l', '--length', type=int, default=12, help='Password length')
    parser.add_argument('-x', '--complexity', choices=['low', 'medium', 'high', 'pin'], 
                       default='high', help='Password complexity')
    args = parser.parse_args()
    
    if any(vars(args).values()):
        # If command line arguments provided
        passwords = generator.generate_multiple_passwords(args.count, args.length, args.complexity)
        display_passwords(passwords, show_entropy=True)
    else:
        # Interactive mode
        count, length, complexity, show_entropy = get_user_input()
        passwords = generator.generate_multiple_passwords(count, length, complexity)
        display_passwords(passwords, show_entropy)

if __name__ == "__main__":
    main()