# Returns the allocated seats array based on the room details
# allocated_seats = []





def get_allocated_seats(room_details):
    print('Room Details , ', room_details)
    allocated_seats = []
    for room in room_details:
        room_str = str(room[0]) + str(',') + str(room[1])
        for row in range(1, int(room[2])+1):
            for column in range(1, int(room[3])+1):
                allocated_seats.append(
                str(room_str + ",:" + str(row) + "," + str(column)))

            #print(room_str + ",:" + str(row) + "," + str(column))
    print("Allocated Seats , ", allocated_seats)
    return allocated_seats

# Helper fucntion to extract details of a gene and maps to a room location.


def convert_location_row_col(seat_location):

    seat_row, seat_col = (seat_location.split(sep=":")[1]).split(sep=",")
    seat_col = int(seat_col)
    seat_row = int(seat_row)

    return seat_row, seat_col