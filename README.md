# FacialRecognization
Facial Recognization without any Neural Networks, thus limiting flexibility. It's enough to work with for beginners.

The data_gathering.py file uses the video feed input to take in the faces of the users, along with a user id input by the user. The no.of images to be taken for each person is changeable by tweaking around the if condition for the while loop's exit. 
Training is to be run for obtaining a 'yml' file that can be used to identify the faces of the registered users.
There isn't much functionality with the name association of the users. And it must be entered manually into the code of Facial_Recognition into it's name's array

Also two directories are needed to store the dataset( the images gathered) separate from the rest of the program.
Download and place the frontalface haarcascade into directories for this to work.
You need to run Training every time a new face has been added. And the data gatherin itself is in a current state to accept only 1 user input per run. I plan on improving that.
