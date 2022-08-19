# Blackjack-Card-Counter-Object-Detection



This program is designed to count cards and calculate the best possible move for the player in a live Blackjack game. A neural network was trained using the Tensorflow 2.9.1 Object Detection API to detect playing cards and the detection is performed on an OpenCV 4.6.0 webcam feed.



# Mode 1: Card Counting Practice
* The purpose of this mode is to allow user's to practice card counting by displaying the current deck's count.

![Alt Text](https://media.giphy.com/media/yDYbF1KRknihaDIqVb/giphy-downsized-large.gif)

# Mode 2: Dealer vs. Player
* This mode calculates the player's best next move based on the overall deck's count, player and dealer's hand totals.
* NOTE: This is based on the Soft 17 Blackjack Deviation.

<img src="https://media.giphy.com/media/O49zPhgr0nj8KK2CP5/giphy-downsized-large.gif" alt="Sublime's custom image"/>

# There are two main sections for this project:

## 1. Install TensorFlow Object Detection API to Train a Custom Neural Network
* Train a neural network to detect all 52 types of playing cards in a deck. 
* The dataset that I used for this model is from: https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/1

<img src="https://i.imgur.com/sFVkPm7.png"/>


* The neural network architecture that I chose to train for this application is the SSD_RESNET152_V1_FPN_640x640_COCO17_TPU8
* My script will go through the entire process of creating the label map, TFRecords, and model pipeline config files required to train any Tensorflow 2 model for this specific application.
* You will observe the model's training process using Tensorboard: 

<img src = "https://i.imgur.com/ABy3j4Z.png"/> 


* Once you have successfully trained the model without finding any concerns in the training process, you will export the frozen graph to use it in part 2.
* I also included a section on how to export this as a TFLite model if you intend on deploying to a mobile device. NOTE: Not all model architectures are compatible in the TFLite format due to conflicting ops.

## 2. Perform Real time object detection:
* You will load the trained neural network model from part one and feed the inputs from a webcam feed to perform object detection. 
* OpenCV is used to handle the webcam input, draw the bounding boxes around detected cards, and the corresponding game information required by the user.
* When you feed the neural network a frame containing any one of the 52 playing cards, the neural network will output the following:
  1. Which class/card it believes that the detected object is
  2. The confidence/detection score of this detection
  3. The coordinates of the box that is bounding the detection
* With these output parameters, you can map out what the card is, and set a threshold on the detection score in order to actually display a bounding box.


# Current Limitations:
1. The count is based on a single deck game. You can easily scale the count by dividing by the total number of decks in the shoe.
2. Multiple deck games will also need to the program to allow detections of multiple identical cards.
3. As for any object detection model, speed and accuracy of the object detection model will always be a limiting factor in performance. I intend on training the YOLOV5 model for this application in the near future.
4. Need to allow seperate hand totals and next moves for a player who splits his hand into two.
