# wing

https://www.winglang.io/docs/start-here/local

Super useful for avoiding AI provider lock in, i.e. avoiding the trouble
of migrating from Azure to AWS and vice versa.


IAM roles are created depending on the wing file. This lets us avoid
having to a lot of time on that.

Wing comes with its own console where we can simulate the cloud experience.



### definitions

- Preflight: the phase where we define the infrastructure
- Inflight: where we define the code that runs on the cloud
- Depending on the two above, the API of a bucket for example, will change



### install

```bash
npm install -g winglang # https://github.com/winglang
npm i @winglibs/openai # a trusted wing lib (https://github.com/winglang/winglibs/tree/main)
```


### Compiling

```bash
wing compile -t tf-aws main.w 
```

You can also use tf-azure or tf-gcp. 

