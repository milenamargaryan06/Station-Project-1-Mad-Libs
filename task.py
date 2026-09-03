import random

# List of story templates using standard string placeholders
templates = [
    # Template 1: Hospital
    "It was about {0} {1} ago when I arrived at the hospital in a {2}. "
    "The hospital is a/an {3} place, there are a lot of {4} {5} here. "
    "There are nurses here who have {6} {7}. If someone wants to come into my room I told them that they have to {8} first. "
    "I’ve decorated my room with {9} {10}. Today I talked to a doctor and they were wearing a {11} on their {12}. "
    "I heard that all doctors {13} {14} every day for breakfast. "
    "The most {15} thing about being in the hospital is the {16} {17}!",

    # Template 2: Camping
    "This weekend I am going camping with {0}. I packed my lantern, sleeping bag, and {1}. "
    "I am so {2} to {3} in a tent. I am {4} we might see a(n) {5}, I hear they’re kind of dangerous. "
    "While we’re camping, we are going to hike, fish, and {6}. "
    "I have heard that the {7} lake is great for {8}. "
    "Then we will {9} hike through the forest for {10} {11}. "
    "If I see a {12} {13} while hiking, I am going to bring it home as a pet! "
    "At night we will tell {14} {15} stories and roast {16} around the campfire!!",

    # Template 3: Enchanted Castle
    "Dear {0}, I am writing to you from a {1} castle in an enchanted forest. "
    "I found myself here one day after going for a ride on a {2} {3} in {4}. "
    "There are {5} {6} and {7} {8} here! "
    "In the {9} there is a pool full of {10}. "
    "I fall asleep each night on a {11} of {12} and dream of {13} {14}. "
    "It feels as though I have lived here for {15} {16}. "
    "I hope one day you can visit, although the only way to get here now is {17} on a {18} {19}!!"
]

# Prompts corresponding to each template's blank spaces
prompts_list = [
    # Prompts for Template 1
    [
        "Number", "Measure of time", "Mode of Transportation", "Adjective", 
        "Adjective2", "Noun", "Color", "Part of the Body", "Verb", 
        "Number2", "Noun2", "Noun3", "Part of the Body 2", "Verb2", 
        "Noun4", "Adjective3", "Silly Word", "Noun5"
    ],
    # Prompts for Template 2
    [
        "Person's Name", "Noun", "Adjective (Feeling)", "Verb", 
        "Adjective (Feeling) 2", "Animal", "Verb2", "Color", 
        "Verb (ending in ing)", "Adverb (ending in ly)", "Number", 
        "Measure of Time", "Color2", "Animal2", "Number2", 
        "Silly Word", "Noun2"
    ],
    # Prompts for Template 3
    [
        "Person's Name", "Adjective", "Color", "Animal", "Place", 
        "Adjective2", "Magical Creature (Plural)", "Adjective3", 
        "Magical Creature (Plural) 2", "Room in a House", "Noun", 
        "Noun2", "Noun (Plural)", "Adjective4", "Noun (Plural) 2", 
        "Number", "Measure of time", "Verb (ending in ing)", 
        "Adjective5", "Noun3"
    ]
]

def play_mad_libs():
    print("=" * 40)
    print("      WELCOME TO THE MAD LIBS GAME!      ")
    print("=" * 40)
    print("Select a story template:")
    print("1. Hospital Visit")
    print("2. Camping Trip")
    print("3. Enchanted Castle")
    print("4. Random Choice!")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    # Conditionals to set template index
    if choice == '1':
        template_idx = 0
    elif choice == '2':
        template_idx = 1
    elif choice == '3':
        template_idx = 2
    elif choice == '4':
        template_idx = random.randint(0, 2)
    else:
        print("Invalid choice! Picking a random template for you.")
        template_idx = random.randint(0, 2)

    selected_prompts = prompts_list[template_idx]
    selected_template = templates[template_idx]
    
    user_inputs = []
    print("\nPlease fill in the blanks:")
    
    # Loop over requirements and fill inputs array
    for prompt in selected_prompts:
        word = input(f"Enter a/an {prompt}: ").strip()
        while not word:  # Simple validation loop
            word = input(f"Field cannot be empty. Please enter a/an {prompt}: ").strip()
        user_inputs.append(word)

    # Generate final story
    story = selected_template.format(*user_inputs)
    
    print("\n" + "=" * 40)
    print("          YOUR MAD LIBS STORY          ")
    print("=" * 40)
    print(story)
    print("=" * 40)

if __name__ == "__main__":
    play_mad_libs()
