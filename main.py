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
    return -1
def milimeterConversion(inputNumber,unit_convert):
    if unit_convert=="m":
        return (inputNumber/1000)
    elif unit_convert=="cm":
        return (inputNumber/10)
    elif unit_convert=="mm":
        return inputNumber
    return -1
def  centimeterConversion(inputNumber,unit_convert):
    if unit_convert=="m":
        return (inputNumber/100)
    elif unit_convert=="cm":
        return inputNumber
    elif unit_convert=="mm":
        return (inputNumber*10)
    return -1

def weightConversion(inputNumber,unit_input,unit_convert):
    if unit_input== "g":
        return gramConversion(inputNumber,unit_convert)
    elif unit_input== "mg":
        return miligramConversion(inputNumber,unit_convert)
    elif unit_input== "kg":
        return kilogramConversion(inputNumber,unit_convert)
    return -1
    

def gramConversion(inputNumber,unit_convert):
    if unit_convert=="g":
        return inputNumber
    elif unit_convert=="mg":
        return (inputNumber*1000)
    elif unit_convert=="kg":
        return (inputNumber/1000)
    return -1

def miligramConversion(inputNumber,unit_convert):
    if unit_convert=="g":
        return inputNumber/1000
    elif unit_convert=="mg":
        return inputNumber
    elif unit_convert=="kg":
        return (inputNumber/1000000)
    return -1

def kilogramConversion(inputNumber,unit_convert):
    if unit_convert=="g":
        return (inputNumber*1000)
    elif unit_convert=="mg":
        return (inputNumber*1000000)
    elif unit_convert=="kg":
        return inputNumber
    return -1


def temperatureConversion(inputNumber,unit_input,unit_convert):
    if unit_input=="C":
        return celciusConversion(inputNumber,unit_convert)
    elif unit_input=="K":
        return kelvinConversion(inputNumber,unit_convert)
    elif unit_input=="F":
        return farenhiteConversion(inputNumber,unit_convert)
    return -1
    

def celciusConversion(inputNumber,unit_convert):
    if unit_convert=="C":
        return inputNumber
    elif unit_convert=="F":
        return (inputNumber*1.8 +32)
    elif unit_convert=="K":
        return (inputNumber+273.15)
    return -1


def farenhiteConversion(inputNumber,unit_convert):
    if unit_convert=="C":
        return ((inputNumber-32)*(5/9))
    elif unit_convert=="F":
        return inputNumber
    elif unit_convert=="K":
        return ((inputNumber-32)*(5/9) + 273.15)
    return -1

def kelvinConversion(inputNumber,unit_convert):
    if unit_convert=="C":
        return (inputNumber-273.15)
    elif unit_convert=="F":
        return ((inputNumber-273.15)*1.8 +32)
    elif unit_convert=="K":
        return inputNumber
    return -1
    
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def Length():
    if request.method=="POST":
        inputNumber=float(request.form.get("number"))
        unit_input=request.form.get("unit of number")
        unit_convert=request.form.get("unit to convert into")
        converted_Number=lengthConversionGuide(inputNumber,unit_input,unit_convert)
        return redirect(url_for("converted", value=converted_Number, unit=unit_convert))
    return render_template("length.html")

@app.route('/weight',methods=["POST","GET"])
def weight():
    if request.method=="POST":
        inputNumber=float(request.form.get("number"))
        unit_input=request.form.get("unit of number")
        unit_convert=request.form.get("unit to convert into")
        converted_Number=weightConversion(inputNumber,unit_input,unit_convert)
        return redirect(url_for("converted", value=converted_Number, unit=unit_convert))
    return render_template("weight.html")

@app.route('/temperature',methods=["POST","GET"])
def temperature():
    if request.method=="POST":
        inputNumber=float(request.form.get("number"))
        unit_input=request.form.get("unit of number")
        unit_convert=request.form.get("unit to convert into")
        converted_Number=temperatureConversion(inputNumber,unit_input,unit_convert)
        return redirect(url_for("converted", value=converted_Number, unit=unit_convert))
    return render_template("temperature.html")

@app.route('/converted')
def converted():
    value= request.args.get("value")
    unit=request.args.get("unit")
    return render_template("converted value.html",value=value,unit=unit)


if __name__ =="__main__":
    app.run(debug=True)

