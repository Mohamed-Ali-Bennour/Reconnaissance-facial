import cv2
#from gpiozero import buzzer
#bz = Buzzer(0)

# intitation de la capture por detecter 
capteur = cv2.VideoCapture(0,cv2.CAP_DSHOW)
detector = cv2.CascadeClassifier("contour_visage.xml")

while (True):
 # is_reading:bool etat de le captuer active true,pas active false 
 # image_capturee:image  l image captuer sous forme d un matrice de pixel
  is_reading,image_capturee=capteur.read()
  
  faces = detector.detectMultiScale(image_capturee)
    
 # executer une interface pour charge les image capturee
  for (x, y, w, h) in faces:
  cv2.rectangle(image_capturee, (x, y), (x+w, y+h), (0, 255, 0), 2)
  #print('\a')
  #bz.on()
    
  cv2.imshow('projet iott', image_capturee)

  if cv2.waitKey(1) & ord('d'):
	  break


capteur.release()
cv2.destroyAllWindows()

   



                                       
                                       