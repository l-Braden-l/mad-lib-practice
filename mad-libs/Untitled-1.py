
#Braden Leach
# SEP 09 16 2024
# Mad Lib Practice




noun = input('Noun: ')
verb = input('verb: ')
noun2 = input('noun: ')
noun3 = input('noun: ')
verb2 = input('verb, ending in ing: ')
noun4 = input('noun: ')

x= verb2.upper()
y = noun.lower()
mad_lib = f'Hello, you live in a {y}, and after going for a walk you start to {verb}. When you get tired from that you decide to sit on your {noun2}. After you wake up from your nap you start talking to your {noun3}. \nWhen walking to the mall you think to start {x} your bike instead. Lastly on your way back home you see your sister with a brand new {noun4}.'
print(mad_lib)