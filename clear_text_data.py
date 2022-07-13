# EDA pamages 
import pandas as pd
# Data Viz pakages
import matplotlib.pyplot as plt
import seaborn as sns
#hide earrings 
import warnings
warnings.filterwarnings('ignore')
#load data
df = pd.read_csv("C:\\Users\\haier\\Downloads\\covid19_tweets.csv")
def get_clean_data_column (new_column_name , column_name ):
    df[new_column_name] = df[column_name].apply(nfx.remove_emojis)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_numbers)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_punctuations)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_special_characters)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_multiple_spaces)
    df[new_column_name] = df[new_column_name].apply(nfx.remove_stopwords)
    return df[new_column_name]
result = get_clean_data_column(new_column_name='cleaning_user_name',column_name='user_name')
#df[['user_name','cleaning_user_name']].head(50)