# GenAI
Prompting Techniques for Design Requirements of Theme Park Optimization Application

This project explores several LLM Prompting Techniques to determine the requirements of a hypothetical application to minimize wait times at a theme park.
* Authors: Frank Meoni (https://github.com/frankpmjr54/GenAI.git)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)
Research Question
What Prompt Techniques will yield the best requirements for a theoretical application to minimize wait times at a theme park and avoid exorbitant skip-the-line fees?

________________________________________
 Arguments
The more detailed the prompt, the more detailed and accurate the requirements will be.
What is already known about this topic
Software requirements are typically not complete and inaccurate.  Although “agile” techniques are an attempt to handle requirements as a project evolves, it is still an imprecise endeavor that leads to wasted time and energy.  Using LLMs and Generative AI can help to create requirements that are more precise and will encompass factors that a typical BA may leave out.  An LLM has the knowledge of many BAs and software developers.  
The challenge of using an LLM to write requirements is in how it is asked or prompted.  Prompt engineering techniques have evolved from simple questions like zero-shot prompting, a question with no context or instruction, through methods like Chain-of-Thought (CoT), Few-Shot, and Role-Based prompts.  
Even with advanced prompting techniques, LLMs are not infallible; they are subject to issues like hallucinations, responses that seem reasonable but are in fact nonsense.  Its like when your uncle starts explaining how software works, even though he is an accountant.  He sounds reasonable but is trying to explain why coding in red font takes up less memory.  
 What this research is exploring
This experiment will use several LLM prompts to define the requirements of a fictious application that will minimize line wait times for a theme park.  These prompts will start from the simplest zero-shot, and work through several levels until finally using two Level-2 prompt techniques.  The responses will be observed and evaluated in terms of how well the requirements are written.  In addition, to exploring different prompts, the parameters of the prompt will be varied to explore how that changes the responses. The prompt techniques used in this experiment start with what are called Level 0, they include zero shot, a question with no context or additional information; few shots, question with some context, in this experiment there are two versions of this, few shots/role based and few shots V2.  Few shots/role based adds a prefix to the prompt that specified “you are a software developer” and Few shots V2 uses the that prefix as well as a suffix “provide a detailed response showing functional requirements as well as assumptions regarding input by the users and UI requirements.”  Moving to Level 1 prompts, Chain of Thought and what is called Refined Prompt were tested and this is a prompt that poses a question but is also prefaced by logical steps or information that helps bring context to how the response should be crafted and to align the logic with the user as opposed to an outside source (where ever the LLM gets it from). Refined Prompt is an iterative prompt that asks the LLM to refine the prompt to produce a better result.  Finally there are two Level 2 prompts, Refine Prompt Level 2 and Tree of Thought.  Refine Prompt Level 2 is an extension of Refine Prompt, using the output of a refined prompt to be further refined.  Tree of Thought is the most complex of the prompts and gives the best overall detailed requirements, including functionality I did not take into account.  This technique uses the base prompt of “Please design the requirements for an application to reduce wait times at a theme park…” and adding three different “approaches”, step by step reasoning, using real world examples, compare current solutions and choosing the best.  These were then “evaluated”, by looking for the longest response (assuming longer is more detailed) , and only presenting that response.  
Implications for practice
As stated earlier, having better requirements at the start of a project can reduce and possibly eliminate wasted time and energy on the part of the programmer.  In practice even poorly written requirements can get sign-off because most stakeholders skim them without a clear understanding of how the requirements will become a production ready application.
Research Method
Phase 1: Prompt Technique Evaluation
•	Test the following Level-0 techniques
o	Zero-shot
o	Few-shot/Role Based
o	Few Shot V2
•	Test the following Level 1 techniques
o	Chain of Thought
o	Refined prompt
•	Test the following Level 2 Techniques (advanced)
o	Refined Prompt Level 2
o	Tree of Thought
•	Each response will be evaluated for completeness and compared to the other responses.  This part will be subjective to the observer, but the observer is a trained software engineer.
Phase 2: Parameter Tuning & Experimentation
•	Adjust temperature (0.5 ,1.0) to measure impact on creativity vs. precision.
•	Test different num_predict values to find the optimal response length.
Phase 3: Comparative Analysis
The prompts are for the same goal, write requirements for the creation of an application to reduce wait times in a theme park.  The analysis will compare each response to the rest of the responses and rank them based on completeness are all parts of the application considered data sources, devices, platforms, etc.  Rank will be reduced if hallucinations or issues like Semantic Drift are found.
________________________________________
Results
Key Findings:
•	num_predict = 100 is too low, most of the responses were cut off.
•	Higher temperature of the prompt, the more likely it will go off topic (semantic drift) or just speak nonsense but also includes more creative ideas for the application.
o	Few shots and Few Shots V2 (temp = 1.0) both responded with Code that didn’t match the goal. 
o	Refined Prompt (temp = 1.0) included an ML component that was not suggested by previous responses and also included an outline of the requirements in a much easier to read format then previous responses.
•	Tree of Thought (temp = 0.5) was by far the most comprehensive response taking into account social media, gamification, chat bots, all of which seems to be hyper focused on the goal.  However, it did not necessarily contain the most detail, it was the best outline for what to build but didn’t include details on how it should be built. 
Limitations:
•	There is a wide range of responses that go from highly detailed descriptions of what this application should be to a discussion about a museum tour.   The prompt technique makes a significant difference in how the LLM responds. In addition varying the parameters also impacts the response.
•	LLMs make a good tool to help define requirements but it takes someone with knowledge of prompting techniques as well as software development experience to ensure the response is viable.
________________________________________
Further research 
Future work in this study can be focused on many areas and it’s important to test each part on its own.  For example, test zero shot by using the same prompt and vary each parameter (like temperature) on its own then jointly with another parameter to explore the variation in responses. In addition, there are many other knowledge domains that can be studied such as medicine and tax law.  

