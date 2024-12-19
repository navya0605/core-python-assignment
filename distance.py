def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    return base_fare + (distance * distance_fare)
trips_input = input("Enter the distances for the trips (comma-separated, e.g. 5, 10, 3): ")
trips = [float(distance.strip()) for distance in trips_input.split(",")]

total_fare = 0

trip_number = 1
for distance in trips:
    fare = calculate_fare(distance)
    print(f"Trip {trip_number}: ${fare}")
    total_fare += fare
    trip_number += 1  
print(f"\nTotal Fare: ${total_fare}")
