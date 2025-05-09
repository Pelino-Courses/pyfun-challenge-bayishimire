import datetime
def date_difference(date1, date2):
    """
    Calculate the difference in days between two dates.
    Args:
        date1 (str): The first date in 'YYYY-MM-DD' format.
        date2 (str): The second date in 'YYYY-MM-DD' format.
    Returns:
        int: The difference in days between the two dates.
    """
    # Convert string dates to datetime objects
    
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')

    # Calculate the difference in days
    diference_day= date2 - date1

    return diference_day.days


# Example usage  
if __name__ == "__main__":
 # Get user input for two dates
  print("enter date respect format date format YYYY-MM-DD") 
  date1=input("Enter the first date (YYYY-MM-DD): ")

  date2=input("Enter the second date (YYYY-MM-DD): ")

try:
    date_difference(date1, date2)
    print(f"The differenceof {date1} and {date2}in days is: {date_difference(date1, date2)}") 
except ValueError:
    print("invalid format entering . Please use 'YYYY-MM-DD'. ")