from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import sqlite3
import pandas as pd
import numpy as np
from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import cv2

app = Flask(__name__)
app.secret_key = '5766ghghgg7654dfd7h9hsfsfh'

dic = {0 : 'Normal', 1 : 'Osteoporosis'}
      

@app.route('/')
def home():
    return render_template('signup.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        full_name = request.form['fullname']
        address = request.form['address']
        email = request.form['email']
        phone_number = request.form['phonenumber']
        gender = request.form['gender']
        age = request.form['age']
        dob = request.form['dob']
        medical_history = request.form['medical']
        blood_group = request.form['bloodgroup']
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists in the database
        conn = sqlite3.connect('C:/Users/Sahil gade/OneDrive/Desktop/osteoporosis_detection/flask/database/Medical.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_details WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user is not None:
            # If the user already exists, add a flash message and redirect back to the signup page
            session['message'] = 'Username already taken. Please choose another one.'
            
            return redirect(url_for('signup', error='Username already exist.'))
        
            
        else:
            # If the user does not exist, insert the new user into the database and redirect to the login page
            conn = sqlite3.connect('C:/Users/Sahil gade/OneDrive/Desktop/osteoporosis_detection/flask/database/Medical.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user_details (full_name, address, email, phone_number, gender, age, dob, medical_history, blood_group, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (full_name, address, email, phone_number, gender, age, dob, medical_history, blood_group, username, password))
            conn.commit()
            conn.close()
            
            return redirect(url_for('login'))
        
    elif request.args.get('error') is None:    
        return render_template('signup.html')
        
    else:   
        error = request.args.get('error')
        return render_template('signup.html', error=error)



@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('C:/Users/Sahil gade/OneDrive/Desktop/osteoporosis_detection/flask/database/Medical.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM user_details WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()
        
        if user is not None:
            session['username'] = user[9]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
   else:
        return render_template('login.html')


@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', current_user=session['username'])
    return redirect(url_for('login'))   



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        conn = sqlite3.connect('C:/Users/Sahil gade/OneDrive/Desktop/osteoporosis_detection/flask/database/Medical.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_feedback (name, email, subject, message) VALUES (?, ?, ?, ?)", (name, email, subject, message))
        conn.commit()
        conn.close()
        return redirect(url_for('contact'))
    
    
    return render_template('contact.html') 


@app.route('/jumbo')
def jumbo():
    return render_template('jumbo.html')

@app.route('/disease')
def disease():
    return render_template('disease.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


#### Machine Learning Code
img_size=256
model = load_model('model.h5')

model.make_predict_function()

def predict_label(img_path):
    img=cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    resized=cv2.resize(gray,(img_size,img_size)) 
    i = img_to_array(resized)/255.0
    i = i.reshape(1,img_size,img_size,1)
    predict_x=model.predict(i) 
    p=np.argmax(predict_x,axis=1)
    return dic[p[0]]


@app.route('/predict',methods=['POST'])
def predict():
#     '''
#     For rendering results on HTML GUI
    
#     '''

    if request.method == 'POST':
       img = request.files['file']
       img_path = "uploads/" + img.filename    
       img.save(img_path)
       p = predict_label(img_path)
       return str(p).lower()
       
    #    return render_template('disease.html', prediction_text='{}'.format(str(p).lower()))
 

if __name__ == "__main__":
    app.run(debug=True)
