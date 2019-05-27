# Q&A Extraction from Factual Text
---
Final year project in the area of NLP implementing many tools not previously worked with such as Django, NGINX, Docker, AWS EC2 and more.

Available at - https://extractor.thesvinti.com/

### Build Instructions
---
As this is running on an AWS instance, it can be accessed at anytime from
https://extractor.thesvinti.com/.

Building and running the project is  not necessary,  nonetheless, is made very simple. Once it the project is cloned from git, enter the root of the project in your terminal of choice. I have made it very simple to build and run the project through scripts to automate the process. Simply run the scripts, autobuild-extractor and afterwards, autorun-extractor as shown below in a single command:

```
sudo ./autobuild-containers && sudo ./autorun-containers
```

Note, this project can only be build on a linux operating system such as Ubuntu.
After building and running, one can now access the project locally, open a browser and input **localhost:8000** in the url bar, which will bring you to the project.

### Tech Stack
---
![Stack](stack.png)

