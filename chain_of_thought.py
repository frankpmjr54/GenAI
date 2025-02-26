##
## CHAIN-OF-THOUGHT  PROMPTING
##

from _pipeline import create_payload, model_req


#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Please solve step by step.  Please show the requirements to build an application that will take the current attraction times of a theme park and suggest the next three attractions to ride that minimizes wait times, please break it down step by step"


#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
CHAIN_OF_THOUGHT = "You are a software developer that works for Disney. What types of data sources will be needed?  What types of data sources will be needed? A: Current wait times.  What devices will it run on? A: Mobile phones. How will the user interface look? A:A list with the next three attractions should display. "
                
                  
f"""
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.
The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.
The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.
Now Add all odd numbers until {MESSAGE} and let me know. 
Provide only the answer, no explanation!
"""

PROMPT = MESSAGE  + '\n' + CHAIN_OF_THOUGHT 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')
