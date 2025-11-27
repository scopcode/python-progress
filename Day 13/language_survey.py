from survey import AnonymousSurvey

question = "What language did you first learn to speak?"

my_survey = AnonymousSurvey(question)
my_survey.show_question()

print("Press 'q' to quit any time")

while True:
    response = input("Language :")
    if response == "q":
        break
    my_survey.store_responses(response)

print("\nThankyou every one who have partivipated in the survey.")
my_survey.show_results()
