import random
import string

#this is a list to store existed reference
references = []

def generate_booking_reference():
    # Set the length of the booking reference
    length = 8

    # Define all possible characters for the reference(characters and number)
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Generate a random reference(pick 8)
    reference = ''.join(random.choice(chars) for _ in range(length))

    # Check if the reference is unique
    # store the generated references in a list
    # and check if the newly generated reference already exists
    # For the purpose of this example, let's assume we have a list called 'references'
    while reference in references:
        reference = ''.join(random.choice(chars) for _ in range(length))

    # Once a unique reference is generated, add it to the list or database
    references.append(reference)

    # Return the generated reference
    return reference

print(generate_booking_reference())