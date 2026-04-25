
def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {str(estimated_time)} hours")

trip_planner_welcome("John Doe")

estimate = estimated_time_rounded(2.5)
print(estimate)

destination_setup("Dublin", "London", estimate, "Airplane")

