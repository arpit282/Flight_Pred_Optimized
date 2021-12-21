### Hi there 👋, Flight Prediction Optimization
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqDZNbC0GF3ZPQGxOPJEQDwLTVMbAgnLXx9Q&usqp=CAU)



**The previous project on flight prediction has been optimized, by selecting more advanced feature selection techniques.**

- Filter Method
**Variance Threshold**
**Mutual Importance**

### Analysis:

- There are columns 'Airline', 'Date_of_Journey', 'Source', 'Destination', 'Route', 'Dep_Time', 'Arrival_Time', 'Duration', 'Total_Stops', 'Additional_Info', 'Price
- Price is the only Numerical column
- Total 11 columns
- There are 2 NAN values, and they are in same row (Air India) , they are Route and Total stops
- There are total 12 Airlines: ['IndiGo' 'Air India' 'Jet Airways' 'SpiceJet' 'Multiple carriers' 'GoAir' 'Vistara' 'Air Asia' 'Vistara Premium economy' 'Jet Airways Business' 'Multiple carriers Premium economy' 'Trujet']
- There are total 5 Sources: ['Banglore' 'Kolkata' 'Delhi' 'Chennai' 'Mumbai']
- Total 6 Destination: ['New Delhi' 'Banglore' 'Cochin' 'Kolkata' 'Delhi' 'Hyderabad']
- 5 types of stops: ['non-stop' '2 stops' '1 stop' '3 stops' '4 stops']
- Total 10 additional information
- This data is of year 2019
- April has the least no of flights
- June has the most no of flights

### Conclusion:
- R2 Score:  0.7870853276492524
- Mean absolute Score:  865.1498372819618
- Mean Square Score:  3568305.4385348638
- Root Mean Square Error:  1888.995881026442


### How to work on this:
- Clone the repository
- Create an environment
- Activate this environment
- Then use **"python app.py"**
