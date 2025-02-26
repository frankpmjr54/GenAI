##
## refined prompt level2
##

from _pipeline import create_payload, model_req


MESSAGE = "Please show the requirements to build an application that will take the current attraction times of a theme park and suggest the next three attractions to ride that minimizes wait times"
#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPTPrime = MESSAGE
PROMPT = MESSAGE

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

def tree_of_thought(question):
    """ Generate multiple thought paths for solving a problem. """
    responses = []
    promptTree = [
        f"Step 1: {question}\nStep 2: Approach using logic and step-by-step reasoning.",
        f"Step 1: {question}\nStep 2: Approach using real-world examples and analogies.",
        f"Step 1: {question}\nStep 2: Approach by comparing different solutions and choosing the best."]
    PROMPT = promptTree[0]
    response1 =  model_req(payload=payload)
    PROMPT = promptTree[1]
    response2 =  model_req(payload=payload)
    PROMPT = promptTree[2]
    response3 = model_req(payload=payload)
    responses = [response1, response2]
    return responses

      
    

def evaluate_responses(responses):
        
    scored_responses = [(resp, len(resp)) for resp in responses]  # Use response length as a simple score
    best_response = max(scored_responses, key=lambda x: x[1])[0]  # Choose the longest (most detailed) response
    
    return best_response

print (evaluate_responses(tree_of_thought(PROMPTPrime)))
#if time: print(f'Time taken: {time}s')
