# 1) Get user name and replace all "a" in the sting to "i"

# EXAMPLE
# Karolina
# Kirolini

name = input("Enter user name:\n")
print(name.replace("a", "i"))

# 2) Get favorit lyric row from song from user and split it

# EXAMPLE
# 'Cause we're choking
# And left for dead, but we're coping
# Somebody, save our souls

# [Cause , we're ,choking , And]

lyrics_row = input("\n Eneter the row:\n")
print(lyrics_row.split(" "))

# 3) Get string from user and convert it to upperCase

# EXAMPLE
# kiR
# KIR

print("\n" + name + "\n" + name.upper() + "\n")

# 4) Get user name from upperCase convert it to lowerCase and than capitalize it

# EXAMPLE
# KIR
# kir
# Kir

print(name + "\n" + name.lower() + "\n" + name.capitalize() + "\n")

# 5) Get from user expression that contain 20 expressions , but then - cut it to 20 symbols

text = """Marco Polo is famous for his journeys across Asia. 
He was one of the first Europeans to travel in Mongolia and China. 
He wrote a famous book called 'The Travels'.
He was born in Venice, Italy in 1254. In 1272, when he was only 17 years old, 
he travelled to Asia with his father and uncle. The journey was very long. 
They visited a lot of places and saw wonderful things: eye glasses, ice-cream, 
spaghetti and the riches of Asia.
After three years they entered China through the Great Wall. In 1275 Kublai Khon, 
the Emperor of China, met the visitors at his Summer Palace 
in the capital of China at Xanadu. The palace was very beautiful. 
There were a lot of gold things and silk curtains. 
The Emperor gave a big banquet. 
There were more than a thousand people in the palace. 
On the emperor birthday 5,000 soldiers rode through the city to the palace on elephants. 
Marco Polo visited some huge markets, where merchants from all over the world bought 
and sold all kinds of things. 
He was happy to see one of the greatest cities of the thirteenth century and 
spent 18 years in China.
When he returned to Italy in 1295, he became a popular storyteller. 
People came to his home to hear stories about his journeys in the East. 
Many of them did not believe him. When he died, he said: 
I haven told half of what I saw, because no one can believe it.
"""

print(text[:20])

# EXAMPLE
#  "loremofsm dfk mlskdmf lskdmlsdk mfsldkf mlsdf lskdm lksdm lfkm lskfdm lsdkm flskf msldf lskdng lksndglk n lskdn lknsd lkn ldsknglk snglksdn lgkn lkndlgk nlsdkng lkns"
# "loremofsm dfk mlskdmf lskdmlsdk"
