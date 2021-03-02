import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# Year based Functions
# Apple
def Apple_SpecificYear_OneColumn19(colName):
    apple = pd.read_csv('./2019/AAPL.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_SpecificYear_AllColumns19():
    apple = pd.read_csv('./2019/AAPL.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_SpecificYear_OneColumn20(colName):
    apple = pd.read_csv('./2020/AAPL.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_SpecificYear_AllColumns20():
    apple = pd.read_csv('./2020/AAPL.csv')
    
    # All Columns for Specific Year
    plot.plot(apple[['Low','High','Adj Close']], apple['Date'])
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_AllYears_OneColumn(colName):
    apple = pd.read_csv('./Combined/AAPL.csv')

    plot.plot(apple[colName], apple['Date'])
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_AllYears_AllColumns():
    apple = pd.read_csv('./Combined/AAPL.csv')

    plot.plot(apple[['Low','High','Adj Close']], apple['Date'])
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

# Google
def Google_SpecificYear_OneColumn19(colName):
    google = pd.read_csv('./2019/GOOG.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_SpecificYear_AllColumns19():
    google = pd.read_csv('./2019/GOOG.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_SpecificYear_OneColumn20(colName):
    google = pd.read_csv('./2020/GOOG.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_SpecificYear_AllColumns20():
    google = pd.read_csv('./2020/GOOG.csv')
    
    # All Columns for Specific Year
    plot.plot(google[['Low','High','Adj Close']], google['Date'])
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_AllYears_OneColumn(colName):
    google = pd.read_csv('./Combined/GOOG.csv')

    plot.plot(google[colName], google['Date'])
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_AllYears_AllColumns():
    google = pd.read_csv('./Combined/GOOG.csv')

    plot.plot(google[['Low','High','Adj Close']], google['Date'])
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()


# Month based Functions
# Apple
def Apple_SpecificMonth_OneColumn20(monthName, colName):
    if monthName == 'January':
        apple = pd.read_csv('./2020/Months/appleJan.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2020/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2020/Months/appleMar.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2020/Months/appleApr.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2020/Months/appleMay.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2020/Months/appleJun.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2020/Months/appleJul.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2020/Months/appleAug.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2020/Months/appleSep.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2020/Months/appleOct.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2020/Months/appleNov.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2020/Months/appleDec.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    
def Apple_SpecificMonth_AllColumns20(monthName):
    if monthName == 'January':
        apple = pd.read_csv('./2020/Months/appleJan.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2020/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2020/Months/appleMar.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2020/Months/appleApr.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2020/Months/appleMay.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2020/Months/appleJun.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2020/Months/appleJul.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2020/Months/appleAug.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2020/Months/appleSep.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2020/Months/appleOct.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2020/Months/appleNov.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2020/Months/appleDec.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()

def Apple_SpecificMonth_OneColumn19(monthName, colName):
    if monthName == 'January':
        apple = pd.read_csv('./2019/Months/appleJan.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2019/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2019/Months/appleMar.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2019/Months/appleApr.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2019/Months/appleMay.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2019/Months/appleJun.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2019/Months/appleJul.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2019/Months/appleAug.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2019/Months/appleSep.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2019/Months/appleOct.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2019/Months/appleNov.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2019/Months/appleDec.csv')
        # Specific Column for Specific Year
        plt = apple[colName]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    
def Apple_SpecificMonth_AllColumns19(monthName):
    if monthName == 'January':
        apple = pd.read_csv('./2019/Months/appleJan.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2019/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2019/Months/appleMar.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2019/Months/appleApr.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2019/Months/appleMay.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2019/Months/appleJun.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2019/Months/appleJul.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2019/Months/appleAug.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2019/Months/appleSep.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2019/Months/appleOct.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2019/Months/appleNov.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2019/Months/appleDec.csv')
        # Specific Column for Specific Year
        plt = apple[['Low','High','Adj Close']]
        date = apple['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()

# Google
def Google_SpecificMonth_OneColumn20(monthName, colName):
    if monthName == 'January':
        google = pd.read_csv('./2020/Months/googleJan.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'February':
        google = pd.read_csv('./2020/Months/googleFeb.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'March':
        google = pd.read_csv('./2020/Months/googleMar.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'April':
        google = pd.read_csv('./2020/Months/googleApr.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'May':
        google = pd.read_csv('./2020/Months/googleMay.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'June':
        google = pd.read_csv('./2020/Months/googleJun.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'July':
        google = pd.read_csv('./2020/Months/googleJul.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'August':
        google = pd.read_csv('./2020/Months/googleAug.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'September':
        google = pd.read_csv('./2020/Months/googleSep.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'October':
        google = pd.read_csv('./2020/Months/googleOct.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'November':
        google = pd.read_csv('./2020/Months/googleNov.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'December':
        google = pd.read_csv('./2020/Months/googleDec.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    
def Google_SpecificMonth_AllColumns20(monthName):
    if monthName == 'January':
        google = pd.read_csv('./2020/Months/googleJan.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'February':
        google = pd.read_csv('./2020/Months/googleFeb.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'March':
        google = pd.read_csv('./2020/Months/googleMar.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'April':
        google = pd.read_csv('./2020/Months/googleApr.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'May':
        google = pd.read_csv('./2020/Months/googleMay.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'June':
        google = pd.read_csv('./2020/Months/googleJun.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'July':
        google = pd.read_csv('./2020/Months/googleJul.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'August':
        google = pd.read_csv('./2020/Months/googleAug.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'September':
        google = pd.read_csv('./2020/Months/googleSep.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'October':
        google = pd.read_csv('./2020/Months/googleOct.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'November':
        google = pd.read_csv('./2020/Months/googleNov.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'December':
        google = pd.read_csv('./2020/Months/googleDec.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()

def Google_SpecificMonth_OneColumn19(monthName, colName):
    if monthName == 'January':
        google = pd.read_csv('./2019/Months/googleJan.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'February':
        google = pd.read_csv('./2019/Months/googleFeb.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'March':
        google = pd.read_csv('./2019/Months/googleMar.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'April':
        google = pd.read_csv('./2019/Months/googleApr.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'May':
        google = pd.read_csv('./2019/Months/googleMay.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'June':
        google = pd.read_csv('./2019/Months/googleJun.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'July':
        google = pd.read_csv('./2019/Months/googleJul.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'August':
        google = pd.read_csv('./2019/Months/googleAug.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'September':
        google = pd.read_csv('./2019/Months/googleSep.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'October':
        google = pd.read_csv('./2019/Months/googleOct.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'November':
        google = pd.read_csv('./2019/Months/googleNov.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    if monthName == 'December':
        google = pd.read_csv('./2019/Months/googleDec.csv')
        # Specific Column for Specific Year
        plt = google[colName]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(colName)
        plot.show()
    
def Google_SpecificMonth_AllColumns19(monthName):
    if monthName == 'January':
        google = pd.read_csv('./2019/Months/googleJan.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'February':
        google = pd.read_csv('./2019/Months/googleFeb.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'March':
        google = pd.read_csv('./2019/Months/googleMar.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'April':
        google = pd.read_csv('./2019/Months/googleApr.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'May':
        google = pd.read_csv('./2019/Months/googleMay.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'June':
        google = pd.read_csv('./2019/Months/googleJun.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'July':
        google = pd.read_csv('./2019/Months/googleJul.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'August':
        google = pd.read_csv('./2019/Months/googleAug.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'September':
        google = pd.read_csv('./2019/Months/googleSep.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'October':
        google = pd.read_csv('./2019/Months/googleOct.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'November':
        google = pd.read_csv('./2019/Months/googleNov.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()
    if monthName == 'December':
        google = pd.read_csv('./2019/Months/googleDec.csv')
        # Specific Column for Specific Year
        plt = google[['Low','High','Adj Close']]
        date = google['Date']
        plot.plot(plt, date)
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.legend(['Low','High','Adj Close'])
        plot.show()


# Date based Functions
def Apple_SpecificDate_AllDates20(monthName):
    if monthName == 'January':
        apple = pd.read_csv('./2020/Months/appleJan.csv')
        print(apple['Date'])
    if monthName == 'February':
        apple = pd.read_csv('./2020/Months/appleFeb.csv')
        print(apple['Date'])
    if monthName == 'March':
        apple = pd.read_csv('./2020/Months/appleMar.csv')
        print(apple['Date'])
    if monthName == 'April':
        apple = pd.read_csv('./2020/Months/appleApr.csv')
        print(apple['Date'])
    if monthName == 'May':
        apple = pd.read_csv('./2020/Months/appleMay.csv')
        print(apple['Date'])
    if monthName == 'June':
        apple = pd.read_csv('./2020/Months/appleJun.csv')
        print(apple['Date'])
    if monthName == 'July':
        apple = pd.read_csv('./2020/Months/appleJul.csv')
        print(apple['Date'])
    if monthName == 'August':
        apple = pd.read_csv('./2020/Months/appleAug.csv')
        print(apple['Date'])
    if monthName == 'September':
        apple = pd.read_csv('./2020/Months/appleSep.csv')
        print(apple['Date'])
    if monthName == 'October':
        apple = pd.read_csv('./2020/Months/appleOct.csv')
        print(apple['Date'])
    if monthName == 'November':
        apple = pd.read_csv('./2020/Months/appleNov.csv')
        print(apple['Date'])
    if monthName == 'December':
        apple = pd.read_csv('./2020/Months/appleDec.csv')
        print(apple['Date'])
    
def Apple_SpecificDate_OneColumn20(monthName, specificDate, colName):
    if monthName == 'January':
        apple = pd.read_csv('./2020/Months/appleJan.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2020/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2020/Months/appleMar.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2020/Months/appleApr.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2020/Months/appleMay.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2020/Months/appleJun.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2020/Months/appleJul.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2020/Months/appleAug.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2020/Months/appleSep.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2020/Months/appleOct.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2020/Months/appleNov.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2020/Months/appleDec.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()

def Apple_SpecificDate_AllColumns20(monthName, specificDate):
    if monthName == 'January':
        apple = pd.read_csv('./2020/Months/appleJan.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2020/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2020/Months/appleMar.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2020/Months/appleApr.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2020/Months/appleMay.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2020/Months/appleJun.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2020/Months/appleJul.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2020/Months/appleAug.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2020/Months/appleSep.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2020/Months/appleOct.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2020/Months/appleNov.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2020/Months/appleDec.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()


def Apple_SpecificDate_AllDates19(monthName):
    if monthName == 'January':
        apple = pd.read_csv('./2019/Months/appleJan.csv')
        print(apple['Date'])
    if monthName == 'February':
        apple = pd.read_csv('./2019/Months/appleFeb.csv')
        print(apple['Date'])
    if monthName == 'March':
        apple = pd.read_csv('./2019/Months/appleMar.csv')
        print(apple['Date'])
    if monthName == 'April':
        apple = pd.read_csv('./2019/Months/appleApr.csv')
        print(apple['Date'])
    if monthName == 'May':
        apple = pd.read_csv('./2019/Months/appleMay.csv')
        print(apple['Date'])
    if monthName == 'June':
        apple = pd.read_csv('./2019/Months/appleJun.csv')
        print(apple['Date'])
    if monthName == 'July':
        apple = pd.read_csv('./2019/Months/appleJul.csv')
        print(apple['Date'])
    if monthName == 'August':
        apple = pd.read_csv('./2019/Months/appleAug.csv')
        print(apple['Date'])
    if monthName == 'September':
        apple = pd.read_csv('./2019/Months/appleSep.csv')
        print(apple['Date'])
    if monthName == 'October':
        apple = pd.read_csv('./2019/Months/appleOct.csv')
        print(apple['Date'])
    if monthName == 'November':
        apple = pd.read_csv('./2019/Months/appleNov.csv')
        print(apple['Date'])
    if monthName == 'December':
        apple = pd.read_csv('./2019/Months/appleDec.csv')
        print(apple['Date'])
    
def Apple_SpecificDate_OneColumn19(monthName, specificDate, colName):
    if monthName == 'January':
        apple = pd.read_csv('./2019/Months/appleJan.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2019/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2019/Months/appleMar.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2019/Months/appleApr.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2019/Months/appleMay.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2019/Months/appleJun.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2019/Months/appleJul.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2019/Months/appleAug.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2019/Months/appleSep.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2019/Months/appleOct.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2019/Months/appleNov.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2019/Months/appleDec.csv')
        # Specific Column for Specific Year
        plot.plot(apple[colName], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()

def Apple_SpecificDate_AllColumns19(monthName, specificDate):
    if monthName == 'January':
        apple = pd.read_csv('./2019/Months/appleJan.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'February':
        apple = pd.read_csv('./2019/Months/appleFeb.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'March':
        apple = pd.read_csv('./2019/Months/appleMar.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'April':
        apple = pd.read_csv('./2019/Months/appleApr.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'May':
        apple = pd.read_csv('./2019/Months/appleMay.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'June':
        apple = pd.read_csv('./2019/Months/appleJun.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'July':
        apple = pd.read_csv('./2019/Months/appleJul.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'August':
        apple = pd.read_csv('./2019/Months/appleAug.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'September':
        apple = pd.read_csv('./2019/Months/appleSep.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'October':
        apple = pd.read_csv('./2019/Months/appleOct.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'November':
        apple = pd.read_csv('./2019/Months/appleNov.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()
    if monthName == 'December':
        apple = pd.read_csv('./2019/Months/appleDec.csv')
        # Specific Column for Specific Year
        plot.plot(apple[['Low', 'High', 'Adj Close']], apple[specificDate])
        plot.tight_layout()
        plot.xticks(rotation=270)
        plot.show()

# Half Yearly based Functions
# Apple
def Apple_HalfYearly_1_OneColumn19(colName):
    apple = pd.read_csv('./2019/HalfYearly/AAPL_H1.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_HalfYearly_2_OneColumn19(colName):
    apple = pd.read_csv('./2019/HalfYearly/AAPL_H2.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_HalfYearly_1_AllColumns19():
    apple = pd.read_csv('./2019/HalfYearly/AAPL_H1.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_HalfYearly_2_AllColumns19():
    apple = pd.read_csv('./2019/HalfYearly/AAPL_H2.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_HalfYearly_1_OneColumn20(colName):
    apple = pd.read_csv('./2020/HalfYearly/AAPL_H1.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_HalfYearly_2_OneColumn20(colName):
    apple = pd.read_csv('./2020/HalfYearly/AAPL_H2.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_HalfYearly_1_AllColumns20():
    apple = pd.read_csv('./2020/HalfYearly/AAPL_H1.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_HalfYearly_2_AllColumns20():
    apple = pd.read_csv('./2020/HalfYearly/AAPL_H2.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

# Google
def Google_HalfYearly_1_OneColumn19(colName):
    google = pd.read_csv('./2019/HalfYearly/GOOG_H1.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_HalfYearly_2_OneColumn19(colName):
    google = pd.read_csv('./2019/HalfYearly/GOOG_H2.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_HalfYearly_1_AllColumns19():
    google = pd.read_csv('./2019/HalfYearly/GOOG_H1.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_HalfYearly_2_AllColumns19():
    google = pd.read_csv('./2019/HalfYearly/GOOG_H2.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_HalfYearly_1_OneColumn20(colName):
    google = pd.read_csv('./2020/HalfYearly/GOOG_H1.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_HalfYearly_2_OneColumn20(colName):
    google = pd.read_csv('./2020/HalfYearly/GOOG_H2.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_HalfYearly_1_AllColumns20():
    google = pd.read_csv('./2020/HalfYearly/GOOG_H1.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_HalfYearly_2_AllColumns20():
    google = pd.read_csv('./2020/HalfYearly/GOOG_H2.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()


# Quarterly based Functions
# Apple
def Apple_Quarterly_1_OneColumn19(colName):
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q1.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_Quarterly_2_OneColumn19(colName):
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q2.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_Quarterly_3_OneColumn19(colName):
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q3.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_Quarterly_4_OneColumn19(colName):
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q4.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()


def Apple_Quarterly_1_AllColumns19():
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q1.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_Quarterly_2_AllColumns19():
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q2.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_Quarterly_3_AllColumns19():
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q3.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_Quarterly_4_AllColumns19():
    apple = pd.read_csv('./2019/Quarterly/AAPL_Q4.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()


def Apple_Quarterly_1_OneColumn20(colName):
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q1.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_Quarterly_2_OneColumn20(colName):
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q2.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_Quarterly_3_OneColumn20(colName):
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q3.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Apple_Quarterly_4_OneColumn20(colName):
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q4.csv')

    # Specific Column for Specific Year
    plt = apple[colName]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()


def Apple_Quarterly_1_AllColumns20():
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q1.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_Quarterly_2_AllColumns20():
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q2.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_Quarterly_3_AllColumns20():
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q3.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Apple_Quarterly_4_AllColumns20():
    apple = pd.read_csv('./2020/Quarterly/AAPL_Q4.csv')
    
    # All Columns for Specific Year
    plt = apple[['Low','High','Adj Close']]
    date = apple['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()


# Google
def Google_Quarterly_1_OneColumn19(colName):
    google = pd.read_csv('./2019/Quarterly/GOOG_Q1.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_Quarterly_2_OneColumn19(colName):
    google = pd.read_csv('./2019/Quarterly/GOOG_Q2.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_Quarterly_3_OneColumn19(colName):
    google = pd.read_csv('./2019/Quarterly/GOOG_Q3.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_Quarterly_4_OneColumn19(colName):
    google = pd.read_csv('./2019/Quarterly/GOOG_Q4.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()


def Google_Quarterly_1_AllColumns19():
    google = pd.read_csv('./2019/Quarterly/GOOG_Q1.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_Quarterly_2_AllColumns19():
    google = pd.read_csv('./2019/Quarterly/GOOG_Q2.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_Quarterly_3_AllColumns19():
    google = pd.read_csv('./2019/Quarterly/GOOG_Q3.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_Quarterly_4_AllColumns19():
    google = pd.read_csv('./2019/Quarterly/GOOG_Q4.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()


def Google_Quarterly_1_OneColumn20(colName):
    google = pd.read_csv('./2020/Quarterly/GOOG_Q1.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_Quarterly_2_OneColumn20(colName):
    google = pd.read_csv('./2020/Quarterly/GOOG_Q2.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_Quarterly_3_OneColumn20(colName):
    google = pd.read_csv('./2020/Quarterly/GOOG_Q3.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()

def Google_Quarterly_4_OneColumn20(colName):
    google = pd.read_csv('./2020/Quarterly/GOOG_Q4.csv')

    # Specific Column for Specific Year
    plt = google[colName]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(colName)
    plot.show()


def Google_Quarterly_1_AllColumns20():
    google = pd.read_csv('./2020/Quarterly/GOOG_Q1.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_Quarterly_2_AllColumns20():
    google = pd.read_csv('./2020/Quarterly/GOOG_Q2.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_Quarterly_3_AllColumns20():
    google = pd.read_csv('./2020/Quarterly/GOOG_Q3.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

def Google_Quarterly_4_AllColumns20():
    google = pd.read_csv('./2020/Quarterly/GOOG_Q4.csv')
    
    # All Columns for Specific Year
    plt = google[['Low','High','Adj Close']]
    date = google['Date']
    plot.plot(plt, date)
    plot.tight_layout()
    plot.xticks(rotation=90)
    plot.legend(['Low','High','Adj Close'])
    plot.show()

