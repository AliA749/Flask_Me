'''
Sudhir Sukhai
03/07/2024
description: A basic flask program
'''
from flask import Flask, render_template, request,redirect, url_for
import math
app = Flask(__name__)

Equation = 0
P1 = ""
P2 = ""
Sign = ""
Process = ""
abs1 = ""
abs2 = ""
Message=""

@app.route('/')
def main():
    return render_template('FinCalc.html')


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
        return render_template("SimpInt.html")
    elif button_clicked == 'CI':
        return render_template("CompInt.html")
    elif button_clicked == 'IT':
        return render_template("Income.html")
    else:
        update_number(button_clicked)
        Message=""

    return render_template('FinCalc.html', P1=P1, Sign=Sign, P2=P2, Process=Process,
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
    return render_template('FinCalc.html',Message=Message)

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
    return render_template('FinCalc.html',Message=Message)

@app.route('/Income', methods=['POST'])
def Income():
    Inc = float(request.form.get("txtInc"))
    Hours = float(request.form.get("txtHours"))
    Monthdays = float(request.form.get("txtTime"))
    NegDays=float(request.form.get("txtNegTime"))
    YearlyInc = Inc*Hours*(Monthdays-NegDays)
    MonthlyInc= YearlyInc/12
    M/YInc = "$"+str(YearlyInc)+" / $"+str(MonthlyInc)
    Message = "The expected yearly/Monthly income is " + M/YInc
    return render_template('FinCalc.html',Message=Message)


if __name__ == '__main__':
    app.run()
