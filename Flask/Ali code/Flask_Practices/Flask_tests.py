from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
    if request.method == "GET":
        return render_template('personalityquiz.html')
    else:
        result = results()
        return redirect(url_for(result))

@app.route('/happy')
def happy():
    result = "(A happy person) has a sense of contentment and joy.Their outlook on life is optimistic, finding delight in simple pleasures and maintaining a healthy balance between life and society. Happy individuals tend to be resilient in the face of challenges, focusing on solutions rather than dwelling on problems, and they spread happiness to those around them."
    return render_template('saveinfo.html', results=result)


@app.route('/anxious')
def anxious():
    result = "(An anxious personality) is shown by constant feelings of fear that can significantly impact daily life. Individuals with an anxious personality may often experience excessive concern about various aspects of their lives, leading to difficulty in managing themselves."
    return render_template('saveinfo.html', results=result)

@app.route('/perfectionist')
def perfectionist():
    result = "(A perfectionist) is someone who strives for flawlessness and sets exceptionally high standards for themselves, often feeling dissatisfaction when they see their work or achievements as falling short of their own criteria. They may exhibit tendencies of meticulousness, an intense focus on detail."
    return render_template('saveinfo.html', results=result)

@app.route('/introvert')
def introvert():
    result = "(An introvert) is typically characterized by a preference for solitude, often feeling energized by solitary activities and introspection. They may engage in deep, meaningful conversations with a small circle of close friends."
    return render_template('saveinfo.html', results=result)

@app.route('/extrovert')
def extrovert():
    result = "(An extrovert) typically thrives in social situations, gaining energy from interaction with others and often exhibiting outgoing, talkative, and assertive traits."
    return render_template('saveinfo.html', results=result)

@app.route('/adventurous')
def adventurous():
    result = "(An adventurous person)thrives on novelty, embraces uncertainty, and seeks out thrilling experiences to continuously push their boundaries and expand their horizons."
    return render_template('saveinfo.html', results=result)

def results():
    answer_choice = request.form.get('personalitychoice1')
    answer_choice2 = request.form.get('personalitychoice2')
    answer_choice3 = request.form.get('personalitychoice3')
    answer_choice4 = request.form.get('personalitychoice4')
    answer_choice5 = request.form.get('personalitychoice5')
    
    if answer_choice and answer_choice2 and answer_choice3 and answer_choice4 and answer_choice5 != "":
        happyarr = ["yes", "yes", "yes", "yes", "no"]
        anxiousarr = ["no", "no", "no", "no", "yes"]
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
            
    else:
        abort(403)

if __name__=="__main__":
    app.run()
