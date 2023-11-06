### DVC is the "Git for data"


In this little project, I try to use its data tracking capabilities. 

See here for documentation and nice guides: https://dvc.org/doc


### Here is how it works.

First you need to get some data. 

* Do:
```
dvc add [data]
```
to start tracking your dataset.



DVC will store information about the data in a .dvc file. 
E.g. if my data is a folder called CamVid, there will be a file called CamVid.dvc.

The .dvc file is meant to be tracked using Git.


Next:
```
git add [.dvc file] [.gitignore]
git commit -m "original data added"
```
which our original data file has been added to (the dvc file))

Note: dvc add has moved the data to the project's cache under .dvc/cache at the root of your git repo. 


Next:
```
mkdir /tmp/dvcstore #for local file storage (you could also use a remote storage)
dvc remote add -d myremote /tmp/dvcstore
dvc push # "upload data" (this is local) This copies the cached data to the remote storage. You ca find it under "/tmp/dvcstore" on local
```


To get data from the "remote", do:
```
dvc pull # (to test this on the local, you need to remove the cache under .dvc/cache and the data itself in your repo (not the data stored in your local file storage). 
```


### Changes: 

Suppose we augmented the data (I used a data augmentation script using pytorch). Then we should do:
```
dvc add [data] # to again track the latest changes.
```

We then run:
```
dvc push 
git commit [data].dvc -m "data set change" #This uploads the changes and tracks it. 
```

### Switching between version.

We can do:
```
git checkout HEAD~1" [data.dvc] 
dvc checkout 
```
to get the previous version of our data.
We can then commit that using:
```
git commit [data.dvc] -m "Revert data changes"
```


Finally, dvc can also track other stuff such as pipeline versions, metrics, parameters and plots.


