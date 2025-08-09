from flask import Flask, render_template, request, redirect

app = Flask(__name__)
TASK_FILE = "tasks.txt"

# def add_numbers(a, b):
#     return a + b

def write_task(task):
    with open(TASK_FILE, "a") as doc:
        doc.write(task + "\n")
        
def read_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

# CRUD 
# Create, Remove, Update, Display

@app.route('/', methods=["GET", "POST"]) #landing page
# Commenting any code in VS Code  Ctrl K C
def home():

    if request.method == "POST":
        task = request.form.get("task")
        
        if task:
            write_task(task)
            
        return redirect("/")
    
    return render_template("index.html", tasks = read_tasks())

@app.route("/delete", methods=["POST"])
def delete_task():
    task_to_delete = request.form.get("task_to_delete")
    tasks = read_tasks()
    updated_tasks = [task for task in tasks if task != task_to_delete]
    
    with open(TASK_FILE,"w") as file:
        for task in updated_tasks:
            file.write(task + "\n")
            
    return redirect("/")

## EDITING bonus
# @app.route("/edit", methods=["POST"])
# def edit_task():
#     old_task = request.form.get("old_task")
#     new_task = request.form.get("new_task")
#     tasks = read_tasks()

#     updated_tasks = []
#     found = False
#     for task in tasks:
#         if task == old_task and not found:
#             updated_tasks.append(new_task)
#             found = True
#         else:
#             updated_tasks.append(task)

#     with open(TASK_FILE, "w") as f:
#         for task in updated_tasks:
#             f.write(task + "\n")

    # return redirect("/")
    
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)