from xl2dict import *

myxlobject= XlToDict()
a = myxlobject.convert_sheet_to_dict(file_path="abc.xls", sheet="First Sheet",
                                 filter_variables_dict={"User Type" : "Admin", "Environment" : "Dev"})
print(myxlobject)