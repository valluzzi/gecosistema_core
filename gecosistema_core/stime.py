# -------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2012-2018 Luzzi Valerio 
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#
# Name:        stime.py
# Purpose:
#
# Author:      Luzzi Valerio
#
# Created:     08/08/2018
# -------------------------------------------------------------------------------
from .strings import isstring
import datetime

def now():
    """
    now - shortcut for datetime.datetime.now
    """
    return datetime.datetime.now()

def time_from(t):
    """
    time_from -  return the time (seconds) from time t
    """
    return (datetime.datetime.now()-t).total_seconds()

def checkpoint(t, name = ""):
    """
    checkpoint
    """
    print("Time elapsed from %s: %ss."%(name,time_from(t)))


def strftime(frmt, text):
    """
    strftime
    """
    if not text:
        return datetime.datetime.now()
    elif isinstance(text, (datetime.datetime,datetime.date,) ):
        return text.strftime(frmt)
    elif isstring(text):
        date = datetime.datetime.strptime(text, "%Y-%m-%d")
        return date.strftime(frmt)

    return ""

def month_diff(dateA,dateB):
    """
    month_diff - Month difference
    """
    periodA = strftime("%Y%m",dateA)
    YA, mA = int(periodA[:4]), int(periodA[4:])
    periodB = strftime("%Y%m",dateB)
    YB, mB = int(periodB[:4]), int(periodB[4:])
    return (YA-YB)*12 + (mA-mB)

def firstdayofmonth(date):
    """
    firstdayofmonth
    """
    if isstring(date) and len(date)==6:
        date = datetime.datetime.strptime(date+"01","%Y%m%d").date()
    elif isstring(date) and len(date)==10 and "-" in date:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    date = strftime("%Y-%m-01", date)
    return datetime.datetime.strptime(date,"%Y-%m-%d").date()

def lastdayofmonth(date):
    """
    lastdayofmonth
    """
    date = firstdayofmonth(date)

    for d in (28, 29, 30, 31):
        date1 = datetime.date(date.year, date.month, d)
        if (date1 + datetime.timedelta(days=1)).month != date.month:
            return date1
    return None

def days_of_month(date):
    """
    days_of_month
    """
    return int(strftime("%d", lastdayofmonth(date)))