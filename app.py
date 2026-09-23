from flask import Flask, render_template_string, request, redirect, jsonify

app = Flask(__name__)
tasks = []

PAGE = """
<!DOCTYPE html>
<html>
<head><title>DevOps Task List</title>
<style>
 body{font-family:sans-serif;max-width:500px;margin:40px auto}
 input{padding:6px;width:70%} button{padding:6px 12px}
</style></head>
<body>
 <h1>DevOps Task List</h1>
 <p>Version 2 - auto-deployed by the CI/CD pipeline</p>
 <form method="post">
  <input name="task" placeholder="New task" required>
  <button type="submit">Add</button>
 </form>
 <ul>{% for t in tasks %}<li>{{ t }}</li>{% endfor %}</ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            tasks.append(task)
        return redirect("/")
    return render_template_string(PAGE, tasks=tasks)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
