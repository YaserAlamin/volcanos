'''
main program to test the function "createVolcanoKML()"
'''

# import the function from the module to be able to use it.
from createVolcanoKML import createVolcanoKML #WHY DO I NEED TO USE FROM AND THEN IMPORT INSTEAD OF ONLY IMPORT ?
#Y: acully you just need 'import createVolcanoKML' becuse it only one function in there !!! so you can change it ( its the same )    
if __name__=='__main__': #CAN YOU EXPLAIN ME THE STRUCTURE OF THIS?
    #Y: i cannot explain here much realy , it's part of python logic (its mean the "main" program start here 
    
    sourcefile='ListOfVolcanos.csv' #SOURCE FILE - LIST CSV
    destinationfile='All volcanos.kml' #DESTINATION FILE - KLM FILE ALL VOLCANOS.KLM
    listTitle='A list of all volcanos' #LIST TITLE - A LIST OF ALL VOLCANOS 
    
    # choose any location or status or type , if it's "None" then "all" will be chosen - WHY DID YOU NEED TO DO IT ?
    # you dont need to you can leave it empty its the same as NONE , but i was making smae testing , the only thing is
    # (the optional parameters should be in the same order (..., location, status, type) if the last ones not there its ok it will take NONE by dufult,
    # like the example in "italy"
    # but if one in middile not there the program will not understand like the example in "greece"
    # if you will not put none and put "Stratovolcano" after "Greece" the code will assume it the state not the type

    # this part for testing the function 
    Vlocation=None
    Vstatus=None
    Vtype=None
    createVolcanoKML(1, 2, listTitle, Vlocation, Vstatus, Vtype)   #WHY DO YOU NEED TO CREATE THIS ONE AND THE ONE BELLOW? WHAT THE NUMBERS 1 AND 2 MEANS?
    #Y: i was testing again if will give error if inter a number insted of name ( and it give me error) 
    createVolcanoKML(sourcefile, destinationfile, listTitle, Vlocation, Vstatus, Vtype)   


    # this part for example needed 
    createVolcanoKML("ListOfVolcanos.csv", "Italy.kml", "Volcanos in Italy", "Italy")#WHY THERE IS NOT NONE AND NONE AFTER ITALY? LIKE THE EXAMPLE IN GREECE.
    createVolcanoKML("ListOfVolcanos.csv", "Niscaragua.kml", "Historical volcanos in Nicaragua", "Nicaragua", "Historical")
    createVolcanoKML("ListOfVolcanos.csv", "Grseece.kml", "Stratovolcanos in Greece", "Greece", None, "Stratovolcano")
    
    
