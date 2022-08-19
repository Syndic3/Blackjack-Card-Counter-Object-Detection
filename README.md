# Blackjack-Card-Counter-Object-Detection



This program is designed to count cards and calculate the best possible move for the player in a live Blackjack game. A neural network was trained using the Tensorflow Object Detection API to detect playing cards and the detection is performed on an OpenCV webcam feed.


# Mode 1: Card Counting Practice
* This mode is simply 
![Alt Text](https://media.giphy.com/media/yDYbF1KRknihaDIqVb/giphy-downsized-large.gif)

# Mode 2: Dealer vs. Player

<img src="https://media.giphy.com/media/O49zPhgr0nj8KK2CP5/giphy-downsized-large.gif" alt="Sublime's custom image"/>

# There are two main sections for this project:

## 1. Install TensorFlow Object Detection API to Train a Custom Neural Network
* Train a neural network to detect all 52 types of playing cards in a deck. 
* The dataset that I used for this model is from: https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/1
<img src = "https://i.imgur.com/sFVkPm7.png">
* The neural network that I chose for this application is the SSD_RESNET152_V1_FPN_640x640_COCO17_TPU8 neural network architecture.
* My script will go through the entire process of creating the label map, TFRecords, and model pipeline config files required to train any Tensorflow 2 model for this specific application.
* You will observe the model's training process using Tensorboard: 
<img src = "https://i.imgur.com/ABy3j4Z.png"> 
* Once you have successfully trained the model without finding any concerns in the training process, you will export the frozen graph to use it in part 2.
* I also included a section on how to export this as a TFLite model if you intend on deploying to a mobile device. NOTE: Not all model architectures are compatible in the TFLite format due to conflicting ops.

## 2. Perform Real time object detection:

- where you will load the trained neural network from part one and feed it a live webcam feed to perform object detection. 
-Using the neural network's output, you will then be able to determine the following: 1. The current count of the deck, both the dealer's and player's hand total, and the best next move for the player (based on Stand on Soft 17 Blackjack rules).




# Current Restrictions:
1. Count is based on a single deck game. You can easily scale the count by dividing by the number of decks in a shoe.
2. I will also need to allow for detections of multiple identical cards if this is used for a multi-deck game.
3. As for any object detection model, speed and accuracy of the object detection model will always be a limiting factor in performance.
