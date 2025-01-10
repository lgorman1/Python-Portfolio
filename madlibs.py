def madlib():
    print("""Hi! Welcome to the madlib!
    Please complete the following  requests to build your story:""")
    adjective = input("Enter an adjective")
    adjective2 = input("Enter a second adjective")
    bird = input("Enter a type of bird")
    room = input("Enter a room in a house")
    verbpt = input("Enter a verb in the past tense")
    verb = input("Enter a verb")
    relative = input("Enter a relatives name")
    noun = input("Enter a noun")
    liquid = input("Enter a liquid")
    verbing = input("Enter a verb ending in -ing")
    body = input("Enter a part of the body (plural)")
    pnoun = input("Enter a plural noun")
    verbing2 = input("Enter another verb ending in -ing")
    noun2 = input("Enter another noun")
    print("""Thank you for your inputs! Here is the story:
          """)
    print(""" It was a """ + str(adjective) + " , cold December day. I woke up to the " + str(adjective2) + """ smell of
    """ + str(bird) + " roasting in the " + str(room) + """ downstairs. I
    """ + str(verbpt) + " down the stairs to see if I could help " + str(verb) + """ the dinner. My mom said, 'See if """ + str(relative) + """ needs a fresh """ + str(noun) + ".' So I carried a tray of glasses full of " + str(liquid) + " into the " + str(verbing) + " room. When I got there, I couldn't believe my " + str(body) + "! There was " + str(pnoun) + str(verbing2) + " on the " + str(noun2) + "!")

    print("""
    Wow, that was an amazing story! Thank you for playing!""")
#main
madlib()
