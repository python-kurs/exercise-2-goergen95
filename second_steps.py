# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database['GOES'] = 2000
sat_database['worldview'] =0.31

# 2) print out all satellite names contained in the dictionary [2P]
sep = ", "
print("I have the following satellite in my database:{}{}".format(sep.join(sat_database.keys()),"."))
# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
satName = input("Which satellite's resolution do you want to know? Please enter the name:")
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]
# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
if not satName.upper() in sat_database:
    print("The satellite {}, which you are asking for, unfortunatley is not in the database.".format(satName))
else:
    print("The resoultion of {} is {} meters.".format(satName,sat_database[satName.upper()]))




