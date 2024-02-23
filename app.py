from flask import Flask, render_template,request,redirect,url_for

#creating an instance from the flask class
app=Flask(__name__,template_folder='templates')

tasks=[]
@app.route('/')
def index():
    return render_template('index.html',tasks=tasks)

@app.route('/add',methods=['POST','GET'])
def Create_new_task():
    task=request.form.get(task)
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')

def delete_task(index):
    if 0<=index<len(tasks):
        del tasks[index]
        return redirect('url_for')

if __name__=="main":
    app.run(debug=True)