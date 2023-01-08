# TripAdvisor-Analyser
Create an excel file with Restaurant datas from TripAdvisor. Name, link, stars and reviews. Download all review of a city.
Requirements:

Python 3

Install requirements:

pip3 install -r requirements.txt

Commands:

python3 "AnalisiTripAdvisorITA.py"  

It will ask you for link of city like that:
https://www.tripadvisor.it/Restourants-g1933367-Mondaino_Province_of_Rimini_Emilia_Romagna-Vacations.html

It will create a new file excel called "risultatiITA.xlsx" with datas of all restaurants.

After that you can download all reviews from that city with command:

python3 "OttieniRecensioniITA.py"

Remember that this last operation is very slow and can take long time, it depends on number of reviews.

At the end it will create a file called recensioniIT.txt where are saved all reviews of the city.

Same for ENG