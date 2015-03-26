#!/bin/env python3.4

from random import choice

def main():
	#rooms in numbers
	room_numbers = range(1,21)
	
	#spawning in the game
	wumpus_location = choice(room_numbers)
	player_location = choice(room_numbers)
	gold_location = choice(room_numbers)
	gold2_location = choice(room_numbers)
	pit_location = choice(room_numbers)
	pit2_location = choice(room_numbers)
	bats_location = choice(room_numbers)
	bats2_location = choice(room_numbers)
	
	#set gold parameter
	gold = 0
	
	#set arrow parameter
	arrows = 0
	
	
#fixing that all spawnings are in a free room:
	
	#player has to start in a free cave
	while player_location == wumpus_location:
		player_location = choice(room_numbers)
	while player_location == gold_location:
		player_location = choice(room_numbers)
	while player_location == gold2_location:
		player_location = choice(room_numbers)
	while player_location == pit_location:
		player_location = choice(room_numbers)		
	while player_location == pit2_location:
		player_location = choice(room_numbers)
	while player_location == bats_location:
		player_location = choice(room_numbers)
	while player_location == bats2_location:
		player_location = choice(room_numbers)	
		
	#wumpus in free cave	
	while wumpus_location == gold_location:
		wumpus_location = choice(room_numbers)
	while wumpus_location == gold2_location:
		wumpus_location = choice(room_numbers)
	while wumpus_location == pit_location:
		wumpus_location = choice(room_numbers)
	while wumpus_location == pit2_location:
		wumpus_location = choice(room_numbers)
	while wumpus_location == bats_location:
		wumpus_location = choice(room_numbers)
	while wumpus_location == bats2_location:
		wumpus_location = choice(room_numbers)
	
	#gold1 in free cave
	while gold_location == gold2_location:
		gold_location = choice(room_numbers)
	while gold_location == pit_location:
		gold_location = choice(room_numbers)
	while gold_location == pit2_location:
		gold_location = choice(room_numbers)
	while gold_location == bats_location:
		gold_location = choice(room_numbers)
	while gold_location == bats2_location:
		gold_location = choice(room_numbers)
	
	#gold2 in free cave
	while gold2_location == pit_location:
		gold2_location = choice(room_numbers)
	while gold2_location == pit2_location:
		gold2_location = choice(room_numbers)
	while gold2_location == bats_location:
		gold2_location = choice(room_numbers)
	while gold2_location == bats2_location:
		gold2_location = choice(room_numbers)
	
	#pit in free cave
	while pit_location == pit2_location:
		pit_location = choice(room_numbers)
	while pit_location == bats_location:
		pit_location = choice(room_numbers)
	while pit_location == bats2_location:
		pit_location = choice(room_numbers)
	
	#pit2 in free cave
	while pit2_location == bats_location:
		pit2_location = choice(room_numbers)
	while pit2_location == bats2_location:
		pit2_location = choice(room_numbers)
	
	#bat in free cave
	while bats_location == bats2_location:
		bats_location = choice(room_numbers)
		
	print("Welcome to Hunt the Wumpus!")
	print("You can see", len(room_numbers),"caves")
	print("To play, just type the number")
	print("of the cave you wish to enter next.")
	
	room1 = 1
	room2 = 2
	room3 = 3
	room4 = 4
	room5 = 5
	room6 = 6
	room7 = 7
	room8 = 8
	room9 = 9
	room10 = 10
	room11 = 11
	room12 = 12
	room13 = 13
	room14 = 14
	room15 = 15
	room16 = 16
	room17 = 17
	room18 = 18
	room19 = 19
	room20 = 20
	
	
	#caving
	while True:
		print("You are in room", player_location)
		
		#player near wumpus, in corner rooms
		if(player_location == room1 and (wumpus_location == room2 or wumpus_location == room5)):
			print("I smell the wumpus")
		if(player_location == room4 and (wumpus_location == room3 or wumpus_location == room8)):
			print("I smell the wumpus")
		if(player_location == room17 and (wumpus_location == room13 or wumpus_location == room18)):
			print("I smell the wumpus")
		if(player_location == room20 and (wumpus_location == room19 or wumpus_location == room16)):
			print("I smell the wumpus")
		#player near wompus, on the side of the field
		if(player_location == room2 and (wumpus_location == room1 or wumpus_location == room3 or wumpus_location == room6)):
			print("I smell the wumpus")
		if(player_location == room3 and (wumpus_location == room2 or wumpus_location == room4 or wumpus_location == room7)):
			print("I smell the wompus")
		if(player_location == room5 and (wumpus_location == room1 or wumpus_location == room6 or wumpus_location == room9)):
			print("I smell the wumpus")
		if(player_location == room9 and (wumpus_location == room5 or wumpus_location == room10 or wumpus_location == room13)):
			print("I smell the wumpus")
		if(player_location == room13 and (wumpus_location == room9 or wumpus_location == room14 or wumpus_location == room17)):
			print("I smell the wumpus")
		if(player_location == room8 and (wumpus_location == room4 or wumpus_location == room7 or wumpus_location == room12)):
			print("I smell the wumpus")
		if(player_location == room12 and (wumpus_location == room8 or wumpus_location == room11 or wumpus_location == room16)):
			print("I smell the wumpus")
		if(player_location == room16 and (wumpus_location == room12 or wumpus_location == room15 or wumpus_location == room20)):
			print("I smell the wumpus")
		if(player_location == room18 and (wumpus_location == room14 or wumpus_location == room17 or wumpus_location == room19)):
			print("I smell the wumpus")
		if(player_location == room19 and (wumpus_location == room15 or wumpus_location == room18 or wumpus_location == room20)):
			print("I smell the wumpus")
		#player near wompus, in the middle
		if(player_location == room6 and (wumpus_location == room2 or wumpus_location == room5 or wumpus_location == room7 or wumpus_location == room10)):
			print("I smell the wumpus")
		if(player_location == room7 and (wumpus_location == room3 or wumpus_location == room6 or wumpus_location == room8 or wumpus_location == room11)):
			print("I smell the wumpus")
		if(player_location == room10 and (wumpus_location == room6 or wumpus_location == room9 or wumpus_location == room11 or wumpus_location == room14)):
			print("I smell the wumpus")
		if(player_location == room11 and (wumpus_location == room7 or wumpus_location == room10 or wumpus_location == room12 or wumpus_location == room15)):
			print("I smell the wumpus")
		if(player_location == room14 and (wumpus_location == room10 or wumpus_location == room13 or wumpus_location == room15 or wumpus_location == room18)):
			print("I smell the wumpus")
		if(player_location == room15 and (wumpus_location == room11 or wumpus_location == room14 or wumpus_location == room16 or wumpus_location == room19)):
			print("I smell the wumpus")
		
		#gold
		#player near gold, in corner rooms
		if(player_location == room1 and (gold_location == room2 or gold_location == room5)):
			print("I can see a glimmer")
		if(player_location == room4 and (gold_location == room3 or gold_location == room8)):
			print("I can see a glimmer")
		if(player_location == room17 and (gold_location == room13 or gold_location == room18)):
			print("I can see a glimmer")
		if(player_location == room20 and (gold_location == room19 or gold_location == room16)):
			print("I can see a glimmer")
		#player near gold, on the side of the field
		if(player_location == room2 and (gold_location == room1 or gold_location == room3 or gold_location == room6)):
			print("I can see a glimmer")
		if(player_location == room3 and (gold_location == room2 or gold_location == room4 or gold_location == room7)):
			print("I can see a glimmer")
		if(player_location == room5 and (gold_location == room1 or gold_location == room6 or gold_location == room9)):
			print("I can see a glimmer")
		if(player_location == room9 and (gold_location == room5 or gold_location == room10 or gold_location == room13)):
			print("I can see a glimmer")
		if(player_location == room13 and (gold_location == room9 or gold_location == room14 or gold_location == room17)):
			print("I can see a glimmer")
		if(player_location == room8 and (gold_location == room4 or gold_location == room7 or gold_location == room12)):
			print("I can see a glimmer")
		if(player_location == room12 and (gold_location == room8 or gold_location == room11 or gold_location == room16)):
			print("I can see a glimmer")
		if(player_location == room16 and (gold_location == room12 or gold_location == room15 or gold_location == room20)):
			print("I can see a glimmer")
		if(player_location == room18 and (gold_location == room14 or gold_location == room17 or gold_location == room19)):
			print("I can see a glimmer")
		if(player_location == room19 and (gold_location == room15 or gold_location == room18 or gold_location == room20)):
			print("I can see a glimmer")
		#player near gold, in the middle
		if(player_location == room6 and (gold_location == room2 or gold_location == room5 or gold_location == room7 or gold_location == room10)):
			print("I can see a glimmer")
		if(player_location == room7 and (gold_location == room3 or gold_location == room6 or gold_location == room8 or gold_location == room11)):
			print("I can see a glimmer")
		if(player_location == room10 and (gold_location == room6 or gold_location == room9 or gold_location == room11 or gold_location == room14)):
			print("I can see a glimmer")
		if(player_location == room11 and (gold_location == room7 or gold_location == room10 or gold_location == room12 or gold_location == room15)):
			print("I can see a glimmer")
		if(player_location == room14 and (gold_location == room10 or gold_location == room13 or gold_location == room15 or gold_location == room18)):
			print("I can see a glimmer")
		if(player_location == room15 and (gold_location == room11 or gold_location == room14 or gold_location == room16 or gold_location == room19)):
			print("I can see a glimmer")
			
		## gold2	
		#player near gold, in corner rooms
		if(player_location == room1 and (gold2_location == room2 or gold2_location == room5)):
			print("I can see a glimmer")
		if(player_location == room4 and (gold2_location == room3 or gold2_location == room8)):
			print("I can see a glimmer")
		if(player_location == room17 and (gold2_location == room13 or gold2_location == room18)):
			print("I can see a glimmer")
		if(player_location == room20 and (gold2_location == room19 or gold2_location == room16)):
			print("I can see a glimmer")
		#player near gold, on the side of the field
		if(player_location == room2 and (gold2_location == room1 or gold2_location == room3 or gold2_location == room6)):
			print("I can see a glimmer")
		if(player_location == room3 and (gold2_location == room2 or gold2_location == room4 or gold2_location == room7)):
			print("I can see a glimmer")
		if(player_location == room5 and (gold2_location == room1 or gold2_location == room6 or gold2_location == room9)):
			print("I can see a glimmer")
		if(player_location == room9 and (gold2_location == room5 or gold2_location == room10 or gold2_location == room13)):
			print("I can see a glimmer")
		if(player_location == room13 and (gold2_location == room9 or gold2_location == room14 or gold2_location == room17)):
			print("I can see a glimmer")
		if(player_location == room8 and (gold2_location == room4 or gold2_location == room7 or gold2_location == room12)):
			print("I can see a glimmer")
		if(player_location == room12 and (gold2_location == room8 or gold2_location == room11 or gold2_location == room16)):
			print("I can see a glimmer")
		if(player_location == room16 and (gold2_location == room12 or gold2_location == room15 or gold2_location == room20)):
			print("I can see a glimmer")
		if(player_location == room18 and (gold2_location == room14 or gold2_location == room17 or gold2_location == room19)):
			print("I can see a glimmer")
		if(player_location == room19 and (gold2_location == room15 or gold2_location == room18 or gold2_location == room20)):
			print("I can see a glimmer")
		#player near gold, in the middle
		if(player_location == room6 and (gold2_location == room2 or gold2_location == room5 or gold2_location == room7 or gold2_location == room10)):
			print("I can see a glimmer")
		if(player_location == room7 and (gold2_location == room3 or gold2_location == room6 or gold2_location == room8 or gold2_location == room11)):
			print("I can see a glimmer")
		if(player_location == room10 and (gold2_location == room6 or gold2_location == room9 or gold2_location == room11 or gold2_location == room14)):
			print("I can see a glimmer")
		if(player_location == room11 and (gold2_location == room7 or gold2_location == room10 or gold2_location == room12 or gold2_location == room15)):
			print("I can see a glimmer")
		if(player_location == room14 and (gold2_location == room10 or gold2_location == room13 or gold2_location == room15 or gold2_location == room18)):
			print("I can see a glimmer")
		if(player_location == room15 and (gold2_location == room11 or gold2_location == room14 or gold2_location == room16 or gold2_location == room19)):
			print("I can see a glimmer")
		
		#pit		
		#player near pit, in corner rooms
		if(player_location == room1 and (pit_location == room2 or pit_location == room5)):
			print("I can feel the draft of a pit")
		if(player_location == room4 and (pit_location == room3 or pit_location == room8)):
			print("I can feel the draft of a pit")
		if(player_location == room17 and (pit_location == room13 or pit_location == room18)):
			print("I can feel the draft of a pit")
		if(player_location == room20 and (pit_location == room19 or pit_location == room16)):
			print("I can feel the draft of a pit")
		#player near wompus, on the side of the field
		if(player_location == room2 and (pit_location == room1 or pit_location == room3 or pit_location == room6)):
			print("I can feel the draft of a pit")
		if(player_location == room3 and (pit_location == room2 or pit_location == room4 or pit_location == room7)):
			print("I can feel the draft of a pit")
		if(player_location == room5 and (pit_location == room1 or pit_location == room6 or pit_location == room9)):
			print("I can feel the draft of a pit")
		if(player_location == room9 and (pit_location == room5 or pit_location == room10 or pit_location == room13)):
			print("I can feel the draft of a pit")
		if(player_location == room13 and (pit_location == room9 or pit_location == room14 or pit_location == room17)):
			print("I can feel the draft of a pit")
		if(player_location == room8 and (pit_location == room4 or pit_location == room7 or pit_location == room12)):
			print("I can feel the draft of a pit")
		if(player_location == room12 and (pit_location == room8 or pit_location == room11 or pit_location == room16)):
			print("I can feel the draft of a pit")
		if(player_location == room16 and (pit_location == room12 or pit_location == room15 or pit_location == room20)):
			print("I can feel the draft of a pit")
		if(player_location == room18 and (pit_location == room14 or pit_location == room17 or pit_location == room19)):
			print("I can feel the draft of a pit")
		if(player_location == room19 and (pit_location == room15 or pit_location == room18 or pit_location == room20)):
			print("I can feel the draft of a pit")
		#player near wompus, in the middle
		if(player_location == room6 and (pit_location == room2 or pit_location == room5 or pit_location == room7 or pit_location == room10)):
			print("I can feel the draft of a pit")
		if(player_location == room7 and (pit_location == room3 or pit_location == room6 or pit_location == room8 or pit_location == room11)):
			print("I can feel the draft of a pit")
		if(player_location == room10 and (pit_location == room6 or pit_location == room9 or pit_location == room11 or pit_location == room14)):
			print("I can feel the draft of a pit")
		if(player_location == room11 and (pit_location == room7 or pit_location == room10 or pit_location == room12 or pit_location == room15)):
			print("I can feel the draft of a pit")
		if(player_location == room14 and (pit_location == room10 or pit_location == room13 or pit_location == room15 or pit_location == room18)):
			print("I can feel the draft of a pit")
		if(player_location == room15 and (pit_location == room11 or pit_location == room14 or pit_location == room16 or pit_location == room19)):
			print("I can feel the draft of a pit")
		
		#pit 2	
		#player near pit, in corner rooms
		if(player_location == room1 and (pit2_location == room2 or pit2_location == room5)):
			print("I can feel the draft of a pit")
		if(player_location == room4 and (pit2_location == room3 or pit2_location == room8)):
			print("I can feel the draft of a pit")
		if(player_location == room17 and (pit2_location == room13 or pit2_location == room18)):
			print("I can feel the draft of a pit")
		if(player_location == room20 and (pit2_location == room19 or pit2_location == room16)):
			print("I can feel the draft of a pit")
		#player near pit, on the side of the field
		if(player_location == room2 and (pit2_location == room1 or pit2_location == room3 or pit2_location == room6)):
			print("I can feel the draft of a pit")
		if(player_location == room3 and (pit2_location == room2 or pit2_location == room4 or pit2_location == room7)):
			print("I can feel the draft of a pit")
		if(player_location == room5 and (pit2_location == room1 or pit2_location == room6 or pit2_location == room9)):
			print("I can feel the draft of a pit")
		if(player_location == room9 and (pit2_location == room5 or pit2_location == room10 or pit2_location == room13)):
			print("I can feel the draft of a pit")
		if(player_location == room13 and (pit2_location == room9 or pit2_location == room14 or pit2_location == room17)):
			print("I can feel the draft of a pit")
		if(player_location == room8 and (pit2_location == room4 or pit2_location == room7 or pit2_location == room12)):
			print("I can feel the draft of a pit")
		if(player_location == room12 and (pit2_location == room8 or pit2_location == room11 or pit2_location == room16)):
			print("I can feel the draft of a pit")
		if(player_location == room16 and (pit2_location == room12 or pit2_location == room15 or pit2_location == room20)):
			print("I can feel the draft of a pit")
		if(player_location == room18 and (pit2_location == room14 or pit2_location == room17 or pit2_location == room19)):
			print("I can feel the draft of a pit")
		if(player_location == room19 and (pit2_location == room15 or pit2_location == room18 or pit2_location == room20)):
			print("I can feel the draft of a pit")
		#player near pit, in the middle
		if(player_location == room6 and (pit2_location == room2 or pit2_location == room5 or pit2_location == room7 or pit2_location == room10)):
			print("I can feel the draft of a pit")
		if(player_location == room7 and (pit2_location == room3 or pit2_location == room6 or pit2_location == room8 or pit2_location == room11)):
			print("I can feel the draft of a pit")
		if(player_location == room10 and (pit2_location == room6 or pit2_location == room9 or pit2_location == room11 or pit2_location == room14)):
			print("I can feel the draft of a pit")
		if(player_location == room11 and (pit2_location == room7 or pit2_location == room10 or pit2_location == room12 or pit2_location == room15)):
			print("I can feel the draft of a pit")
		if(player_location == room14 and (pit2_location == room10 or pit2_location == room13 or pit2_location == room15 or pit2_location == room18)):
			print("I can feel the draft of a pit")
		if(player_location == room15 and (pit2_location == room11 or pit2_location == room14 or pit2_location == room16 or pit2_location == room19)):
			print("I can feel the draft of a pit")
			
		#Bat
		#player near bats, in corner rooms
		if(player_location == room1 and (bats_location == room2 or bats_location == room5)):
			print("I can hear the flapping of wings")
		if(player_location == room4 and (bats_location == room3 or bats_location == room8)):
			print("I can hear the flapping of wings")
		if(player_location == room17 and (bats_location == room13 or bats_location == room18)):
			print("I can hear the flapping of wings")
		if(player_location == room20 and (bats_location == room19 or bats_location == room16)):
			print("I can hear the flapping of wings")
		#player near bats, on the side of the field
		if(player_location == room2 and (bats_location == room1 or bats_location == room3 or bats_location == room6)):
			print("I can hear the flapping of wings")
		if(player_location == room3 and (bats_location == room2 or bats_location == room4 or bats_location == room7)):
			print("I can hear the flapping of wings")
		if(player_location == room5 and (bats_location == room1 or bats_location == room6 or bats_location == room9)):
			print("I can hear the flapping of wings")
		if(player_location == room9 and (bats_location == room5 or bats_location == room10 or bats_location == room13)):
			print("I can hear the flapping of wings")
		if(player_location == room13 and (bats_location == room9 or bats_location == room14 or bats_location == room17)):
			print("I can hear the flapping of wings")
		if(player_location == room8 and (bats_location == room4 or bats_location == room7 or bats_location == room12)):
			print("I can hear the flapping of wings")
		if(player_location == room12 and (bats_location == room8 or bats_location == room11 or bats_location == room16)):
			print("I can hear the flapping of wings")
		if(player_location == room16 and (bats_location == room12 or bats_location == room15 or bats_location == room20)):
			print("I can hear the flapping of wings")
		if(player_location == room18 and (bats_location == room14 or bats_location == room17 or bats_location == room19)):
			print("I can hear the flapping of wings")
		if(player_location == room19 and (bats_location == room15 or bats_location == room18 or bats_location == room20)):
			print("I can hear the flapping of wings")
		#player near bats, in the middle
		if(player_location == room6 and (bats_location == room2 or bats_location == room5 or bats_location == room7 or bats_location == room10)):
			print("I can hear the flapping of wings")
		if(player_location == room7 and (bats_location == room3 or bats_location == room6 or bats_location == room8 or bats_location == room11)):
			print("I can hear the flapping of wings")
		if(player_location == room10 and (bats_location == room6 or bats_location == room9 or bats_location == room11 or bats_location == room14)):
			print("I can hear the flapping of wings")
		if(player_location == room11 and (bats_location == room7 or bats_location == room10 or bats_location == room12 or bats_location == room15)):
			print("I can hear the flapping of wings")
		if(player_location == room14 and (bats_location == room10 or bats_location == room13 or bats_location == room15 or bats_location == room18)):
			print("I can hear the flapping of wings")
		if(player_location == room15 and (bats_location == room11 or bats_location == room14 or bats_location == room16 or bats_location == room19)):
			print("I can hear the flapping of wings")
		
		#bat2
        #player near bats, in corner rooms
		if(player_location == room1 and (bats2_location == room2 or bats2_location == room5)):
			print("I can hear the flapping of wings")
		if(player_location == room4 and (bats2_location == room3 or bats2_location == room8)):
			print("I can hear the flapping of wings")
		if(player_location == room17 and (bats2_location == room13 or bats2_location == room18)):
			print("I can hear the flapping of wings")
		if(player_location == room20 and (bats2_location == room19 or bats2_location == room16)):
			print("I can hear the flapping of wings")
		#player near bats, on the side of the field
		if(player_location == room2 and (bats2_location == room1 or bats2_location == room3 or bats2_location == room6)):
			print("I can hear the flapping of wings")
		if(player_location == room3 and (bats2_location == room2 or bats2_location == room4 or bats2_location == room7)):
			print("I can hear the flapping of wings")
		if(player_location == room5 and (bats2_location == room1 or bats2_location == room6 or bats2_location == room9)):
			print("I can hear the flapping of wings")
		if(player_location == room9 and (bats2_location == room5 or bats2_location == room10 or bats2_location == room13)):
			print("I can hear the flapping of wings")
		if(player_location == room13 and (bats2_location == room9 or bats2_location == room14 or bats2_location == room17)):
			print("I can hear the flapping of wings")
		if(player_location == room8 and (bats2_location == room4 or bats2_location == room7 or bats2_location == room12)):
			print("I can hear the flapping of wings")
		if(player_location == room12 and (bats2_location == room8 or bats2_location == room11 or bats2_location == room16)):
			print("I can hear the flapping of wings")
		if(player_location == room16 and (bats2_location == room12 or bats2_location == room15 or bats2_location == room20)):
			print("I can hear the flapping of wings")
		if(player_location == room18 and (bats2_location == room14 or bats2_location == room17 or bats2_location == room19)):
			print("I can hear the flapping of wings")
		if(player_location == room19 and (bats2_location == room15 or bats2_location == room18 or bats2_location == room20)):
			print("I can hear the flapping of wings")
		#player near bats, in the middle
		if(player_location == room6 and (bats2_location == room2 or bats2_location == room5 or bats2_location == room7 or bats2_location == room10)):
			print("I can hear the flapping of wings")
		if(player_location == room7 and (bats_location == room3 or bats2_location == room6 or bats2_location == room8 or bats2_location == room11)):
			print("I can hear the flapping of wings")
		if(player_location == room10 and (bats2_location == room6 or bats2_location == room9 or bats2_location == room11 or bats2_location == room14)):
			print("I can hear the flapping of wings")
		if(player_location == room11 and (bats2_location == room7 or bats2_location == room10 or bats2_location == room12 or bats2_location == room15)):
			print("I can hear the flapping of wings")
		if(player_location == room14 and (bats2_location == room10 or bats2_location == room13 or bats2_location == room15 or bats2_location == room18)):
			print("I can hear the flapping of wings")
		if(player_location == room15 and (bats2_location == room11 or bats2_location == room14 or bats2_location == room16 or bats2_location == room19)):
			print("I can hear the flapping of wings")	
				
