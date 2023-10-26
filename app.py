from flask import Flask, render_template, request, jsonify

import subprocess

app = Flask(__name__, template_folder="templates")


# @app.route serves to direct the request to a mapped URL
# / represents the homepage.
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def generate_text():
    prompt = request.form.get("Prompt", "")
    response = subprocess.run(
        [
            "python",
            "lit_gpt/generate/base.py",
            "--prompt",
            prompt,
            "--checkpoint_dir",
            "lit_gpt/checkpoints/microsoft/phi-1_5",
        ]
    )
    print(response)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
