import re
str="welome.("
# str="welcome@@2To%%python**programming@!!^(^%^"
regex=re.compile('[!@#$%^&*()_}{:?><]')
if(regex.search(str)==None):
    print("No special character present")
else:
    print("sstring contains some sppecial character")
