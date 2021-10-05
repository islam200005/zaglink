
import pyshorteners
from flask import Flask,render_template,request,flash
import sqlite3



app = Flask(__name__)
app.secret_key ='this is my secret key'

@app.route("/", methods=["GET","POST"])
def index():
 
    if request.method == "POST":
        con = sqlite3.connect('mecha2_first.db')
        db = con.cursor()

        subject = request.form.get("subject")
        link = request.form.get("link")
        code = request.form.get("code")
        description = request.form.get("description")
        
        codes = db.execute("SELECT code FROM math")
        s = pyshorteners.Shortener()
        shrinked = s.isgd.short(link)
       
        if not subject:
           message = "هو انا بنجم ؟ هل انا بنجم؟ متختارلك ماده يعم"
           return render_template("index.html", code = code, link = link , description = description , message = message)
        if not link:
            message = "ايوا يعني انا مطلوب مني ايه انا دلوقتى! متجيب اللينك يعم"
            return render_template("index.html", code = code, link = link , description = description , message = message)
        if not code:
            message = "فين يبني الكود يبني متشلنيش"
            return render_template("index.html", code = code, link = link , description = description , message = message)
       
       
        if subject == "math":

            state = False
            for temp_code in codes:
                if code == temp_code[0]:
                    state = True
            if state:
                shrinked=""
                message= "اصحي يا بيه الكود دا موجود اصلا"
            else:
                db.execute("INSERT INTO math (link,code,description,shrinked) VALUES(?,?,?,?)",(link,code, description,shrinked))
                message=" كله عال العال يسط خش عالى بعديه"
        elif subject == "heat":
            state = False
            for temp_code in codes:
                if code == temp_code[0]:
                    state = True
            if state:
                shrinked=""
                message= "اصحي يا بيه الكود دا موجود اصلا"
            else:
                db.execute("INSERT INTO heat (link,code,description,shrinked) VALUES(?,?,?,?)",(link,code, description,shrinked))
                message=" كله عال العال يسط خش عالى بعديه"
        elif subject == "machine":
            state = False
            for temp_code in codes:
                if code == temp_code[0]:
                    state = True
            if state:
                shrinked=""
                message= "اصحي يا بيه الكود دا موجود اصلا"
            else:
                db.execute("INSERT INTO machine (link,code,description,shrinked) VALUES(?,?,?,?)",(link,code, description,shrinked))
                message=" كله عال العال يسط خش عالى بعديه"
        elif subject == "production":
            state = False
            for temp_code in codes:
                if code == temp_code[0]:
                    state = True
            if state:
                shrinked=""
                message= "اصحي يا بيه الكود دا موجود اصلا"
            else:
                db.execute("INSERT INTO production (link,code,description,shrinked) VALUES(?,?,?,?)",(link,code, description,shrinked))
                message=" كله عال العال يسط خش عالى بعديه"
            
        elif subject == "stress":
            state = False
            for temp_code in codes:
                if code == temp_code[0]:
                    state = True
            if state:
                shrinked=""
                message= "اصحي يا بيه الكود دا موجود اصلا"
            else:
                db.execute("INSERT INTO stress (link,code,description,shrinked) VALUES(?,?,?,?)",(link,code, description,shrinked))
                message=" كله عال العال يسط خش عالى بعديه"
        elif subject == "hr":
            state = False
            for temp_code in codes:
                if code == temp_code[0]:
                    state = True
            if state:
                shrinked=""
                message= "اصحي يا بيه الكود دا موجود اصلا"
            else:
                db.execute("INSERT INTO hr (link,code,description,shrinked) VALUES(?,?,?,?)",(link,code, description,shrinked))
                message=" كله عال العال يسط خش عالى بعديه"

        con.commit()
        con.close()
        return render_template("index.html", link = "", code = "" , description = "", shrinked = shrinked,message =message)
        
        

    else:
        
        return render_template("index.html")

