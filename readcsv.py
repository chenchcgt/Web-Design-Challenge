import csv
import pandas as pd

# read file
csvFile = pd.read_csv("Resources/cities.csv") 
  
data = csvFile

# convert to html and save as a file

data.to_html(open('cities_file.html', 'w'))

