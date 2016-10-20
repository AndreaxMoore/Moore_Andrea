choice = input("Would you like to visit..."+
                "\n A: China"+
                "\n B: England: ")

if choice == "A":
    city = input("Would you like to visit..."+
                        "\n A.Shanghai" +
                        "\n B.Beijing: ")
    if city == "A":
    	place =input("Would you like to visit..."+
    	             "\n A.Shanghai World Financial Center"+
    	             "\n B.People's Square")
    	if place == "A":
    		print("Hope you will have a great time at Shanghai World Financial Center!")
    	else:
    		print("Hope you will have a great time at People's Square!")
    else:
    	place = input("Would you like to visit..."+
    	              "\n A.Forbidden City"+
    	              "\n B.Great Wall")
    	if place == "A":
    		print("Hope you will have a great time at Forbidden City!")
    	else:
    		print("Hope you will have a great time at Great Wall!")
else:
	city = input("Would you like to visit..."+
	             "\n A.London"+
	             "\n B.Manchester")
	if city == "A":
		place = input("Would you like to visit..."+
		              "\n A.Big Ben"+
		              "\n B.London Eye")
		if place == "A":
			print("Hope you will have a great time at Big Ben!")
		else:
			print("Hope you will have a great time at London Eye!")
	else:
		place = input("Would you like to visit..."+
		              "\n A.John Rylands Library"+
		              "\n B.Manchester Town Hall")
		if place == "A":
			print("Hope you will have a great time at John Rylands Library!")
		else:
			print("Hope you will have a great time at Manchester Town Hall!")

