##
## ZERO SHOT PROMPTING
##

from _pipeline import create_payload, model_req


MESSAGE = "Please show the requirements to build an application that will take the current attraction times of a theme park and suggest the next three attractions to ride that minimizes wait times"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT = MESSAGE 

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
