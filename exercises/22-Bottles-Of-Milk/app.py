def number_of_bottles():
    strofa = " bottles of milk on the wall.\n "
    strofa2 = " bottles of milk.\n Take one down and pass it around, "
    strofafinal = " bottle of milk on the wall.\n "
    strofafinal2 = " bottle of milk.\n Take one down and pass it around, "
    strofafinal3 = "no more bottles of milk on the wall. "
    finalsong = "No more bottles of milk on the wall"
    finalsong2 = ", no more bottles of milk."  
    finalsong3 = "Go to the store and buy some more, 99 bottles of milk on the wall.\n"
    cancion = ""
    for i in range(1,99):
        cant = str(i)
        if i == 1:
            cancion = cancion + cant + strofafinal + cant + strofafinal2 + strofafinal3 + finalsong + finalsong2 + finalsong3
        else:
            cancion = cancion + cant + strofa + cant + strofa2
    
    print (cancion)

number_of_bottles ()