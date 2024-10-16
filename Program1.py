# Donovan Appelhans
# UWYO COSC 1010
# 10/14/2024
# HW 01
# Lab Section: 12
# Sources, people worked with, help given to: 
# COSC1010_lec9-Dictionaries

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
#students = [
#     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
#     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
#    {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
#    {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
#]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution
Alice_scores = {"Math": 85, "Science": 90, "English": 78}
Alice_avg_score = 0
for value in Alice_scores.values():
    Alice_avg_score += value
Alice_avg_score = Alice_avg_score / len(Alice_scores.values())
print("Alices average score was ", Alice_avg_score)

Bob_scores = {"Math": 70, "Science": 88, "English": 82}
Bob_avg_score = 0
for value in Bob_scores.values():
    Bob_avg_score += value
Bob_avg_score = Bob_avg_score / len(Bob_scores.values())
print("Bobs average score was ", Bob_avg_score)

Charlie_scores = {"Math": 92, "Science": 81, "English": 89}
Charlie_avg_score = 0
for value in Charlie_scores.values():
    Charlie_avg_score += value
Charlie_avg_score = Charlie_avg_score / len(Charlie_scores.values())
print("Charlies average score was ", Charlie_avg_score)

David_scores = {"Math": 60, "Science": 75, "English": 80}
David_avg_score = 0
for value in David_scores.values():
    David_avg_score += value
David_avg_score = David_avg_score / len(David_scores.values())
print("Alices average score was ", David_avg_score)

Test_avgs = {

}
Test_avgs["Alice"] = Alice_avg_score
Test_avgs["Bob"] = Bob_avg_score
Test_avgs["Charlie"] = Charlie_avg_score
Test_avgs["David"] = David_avg_score
print(Test_avgs)

for key, value in Test_avgs.items():
    if value >= 80:
        print(f"{[key]}", "average is 80 or over.")