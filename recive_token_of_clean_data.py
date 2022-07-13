def get_token (function_name):
    tokens = [token for line in function_name for token in line.split()]
    return tokens 
#result = get_token(get_clean_list('cleaning_user_name'))