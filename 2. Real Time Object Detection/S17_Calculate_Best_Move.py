#!/usr/bin/env python
# coding: utf-8

# In[1]:


#calculate sum of all non-ace cards in hand first

def calculate_hand(hand_total,x):
    if x.isalpha(): #J,Q,K 
        hand_total+=10
    else: #2,3,4,5,6,7,8,9,10
        hand_total=hand_total+int(x)
    return hand_total


# In[2]:


#this function handles calculating the soft/hard totals of a hand given a list of detections

#Calculate the hand's soft/hard total if it contains aces

def hand_total(input_hand):
    detections_list=input_hand
    ace_count = 0 
    card_total = 0
    soft_total = False
    for i in detections_list:
        i = str(i)[:-1] #trim the suit character from each string in the list
        
        if (i =='A'): #count number of aces in hand
            ace_count+=1
        else: #only add the non-aces to the card total first
            card_total = calculate_hand(card_total,i)

    #adding aces to card total IF they exist:
    remainder = 21-card_total
    ace_11 = 0
    
    # >1 ace in hand
    if (ace_count>0 and remainder/11>1):
        ace_11 = 1
        ace_count -= 1 #subtract the ace that became '11'
 
        #if having an ace == 11 causes a bust, then every ace must equal 1
    
        if ((card_total + ace_11*11 + (ace_count))>21): 
            #convert the ace_11 to == 1 
            ace_11 -=1
            ace_count +=1
        
        card_total = card_total + ace_count * 1 + ace_11 * 11
    else: 
        card_total = card_total + ace_count * 1
    
    if ace_11>0:
        soft_total=True
    
    return card_total, soft_total


# In[3]:


#check if the card values without suits match.
def is_hand_pair(player_detections):
    if (str(player_detections[0])[:-1]==str(player_detections[1])[:-1]):
        return True


# In[4]:


#Calculate move based on count, dealers up-card, and on player's soft-total

def soft_totals(player_detections,player_hand_total, dealer_total, count):
    if player_hand_total == 20:
        return 'Stand'
    elif player_hand_total == 19:
        if dealer_total == 4:
            if count >= 3:
                return 'Double'
            else:
                return 'Stand'
        elif dealer_total == 5:
            if count >=1:    
                return 'Double'
            else:
                return 'Stand'
        elif dealer_total == 6:
            if count >=1:
                return 'Double'
            else:
                return 'Stand'
        else:
            return 'Stand'
    elif player_hand_total == 18:
        if dealer_total>=2 and dealer_total<=6:
            return 'Double'
        elif dealer_total in {7,8}:
            return 'Stand'
        else: 
            return 'Hit'
    
    elif player_hand_total == 17:
        if (dealer_total == 2):
            if count >=1:
                return 'Double'
            else: 
                return 'Hit'
                
        elif (dealer_total>=3 and dealer_total<=6):
            return 'Double'
        else:
            return 'Hit'
        
    elif player_hand_total in {16,15}:
        if dealer_total>=4 and dealer_total<=6:
            return 'Double'
        else: 
            return 'Hit'
    elif player_hand_total in {14,13}:
        if dealer_total in [5,6]:
            return 'Double'
        else: 
            return 'Hit'


# In[5]:


