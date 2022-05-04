'''
main program to test the function "createVolcanoKML()"
Created on Apr 23, 2015
@author: Yaser Alamin (yr.alamin)
'''
# import the function from the module to be able to use it.
from createVolcanoKML import createVolcanoKML
    
if __name__=='__main__':
    
    sourcefile='ListOfVolcanos.csv'
    destinationfile='All volcanos.kml'
    listTitle='A list of all volcanos'
    
    # choose any location or status or type , if it's "None" then "all" will be chosen 
    Vlocation=None
    Vstatus=None
    Vtype=None
    createVolcanoKML(1, 2, listTitle, Vlocation, Vstatus, Vtype)
    createVolcanoKML(sourcefile, destinationfile, listTitle, Vlocation, Vstatus, Vtype)   
    
    createVolcanoKML("ListOfVolcanos.csv", "Italy.kml", "Volcanos in Italy", "Italy")
    createVolcanoKML("ListOfVolcanos.csv", "Niscaragua.kml", "Historical volcanos in Nicaragua", "Nicaragua", "Historical")
    createVolcanoKML("ListOfVolcanos.csv", "Grseece.kml", "Stratovolcanos in Greece", "Greece", None, "Stratovolcano")
    
    