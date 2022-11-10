# Computer Vision RPS

## Model training
The model was created using the website teachablemachine.withgoogle.com.
The model was trained to sort images into one of four classes: rock, paper, scissors and nothing. The training set was images of me making the signs into my webcam. The model seems to work great for pictures of me holding up the symbol, but given an unfamiliar setting it might be a bit haphazard. This could of course be improved by providing a much larger training set.

## manual_rps.py 
The manual rock-paper-scissors programme uses OOP to create a game where the user chooses their option within the terminal. It's best of 1.

## camera_rps.py
The camera rock-paper-scissors programme uses computer vision to create a game where the user chooses their option by intereacting with the camera. This uses the model that wast trained previously. Honestly, the code for this project is a bit ugly, but I'm really happy with the resulting functionality. Doing everything in OOP would be more "correct" I'm sure but the programme seems to run fine without it.