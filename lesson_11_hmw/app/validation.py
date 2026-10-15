
def validate_name(name):
    return len(name.strip())>=2
def validate_author(author):
    return len(author.strip())>=2
    
def validate_year(year):
    return int(year)>0 and int(year)<=2026
    