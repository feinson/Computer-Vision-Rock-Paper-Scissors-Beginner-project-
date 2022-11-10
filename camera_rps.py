import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

x=time.time()
while (time.time()-x)<7:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)

    count_down = str(7-np.floor(time.time()-x))
    cv2.putText(frame, count_down, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
    cv2.imshow('frame', frame)
    
    # Press q to close the window
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()



def get_prediction():
    choices_list = ['Rock', 'Paper', 'Scissors', 'Nothing']
    choice = choices_list[prediction.argmax()]
    print(f"You chose {choice}")

get_prediction()
