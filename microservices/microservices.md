### Microservices
Microservices are an architectural approach to building applications as a collection of small, modular,
independently deployable services.

------------------------------------------------
We have users interacting with out application.
The UI of our application is interacting with systems in the background, in the cloud.
The UI can be a monolith or a set of microservices.
In a monolith, making a change to one service results you having to regenerate the application,
so we cannot access just one component without affecting the others.

With microservices, ideally: If one of our microservices is not working correctly, we can take it out and fix it without
having to reset the other microservices. Separation of concerns.

-----------------------------------------------------

Examples of ML microservices:
* training
* serving
* data processing
* monitoring
* experiment tracking

Benefits:
* Independent scaling
* Fault Isolation
* Flexible deployment
* etc.

Main Challenges:
* Added Complexity
* Need for coordination between services

Pros:
* Faster iteration and more robust ML systems
