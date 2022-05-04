'''
    This module is for createvolcanoKML function
    Created on Apr 23, 2015
    @author: Yaser Alamin (yr.alamin)
'''

import csv
import os


''' 
    This function that can be with:
    three compulsory arguments (sourcefile , destinationfile ,listTitle,)
    and three optional arguments( Volcano location,status,and type)
    if any optional arguments not presented all possible option will be taken in account  
    Created on Apr 23, 2015
    @author: Yaser Alamin (yr.alamin)    
'''

def createVolcanoKML(sourcefile,destinationfile,listTitle,Vlocation=None,Vstatus=None,Vtype=None):
    
    #check the input before 
    st=  type('str')
    if (type(sourcefile)!=st or type(destinationfile)!=st or type(listTitle)!=st ):
        print('Error: The Input should be string, between single or double quotation marks')
    elif os.path.isfile(destinationfile):
        print('Error: The destination file already exist.')
    elif not os.path.isfile(sourcefile):
        print ('Error: The source file is not available, or not in the source folder')
    else:
        s_len=len(sourcefile)
        d_len=len(destinationfile)
        if not sourcefile[s_len-4:s_len].lower() == '.csv':
            print ('Error: The source file should be .csv file.')
        elif not destinationfile[d_len-4:d_len].lower() == '.kml':
            print('Error: The destination file should end with (.kml).')
        else:
            GOcreateVolcanoKML(sourcefile,destinationfile,listTitle,Vlocation,Vstatus,Vtype)
    
        
        
    
    
def GOcreateVolcanoKML(sourcefile,destinationfile,listTitle,Vlocation,Vstatus,Vtype):
    
   
    # check the optional arguments and set Parameters For General Description use
    if Vlocation == None:
        allLocations = True
        d_loc = 'All Location' # For General Description use
    else:
        allLocations=False
        d_loc= Vlocation
        
    if Vstatus == None:
        allStatus = True
        d_stt = 'All ' # For General Description use
    else:
        allStatus=False
        d_stt= Vstatus
        
    if Vtype == None:
        allType = True
        d_typ = "All " # For General Description use
    else:
        allType=False
        d_typ= Vtype
        
    # the General Description set
    gen_desc= 'This map contain a selection of volcanos in %s, with %s status, and %s type.' \
                    % (d_loc, d_stt, d_typ)
    
    
    # create kmlFile  class instant
    kmlfile = KMLFile(listTitle,gen_desc)
    
    csvLno=0 # this is a counter to be used as line number for csv file 
    
    # read the CSV file that contain volcanos informations
    with open(sourcefile) as vol_data:
        read_vols = csv.reader(vol_data, delimiter=';')  
        # choose the delimiter depend on the CSV file, ( here they use ';' for separation)
        for volInfo in read_vols:
            if volInfo[0] == 'NAME': # for first line contain the title of the table only 
                csvLno +=1
            else:
                csvLno +=1  
                # this following (if, else) statements for check location, Status, and type 
                # of volcano if it's needed to be add to KML file  
                if allLocations:
                    if allStatus:
                        if allType:
                            kmlfile.addVol(volInfo,csvLno)
                        else:
                            if volInfo[8] == Vtype:
                                kmlfile.addVol(volInfo,csvLno)
                    else:
                        if volInfo[2] == Vstatus:
                            if allType:
                                kmlfile.addVol(volInfo,csvLno)
                            else:
                                if volInfo[8] == Vtype:
                                    kmlfile.addVol(volInfo,csvLno)
                else:
                    if volInfo[1] == Vlocation:
                        if allStatus:
                            if allType:
                                kmlfile.addVol(volInfo,csvLno)
                            else:
                                if volInfo[8] == Vtype:
                                    kmlfile.addVol(volInfo,csvLno)
                        else:
                            if volInfo[2] == Vstatus:
                                if allType:
                                    kmlfile.addVol(volInfo,csvLno)
                                else:
                                    if volInfo[8] == Vtype:
                                        kmlfile.addVol(volInfo,csvLno)
                                        
                                         
                
                # END, volcano to be add to KML file
    
    
    # Create the KML file  
    if not kmlfile.ffile == []:
        kmlf=open(destinationfile,'w')
        kmlf.write(kmlfile.ffile)
        kmlf.close()
                
        nVadded = len(kmlfile.voladdList)
        print('KML file created with name "%s", include %d volcanos.' % (destinationfile, nVadded))

    else:
        print('There is no volcano to be add to the list!!!, kml file not create.')
    
    # finishing indicator (( print function can be canceled))
    
 
