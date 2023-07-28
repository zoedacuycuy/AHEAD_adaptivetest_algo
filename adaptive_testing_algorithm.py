# TODO: interact with database
# Database not given
# Assume database is comprised of 2 tables, student and testitems
# Tables not given, use Pandas dataframe and randomly generated values for both tables in the meantime
import pandas as pd

student_path = r'E:\AHEAD Work Files\Adaptive Tech\Adaptive Testing Algorithm\AHEAD_adaptivetest_algo\table_students.csv'
testitems_path = r'E:\AHEAD Work Files\Adaptive Tech\Adaptive Testing Algorithm\AHEAD_adaptivetest_algo\table_testitems.csv'

student_df = pd.read_csv(student_path)
print(student_df.shape)
print(student_df.head)
print(student_df.dtypes)

# student taking the test is assumed to be the first row
# shuffling the table in order to get random sample of student
# should be taken from account in UI
student_df = student_df.sample(frac=1)
current_student = student_df.iloc[0]
current_student['proficiency'] = current_student['proficiency'] / 10 * 3
print("current student prof: " + str(current_student['proficiency']))

testitems_df = pd.read_csv(testitems_path)

# TODO: initialize test with initial set of questions of moderate difficulty

# filters out questions to get moderate difficulty only
questions_df = testitems_df.query(' diff == 2 ')

# TODO: present first question to the test taker
# shuffles the datagrame
questions_df = questions_df.sample(frac=1)

# takes the first row of the dataframe as the first question
firstq = questions_df.iloc[0]
print(firstq)

# TODO: receive test taker's response and evaluate its correctness
# list of responses that the student can answer
# IDK is arbitrary for the identification questions
# temporarily a dictionary; will take in HTML form responses in the future
responses_list = ['A', 'B', 'C', 'D', 'TRUE', 'FALSE', 'IDK']

# randomizes student answer from list in the dictionary
import random
student_response = random.choice(responses_list)

# checks if the answer is correct
correct = False
if student_response == firstq['answer']:
    correct = True

# TODO: calculate test taker's performance metrics based on responses such as number of correct answers and response time
import math
probability = firstq['guess'] + ( (1 - firstq['guess']) / (1+math.exp((-1.702 * firstq['discrim']) * (current_student['proficiency'] - firstq['diff']) )))

print("probability: " + str(probability))

# TODO: select next question from question pool based on adjusted difficulty level
# TODO: if test taker answers a question correctly within a time frame, increase the difficulty level for the next question
# TODO: if test taker answers a question incorrectly, decrease difficulty level for the next question

# TODO: Present next question to test taker until test is completed

# TODO: Calculate test taker's final score based on their performance throughout the test

# TODO: Provide immediate feedback on the test taker's performance after each question or at the end of the test