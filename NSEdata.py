#Importing NSE python code
from nsepy import get_history
#Importing datetime packages
from datetime import date, timedelta
days = -30 #Declaring date past 30 day if you want for past 2 month replace 30 by 60
end_date = date.today() #current date
start_date =  end_date + timedelta(days= days) #past 30 days
#Capturing the data of ICICI BANK
data = get_history(symbol="ICICIBANK", start=date(2021,1,1), end=date.today()) 
#We sorted the value in Descending format
data = data.sort_values(by='Date',ascending=False)
print(data)
print(data.columns)
#Stroing the ICICI Bank share data in local machine
data.to_csv("ICICI_BANK_2022.csv")
