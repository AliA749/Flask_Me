'''
Sudhir Sukhai/ Ali
03/07/2024
description: A basic flask program
'''
import webbrowser
from flask import Flask,render_template,request, url_for,redirect

app = Flask(__name__)
Equation = 0
P1 = ""
P2 = ""
Sign = ""
Process = ""
abs1 = ""
abs2 = ""
Message=""

@app.route("/",methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template("Login.html")
    else:
        return GetInfo()
def GetInfo():
    #classes
    global username
    arrName=["Sudhir","Ali","Pigis","Temp","s"]
    arrPass=["MyPass1","Admin2","Admin3","temp1","s"]
    lenName= len(arrName)
    lenPass= len(arrPass)
    username = request.form.get('txtname')
    Pass = request.form.get('txtpass')
    Error="Wrong name or pass"
    Runs=int(0)
    while (Runs != lenName):
        if (username!="" and Pass!=""):
            if (username == arrName[Runs]) :
                if (Pass == arrPass[Runs]):
                    return redirect('/Personalinfo') 
        Runs=Runs+1
    return render_template("Login.html",Error=Error)

@app.route("/Personalinfo",methods=['GET','POST'])
def StartP2():
    if request.method == 'GET':
        return render_template("Next.html",Name=username)
    else:
        return GetPersonalinfo()

def GetPersonalinfo():
    global fullname,Age,Email,DOB,School,ID,imgSLC,SLC
    fullname = request.form.get('txtfullname')
    Age =  request.form.get('txtage')
    Email = request.form.get('txtemail')
    DOB = request.form.get('txtDOB')
    School = request.form.get('txtSchool')
    ID = request.form.get('txtID')
    SLC = request.form.get('SLCselector')
    if (SLC != ""):
        switcher = {
            "Pre-Med": "\static\PreMed.jpeg",
            "HSSE": "\static\HSSE.jpeg",
            "Global Citizens": "\static\ClobCit.jpeg",
            "Humanities": "\static\Hms.jpeg",
            "APVA": "\static\APVA.jpeg",
            "Public Service" : "\static\PS.jpeg",
            "TOT": "\static\TOT.jpeg"
        }
    imgSLC= switcher.get(SLC)
    return redirect('/Transfer') 

@app.route("/Transfer",methods=['GET','POST'])
def StartP3():
    if request.method == 'GET':
        return render_template("Transfer.html",fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)
    else:
        return GetResult()

def GetResult():
    Error="Select an option"
    selected=request.form.get("Selector")
    if (selected == ""):
        return render_template("Transfer.html",Error=Error)
    elif (selected == "GenInterest"):
        return redirect('/GenInterest')
    elif (selected == "FinCalc"):
        return redirect('/FinCalc')








        
@app.route("/FinCalc",methods=['GET','POST'])
def FinCalc1():
    if request.method == 'GET':
        return render_template("FinCalc.html",fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)

@app.route('/calculate', methods=['POST'])
def calculate():
    global Equation, P1, P2, Sign, Process,Message
    button_clicked = request.form['btn']

    if button_clicked == 'C':
        clear()
    elif button_clicked == '=':
        result()
    elif button_clicked in ['+', '-', 'x', '/' , '^']:
        update_sign(button_clicked)
    elif button_clicked == '.':
        decimal()
    elif button_clicked == '%':
        percent()
    elif button_clicked == '±':
        negative()
    elif button_clicked == '√':
        Sqrt()
    elif button_clicked == '^2':
        Pow2()
    elif button_clicked == 'e':
        e()
    elif button_clicked == 'π':
        Pi()
    elif button_clicked == '|x|':
        Abs()
    elif button_clicked == 'Sin':
        Sin()
    elif button_clicked == 'Cos':
        Cos()
    elif button_clicked == 'Tan':
        Tan()
    elif button_clicked == 'SI':
        return render_template("SimpInt.html",fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)
    elif button_clicked == 'CI':
        return render_template("CompInt.html",fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)
    elif button_clicked == 'IT':
        return render_template("Income.html",fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)
    else:
        update_number(button_clicked)
        Message=""

    return render_template('FinCalc.html', fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC, P1=P1, Sign=Sign, P2=P2, Process=Process,
                           abs1=abs1,abs2=abs2, Message=Message)


def clear():
    global P1, P2, Sign, Process
    P1 = ""
    P2 = ""
    Sign = ""
    Process = ""
    abs1 = ""
    abs2 = ""

def update_sign(button_clicked):
    global P1, P2, Sign
    if Sign and P2:
        result()
    else:
        P1 = P2
        P2 = ""
        Sign = button_clicked


def update_number(button_clicked):
    global P2
    P2 = P2+button_clicked


def decimal():
    global P2
    if '.' not in P2:
        P2 += '.'


def percent():
    global P2
    P2 = str(float(P2) / 100)


def negative():
    global P2
    if P2.startswith('-'):
        P2 = P2[1:]
    else:
        P2 = '-' + P2

def Sqrt():
    global P2
    P2 = float(P2)
    P2 = math.sqrt(P2)
    P2 = str(round(P2,2))

def Pow2():
    global P1,P2,Sign
    P2=float(P2)
    P2 = str(math.pow(P2, 2))

def Abs():
    global abs1, abs2
    if '|' not in abs1:
        abs1 = "|"
        abs2 = "|"
    else:
        abs1 = ""
        abs2 = ""

        
def Pi():
    global P1, P2, Sign
    if Sign !="" and P2!="":
        result()
        Sign = "x"
        P2 = "π"
    elif Sign == "" and P2 != "":
        P1 = P2
        Sign = "x"
        P2 = "π"
    elif Sign == "" and P2 == "" and P1=="":
        P2="π"

def e():
    global P1, P2, Sign
    if Sign !="" and P2!="":
        result()
        Sign = "x"
        P2 = "e"
    elif Sign == "" and P2 != "":
        P1 = P2
        Sign = "x"
        P2 = "e"
    elif Sign == "" and P2 == "" and P1=="":
        P2="e"

def Sin():
    global P1, P2, Sign
    if Sign !="" and P2!="":
        result()
        Sign = "x"
        P2 = "Sin("
    elif Sign == "" and P2 != "":
        P1 = P2
        Sign = "x"
        P2 = "Sin("
    elif Sign == "" and P2 == "" and P1=="":
        P2="Sin("
def Cos():
    global P1, P2, Sign
    if Sign !="" and P2!="":
        result()
        Sign = "x"
        P2 = "Cos("
    elif Sign == "" and P2 != "":
        P1 = P2
        Sign = "x"
        P2 = "Cos("
    elif Sign == "" and P2 == "" and P1=="":
        P2="Cos("
def Tan():
    global P1, P2, Sign
    if Sign !="" and P2!="":
        result()
        Sign = "x"
        P2 = "Tan("
    elif Sign == "" and P2 != "":
        P1 = P2
        Sign = "x"
        P2 = "Tan("
    elif Sign == "" and P2 == "" and P1=="":
        P2="Tan("

def result():
    global P1, P2, Sign, Process
    calc()
    P1=""
    P2 = Process
    Sign = ""


def calc():
    global Process, P1, P2, Sign,abs1,abs2
    print("s")
    Convert()
    print("s")
    if Sign == '+':
        Process = float(P1) + float(P2)
    elif Sign == '-':
        print("s")
        Process = float(P1) - float(P2)
        print(Process)
    elif Sign == 'x':
        Process = float(P1) * float(P2)
    elif Sign == '/':
            Process = float(P1) / float(P2)
    elif Sign == '^':
            Process = math.pow(float(P1),float(P2))
    else:
        if P2 == '0':
            Process = "Error"
    Process = str(round(float(Process),2))
    print(Process)
    if abs1 == "|":
        if float(Process) < 0:
            Process = str(float(Process) * -1)
            abs1=""
            abs2=""
    print(Process)
    
def Convert():
    global P1, P2, Sign
    if ("Sin(" in P2):
        P2 = P2.replace("Sin(","0")
        P2 = str(math.sin(float(P2)))
    elif ("Cos(" in P2):
        P2 = P2.replace("Cos(","0")
        P2 = str(math.cos(float(P2)))
    elif ("Tan(" in P2):
        P2 = P2.replace("Tan(","0")
        P2 = str(math.tan(float(P2)))
    elif ("Sin(" in P1):
        P1 = P1.replace("Sin(","0")
        P1 = str(math.sin(float(P1)))
    elif ("Cos(" in P1):
        P1 = P1.replace("Cos(","0")
        P1 = str(math.cos(float(P1)))
    elif ("Tan(" in P1):
        P1 = P1.replace("Tan(","0")
        P1 = str(math.tan(float(P1)))
    match(P1):
        case "e":
          P1 = math.e
        case "π":
          P1 = math.pi
    match(P2):
        case "e":
          P2 = math.e
        case "π":
          P2 = math.pi

@app.route('/SimpInt', methods=['POST'])
def SimpInt():
    Pri = float(request.form.get("txtPrincipal"))
    Rate = float(request.form.get("txtRate"))
    Time = float(request.form.get("txtTime"))
    SimpleInt = round((Pri*Rate*Time)/100,2)
    Payment = SimpleInt+Pri
    Message = "The expected payment is " + str(Payment)
    return render_template('FinCalc.html',fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC,Message=Message)

@app.route('/CompInt', methods=['POST'])
def CompInt():
    Pri = float(request.form.get("txtPrincipal"))
    Rate = float(request.form.get("txtRate"))
    Time = float(request.form.get("txtTime"))
    n = float(request.form.get("txtComp"))
    CompInt= Pri*pow((1+(Rate/n)),(n*Time))
    CompInt = round(CompInt,2)
    Payment = CompInt+Pri
    Message = "The expected payment/gain is " + str(Payment)
    return render_template('FinCalc.html',fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC,Message=Message)

@app.route('/Income', methods=['POST'])
def Income():
    Inc = float(request.form.get("txtInc"))
    Hours = float(request.form.get("txtHours"))
    Monthdays = float(request.form.get("txtTime"))
    NegDays=float(request.form.get("txtNegTime"))
    YearlyInc = Inc*Hours*(Monthdays-NegDays)
    MonthlyInc= YearlyInc/12
    MorYInc = "$"+str(YearlyInc)+" / $"+str(MonthlyInc)
    Message = "The expected yearly/Monthly income is " + MorYInc
    return render_template('FinCalc.html',fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC,Message=Message)



@app.route("/GenInterest",methods=['GET','POST'])
def GenInterest1():
    if request.method == "GET":
        return render_template('Personalityquiz.html',fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)
    else:
        result = results()
        return redirect(url_for(result))

@app.route('/happy')
def happy():
    result = "(A happy person) has a sense of contentment and joy.Their outlook on life is optimistic, finding delight in simple pleasures and maintaining a healthy balance between life and society. Happy individuals tend to be resilient in the face of challenges, focusing on solutions rather than dwelling on problems, and they spread happiness to those around them."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC )


