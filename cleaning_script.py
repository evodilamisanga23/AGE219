# allow the pandas library to work in the programme.
import pandas as Pd
# load the merged data
df = Pd.read_csv("merged_data.csv")
# remove duplicated rows
df = df.drop_duplicates()
# remove rows where all values are missing
df = df.dropna(how="all")
# remove leading spaces from column names
df.columns = df.columns.str.strip()
# remove leading spaces from text data
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()
# fill all missing numeric values with 0
numeric_cols = df.select_dtypes(include="number").fillna(0)
# fill all missing text values with "unknown"
text_cols = df.select_dtypes(include="object").columns
df[text_cols] = df[text_cols].fillna("unknown")
# save cleaned data
df.to_csv("cleaned_sales.csv", index=False)
print("data cleaning completed successfullyl")