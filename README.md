# Q&A Extraction from Factual Text

Final year project in the area of NLP implementing many tools not previously worked with such as Django, NGINX, Docker, AWS EC2 and more.

Available at - https://extractor.thesvinti.com/

### Build Instructions
---
As this is running on an AWS instance, it can be accessed at anytime from
https://extractor.thesvinti.com/.

Building and running the project is  not necessary,  nonetheless, is made very simple. Once it the project is cloned from git, enter the root of the project in your terminal of choice. I have made it very simple to build and run the project through scripts to automate the process. Simply run the scripts, autobuild-extractor and afterwards, autorun-extractor as shown below in a single command:

```
sudo chmod +x autobuild-containers && sudo chmod +x autorun-containers
sudo ./autobuild-containers && sudo ./autorun-containers
```

Note, this project can only be build on a linux operating system such as Ubuntu.
After building and running, one can now access the project locally, open a browser and input **localhost:8000** in the url bar, which will bring you to the project.

### Tech Stack
---
![Stack](stack.png)


*Marking Breakdown*
```
Design - 15%
Has the project been designed to a high standard?
Does the project clearly demonstrate the use of appropriate design principles?
Is the design appropriate for the given problem?

Implementation - 30%
Has the project been implemented to a high standard?
Has the project been implemented in accordance with the design?
Does the implementation involve a considerable amount of technical difficulty?

Validation - 15%
Has the developed system been tested thoroughly?
What types of testing have been employed? Unit testing? Component testing? System Testing? Testing Tools used? Etc..
Has the developed system been thoroughly validated with respect to the potential end users?

Main documentation - 10%
Is the documentation thorough, complete and of a sufficiently high standard?

Functional Specification - 10%
Was the functional spec of a high standard and an aid to the design and implementation?

Blog - 5%
Does the blog clearly track the progress of the project and record the software engineering process?

Presentation at demo - 10%
Was the presentation thorough, professional and of a sufficiently high standard?

Video walkthrough - 5%
Is the video thorough, complete and of a sufficiently high standard? 
```

# Final Result = 89%
