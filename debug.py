from functions import *

cols = ['Low','High','Adj Close','Volume']
month = ['January','February','March','April','May','June','July','August','September','October','November','December']

for i in cols:
    Apple_SpecificYear_OneColumn19(colName=i)
    Apple_SpecificYear_OneColumn20(colName=i)
    Apple_AllYears_OneColumn(colName=i)

Apple_AllYears_AllColumns()
Apple_SpecificYear_AllColumns19()
Apple_SpecificYear_AllColumns20()
# 15
for i in cols:
    Google_SpecificYear_OneColumn19(colName=i)
    Google_SpecificYear_OneColumn20(colName=i)
    Google_AllYears_OneColumn(colName=i)
    
Google_AllYears_AllColumns()
Google_SpecificYear_AllColumns19()
Google_SpecificYear_AllColumns20()
# 15
for i in cols:
    for j in month:
        Apple_SpecificMonth_OneColumn19(colName=i,monthName=j)
        Apple_SpecificMonth_AllColumns19(monthName=j)
        Apple_SpecificMonth_OneColumn20(colName=i,monthName=j)
        Apple_SpecificMonth_AllColumns20(monthName=j)

        Google_SpecificMonth_OneColumn19(colName=i,monthName=j)
        Google_SpecificMonth_AllColumns19(monthName=j)
        Google_SpecificMonth_OneColumn20(colName=i,monthName=j)
        Google_SpecificMonth_AllColumns20(monthName=j)
# 384
for i in cols:
    Apple_HalfYearly_1_OneColumn19(colName=i)
    Apple_HalfYearly_2_OneColumn19(colName=i)
    Apple_HalfYearly_1_OneColumn20(colName=i)
    Apple_HalfYearly_2_OneColumn20(colName=i)

Apple_HalfYearly_1_AllColumns19()
Apple_HalfYearly_2_AllColumns19()
Apple_HalfYearly_1_AllColumns20()
Apple_HalfYearly_2_AllColumns20()
# 20
for i in cols:
    Google_HalfYearly_1_OneColumn19(colName=i)
    Google_HalfYearly_2_OneColumn19(colName=i)
    Google_HalfYearly_1_OneColumn20(colName=i)
    Google_HalfYearly_2_OneColumn20(colName=i)

Google_HalfYearly_1_AllColumns19()
Google_HalfYearly_2_AllColumns19()
Google_HalfYearly_1_AllColumns20()
Google_HalfYearly_2_AllColumns20()
# 20
for i in cols:
    Apple_Quarterly_1_OneColumn19(colName=i)
    Apple_Quarterly_2_OneColumn19(colName=i)
    Apple_Quarterly_3_OneColumn19(colName=i)
    Apple_Quarterly_4_OneColumn19(colName=i)

Apple_Quarterly_1_AllColumns19()
Apple_Quarterly_2_AllColumns19()
Apple_Quarterly_3_AllColumns19()
Apple_Quarterly_4_AllColumns19()
# 20
for i in cols:
    Apple_Quarterly_1_OneColumn20(colName=i)
    Apple_Quarterly_2_OneColumn20(colName=i)
    Apple_Quarterly_3_OneColumn20(colName=i)
    Apple_Quarterly_4_OneColumn20(colName=i)


Apple_Quarterly_1_AllColumns20()
Apple_Quarterly_2_AllColumns20()
Apple_Quarterly_3_AllColumns20()
Apple_Quarterly_4_AllColumns20()
# 20
for i in cols:
    Google_Quarterly_1_OneColumn19(colName=i)
    Google_Quarterly_2_OneColumn19(colName=i)
    Google_Quarterly_3_OneColumn19(colName=i)
    Google_Quarterly_4_OneColumn19(colName=i)


Google_Quarterly_1_AllColumns19()
Google_Quarterly_2_AllColumns19()
Google_Quarterly_3_AllColumns19()
Google_Quarterly_4_AllColumns19()
# 20
for i in cols:
    Google_Quarterly_1_OneColumn20(colName=i)
    Google_Quarterly_2_OneColumn20(colName=i)
    Google_Quarterly_3_OneColumn20(colName=i)
    Google_Quarterly_4_OneColumn20(colName=i)


Google_Quarterly_1_AllColumns20()
Google_Quarterly_2_AllColumns20()
Google_Quarterly_3_AllColumns20()
Google_Quarterly_4_AllColumns20()
# 20