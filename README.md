# Trivia-question-loader
#### By alejandro de los Santos.     alejandrodlsp.com



A python script that loads trivia questions from  https://opentdb.com/  API  and deserializes them into objects for easy use.
It makes use of session tokens to make sure questions are not repeated.


#### Example usage of script:

```python
# import question loader script
import questionLoader                                                      
# create a new question set
question_set = questionLoader.question_set("10","9","medium","multiple")
# get list of questions from question set
questions = question_set.get()                                             

# loop trough questions in the questions list
for i in range(0,len(questions)):                                           
	print(questions[i].question)                                              
``` 
