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
testitems_df = pd.read_csv(testitems_path)
print(testitems_df.shape)

# TODO: initialize test with initial set of questions of moderate difficulty

# filters out questions to get moderate difficulty only
questions_df = testitems_df.query(' diff == 2 ')
print(questions_df.head)

# TODO: present first question to the test taker

# TODO: receive test taker's response and evaluate its correctness

# TODO: calculate test taker's performance metrics based on responses such as number of correct answers and response time

# TODO: select next question from question pool based on adjusted difficulty level
# TODO: if test taker answers a question correctly within a time frame, increase the difficulty level for the next question
# TODO: if test taker answers a question incorrectly, decrease difficulty level for the next question

# TODO: Present next question to test taker until test is completed

# TODO: Calculate test taker's final score based on their performance throughout the test

# TODO: Provide immediate feedback on the test taker's performance after each question or at the end of the test