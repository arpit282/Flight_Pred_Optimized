from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd
import sklearn

app = Flask(__name__)
model = pickle.load(open("flight_pd.pkl","rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/flightprediction",methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        date_dep = request.form["Dep_Time"]

        Jour_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Jour_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        date_arrival = request.form["Arrival_Time"]

        Arrival_hour = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").minute)

        Dur_hr = abs(Arrival_hour - Dep_hour)
        Dur_min = abs(Arrival_min - Dep_min)

        Total_Stops = int(request.form["Stops"])

        day_night = request.form["dn"]


        weeks = int(request.form["Week"])

        # Airlines
        Airline = request.form["airline"]
        if (Airline == 'IndiGo'):
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0

        elif (Airline == 'Air India'):

            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif (Airline == 'Multiple carriers'):

            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif (Airline == 'SpiceJet'):

            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0

        elif (Airline == 'Vistara'):

            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0

        elif (Airline == 'GoAir'):

            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1


        else:

            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)

        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # ['Total_Stops', 'Month', 'date', 'Week', 'Dep_hr', 'Dep_min', 'Arr_hr',
        #  'Arr_min', 'Dur_hr', 'Dur_min', 'Airline_Air India', 'Airline_GoAir',
        #  'Airline_IndiGo', 'Airline_Multiple carriers', 'Airline_SpiceJet',
        #  'Airline_Vistara', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata',
        #  'Source_Mumbai', 'Destination_Cochin', 'Destination_Hyderabad',
        #  'Destination_Kolkata', 'Destination_New Delhi',
        #  'Day_Night_Night_flight']

        prediction = model.predict([[Total_Stops,Jour_month,Jour_day,weeks,Dep_hour,Dep_min,
                                     Arrival_hour,Arrival_min,Dur_hr,Dur_min,Air_India,
                                     GoAir,IndiGo,Multiple_carriers,SpiceJet,Vistara,
                                     s_Chennai,s_Delhi,s_Kolkata,s_Mumbai,d_Cochin,
                                     d_Hyderabad,d_Kolkata,d_New_Delhi,day_night]])

        Price_Prediction = round(prediction[0], 2)

        return render_template('index.html', pred="Your Fight Price Prediction is ₹ {}".format(Price_Prediction))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

