#This program accepts input from the user in 'Mad Lib' style and outputs an amusing
#introductory news paragraph. 


# Begin the article
article = "Wall Street"

# Accept a variable from the user
var1 = input("Please enter a verb. >>")
article += var1 + " sank on Monday, following the steepest decline in "

# Continue accepting variables through the end of the article
var2 = input("Please enter the name of a country. >>")
article += var2 + "stocks in eight years, on worries "

var3 = input("Please enter an adjective. >>")
article += var3 + " growth in the world's No. "

var4 = input("Please enter a number. >>")
article += var4 + " economy would hurt its key "

var5 = input("Please enter the name of a rock & roll band. >>")
article += var5 + " partners."

print("\n\n")
print(article)
print("\n\n")