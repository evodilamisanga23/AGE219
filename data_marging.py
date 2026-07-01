import pandas as pd # all pandas libral in order to marge data
data = ["YEAR1.csv","YEAR2.csv","YEAR3.csv","YEAR4.csv","YEAR5.csv","YEAR6.csv","YEAR7.csv","YEAR8.csv","YEAR9.csv","YEAR10.csV" ]
for data in data:
    read_data = pd.read_csv(data)
    merged_data = pd.concat([read_data], ignore_index=True)
    # The data will be in a single csv data used to collect all ten years 
merged_data. to_csv("merged_data.csv",index=False)       