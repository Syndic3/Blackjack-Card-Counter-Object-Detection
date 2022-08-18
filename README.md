# Blackjack-Card-Counter-Object-Detection


I created this program to count cards for a live Blackjack game using a trained neural network and live webcam feed using OpenCV.

There are two main sections for this project:

1. Install tensorflow, and train a neural network to detect all 52 types of playing cards in a deck.
2. Real time object detection; where you will load the trained neural network from part one and feed it a live webcam feed to perform object detection. Using the neural network's output, you will then be able to determine the following: 1. The current count of the deck, both the dealer's and player's hand total, and the best next move for the player (based on Stand on Soft 17 Blackjack rules).







#Current Restrictions:
1. Count is based on a single deck game. You can easily scale the count by dividing by the number of decks in a shoe.
2. I will also need to allow for detections of multiple identical cards if this is used for a multi-deck game.
3. As for any object detection model, speed and accuracy of the object detection model will always be a limiting factor in performance.