#Calculate move based on count, dealers up-card, and on player's hard-total
def hard_totals(player_detections,player_hand_total, dealer_total, count):
    if player_hand_total >=17 and player_hand_total <= 21:
        return 'Stand'
    elif player_hand_total == 16:
        if dealer_total == 9:
            if count >=4:
                return 'Stand'
            else:
                return 'Hit'
        elif dealer_total == 10:
            if count >=0:
                return 'Stand'
            else: 
                return 'Hit'
        elif dealer_total in {7,8,11}:
            return 'Hit'
        else:
            return 'Stand'
    elif player_hand_total == 15:
        if dealer_total == 10:
            if count >=4:
                return 'Stand'
            else: 
                return 'Hit'
            
        elif dealer_total>=2 and dealer_total<=6:
            return 'Stand'
        else: 
            return 'Hit'
    elif player_hand_total == 14:
        if dealer_total>=2 and dealer_total <=6:
            return 'Stand'
        else: 
            return 'Hit'

    elif player_hand_total == 13:
        if dealer_total ==2:
            if count<=-1:
                return 'Hit'
            else: 
                return 'Stand'
        
        elif dealer_total>=3 and dealer_total <=6:
            return 'Stand'
        else: 
            return 'Hit'
    
    elif player_hand_total == 12:
        if dealer_total ==2:
            if count >=3:
                return 'Stand'
            else:
                return 'Hit'
        elif dealer_total == 3:
            if count >=2:
                return 'Stand'
            else:
                return 'Hit'
        elif dealer_total == 4:
            if count <=0:
                return 'Hit'
            else:
                return 'Stand'
        elif dealer_total in {5,6}:
            return 'Stand'
        elif dealer_total>=6 and dealer_total<=11:
            return 'Hit'
        else: 
            return 'Hit'
        
    elif player_hand_total == 11:
        if dealer_total == 11:
            if count >=1:
                return 'Double'
            else:
                return 'Hit'
        else:
            return 'Double'
    
    elif player_hand_total == 10:
        if (dealer_total in {10,11}):
            if count >=4:
                return 'Double'
            else: 
                return 'Hit'
        else:
            return 'Double'
    elif player_hand_total == 9:
        if dealer_total == 7:
            if count >= 3:
                return 'Double'
            else:
                return 'Hit'
        elif dealer_total == 2:
            if count >=1:
                return 'Double'
            else:
                return 'Hit'
        elif dealer_total >=3 and dealer_total <=6:
            return 'Double'
        else: 
            return 'Hit'
            
    elif player_hand_total == 8:
        if dealer_total == 6 and count >=2:
            return 'Double'
        else:
            return 'Hit'
    else:
        return 'Hit'
    


# In[14]:


def soft_17(player_detections, dealer_hand_total, count):
    
    player_detections=player_detections[0]
    player_hand_size = len(player_detections)
   

    player_hand_total, soft_total = hand_total(player_detections)

    #print("player's hand == ", player_detections)
    
    decision= None
    
    #Step 1: Check if hand is == 2 cards, then check if it is a pair.
    
    if player_hand_size == 2:
        #Step 2: Check if hand is a pair
        if is_hand_pair(player_detections):
            #if it is a pair, then call pairs()
            decision = pairs(player_detections, dealer_hand_total, count)    
        else: #Not a pair
            decision = 'Continue'
            
    #Step 2: If this player previously hit, or the original hand is not a pair:
    
    if player_hand_size >2 or decision == 'Continue':
        #2.A Hand is a Soft-total
        if soft_total == True:
            decision = soft_totals(player_detections,player_hand_total, dealer_hand_total, count)
        #2.B Hand is a Hard-Total
        else:
            decision = hard_totals(player_detections,player_hand_total, dealer_hand_total, count)    
    return decision    
    
    


# In[7]:


def pairs(player_detection, dealer_total, count):
    player_pair = player_detection[0][:-1]
    
    if player_pair in ('A','8'):
        return 'Split'
    if player_pair == 'A':
        return 'Split'
    
    elif player_pair == '10':
        print("pairs() == 10")
        if count <4:
            return 'Stand'
        else:
            if dealer_total == 6 and count >=4:
                return 'Split'
            elif dealer_total == 5 and count >=5:
                return 'Split'
            elif dealer_total == 4 and count >=6:
                return 'Split'
            else:
                return 'Stand'
            
    elif player_pair == '9':
        if dealer_total in [7,10,11]:
            return 'Stand'
        else:
            return 'Split'
        
    elif player_pair =='7':
        if dealer_total in [8,9,10,11]:
            return 'Continue'
        else:
            return 'Split' 
    
    elif player_pair == '6':
        if dealer_total in (3,4,5,6):
            return 'Split'
        else:
            return 'Continue' 
        
    elif player_pair in ('5','4'): #Double after stand is typically not seen in my experience
        return 'Continue'
    
    elif player_pair in ('3','2'):
        if (dealer_total in (4,5,6,7)):
            return 'Split'
        else:
            return 'Continue'

    
    
