import cv2
import numpy as np
import time
import random
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
#data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
list_of_moves = ['Rock', 'Paper', 'Scissors', 'Nothing']
list_of_comp_moves = ['Rock', 'Paper', 'Scissors']

detector = HandDetector(maxHands=1)

def get_prediction(frame,hands):
    
    hand = hands[0]
    fingers = detector.fingersUp(hand)
    if sum(fingers) == 0:
        index = 0
    elif sum(fingers) == 2:
        index = 2
    elif sum(fingers) == 5:
        index = 1
    else:
        index = 3
    choice = list_of_moves[index]
    #print(f"You chose {choice}")
    return choice

def get_winner(computer_choice, user_choice):

        hierarchy = ["Rock", "Scissors", "Paper", "Rock"]

        if user_choice == "Nothing" or computer_choice == user_choice:
            return 0

        elif hierarchy.index(computer_choice) + 1 == hierarchy.index(user_choice,1):
            #print("You lost")
            return -1
            
        else:
            #print("You won!")
            return 1

computer_score = 0
user_score = 0
toggle = False
finished = False

x=time.time()
while True:
    ret, frame = cap.read()
    hands, img = detector.findHands(frame)
    cv2.putText(frame, "(Best of three)", (200,40),cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255),2)

    if (computer_score>1 or user_score>1):
        if computer_score>user_score:
            cv2.putText(frame, "Oh dear. Computer Wins :( ", (70,200),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
        if computer_score<user_score:
            cv2.putText(frame, "You Win!", (200,200),cv2.FONT_HERSHEY_COMPLEX, 1.2, (0,255,0),3)
        finished = True


    if toggle:
        x=time.time()
        #print(f"countdown reset")
        toggle = False
    
    count_down = 5-((np.floor(time.time()-x))%10)
    show_time = str(count_down)

    
    if (finished and count_down <=2 and cv2.waitKey(1)) or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    elif count_down >=0:
        cv2.putText(frame, show_time, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),3)
    else:
        try: 
            cv2.putText(frame, f"You chose {user_choice}", (400,250), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)
            cv2.putText(frame, f"Computer chose {computer_choice}", (30,250), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)
            if count_down < -3:
                result=get_winner(computer_choice,user_choice)
                if result ==1:
                    user_score += 1
                elif result == -1:
                    computer_score +=1
                #print("we got to here")
                del result
                del user_choice
                del computer_choice
                toggle = True
                    
        except:
            computer_choice = random.choice(list_of_comp_moves)
            user_choice = get_prediction(frame,hands)
            

    comp_score_str = f"Computer Score: {computer_score}"
    user_score_str = f"Your Score: {user_score}"

    cv2.putText(frame, comp_score_str, (30,400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0),2)
    cv2.putText(frame, user_score_str, (400,400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0),2)
    cv2.imshow('Rock Paper Scissors', frame)
    
    # Press q to close the window
        
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

