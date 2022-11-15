# Computer Vision RPS

## manual_rps.py 
The manual rock-paper-scissors programme uses OOP to create a game where the user chooses their option within the terminal. It's best of 1.

## camera_rps_v1.py (personal model-based)
The camera rock-paper-scissors programme uses computer vision to create a game where the user chooses their option by intereacting with the camera. This uses a model built using the the website 'teachablemachine.withgoogle.com'. The readability of the code for this project could be improved, for example, by avoiding lots of try and except statements. Programming anything involving a continous while loop will involve solving the challenge of everything continuously updating, but there are better solutions to use in the future. A downside of this script, over camera_rps_v2.py is that the model was trained on pictures of myself, which means it may not work on other people very well.

## camera_rps_v2.py (cvzone based)
This script makes use of the library 'cvzone' in order to make more accurate predictions about the hand position. It is also not reliant on a specific person's training set, and therefore has the advantage that it should work equally well for everyone.

