
ratings_input = input("Enter ratings (comma-separated) between 1 and 5: ")
input_ratings = [int(rating.strip()) for rating in ratings_input.split(",")]
positive_feedback_percentage = ((input_ratings.count(5) + input_ratings.count(4)) / len(input_ratings)) * 100
print(f"Positive feedback percentage: {positive_feedback_percentage}%")
