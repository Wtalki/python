import random 
def roll_die(sides):
    return random.randint(1,sides)


def roll_dice(dice_type,num_rolls):
    results = []
    for _ in range(num_rolls):
        result = roll_die(dice_type)
        results.append(result)
    return results
def main():
    print("Welcome to the dice roller simulator!")

    dice_type = int(input("enter the type of die(e.g.,6 for d6, 20 for d20)"))

    num_rolls = int(input("enter the number of rolls: "))
    result = roll_dice(dice_type,num_rolls)
    print(f"\nrolling a d{dice_type} die {num_rolls} times")
    print("results:", result)
    print(f"total of all rolls: {sum(result)}")

main()