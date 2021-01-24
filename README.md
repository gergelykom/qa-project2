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

### My application  
My idea was to create an application that generates true-random numbers and true-random meals. Taking actions based on  
true-randomness starts an unpredictable chain reaction which can, and probably will affect the entire universe,  
the users can therefore change the fate of everything from the comfort of their own home. The app also gives potential outcomes based on the random generations,  
we cannot prove nor disprove whether these predictions will happen or not due to the uncertain timelines and the nature of chaos.
 
### Planning  
For planning and tracking I decided to use trello. The entire application was completed in one sprint but potential improvements for future sprints are also listed.  
I used the MOSCOW methodology to prioritise.  


