from flask import Flask,render_template,request,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,UserMixin,logout_user
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SECRET_KEY']="SHWETANAGAPURE"
db=SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'

class blog(db.Model):
    blog_id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    publish_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    def __repr__(self):
        return f'<blog {self.title}>'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/')
def home():
    data=blog.query.all()
    return render_template('home.html',data=data)

@app.route('/register',methods =["GET","POST"])
def registeration():
    if request.method =="POST" :
        username=request.form.get("Username")
        fname=request.form.get("firstname")
        lname=request.form.get("lastname")
        email=request.form.get("email")
        password=request.form.get("password")
        user= User(username=username,fname=fname,lname=lname,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash("User has been register succesfully","Success")
        return redirect("/login")
    return render_template("register.html")

@app.route('/login',methods =["GET","POST"])
def login():
    if request.method == "POST":
        username=request.form.get("Username")
        password=request.form.get("password")
        user=User.query.filter_by(username=username,password=password).first()
        if user and password==user.password:
            login_user(user)
            flash("Login Successful","Success")
            return redirect("/")
        else:
            flash("Invalid username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
@app.route("/blogpost",methods=["GET","POST"])
def blogpost():
   if request.method =="POST" :
        title=request.form.get("title")
        author=request.form.get("author")
        content=request.form.get("content")
        blogs= blog(title=title,author=author,content=content)
        db.session.add(blogs)
        db.session.commit()
        flash("Blog has been  succesfully Published","Success")
        return redirect("/")
   return render_template("blog.html")
@app.route("/blog_detail/<int:blog_id>",methods=["GET","POST"])
def blogd(blog_id):
    blogs=blog.query.get(blog_id)
    return render_template("blog_detail.html",blogs=blogs)

@app.route("/delete/<int:blog_id>",methods=["GET","POST"])
def delete(blog_id):
    blogs=blog.query.get(blog_id)
    db.session.delete(blogs)
    db.session.commit()
    flash("post has been deleted")
    return redirect("/")

@app.route("/edit/<int:blog_id>", methods=["GET", "POST"])
def edit(blog_id):
    blog_post = blog.query.get(blog_id)
    if blog_post is None:
        flash("Blog post not found")
        return redirect("/")
    
    if request.method == "POST":
        blog_post.title = request.form.get('title')
        blog_post.author = request.form.get("author")
        blog_post.content = request.form.get('content')
        db.session.commit()
        flash("Blog post has been updated", "Success")
        return redirect('/')
    
    return render_template("edit.html", blogs=blog_post)
if __name__ == "__main__":
    app.run(debug=True)
