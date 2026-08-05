from flask import Flask,render_template,redirect,request,url_for

def lengthConversionGuide(inputNumber,unit_input,unit_convert):
    convertedinput=0
    if unit_input=='m':
       convertedinput= meterConversion(inputNumber,unit_convert)
    if unit_input=='mm':
       convertedinput= milimeterConversion(inputNumber,unit_convert)
    if unit_input=='cm':
       convertedinput= centimeterConversion(inputNumber,unit_convert)
    return convertedinput

def meterConversion(inputNumber,unit_convert):
    if unit_convert=="m":
        return inputNumber
    elif unit_convert=="cm":
        return (inputNumber*100)
    elif unit_convert=="mm":
        return (inputNumber*1000)

def milimeterConversion(inputNumber,unit_convert):
    if unit_convert=="m":
        return (inputNumber/1000)
    elif unit_convert=="cm":
        return (inputNumber/10)
    elif unit_convert=="mm":
        return inputNumber
def centimeterConversion(inputNumber,unit_convert):
    if unit_convert=="m":
        return (inputNumber/100)
    elif unit_convert=="cm":
        return inputNumber
    elif unit_convert=="mm":
        return (inputNumber*10)

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=="POST":
        inputNumber=float(request.form.get("number"))
        unit_input=request.form.get("unit of number")
        unit_convert=request.form.get("unit to convert into")
        converted_Number=lengthConversionGuide(inputNumber,unit_input,unit_convert)
        print( converted_Number)
        return redirect(url_for("result", value=converted_Number, unit=unit_convert))


    return render_template("index.html")
@app.route('/result')
def result():
    value= request.args.get("value")
    unit=request.args.get("unit")
    return render_template("converted length.html",value=value,unit=unit)

if __name__ =="__main__":
    app.run(debug=True)

