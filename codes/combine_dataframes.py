import pandas as pd

# List to store individual DataFrames
dataframes_list = []

# Loop through each file and read it into a DataFrame
for page_num in range(1, 193):
    file_path = f'../data/crawled_heho_myths/heho_page{page_num}.txt'
    df = pd.read_csv(file_path, sep='\t')
    dataframes_list.append(df)

# Concatenate all DataFrames into one large DataFrame
combined_dataframe = pd.concat(dataframes_list, ignore_index=True)
print(combined_dataframe)


# Save combined_dataframe to a TSV file
output_file_path = '../data/combined_dataframe.tsv'
combined_dataframe.to_csv(output_file_path, sep='\t', index=False)  # Set index=False to exclude the DataFrame's index from the file
