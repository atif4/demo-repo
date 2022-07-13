def get_clean_list (new_column_name):
    clean_list = df[new_column_name].apply(nfx.remove_stopwords).tolist()
    return clean_list
#result = get_clean_list('cleaning_user_name')