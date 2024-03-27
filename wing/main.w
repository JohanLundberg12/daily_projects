bring cloud;
bring openai;

let b = new cloud.Bucket();

// will look for the key in ~/.wing/secrets.json
let key = new cloud.Secret(name: "OPEN_API_KEY");
let oai = new openai.OpenAI(apiKeySecret: key);


let f1 = new cloud.Function(inflight () => {
    b.put("Hello.txt", "Hello, World!");
}) as "Function1";


let f2 = new cloud.Function(inflight () => {
    let joke = oai.createCompletion("tell me a short joke", model:"gpt-3.5-turbo");
    log(joke);
}) as "OpenAIJoke";