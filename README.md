## Table of Contents
- [Brief](#Brief)  
  - [Requirements](#Requirements)  
    - [Scope](#Scope)  
    - [Platform&nbsp;Requirements](#Platform&nbsp;Requirements)
    
- [My&nbsp;application](#My&nbsp;Application)  
  - [Documentation](#Documentation)
    - [Risk&nbsp;Assessment](#Risk&nbsp;Assessment)
    - [Database&nbsp;(ED)](#Database&nbsp;(ED))
    - [Original&nbsp;CI&nbsp;Pipeline](#Original&nbsp;CI&nbsp;Pipeline)
    - [Final&nbsp;CI&nbsp;Pipeline](#Final&nbsp;CI&nbsp;Pipeline)
    - [Application&nbsp;layout](#Application&nbsp;layout)
   
 - [Testing](#Testing)
 - [Design](#Design)
 - [Future&nbsp;Improvements](#Future&nbsp;Improvements)
 
 ## Brief
 The second project focused on the implementation of all the tools we learned in the first half of our  
 DevOps course.
 
 ### Requirements
 The MVP was a 4 service application which was required to generate random objects. Service 1  
 was the point of interaction between the user and the backend. Service 2-3 generated random  
 objects, while service 4 also created an object based on the results of service 2 and 3.  
 The MVP also required full CI/CD pipeline, implemented integrated into a version control system  
 using the feature-branch model.  
 
 ### Scope (as mentioned on DevOps Core Practical Project Specification)
 - An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.  
 - This could also provide a record of any issues or risks that you faced creating your project.  
 - An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently  
 be built through a CI server and deployed to a cloud-based virtual machine.  
 - If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application  
 - The project must follow the Service-oriented architecture that has been asked for.  
 - The project must be deployed using containerisation and an orchestration tool.  
 - As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.  
 - The project must make use of a reverse proxy to make your application accessible to the user.  
 
### Platform Requirements
- Trello board  
- Reverse Proxy and load-balancing: NGINX  
- Orchestration Tool: Docker Swarm  
- Containerisation tool: Docker  
- Cloud server: GCP virtual machines  
- CI server: Jenkins  
- Version Control: Git  
- Configuration Management: Ansible  

## My application  
My idea was to create an application that generates true-random numbers and true-random meals. Taking actions based on  
true-randomness starts an unpredictable chain reaction which can, and probably will affect the entire universe,  
the users can therefore change the fate of everything from the comfort of their own home. The app also gives potential outcomes based on the random generations,  
we cannot prove nor disprove whether these predictions will happen or not due to the uncertain timelines and the nature of chaos.  

Service-2 generates a random number.
Service-3 generates a random meal.
Service-4 returns a potential future event that could be end up happening, based on the random number and meal that was generated.
 
### Planning  
For planning and tracking I decided to use trello. The entire application was completed in one sprint but potential improvements for future sprints are also listed.  
I used the MOSCOW methodology to prioritise.  

This was my original planning board towards the beginning of the project:
![Trello1](https://github.com/gergelykom/qa-project2/blob/main/images/trello-initial.JPG)  

My board at the end of the project:  
![Trello2](https://github.com/gergelykom/qa-project2/blob/main/images/trello-final.JPG)  

## Documentation  

### Risk-assessment  
Unlike my application from my previous project, the current app has far fewer risks associated with it. The first main reason is, that there is never any need for the users to enter personal data, the app is also much simpler. The second reason is the fact that it doesn't deal with the scientific community as heavily, which caused quite a few risks.  
The risk assessment tables highlight potential problems in the pipeline and during deployment, the updated version also contains risks that I personally faced during the project.  

The original risk assessment table:  
![Risk1](https://github.com/gergelykom/qa-project2/blob/main/images/risk-initial.JPG)  

The final version:  
![Risk2](https://github.com/gergelykom/qa-project2/blob/main/images/risk-final.JPG)  

###Database (ED)  
The database used for this project is very simple, both versions use the same database and there are no relationships.  

ED:  
![ED](https://github.com/gergelykom/qa-project2/blob/main/images/ED%20chart.JPG)

### Before The CI pipeline set up  
The following image will show how the CI pipeline looked at the beginning of the project. There was very little automation, everything had to be done manually. This was both time consuming and created a lot of unecessary errors (typos due to human error).  

![CI1](https://github.com/gergelykom/qa-project2/blob/main/images/Initial%20CI%20pipeline.JPG)  

### After the CI/CD pipeline set-up  
Once the CI pipeline was set up Jenkins could automatically set up the swarm, test the application and deploy it from a change or push in the applications repository. The CI/CD pipeline reduced the time spent on repeating tedious code, made maintainance much easier, allowed changes and test results to be seen in a few minutes. This has even more potential in a team setting. The image below shows the power of automation and DevOps:  

![CI2](https://github.com/gergelykom/qa-project2/blob/main/images/Final%20CI%20pipeline.JPG)  

### Layout  
The image below shows the layout of the swarm and the load balancer:  

![Layout](https://github.com/gergelykom/qa-project2/blob/main/images/abstract.JPG)

### Application services layout  
The image below shows the layout of the application services:  

![App-Layout](https://github.com/gergelykom/qa-project2/blob/main/images/app-final.JPG)  

## Testing  
The application was tested through unit-testing and mock-testing to ensure all functions and requests work as intended. Once the CI pipeline was set up the testing was done automatically through Jenkins. Reports of the test are displayed after every build.  

![Serv-1 Test](https://github.com/gergelykom/qa-project2/blob/main/images/test-1.JPG)  
![Serv-2 Test](https://github.com/gergelykom/qa-project2/blob/main/images/test-2.JPG)  
![Serv-3 Test](https://github.com/gergelykom/qa-project2/blob/main/images/test-3.JPG)  
![Serv-4 Test](https://github.com/gergelykom/qa-project2/blob/main/images/test-4.JPG)  

## Showing a successful build in Jenkins  

![Jenkins build](https://github.com/gergelykom/qa-project2/blob/main/images/jenkins.JPG)  

## Front-end Design  
The front-end design of the application is quite simplistic.  

This is the basic version of the application:  
![Basic](https://github.com/gergelykom/qa-project2/blob/main/images/version-1app.JPG)  

The second version:  
![GF edition](https://github.com/gergelykom/qa-project2/blob/main/images/version-2app.JPG)  

## Potential Improvements  

The MVP could be improved further:  
- Changing the pseudo-random generation of service 2 and 3 to true random, this could be done through a module which recieves numbers from Random.org  
- Adding multiple outcomes to service-4, since the app would generate true "Quantum meals", there would be different outcomes based on when the meal is eaten, whether you choose to eat the meal or not etc.  
- Improving the UI, adding CSS, (this app should not have full CRUD, update and delete would result in a completely different chain of events)  
- Expanding the swarm for more stability and performance.  

## Potential issues  
There have been some issues with github not merging the changes made to the branches.  

## Acknowledgements  
Nathan Forester and Harry Volker for all their help and patience!  

Gergely Komuves