'''
this is the class to used by the function
Class Created on Apr 23, 2015
@author: Yaser Alamin (yr.alamin)
'''
class KMLFile: 
                
    fileCode0='''<?xml version="1.0" encoding="utf-8"?>
<kml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://earth.google.com/kml/2.1">
<Document>
<name>'''
    Title=[] # come from the use (ex:Stratovolcanos in Greece)
    fileCode1='''</name>
<description>'''
    Gen_description=[] #This map contains a selection of volcanos.
    fileCode2='''</description>
<Placemark>
<name>'''
    Vname=[] # read from csv when  apply addVol sub-function 
    fileCode3='''</name>
<description>'''
    description=[] # contain status , types, and elev of volcano (read from csv when  apply addVol sub-function)
    fileCode4='''</description>
<Point><coordinates>'''
    lon =[] # 24.44
    comma=''','''     # DONT forget comma
    lat =[] # 36.699
    fileCode5='''</coordinates></Point>
</Placemark>
</Document>
</kml>'''
    
    ffile=[]
    FVol = True
    voladdList=[]
    
    # Class methods
    def __init__(self, Tit, gen_des):
        self.voladdList=[]
        self.Title=Tit
        self.Gen_description=gen_des
        
        
    def addFVol(self,Vinfo=None): 
        # this method to create first volcano with full kml file 
                        
        # inserting information of volcano
        self.Vname=Vinfo[0]
        self.description='Volcano of type %s, status of  %s, and have elevation of %s'%\
                             (Vinfo[8] , Vinfo[2] , Vinfo[7])
        
        # longitude of the volcano in degrees; positive for 
        #  the Eastern hemisphere and negative for the Western hemisphere.
        if Vinfo[6] == 'W':
            self.lon = '-'+Vinfo[5]
        elif Vinfo[6].upper() == 'E':
            self.lon=Vinfo[5]
        else:
            print('Longitude: Hemisphere direction: not correct entry, '),
            return 0
        
        # latitude of the volcano in degrees; positive for the Northern hemisphere 
        #  and negative for the Southern hemisphere.
        if Vinfo[4] == 'S':
            self.lat = '-'+Vinfo[3]
        elif Vinfo[4].upper() == 'N':
            self.lat=Vinfo[3]
        else:
            print('Latitude: Hemisphere direction: not correct entry, '),
            return 0
        
        
        #create string (file text) to be save as kml file
        self.ffile=(self.fileCode0+self.Title+self.fileCode1+self.Gen_description+
                    self.fileCode2+self.Vname+self.fileCode3+self.description+self.fileCode4+
                    self.lon+self.comma+self.lat+self.fileCode5)
        return 1
    
    
    def addVol(self,Vinfo=None, csvLineNo=None):
        
        addnewvolcano = self.addnVol(Vinfo)
        if not addnewvolcano:
            print("this volcano (on line %d) in csv file did not added to KML file." %csvLineNo)
                    
                            
    def addnVol(self, Vinfo): 
        
        # basic check of the value of info presented for volcano 
        if Vinfo == None:
            print 'Warning: No info for the volcano, ',
            return 0
        
        if len(Vinfo) != 9:
            print 'Warning: The info not complete, ',
            return 0
        
        # check if the volcano if it is replicated
        for voladded in self.voladdList:
            if Vinfo == voladded:
                print 'Warning: The volcano replicated, ',
                return 0
         
        self.voladdList.append(Vinfo)   
         
        if self.FVol: # to create first building block of KML file 
            fvx = self.addFVol(Vinfo)
            if fvx == 1:
                self.FVol = False
                
            return fvx
        else: 
            # adding new volcano to kml file that exist  
            
            # find the index where the new volcano to be added 
            addIndex = self.ffile.find('</Placemark>') + len('</Placemark>') 
            # divide the file to two to add the new volcano between 
            b = self.ffile[0:addIndex] # the begin of the text file
            e = self.ffile[addIndex:] # the end of the text file
            
            # description for new volcano
            nV_des='Volcano of type %s, status of  %s, and have elevation of %s'%\
                             (Vinfo[8] , Vinfo[2] , Vinfo[7])
                             
            # longitude of the volcano in degrees; positive for 
            #  the Eastern hemisphere and negative for the Western hemisphere.
            if Vinfo[6] == 'W':
                nlon = '-'+Vinfo[5]
            elif Vinfo[6].upper() == 'E':
                nlon=Vinfo[5]
            else:
                print('Longitude: Hemisphere direction: not correct entry, '),
                return 0
        
            # latitude of the volcano in degrees; positive for the Northern hemisphere 
            #  and negative for the Southern hemisphere.
            if Vinfo[4] == 'S':
                nlat = '-'+Vinfo[3]
            elif Vinfo[4].upper() == 'N':
                nlat=Vinfo[3]
            else:
                print('Latitude: Hemisphere direction: not correct entry, '),
                return 0
            # text of new volcano
            newV='\n<Placemark>\n<name>'+Vinfo[0]+'</name>\n<description>'+nV_des+\
                    '</description>\n<Point><coordinates>'+nlon+','+nlat+\
                        '</coordinates></Point>\n</Placemark>'
            
            # reconstruction of ffile (kml file) with the new volcano
            self.ffile=b+newV+e
            return 1 
        