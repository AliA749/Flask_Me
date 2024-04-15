from flask import Flask, render_template, request

app = Flask(__name__)

Equation = 0
P1 = ""
P2 = ""
Sign = ""
Process = ""


@app.route('/')
def main():
    return render_template('calc.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    global Equation, P1, P2, Sign, Process
    button_clicked = request.form['btn']
    if button_clicked == 'C':
        clear()
    elif button_clicked == '=':
        result()
    elif button_clicked in ['+', '-', 'x', '/']:
        update_sign(button_clicked)
    elif button_clicked == '.':
        decimal()
    elif button_clicked == '%':
        percent()
    elif button_clicked == '±':
        negative()
    else:
        update_number(button_clicked)
    return render_template('calc.html', P1=P1, Sign=Sign, P2=P2, Process=Process)


def clear():
    global P1, P2, Sign, Process
    P1 = ""
    P2 = ""
    Sign = ""
    Process = ""


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
    P2 += button_clicked


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


def result():
    global P1, P2, Sign, Process
    calc()
    P1 = Process
    P2 = ""
    Sign = ""


def calc():
    global Process, P1, P2, Sign
    if Sign == '+':
        Process = str(float(P1) + float(P2))
    elif Sign == '-':
        Process = str(float(P1) - float(P2))
    elif Sign == 'x':
        Process = str(float(P1) * float(P2))
    elif Sign == '/':
        if P2 == '0':
            Process = "Error"
        else:
            Process = str(float(P1) / float(P2))


if __name__ == '__main__':
    app.run()
