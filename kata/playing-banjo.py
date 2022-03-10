# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# alternative solutions:

# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'


# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return "{} plays banjo".format(name)
#     return "{} does not play banjo".format(name)


# def areYouPlayingBanjo(name):
#     if name.startswith('R') or name.startswith('r'):
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'