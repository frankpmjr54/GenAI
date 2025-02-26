##
## refined prompt
##

from _pipeline import create_payload, model_req


MESSAGE = "Please show the requirements to build an application that will take the current attraction times of a theme park and suggest the next three attractions to ride that minimizes wait times"
TEMPLATE_BEFORE = "Please refine the following prompt to be more clear:"
#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=1000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
PROMPT = response
time1 = time
time, response = model_req(payload=payload)
time2 = time
time = time1 + time2

print(response)
if time: print(f'Time taken: {time}s')
