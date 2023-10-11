# Python-Coding-Challenges

Question 1

Write a program that prints the numbers from 1 to 100. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. For numbers which are multiples of both 3 and 5 print “FizzBuzz”.
Use the following function signature: def fizzbuzz() -> None

Question 2

Write a function that takes a string that may be a float, and returns either the converted string as float or the default value provided as an argument if the string does not represent a float.
Use the following function signature:
def convert_to_float(input_str: str, default: float) -> float

Question 3

Write a function that takes a data object (see Sample Data Object below) as an argument and returns the list of all medications that have “antihtn” in their “drugGroup”. If there are no matching medications, return an empty list.
Use the following function signature:
def get_antihtn_meds(data_obj: dict) -> list

Question 4

Write a function that takes a data object (see Sample Data Object below) as an argument and returns the list of medications whose “doseForm” is any form of “tablet”. If there are no matching medications, return an empty list.
Use the following function signature:
def get_tablet_meds(data_obj: dict) -> list
  
Question 5

Write a function that takes a data object (see Sample Data Object below) as an argument and returns the “ndc9” value of the medication that was filled most recently. If there’s a tie, return any of the “ndc9” for medications filled on that day. If there are no medications, return None.
Use the following function signature:
def get_latest_med_ndc(data_obj: dict) -> Optional[str]
