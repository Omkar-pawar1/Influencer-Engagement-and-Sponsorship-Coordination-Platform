from flask import Flask,render_template,request,url_for
from flask import current_app as app
from .models import db,Sponsor,Influencer,Category


@app.route("/")
def Loginform():
    return render_template('registrationform.html')

@app.route("/Create_Influencer_User", methods=['POST'])
def Create_Influencer_User():
    name=request.form['username']
    email=request.form['email']
    password=request.form['password']
    category=request.form['category']
    niche=request.form['niche']
    reach=request.form['reach']
    new_influencer=Influencer(name=name,email=email,password=password,reach=reach)
    db.session.add(new_influencer)
    db.session.commit()

    influencer_category=Category(category=category,niche=niche,influencer_id=new_influencer.id)
    db.session.commit()


    print("added i_user successfully")
    return render_template('influencer_home_page.html')

@app.route("/Create_Sponsor_User", methods=['POST'])
def Create_Sponsor_User():
    company_name=request.form['cname']
    email=request.form['email']
    password=request.form['password']
    industry=request.form['industry']
    budget=request.form['budget']
    S_User=Sponsor(company_name=company_name,email=email,password=password,industry=industry,budget=budget)
    db.session.add(S_User)
    db.session.commit()
    print("added s_user successfully")
    return render_template('sponsor_home_page.html')



@app.route("/Login_form_for_influencer")
def Login_form_for_influencer():
    return render_template('influencer_login_form.html')


@app.route("/Login_form_for_sponsor")
def Login_form_for_sponser():
    return render_template('sponsor_login_form.html')


@app.route("/Login_Influencer", methods=['GET','POST'])
def Login_Influencer():
    email=request.form['email']
    password=request.form['password']
    user=Influencer.query.filter_by(email=email).first()
    if user.password==password:
        return render_template('influencer_home_page.html')
    else:
        return ("wrong credintials please log in again")

@app.route("/Login_Sponsor", methods=['GET','POST'])
def Login_Sponsor():
    email=request.form['email']
    password=request.form['password']
    user=Sponsor.query.filter_by(email=email).first()
    if user.password==password:
        return render_template('sponsor_home_page.html')
    else:
        return ("wrong credintials please log in again")

