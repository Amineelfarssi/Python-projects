from csv import writer,reader
import matplotlib.pyplot as plt
import datetime
import time
import os
import operator
import pandas as pd
import numpy as np
import os
import sys
from itertools import cycle


class Event():
    
    def __init__(self,name : str, event : str ,location : str ,month : str ,days: list, numbers:list,num_desc):
        
        self.name = name.lower()
        self.event = event.lower()
        self.location = location.lower() 
        self.month = month.lower() 
        if len(days) == len(numbers):
            self.days = sorted(days)
            self.numbers = [x for _,x in sorted(zip(days,numbers))]
        else:
            raise ValueError('Invalid numbers')
        self.num_desc = num_desc.lower()
        self.filename= self.name+"_"+self.event + "_"+ self.month
        
    def generate_data(self,save=True):
        V1=np.empty(31)
        V1[:] = np.NaN
        df=pd.DataFrame(data={0:np.linspace(1,31,31), 1:V1},columns=[0,1])
        dic = dict(zip(self.days, self.numbers))
        for i in dic.keys():
            if i in list(df[0]):
                df.loc[df[0]==i, 1]=dic[i]
        if(save):
             df.to_csv(self.filename+'.csv',index=False)
        return df
    
    def generate_plot(self):
        plt.style.use('ggplot')
        self.generate_data(save=False).dropna(axis=0,subset=[1]).plot(x=0,y=1,grid=True,legend=None,marker='o')
        plt.title(f"{self.month} / {self.event} / {self.location} \n MONTHLY EVENT TRACKER \n close graph to continue, press  X")
        plt.xlabel("DAYS OF THE MONTH")
        plt.ylabel(f"{self.num_desc}")
           
    
    def __str__(self):
        return """   
**********************************************************************************************   
                                {}\n
                               {}\n
                        MONTHLY EVENT TRACKER\n
{}\n
The day/days you entered where {}.\n
The {} you entered per day where: {}\n
Your information has been stored and entered on a graph. \n
                      """.format(self.month,self.event,self.name,self.days,self.num_desc,self.numbers)
    
    
  
    
def control_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if (ui=="q!"):
            break
        else:
            if type_ is not None:
                try:
                        if type_==list:
                            pi=[]
                            for i in ui.split(","):
                                try:
                                   pi.append(int(i))
                                except:
                                    continue
                            ui=pi
                        else:
                            ui = type_(ui)
                        #print(ui)
                except ValueError:
                    print("Input type must be {0}.".format(type_.__name__))
                    continue
            if max_ is not None and (  max(ui) > max_  if (type_==list) else  ui>max_ ):
                print("Input must be less than or equal to {0}.".format(max_))
            elif min_ is not None and (min(ui) < min_ if (type_==list) else ui < min_):
                print("Input must be greater than or equal to {0}.".format(min_))
            elif range_ is not None and ui not in range_:
                if isinstance(range_, range):
                    template = "Input must be between {0.start} and {0.stop}."
                    print(template.format(range_))
                else:
                    template = "Input must be {0}."
                    if len(range_) == 1:
                        print(template.format(*range_))
                    else:
                        print(template.format(" or ".join((", ".join(map(str,
                                                                         range_[:-1])),
                                                           str(range_[-1])))))
            else:
                return ui



def modify_df(df,date,numbers):
    if type(date)!="list" and type(numbers)!="list":
        date=list(date)
        numbers=list(numbers)
    dic = dict(zip(date, numbers))
    for i in dic.keys():
        if i in list(df[0]):
            df.loc[df[0]==i, 1]=dic[i]
    return df

def generate_plot(location,month,event,num_desc,df):
    plt.style.use('ggplot')
    df.dropna(axis=0,subset=[1]).plot(x=0,y=1,grid=True,legend=None,marker='o')
    plt.title(f" {month} / {event} / {location} \n MONTHLY EVENT TRACKER \n close graph to continue, press  X")
    plt.xlabel("DAYS OF THE MONTH")
    plt.ylabel(f"{num_desc}")
    
def esc(code):
    return f'\033[{code}m'

class Format:
    end = '\033[0m'
    underline = '\033[4m'


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)