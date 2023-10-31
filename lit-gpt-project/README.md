# Small project exploring the use of lit-gpt and docker + flask

I wanted to practice some MLOps, so I decided on the lit-gpt library and chose a model that I could run with limited RAM. 

The result: A docker application that clones lit-gpt and downloads the model: phi-1_5, which takes ~3 GB of RAM. 
Using flask, you can write to the model through local host. 
