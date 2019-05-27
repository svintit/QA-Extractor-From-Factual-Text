# Q&A Project Blog


#### Post #1 - 03/09/2018
Searching for inspiration for a project idea. I have interest in the NLP area.

The idea of a question answering system such as a chat-bot is intriguing but would not be challenging enough as a final year project.

*Search continues...*

---

#### Post #2 - 15/09/2018

I have thought of an idea which I believe can be challenging and feasible in the time-frame of the project:

I would like to implement a question extraction system which takes user factual text input and outputs questions based on the given text. 

Educational use can be a good reason for why this would be implemented.

---

#### Post #3 - 20/09/2018

Beginning research of the topic of NLP I see NLTK as the most commonly used toolkit for this area. 

Trying to get an idea of the technical stack that is needed to best implement the idea. 

---

#### Post #4 - 25/09/2018

I have chosen to work with some tools that I would not have previously used. This will help to improve my experience greatly.

I will be using Python 3 and Django running on a Docker image communicating with other components using Django REST framework which all will be deployed on an AWS EC2 instance. This will cover the infrastructure of the project.

For the NLP componant, I will use NLTK for all semantic analysis needed. Currently it would seem that Part of Speech tagging (POS) and noun chunks can be a good place to start with NLTK for what I need. 

---

#### Post #5 - 1/10/2018

After a lot more research and confirmed the feasibility and difficulty of this project, I began to create my proposal form for the board to accept or reject the idea. I have little worry of rejection.

---

#### Post #6 - 11/10/2018
Today I completed the proposal form. I had come up with more ideas to create a full system for users to use, including the possibility of creating a session based interface that would allow users to join and answer questions. 

I am looking forward to the approval meeting to get more insight from more knowledgeable people. They will be able to provide more detail on what I need to concetrate on and what features may not be necessary.

---

#### Post #7 - 18/10/2018
Project has been approved and there seemed to have been a lot of interest in it, I was told it is a good idea. They outlined that some features may not be necessary but depending on timeframe I may or may not implement them.

---

#### Post #8 - 30/10/2018
I am continuing to make progress slowly, research continues to take up the bulk of my time. 

So far I have only worked on the main component, the text analysis and hopefully soon, question extraction.

The UI for this will need to be very clean, easy to use and efficient, this will take a long time to implement from scratch but help from CSS classes using Bootstrap will help speed up the process slightly.

I will be beginning work on  the functional specification soon.

---

#### Post #9 - 18/11/2018
I have completed the functional specification in time for the deadline. This provided me with a better insight of my goals and what I need to accomplish in the project timeframe.

From here I will solely concentrate on the extraction component, as this is the main component, it needs to work, whether there is any UI or not.

---

#### Post #10 - 08/02/2019
Up until this point, code written has been a lot of tests and checking functionality, "spaghetti code". I took the time to refactor all the code written to implement correct OO style practices with classes, magic methods and efficient use of functions.

As I believe this is very important in the long run and will help with troubleshooting deep issues, I will also be following PEP8 style very closely to ensure good readability and creating good habits.

---

#### Post #11 - 12/02/2019
Currently still working on the extraction library. I am currently implementing a second function to deeper analyze the text for more specific questions, I believe this could result in less fluency and I believe that both functions would need to create questions and the output of both selected and merged for outputting to the user.

---

#### Post #12 - 13/02/2019
I have decided to take a break from the extraction component to keep motiviation and begin to work on the project framework.

I have decided to use Django as the framework as I have previous experience with this and is very powerful. Along with Django, I am attempting to use Docker for my first time to containerize each component of the project. I believe knowledge of Docker will help me in the future and alleviate any possible deployment issues or running on other machines.

---

#### Post #13 - 17/02/2019
I have restructured the entire src directory to provide a clearer path as Django can make things messy sometimes. 

I have successfully started Docker with Django and created a nice entrypoint script that runs everytime the container runs to make db migrations, migrate them, run tests, collect static files and start the Django server.

I have also begun to work with the Django views.py file for my page rendering, I have a lot to learn here.

--- 

#### Post #14 - 19/02/2019
Postgres is giving me a bit of a headache, integrating seems fine but getting lots of errors when trying to save anything to it.

---

#### Post #15 - 21/02/2019
I believe the Postgres issue is fixed, but time will tell when I begin saving some actual user information.

I have started to work on the UI; HTML, CSS and JS/Jquery will be good friends of mine very soon. I need to create a text input box as the user will need 2 forms of input, text and file.

I am in the process of creating a quick mockup of the UI including the registration page, which currently, I am unsure if I will have time to implement users.

---

#### Post #16 - 28/02/2019
I have worked a lot on the UI and backend integration, I am currently at a point where the first generation of questions I have are outputting to the UI, not clean but it works for now.

I need to work on the File Input now to work in the same way as the text input.

---

#### Post #17 - 05/03/2019
Taking a slight break from the UI, I want to work on the AWS instance side, I have no knowledge in this so this should be fun.

I will be working on creating the instance and setting up and autodeployment system that will use SSH keys to automatically pull code from the GIT master branch every so often using a cronjob. A similar implementation will be done through bash scripts and a cronjob to autostart the containers if they are not running.

---

#### Post #18 - 15/03/2019
I have now implement a download functionality for the outputted questions and answers to the user can take the questions and use them externally in whatever way they see fit.

I have also made some small improvements in the question formations. 

I need to get back to work on the file input.

---

#### Post #19 - 01/04/2019
A lot of work has been done at this point:

 - File input has been implemented
 - Autoscroll on UI for question output implemented
 - Python code restructured again to ensure following of PEP8
 - A second more advanced question extraction function has been implemented and works surprisingly well. This uses POS tag sequencing to create fluent questions.
 
---

#### Post #20 - 28/04/2019
Blog updates have slighly slowed down, current updates:

- Unit testing has been done with 93% coverage achieved 
- Bug fixes
- Beginning functional tests using decoupled and containerized selenium and headless chrome (industry standard)
- More automation for building, entrypoints and autostarts have been made
- More UI work, registering, signing in, integration with backend through API and models
- Better question models created
- Question selection for downloading/saving
- Created session modal and UI
- Anonymous user input through sessions and models
- Automatic session grading using cosine similarity and word vectorization

At this point, the project is mainly complete. I need to work on documentation and UI testing and user testing once the ethics form is approved.

---

#### Post #21 - 04/05/2019
I have 90% completed the techinical specification, user manual. I need to continue work on UI testing and user testing.

Exams are coming up soon and also taking up a lot of time to study for.



#### Post #22 - 19/05/2019
Project, testing and documentation is now all completed. Very happy with how much testing I was able to complete and the industry standard approaches taken.

From now I will work on the presentation for the demonstration, I have learned a lot from this project and I am looking forward to tackling more in the future.
