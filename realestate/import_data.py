import pandas as pd
from listings.models import Property

# Load the dataset
df = pd.read_csv('realestate.csv')

# Iterate through the dataset and create Property objects
for _, row in df.iterrows():
    Property.objects.create(
        location=row['location'],
        size=row['size(bhk)'],
        area_sqft=row['total_sqft'],
        bath=row['bath'],
        balcony=row['balcony'],
        price=row['price']
    )
