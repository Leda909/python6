# Import CSV files
import csv

# Function to display a Welcome Message
def display_menu():
  print("Welcome to the User Preference Manager!")
  print("Please choose an option: ")
  print("1. Enter or update preferences.")
  print("2. View current preferences.")
  print("3. Quit.")

# Function to handle the task of entering or updating user preferences.
def enter_update_preferences(file_path):
  # Use try - except methode to handel errors
  try:
    # with statement open the CSV file. file_path is a parameter, which is the path to the CSV file where preferences will be stored by 'w' to overwrite prior references. 
    with open(file_path, mode='w', newline='') as file:
      # The csv.writer() is a function, used to create a writer object for writing data to the CSV file.
      writer = csv.writer(file)
      # Ask the user to input different preferences
      language = input("Please enter your preferred language: ")
      theme_color = input("Please enter your theme color: ")
      # These values added by using writer.writerow() function with labels from input variables
      writer.writerow(["Language", language])
      writer.writerow(["Theme Color", theme_color])
      print("Preferences saved successfully.")
  except IOError:
    print("An error occurred when writing to the file.")
    
# Function to display the last stored preferences. "file_path is a parameter, the path to the CSV file."
def view_current_preferences(file_path):
  try:
    # with statement open the CSV file through file_path in 'r' as reading mode
    with open(file_path, mode='r') as file:
      # The csv.reader() function , used to create a reader object for reading date from the CSV file.
      reader = csv.reader(file)
      # list(reader) reads all the rows from the CSV file 'prefences' list
      preferences = list(reader)
      # Handel case if there is no data in list.
      if len(preferences) == 0:
        print("No preferences found.")
        return
      else:
        print("Current Preferences:")
        # Print preference by preferences, in a human readable format / for loop
        for preference in preferences:
          # f-string feature to print label and value row by row in a list. value[0] is the label.
          print(f"{preference[0]}: {preference[1]}")
  except FileNotFoundError:
    print("No preferences found.")
  except IOError:
    print("An error occurred while reading the file.")

# Define the main function of the program
def main():
  # Declare the CSV file in path variable
  path = "user_preferences.csv"
  
  # while loop to continously run the code until the user quite.
  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      enter_update_preferences(path)
    elif choice == '2':
      view_current_preferences(path)
    elif choice == '3':
      print("Thank you for using the User Preference Manager. Goodbye!")
      break
    else:
      print("Invalid option. Try again.")

# Conditional block to ensure that the main() function is executed only if the script is run directly.
if __name__ == "__main__":
  main()
