room_capacity = 0
actual_capacity = 0
attending = 0
room_size = 0
meeting_total = 0


def capacity():
    room_capacity = int(input("How many people will the room legally hold?:"))
 
    return room_capacity
    
   



def attendees():
    actual_capacity = int(input("How many people will be attending the meeting?:"))
    
    return actual_capacity




def register(room_size,attending):
    
    meeting_total = room_size - attending
    print("The difference is {0} people".format(meeting_total))
   
    return meeting_total

    


def check_morerooms():
   
  
        print("Error")


#BASE PROGRAM------------------------------------------------------------------------
attending = attendees()
room_size = capacity()
difference = register(room_size,attending)





    
    