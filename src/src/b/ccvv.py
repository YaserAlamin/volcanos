'''
Created on Apr 23, 2015

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
        
        self.Title=Tit
        self.Gen_description=gen_des
        
          
    def printT(self): # this temporary check method
        print(self.ffile)
     
     
    def addFirstRow(self, Vinfo=None):
        pass
    
    
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
            raise ValueError('Longitude: Hemisphere direction: not correct entry')
        
        # latitude of the volcano in degrees; positive for the Northern hemisphere 
        #  and negative for the Southern hemisphere.
        if Vinfo[4] == 'S':
            self.lat = '-'+Vinfo[3]
        elif Vinfo[4].upper() == 'N':
            self.lat=Vinfo[3]
        else:
            raise ValueError('Latitude: Hemisphere direction: not correct entry')
        
        
        #create string (file text) to be save as kml file
        self.ffile=(self.fileCode0+self.Title+self.fileCode1+self.Gen_description+
                    self.fileCode2+self.Vname+self.fileCode3+self.description+self.fileCode4+
                    self.lon+self.comma+self.lat+self.fileCode5)
        
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
            self.addFVol(Vinfo)
            self.FVol = False
            return 1
        else: 
            # adding new volcano to kml file that exist  
            addIndex = self.ffile.find('</Placemark>') + len('</Placemark>') 
            b = self.ffile[0:addIndex]
            e = self.ffile[addIndex:]
            
            nV_des='Volcano of type %s, status of  %s, and have elevation of %s'%\
                             (Vinfo[8] , Vinfo[2] , Vinfo[7])
                             
            # longitude of the volcano in degrees; positive for 
            #  the Eastern hemisphere and negative for the Western hemisphere.
            if Vinfo[6] == 'W':
                nlon = '-'+Vinfo[5]
            elif Vinfo[6].upper() == 'E':
                nlon=Vinfo[5]
            else:
                raise Warning('Longitude: Hemisphere direction: not correct entry')
                return 0
        
            # latitude of the volcano in degrees; positive for the Northern hemisphere 
            #  and negative for the Southern hemisphere.
            if Vinfo[4] == 'S':
                nlat = '-'+Vinfo[3]
            elif Vinfo[4].upper() == 'N':
                nlat=Vinfo[3]
            else:
                raise Warning('Latitude: Hemisphere direction: not correct entry')
                return 0
        
            newV='\n<Placemark>\n<name>'+Vinfo[0]+'</name>\n<description>'+nV_des+\
                    '</description>\n<Point><coordinates>'+nlon+','+nlat+\
                        '</coordinates></Point>\n</Placemark>'
            
            # reconstruction of ffile (kml file) with the new volcano
            self.ffile=b+newV+e
            return 1 
    