@app.route("/remove", methods=["GET","POST"])
def remove():
    if request.method == "POST":
        shrinked = request.form.get("shrinked")
        code = request.form.get("code")
        subject = request.form.get("subject")

        con = sqlite3.connect('mecha2_first.db')
        db = con.cursor()
        if not subject:
            message = "هو انا بنجم ؟ هل انا بنجم؟ متختارلك ماده يعم"
            return render_template("remove.html", shrinked = shrinked, code = code ,message =message)
        
        if not shrinked and not code:
             message = "طب يشيخ انا راضى ذمتك اعرفه ازاى انا كده"
             return render_template("remove.html", shrinked = shrinked, code = code ,message =message)
        
        if subject == "math":
            if shrinked:
                db.execute("DELETE FROM math WHERE shrinked = ?",[shrinked])
            elif code:
                db.execute("DELETE FROM math WHERE code = ?",[code])
        elif subject == "heat":
            if shrinked:
                db.execute("DELETE FROM heat WHERE shrinked = ?",[shrinked])
            elif code:
                db.execute("DELETE FROM heat WHERE code = ?",[code])
        elif subject == "hr":
            if shrinked:
                db.execute("DELETE FROM hr WHERE shrinked = ?",[shrinked])
            elif code:
                db.execute("DELETE FROM hr WHERE code = ?",[code])
        elif subject == "machine":
            if shrinked:
                db.execute("DELETE FROM machine WHERE shrinked = ?",[shrinked])
            elif code:
                db.execute("DELETE FROM machine WHERE code = ?",[code])
        elif subject == "production":
            if shrinked:
                db.execute("DELETE FROM production WHERE shrinked = ?",[shrinked])
            elif code:
                db.execute("DELETE FROM production WHERE code = ?",[code])
        elif subject == "stress":
            if shrinked:
                db.execute("DELETE FROM stress WHERE shrinked = ?",[shrinked])
            elif code:
                db.execute("DELETE FROM stress WHERE code = ?",[code])
    
        rows = db.fetchall()
        con.commit()
        con.close()
        exist_check = False
        for row in rows:
            if code  in row[2] or shrinked  in row[4]:
                exist_check = True
        
        if exist_check:
            message = "تمت العمليه بنجاح"
            

            

            return render_template("remove.html",message = message)
        else:
            message = "هو اصلا مش موجود يسط"
            return render_template("remove.html",message = message)


        

    else:

        return render_template("remove.html")


@app.route("/search", methods=["GET","POST"])
def search():

    if request.method == "POST":
        subject = request.form.get("subject")
        shrinked = request.form.get("shrinked")
        code = request.form.get("code")
        con = sqlite3.connect('mecha2_first.db')
        db = con.cursor()
        
        if not shrinked and not code:
            message="هاتلنا حاجه من اتره طيب"
            return render_template("search.html", shrinked = "", code = "" ,message =message)

        if not subject:
            message = "هو انا بنجم ؟ هل انا بنجم؟ متختارلك ماده يعم"
            return render_template("search.html", shrinked = shrinked, code = code ,message =message)
        if subject == "math":
                if code:
                    rows = db.execute("SELECT * FROM math WHERE code like ?",[code])
                    return render_template("result.html",rows = rows)
                elif shrinked:
                    rows = db.execute("SELECT * FROM math WHERE shrinked like ?",[shrinked])
                    return render_template("result.html",rows = rows)
        if subject == "heat":
                if code:
                    rows = db.execute("SELECT * FROM heat WHERE code like ?",[code])
                    return render_template("result.html",rows = rows)
                elif shrinked:
                    rows = db.execute("SELECT * FROM heat WHERE shrinked like ?",[shrinked])
                    return render_template("result.html",rows = rows)
        if subject == "stress":
                if code:
                    rows = db.execute("SELECT * FROM stress WHERE code like ?",[code])
                    return render_template("result.html",rows = rows)
                elif shrinked:
                    rows = db.execute("SELECT * FROM stress WHERE shrinked like ?",[shrinked])
                    return render_template("result.html",rows = rows)
        if subject == "machine":
                if code:
                    rows = db.execute("SELECT * FROM machine WHERE code like ?",[code])
                    return render_template("result.html",rows = rows)
                elif shrinked:
                    rows = db.execute("SELECT * FROM machine WHERE shrinked like ?",[shrinked])
                    return render_template("result.html",rows = rows)
        if subject == "production":
                if code:
                    rows = db.execute("SELECT * FROM production WHERE code like ?",[code])
                    return render_template("result.html",rows = rows)
                elif shrinked:
                    rows = db.execute("SELECT * FROM production WHERE shrinked like ?",[shrinked])
                    return render_template("result.html",rows = rows)
        if subject == "hr":
                if code:
                    rows = db.execute("SELECT * FROM math WHERE code like ?",[code])
                    return render_template("result.html",rows = rows)
                elif shrinked:
                    rows = db.execute("SELECT * FROM math WHERE shrinked like ?",[shrinked])
                    return render_template("result.html",rows = rows)
    
            
        

    else:
        return render_template("search.html")
    


    return render_template("search.html")

@app.route("/home")
def home():
    


    return render_template("index.html")



