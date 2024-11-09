def mad_libs():
     # Prompt the user to input words for the story
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    verb1 = input("Enter a verb ending in -ing: ")
    verb2 = input("Enter another verb: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")

    story_template = f"""
    Once upon a time in a {adjective1} {place}, there was a {animal} named {noun1}. 
    Every day, {noun1} would go {verb1} in the {place}, hoping to meet a {adjective2} friend.
    One day, {noun1} met {noun2}, who was very good at {verb2}. 
    Together, they had an amazing adventure and became best friends!
    """

    print("\nHere's your Mad Libs story!")
    print(story_template)

mad_libs()