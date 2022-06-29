# The function is not returning the correct values. Can you figure out why?
# Example (Input --> Output ):
# 3 --> "Earth"

def get_planet_name(id):
    if id==1:
        return 'Mercury'
    elif id==2:
        return "Venus"
    elif id==3:
        return "Earth"
    elif id==4:
        return 'Mars'
    elif id==5:
        return 'Jupiter'
    elif id==6:
        return 'Saturn'
    elif id==7:
        return 'Uranus'
    else: return 'Neptune'

# alternative solutions:

# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)


# def get_planet_name(id):
#     planets = {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus", 
#         8: "Neptune",
#     }
#     return planets[id]


# def get_planet_name(id):
#     return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]