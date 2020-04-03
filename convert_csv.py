from datetime import datetime
import csv

placements = ["Reff", "Scenario", "Type of patient", "Metric name", "22/03/2020", "29/03/2020", "05/04/2020",
              "12/04/2020", "19/04/2020", "26/04/2020", "03/05/2020", "10/05/2020", "17/05/2020", "24/05/2020",
              "31/05/2020", "07/06/2020", "14/06/2020", "21/06/2020", "28/06/2020", "05/07/2020", "12/07/2020",
              "19/07/2020", "26/07/2020", "02/08/2020", "09/08/2020", "16/08/2020", "23/08/2020", "30/08/2020",
              "06/09/2020", "13/09/2020", "20/09/2020", "27/09/2020", "04/10/2020", "11/10/2020", "18/10/2020",
              "25/10/2020", "01/11/2020", "08/11/2020", "15/11/2020", "22/11/2020", "29/11/2020", "06/12/2020",
              "13/12/2020", "20/12/2020", "27/12/2020"]

with open('corona.csv', newline='') as f:
    end_csv_handler = open('end_csv.csv', mode="w+")
    reader = csv.reader(f)
    data = list(reader)
    for list in data:
        labels = f"{placements[0]},{list[0]},{placements[1]},{list[1]},{placements[2]},{list[2]}"
        metric_name = list[3]
        for i in range(4, 45):
            timestamp = datetime.strptime(placements[i], "%d/%m/%Y").timestamp()
            end_csv_handler.write(f"{str(timestamp)[:-2]}000000000,{metric_name},{list[i].replace(',', '')},{labels}\n")
        end_csv_handler.flush()
