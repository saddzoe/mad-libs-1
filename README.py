# mad-libs-1
# This is another madlibs game I created using python

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("This Mad Libs game has started.")

name = raw_input("Enter a name: ")

adj = raw_input("Enter an adjective: ")
adj1 = raw_input("Enter a second adjective: ")
adj2 = raw_input("Enter one more adjective: ")

verb = raw_input("Enter a verb: ")

noun = raw_input("Enter a noun: ")
noun1 = raw_input("Enter one more noun: ")

animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
superhero = raw_input("Enter a superhero: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
