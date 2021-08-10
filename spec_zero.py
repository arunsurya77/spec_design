import numpy as np

tdiam = 5 #Telescope Diameter
tfratio = 16 #Telescope Diameter

beamw= 145 #mm
slitwidth= 1 #as
fov= 12 #am
slitlength=fov 

linden= 300 # lines/mm
order=1
lamcen=7000 # Angstorms

fratcam=2.1
pixel_sz=15 #microns






#Derived
tefl=tdiam*tfratio #focal length m
tpltscl= (tdiam*tfratio/206265) * 1000.0 #mm/as
flencol= tfratio*beamw #mm
beamffov= tdiam/(beamw/1000.) * slitlength/60 #degree
slitlengthmm=(beamffov/57.3)*flencol
dthetaw=slitwidth*tpltscl/flencol
dlambda=dthetaw/(order*linden*1e-7)
R=lamcen/dlambda

print(beamffov,R)
