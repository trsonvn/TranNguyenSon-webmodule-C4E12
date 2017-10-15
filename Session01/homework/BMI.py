@app.route('/BMI/<int:height>/<int:weight>')
def BMI(height,weight):
    height_cm = float(input("input height(cm): "))
    weight_kg = float(input("input weight(kg): "))
    height_m = height_cm * 0.01
    BMI = weight_kg / (height_m ** 2)

    if BMI < 16:
        result="Severely underweight"
    elif 16 <= BMI < 18.5:
        result="Underweight"
    elif 18.5 <= BMI < 25:
        result="Normal"
    elif 25 <= BMI <= 30:
        result="Overweight"
    else:
        result="Obese"

    return "BMI: " + str(int(BMI)) + " - " + result