messege_fas = 'fas'
messege_biss = 'biss'

i = 0
while i < 100:

    if i%3 == 0 and i%5 == 0:
        print(messege_fas + messege_biss)

    elif i%3 == 0:
        print(messege_fas)

    elif i%5 == 0:
        print(messege_biss)

    i += 1
    