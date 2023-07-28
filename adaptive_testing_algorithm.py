# TODO: interact with database
# Database not given
# Assume database is comprised of 2 tables, student and testitems
# Tables not given, use Pandas dataframe and randomly generated values for both tables in the meantime
import pandas as pd
import random
import math

student_path = r'E:\AHEAD Work Files\Adaptive Tech\Adaptive Testing Algorithm\AHEAD_adaptivetest_algo\table_students.csv'
testitems_path = r'E:\AHEAD Work Files\Adaptive Tech\Adaptive Testing Algorithm\AHEAD_adaptivetest_algo\table_testitems.csv'

student_df = pd.read_csv(student_path)

# student taking the test is assumed to be the first row
# shuffling the table in order to get random sample of student
# should be taken from account in UI
student_df = student_df.sample(frac=1)
current_student = student_df.iloc[0]
current_student_proficiency = current_student.loc['proficiency']
current_student_proficiency = current_student_proficiency / 10 * 3
print("current student prof: " + str(current_student_proficiency))

# test items table is loaded into the dataframe
testitems_df = pd.read_csv(testitems_path)

# initialize test with initial set of questions of moderate difficulty
# 1 = easy, 2 = moderate, 3 = hard
# initialized at moderate
difficulty_level = 2


true_score = 0 # score of student after the test
expected_score = 0 # depends on probability as calculated by 3PL

starting_proficiency = current_student_proficiency # for stats tracking

num_questions = 10 # number of test items; modify as needed
# Present next question to test taker until test is completed
for i in range(num_questions):
    # queries pandas data frame to get questions of that difficulty
    questions_df = testitems_df.query(' diff == {} '.format(difficulty_level))

    # present question to the test taker
    # shuffles the dataframe
    questions_df = questions_df.sample(frac=1)
    # takes the first row of the dataframe as the first question
    current_question = questions_df.iloc[0]
    print(current_question)

    # receive test taker's response and evaluate its correctness
    # list of responses that the student can answer
    # IDK is arbitrary for the identification questions
    # temporarily a dictionary; will take in HTML form responses in the future
    responses_list = ['A', 'B', 'C', 'D', 'TRUE', 'FALSE', 'IDK']

    # randomizes student answer from list in the dictionary
    # student_response = random.choice(responses_list)

    # uses terminal input for testing
    student_response = input()

    # checks if the answer is correct
    correct = -1
    if student_response == current_question['answer']:
        correct = 1
        true_score += 1
    print("correct: " + str(correct))

    # calculate test taker's performance metrics based on responses such as number of correct answers and response time
    # uses the 3PL formula to calculate the probability of the student to answer correctly
    probability = current_question['guess'] + ( (1 - current_question['guess']) / (1+math.exp((-1.702 * (current_question['discrim'] / 10) ) * (current_student['proficiency'] - current_question['diff']) )))
    print("probability: " + str(probability))

    # if probability is higher than 80%, student should be able to answer
    if probability >= 0.8:
        expected_score += 1

    # if test taker answers a question correctly within a time frame, increase the difficulty level for the next question
    # if test taker answers a question incorrectly, decrease difficulty level for the next question
    # increase in student's proficiency if the answer is correct and decreases if it is wrong
    # higher gain/loss if probability is high since this means user does not belong to that difficulty level; true positive
    # lower gain/loss if probability is low since user performed as expected; false negative
    current_student_proficiency = current_student_proficiency + (( (1 * correct) / 10 * 3) *  probability)
    print("proficiency: " + str(current_student_proficiency))

    # select next question from question pool based on adjusted difficulty level
    if current_student_proficiency <= 1:
        difficulty_level = 1
    elif current_student_proficiency <= 2:
        difficulty_level = 2
    else:
        difficulty_level = 3

    # removes test question from dataframe
    # avoids repetition of test questions
    testitems_df.drop(current_question['item_id'], inplace=True)

# Calculate test taker's final score based on their performance throughout the test
print("final score: " + str(true_score))

# Provide immediate feedback on the test taker's performance after each question or at the end of the test
# feedback on score
if expected_score > true_score:
    print("Underperformed")
elif expected_score == true_score:
    print("Performed")
else:
    print("Overperformed")

# clamps proficiency to 0-3
current_student_proficiency = max(0, current_student_proficiency)
current_student_proficiency = min(3, current_student_proficiency)

# feedback on proficiency
if current_student_proficiency > starting_proficiency:
    print("Improved")
elif current_student_proficiency == starting_proficiency:
    print("Maintained")
elif current_student_proficiency < starting_proficiency:
    print("Worsened")