@app.route('/anxious')
def anxious():
    result = "(An anxious personality) is shown by constant feelings of fear that can significantly impact daily life. Individuals with an anxious personality may often experience excessive concern about various aspects of their lives, leading to difficulty in managing themselves."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)

@app.route('/depressed')
def depressed():
    result = "(An Depressed personality) is shown by constant feelings of fear that can significantly impact daily life. Individuals with an depressed personality may often experience excessive sorrow about various aspects of their lives or may not care for it at all, leading to difficulty in managing their lives."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)

@app.route('/perfectionist')
def perfectionist():
    result = "(A perfectionist) is someone who strives for flawlessness and sets exceptionally high standards for themselves, often feeling dissatisfaction when they see their work or achievements as falling short of their own criteria. They may exhibit tendencies of meticulousness, an intense focus on detail."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC )

@app.route('/introvert')
def introvert():
    result = "(An introvert) is typically characterized by a preference for solitude, often feeling energized by solitary activities and introspection. They may engage in deep, meaningful conversations with a small circle of close friends."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)

@app.route('/extrovert')
def extrovert():
    result = "(An extrovert) typically thrives in social situations, gaining energy from interaction with others and often exhibiting outgoing, talkative, and assertive traits."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)

@app.route('/adventurous')
def adventurous():
    result = "(An adventurous person)thrives on novelty, embraces uncertainty, and seeks out thrilling experiences to continuously push their boundaries and expand their horizons."
    return render_template('saveinfo.html', results=result,fullname=fullname,DOB=DOB,Email=Email,
                               School=School,Age=Age,ID=ID,imgSLC=imgSLC,SLC=SLC)

