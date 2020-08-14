#Lucas mburu

#system takes full details of all visitors and gives out detailed declaration for records.

visitor=input("name please:")

colour =input("Enter HOUSE colour:")

private_word=input("Enter a PRIVATE WORD:")

main_person=input(" Enter the name of main occupant:")

time_arrival=input("Enter time in :")

house_location=input("enter location of house being visited: ")

type_of_visit=input(" courtesy or scheduled:")

print("Hi"  + visitor + "Welcome to our Neighbourhood")

print(" your are here to visit "+ colour + "houses section" )

print("you have been given " + private_word + " by the Host")

print("mr/mrs." + main_person + " shall verify the information on "+ private_word )

print(" we have noted your" + time_arrival + " to see" + main_person + "at"+ house_location )

print("your" + type_of_visit + " with "+ main_person +" is up for aproval and you shall be notified shortly")


#the host is alerted


print(+visitor+ "is coming to visit you" +house_location+"for a" + type_of_visit+ "visit")

aproval= input(" yes/no")

yes=True
no=False

if True:
    print(" your" + visitor + "will be on his way")
elif False:
    print("your "+ visitor+ "wont be allowed in")
else:
    print("invalid input")


#after the guest departs to the host,camera take in movement feed.

import cv2
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()