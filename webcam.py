import cv2

arqCasc1 = 'haarcascade_frontalface_default.xml'
faceCascade1 = cv2.CascadeClassifier(arqCasc1) #classificador para o rosto

webcam = cv2.VideoCapture(0)  #instancia o uso da webcam

while True:
    s, imagem = webcam.read() #pega a imagem da webcam
    imagem = cv2.flip(imagem,180) #espelha a imagem

    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(30, 30),
	    maxSize=(300,300)
    )

    # Desenha um retangulo no rosto 
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Video', imagem) #mostra a imagem capturada na janela

    #Para o código e fecha a janela ao pressionar a tecla q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas