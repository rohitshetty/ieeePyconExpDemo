import pygame,sys,time,math,random
from pygame.locals import *
angle =0                                          #angle of the image
x,y=01,01                                         #position of the image
dimension=20                                      #dimension of image   
angleInc=4                                        #increment step for angle 
dimensionNew=400                                  #new angle
i=0
size=(1360,700)                                     # screen size

RANGE=360                                         #Range of angle
XRANGE=size[0]-100                                #Range of x
YRANGE=size[1]-100                                #range of y
center=(200,202)
def rotate(pic,angleInc,dimensionNew):
 orig=pic.get_rect()
 orig.center=pic.get_rect().center                      #get the centre
 pic=pygame.transform.scale(pic,(dimensionNew,dimensionNew))        #to scale the size dimensionNew is the x y size
 pic=pygame.transform.rotate(pic,angleInc)                   # To rotate the image by angleInc
 
 return pic


xr=input("x\n")                                   # x value for the inital velo
yr=input("y\n")                                   # y value for then initial velo
inc=input("speed \n")                             # velocity mag
name=raw_input("name\n")                          #name of the image
sine=math.sin(math.atan(xr/yr*1.0))               #component of the angle launch sine
cosine=math.cos(math.atan(xr/yr*1.0))             #component of the angle launch cosine
print (sine,cosine)                              

col=(236, 240, 241)                              #background color
screen=pygame.display.set_mode(size)             #set the screen


logo=pygame.image.load(name)                     #name of the image
#logo=pygame.image.load("pyconau_logo.png")
screen.fill(col)                                 #fill screen with that color

pygame.init()
incx=inc
incy=inc
while(1):
 
 screen.fill(col)
 for event in pygame.event.get():                #looks for events like close window
  if event.type==QUIT:
   sys.exit()
 
 xr=xr+incx
 yr=yr+incy
 if(xr>XRANGE-200):
  incx=incx*-1
 if(xr<0):
  incx=incx*-1

 if(yr>YRANGE-200):
   incy=incy*-1
 if(yr<0):
   incy=incy*-1

 x=(xr)*sine
 y=(yr)*cosine

 if(angle>45):
   angleInc=angleInc*-1
 if(angle<-45):
   angleInc=angleInc*-1
 if(dimensionNew>500):
   dimension=dimension*-1
 if(dimensionNew<200):
   dimension=dimension*-1
 dimensionNew=dimension+dimensionNew
 angle=angle+angleInc
 copy=logo
 print copy.get_rect().center
 copy=rotate(copy,angle,dimensionNew)
 screen.blit(copy,(x,y))       #blit means put the image on screen
 print xr,yr,incx,incy
 pygame.display.update()      # update the image
 time.sleep(0.1)

