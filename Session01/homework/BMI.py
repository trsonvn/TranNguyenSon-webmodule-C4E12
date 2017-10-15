@app.route('/BMI/<int:height>/<int:weight>')
def BMI(height,weight):
    height_cm = float(input("input height(cm): "))
    weight_kg = float(input("input weight(kg): "))
    height_m = height_cm * 0.01
    BMI = weight_kg / (height_m ** 2)

    if BMI < 16:
        print("Severely underweight")
    elif 16 <= BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI < 25:
        print("Normal")
    elif 25 <= BMI <= 30:
        print("Overweight")
    else:
        print("Obese")

    return str(BMI)