def get_time_date(column_name,new_column_name_year,new_column_name_month,new_column_name_day):
    df[column_name] = pd.to_datetime(df[column_name])#it is in object type to convert into datetime 
    df[new_column_name_year]=df[column_name].dt.year
    df[new_column_name_month]=df[column_name].dt.month
    df[new_column_name_day]=df[column_name].dt.day
#get_time_date(column_name = 'user_created', new_column_name_year = 'years', new_column_name_month = 'months', new_column_name_day = 'days')
#df[['user_created','years','months','days']]