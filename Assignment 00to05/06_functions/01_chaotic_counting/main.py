import random

# Probability that the function `done` returns True
DONE_LIKELIHOOD = 0.2  # 20% chance to stop

def chaotic_counting():
    """
    Attempts to count from 1 to 10, but may stop early based on random chance.
    """
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Stop counting early
        print(curr_num)

def done():
    """
    Returns True with a probability of DONE_LIKELIHOOD (20%)
    """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
