from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
from mtcnn.mtcnn import MTCNN
import os
import escolha as escolha

#Adicionar o local dos modelos 
#Copiar o local da pasta com os modelos
path = r''


Modelos = [path+'\mascara.h5',path+'\oculos.h5',path+'\fone.h5',path+'\capacete.h5']

escolha.escolha()
x = int(input("Qual EPI deseja identificar: "))
escolha.enq(x)
if x ==5:
	quit()

print('Carregando...')

model = load_model(Modelos[x-1], compile=False)

detector = MTCNN()
cap = cv2.VideoCapture(1)

while True:
    
    ret, frame = cap.read()
    faces = detector.detect_faces(frame)
    
    for face in faces:
        
        x1, y1, w, h = face['box']
        x2, y2 = x1 + w, y1 + h
        
        cv2.imwrite('frame.png', frame)

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open('frame.png')

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        
        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        data[0] = normalized_image_array

        prediction = model.predict(data)
        
        prediction = prediction[0]
    
        if prediction[0] >= prediction[1]:
            label = 'SEM EPI'
            color = (0,0,255)
        else:
            label = 'COM EPI'
            color = (0,255,0)
        
        label_position = (x1+5, y1-5)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame,label, label_position, cv2.FONT_HERSHEY_SIMPLEX,.6,color,2)
        
    cv2.imshow('DETECTOR EPI - IEEE RAS UNESP BAURU', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
os.remove('frame.png')