#######################################################		
		#shoot or move?
		
		
		print("Do you want to shoot or move? (S-M)")
		player_input1 = input(">")
		if (player_input1 == "M" or player_input1 == "m"):
			print("Move to what room? (1-20)")
			player_input = input(">")
			player_location = int(player_input)
		
		#shoot arrows	
		else:
			print("You can only Shoot one Arrow, Use it wisely")
			print("What room do you want to shoot in?")
			player_input2 = input(">")
			if int(player_input2) == int(wumpus_location):
					print("You hit the wumpus !!!, You won and take home", gold, "gold pieces")
					break
			else:
				print("You missed")
				print("Move to what room? (1-20)")
				player_input = input(">")
				player_location = int(player_input)
					
		
		#find gold (1)
		if int(player_input) == (gold_location):
			player_location = int(player_input)
			gold = gold +1
			print("Hey! ..... You Found some Gold!")
			print("You now have", gold, "pieces of gold")
			#gold out of layout
			gold_location = None
			
		
		#find gold (2)
		elif int(player_input) == (gold2_location):
			player_location = int(player_input)
			gold = gold +1
			print("Hey! ..... You Found some Gold!")
			print("You now have", gold, "pieces of gold")
			#gold out of layout
			gold2_location = None
		
		#encouter bat (1)
		elif int(player_input) == bats_location:
			print("Ouch there are bats there!")
			bats_location = None
			player_location = choice(room_numbers)
		
		#encouter bat (2)	
		elif int(player_input) == bats2_location:
			print("Ouch there are bats there!")
			bats2_location = None
			player_location = choice(room_numbers)
				
		#fall into pit
		elif int(player_input) == (pit_location or pit2_location):
			player_location = int(player_input)
			print("Hey! ..... You Fell into a Pit!")
			print("Game over, you ended having", gold, "gold")
			break
			
		#walk into the mighty wumpus		
		else:
				player_location = int(player_input)
				if player_location == wumpus_location:
					print("Aargh!!! You got eaten by the wumpus!")
					print("Game over, the wumpus also stole your gold")
					break
						
main()
