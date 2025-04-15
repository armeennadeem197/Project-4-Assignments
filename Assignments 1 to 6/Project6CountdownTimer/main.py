import time
import sys
from datetime import datetime, timedelta

def countdown_timer(total_seconds):
    """Display a countdown timer with progress visualization"""
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=total_seconds)
    
    print("\n" + "="*40)
    print("⏳ COUNTDOWN TIMER ⏳".center(40))
    print("="*40)
    print(f"Start Time: {start_time.strftime('%H:%M:%S')}")
    print(f"End Time:   {end_time.strftime('%H:%M:%S')}")
    print("="*40 + "\n")
    
    while total_seconds > 0:
        # Calculate time remaining
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        
        # Format the timer display
        timer_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
        
        # Calculate progress percentage
        progress = 100 - (total_seconds / (end_time - start_time).total_seconds() * 100)
        
        # Display the timer with progress bar
        sys.stdout.write("\r")
        sys.stdout.write(f"⏳ {timer_format} |{'█' * int(progress/5):<20}| {progress:.1f}% ")
        sys.stdout.flush()
        
        time.sleep(1)
        total_seconds -= 1
    
    # Final display with blinking effect
    for _ in range(3):
        sys.stdout.write("\rTIME'S UP! 🚨" + " "*50)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r" + " "*50)
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n\n" + "="*40)
    print("⏰ COUNTDOWN COMPLETE!".center(40))
    print("="*40)
    print(f"Started at: {start_time.strftime('%H:%M:%S')}")
    print(f"Finished at: {datetime.now().strftime('%H:%M:%S')}")
    print("="*40)

def get_user_input():
    """Get and validate user input for timer duration"""
    while True:
        try:
            user_input = input("\nEnter countdown duration (HH:MM:SS or seconds): ")
            
            if ":" in user_input:
                # Handle HH:MM:SS format
                h, m, s = map(int, user_input.split(":"))
                return h*3600 + m*60 + s
            else:
                # Handle seconds only
                return int(user_input)
                
        except ValueError:
            print("Invalid input! Please enter time in HH:MM:SS format or seconds only.")

def main():
    print("\n" + "="*40)
    print("🚀 PYTHON COUNTDOWN TIMER".center(40))
    print("="*40)
    
    while True:
        seconds = get_user_input()
        countdown_timer(seconds)
        
        restart = input("\nStart another timer? (y/n): ").lower()
        if restart != 'y':
            print("\nThanks for using the timer! 👋")
            break

if __name__ == "__main__":
    main()