def results():
    answer_choice = request.form.get('personalitychoice1')
    answer_choice2 = request.form.get('personalitychoice2')
    answer_choice3 = request.form.get('personalitychoice3')
    answer_choice4 = request.form.get('personalitychoice4')
    answer_choice5 = request.form.get('personalitychoice5')
    
    if answer_choice and answer_choice2 and answer_choice3 and answer_choice4 and answer_choice5 != "":
        happyarr = ["yes", "yes", "yes", "yes", "no"]
        anxiousarr = ["no", "no", "no", "no", "yes"]
        depressedarr = ["no", "no", "no", "no", "no"]
        perfectionistarr = ["no", "no", "yes", "no", "yes"]
        introvertarr = ["no", "yes", "no", "no", "no"]
        extrovertarr  = ["yes", "yes", "yes", "yes", "yes" ]
        adventurousarr  = ["yes", "yes", "no", "yes", "yes" ]
        if answer_choice == happyarr[0] and answer_choice2 == happyarr[1] and answer_choice3 == happyarr[2] and answer_choice4 == happyarr[3] and answer_choice5 == happyarr[4]:
            return "happy"
        elif answer_choice == anxiousarr[0] and answer_choice2 == anxiousarr[1] and answer_choice3 == anxiousarr[2] and answer_choice4 == anxiousarr[3] and answer_choice5 == anxiousarr[4]:
            return "anxious"
        elif answer_choice == perfectionistarr[0] and answer_choice2 == perfectionistarr[1] and answer_choice3 == perfectionistarr[2] and answer_choice4 == perfectionistarr[3] and answer_choice5 == perfectionistarr[4]:
            return "perfectionist"
        elif answer_choice == introvertarr[0] and answer_choice2 == introvertarr[1] and answer_choice3 == introvertarr[2] and answer_choice4 == introvertarr[3] and answer_choice5 == introvertarr[4]:
            return "introvert"
        elif answer_choice == extrovertarr[0] and answer_choice2 == extrovertarr[1] and answer_choice3 == extrovertarr[2] and answer_choice4 == extrovertarr[3] and answer_choice5 == extrovertarr[4]:
            return "extrovert"
        elif answer_choice == adventurousarr[0] and answer_choice2 == adventurousarr[1] and answer_choice3 == adventurousarr[2] and answer_choice4 == adventurousarr[3] and answer_choice5 == adventurousarr[4]:
            return "adventurous"
        elif answer_choice == depressedarr[0] and answer_choice2 == depressedarr[1] and answer_choice3 == depressedarr[2] and answer_choice4 == depressedarr[3] and answer_choice5 == depressedarr[4]:
            return "depressed"
            
    else:
        abort(403)

if __name__ == "__main__":
    app.run()
