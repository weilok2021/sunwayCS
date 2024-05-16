# Exercise
# Create a new file in Spyder. Define a variable named friends such that it is a nested array in 
# which contains the name, home country, and home state/province of 10 of your friends (real or virtual). 
friend = ['shuen', 'malaysia', 'selangor']
# 1d array

# 2d array
friends = [
    ['John', 'USA', 'California'],
    ['Emily', 'Canada', 'Ontario'],
    ['Mohammed', 'UAE', 'Dubai'],
    ['Sophie', 'France', 'Paris'],
    ['Luis', 'Mexico', 'Jalisco'],
    ['Anna', 'Germany', 'Bavaria'],
    ['Chen', 'China', 'Beijing'],
    ['Maria', 'Brazil', 'São Paulo'],
    ['Yuki', 'Japan', 'Tokyo'],
    ['Aisha', 'Saudi Arabia', 'Riyadh'],
    ["James", "Malaysia", "Malacca"],
    ["Don", "Malaysia", "Pahang"]
]

def filterFriend(name="", home_country="", home_state=""):
    filtered = []
    ## solution 1
    for friend in friends:
        if name == friend[0] or home_country == friend[1] or home_state == friend[2]:
            filtered.append(friend)
    # else, friend not found

    #solution 2
    return filtered
                

