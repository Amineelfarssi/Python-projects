# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 08:03:46 2020

@author: amine
"""
from Tracker.tracker import  *



menu = {}
menu0 = {}

menu['1']="Add name" 
menu['2']="Add event"
menu['3']="Event location"
menu['4']="Month name"
menu['5']="Exit"

menu0['1']="Create a new event" 
menu0['2']="Add to an event" 
menu0['3']="Exit"
if __name__ == '__main__':   
    
    from ctypes import windll
    STD_OUTPUT_HANDLE = -11
    stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    # look at the output and select the color you want
    # for instance hex E is yellow on black
    # hex 1E is yellow on blue
    # hex 2E is yellow on green and so on
    
#    for color in range(0, 75):
#         windll.kernel32.SetConsoleTextAttribute(stdout_handle, color)
#         print("%X --> %s" % (color, "Have a fine day!"))
#         input("Press Enter to go on ... ")    
    
    
    
    windll.kernel32.SetConsoleTextAttribute(stdout_handle, 1)
    print('-------------------------------MONTHLY EVENT TRACKER-----------------------------------------')
    windll.kernel32.SetConsoleTextAttribute(stdout_handle, 14)
    print(
"""
Create your own monthly event tracker. Track your weight or an event like Covid 19 over a month. 

Instructions:
Use only letters when entering names.  
Use only numbers for days of the month,1-31, only commas to separate multiple numbers. 
Use only whole numbers for the descriptive number being tracked, no letters or decimals, 
only commas to separate multiple numbers. Tracked numbers = Days entered. 4 days,4numbers. 
Press ENTER after each entry.
"""
)
    windll.kernel32.SetConsoleTextAttribute(stdout_handle, 2)    
    while True: 

        options=menu0.keys()
        options
        print('Thank you for creating a Monthly Event Tracker. Choose from 1,2 or 3: \n' )
        windll.kernel32.SetConsoleTextAttribute(stdout_handle, 7)
        for entry in options: 
          print (entry, menu0[entry])
        print("\n")
        selection=input("Selection: ") 

        if selection =='1': 
            while True:
                try:
                  windll.kernel32.SetConsoleTextAttribute(stdout_handle, 7)  
                  print( 'Please enter information:' )
                  a= Event(control_input("Add your name: ",str),control_input("Add name of event being tracked: ",str),control_input("Add name of event location: ",str),control_input("Add name of Month: ",str),control_input("Add day of Month (1-31) use only commas between numbers: ",list,min_=1,max_=31),control_input("Add number being tracked, use only commas between numbers: ",list),control_input("Add descriptive name for number being tracked, example (pounds, cases, etc.): " ,str))
                  df1=a.generate_data(save=False)
                  Q8=control_input("Enter Y or N to save the information: ",str).lower()
                  if(Q8=='y'):
                      a.generate_data()
                  Q=input("Generate graph [Y/N]?")
                  if Q in ["y","Y"]:
                      a.generate_plot()
                      q1=input("save the figure [Y/N]?")
                      if q1 in ["y","Y"]:
                         plt.savefig(str(datetime.datetime.now())[:16]+".png" )  
                         plt.show()
                         for i in range(101):
                                 progress(i)
                                 time.sleep(0.005)
                         #break
                      else :
                          plt.show()
                          for i in range(101):
                                 progress(i)
                                 time.sleep(0.005)
                          ###############
                  print(a)
                  q4=input("Would you like to enter more days and numbers? [Y,N]?").lower()
                  while(q4=='y'):
                      if q4 in ["y","Y"]:
                          if(Q8=='y'):
                              df1=pd.read_csv(a.filename+'.csv',index_col = False,header=None)
                              d1=control_input("Add day of Month (1-31) use only commas between numbers:  ",list,min_=1,max_=31)
                              d2=control_input("Add number being tracked, use only commas between numbers:   ",list)
                              a.numbers=d2
                              a.days=d1
                              modify_df(df1,d1,d2)
                              Q9=control_input("Enter Y or N to save the information : ",str).lower()
                              if(Q9=='y'):
                                  df1.to_csv(a.filename+'.csv', index=None)
                              #print (df1)
                              Q10=control_input("Enter Y or N to generate graph [Y, N]:  ",str).lower()
                              if(Q10=='y'):
                                  generate_plot(a.location,a.month,a.event,a.num_desc,df1)
                                  plt.show()
                              print(" ")
                              print(
"""
{}\n
The day/days you entered where {}.\n
The {} you entered per day where: {}\n
Your information has been stored and entered on a graph. \n
  """.format(a.name,a.days,a.num_desc,a.numbers)
  )

    
                              q4=input("Would you like to enter more days and numbers? [Y,N]?").lower()
                              print("  ")
                              
                          else:
                              
                              d1=control_input("Add day of Month (1-31) use only commas between numbers:  ",list,min_=1,max_=31)
                              d2=control_input("Add number being tracked, use only commas between numbers:   ",list)
                              a.numbers=d2
                              a.days=d1
                              df1=a.generate_data(save=False)
                              modify_df(df1,d1,d2)
                              Q9=control_input("Enter Y or N to save the information : ",str).lower()
                              if(Q9=='y'):
                                  df1.to_csv(a.filename+'.csv', index=None)
                              #print (df1)
                              Q10=control_input("Enter Y or N to generate graph [Y, N]:  ",str).lower()
                              if(Q10=='y'):
                                  generate_plot(a.location,a.month,a.event,a.num_desc,df1)
                                  plt.show()
                              for i in range(101):
                                 progress(i)
                                 time.sleep(0.005)
                              print(" ")
                              print(
"""
{}\n
The day/days you entered where {}.\n
The {} you entered per day where: {}\n
Your information has been stored and entered on a graph. \n
  """.format(a.name,a.days,a.num_desc,a.numbers)
  )

    
                              q4=input("Would you like to enter more days and numbers? [Y,N]?").lower()
                              print("  ")
                              
                              
                        
                      else:    
                         
                          
                          break
                  break
                              ###########################
                except:
                      print("The number of tracked days and the tracked data must be of the same size please try again !")
                      print(" ")
                      print("save the data if you want to append new data")
                      y=input("Continue [Y/N]?")
                      if y in ["y","Y"]:
                          continue
                      else:
                            break 
            for i in range(101):
                 progress(i)
                 time.sleep(0.005)
            print("\n")
            print(f"Data Saved to  { os.path.join(os.getcwd(),a.filename)}.csv")
            print("")
            windll.kernel32.SetConsoleTextAttribute(stdout_handle, 2)
            print(f"Thank you for creating your MONTHLY EVENT TRACKER. Please remember the EVENT, MONTH, and Name \nyou used in this event tracker,this is needed to open and update your event file. ")
            windll.kernel32.SetConsoleTextAttribute(stdout_handle, 7)
            print('**********************************************************************************************')
             #{ os.path.join(os.getcwd(),a.filename)}.csv .
            generate_plot(a.location,a.month,a.event,a.num_desc,df1)
            plt.show()
            for i in range(101):
                 progress(i)
                 time.sleep(0.005)
            print("\n")
        elif selection == '2': 
            d21=input("Your name :").lower()
            d22=input("Provide the event name ").lower()
            d23=input("Provide the event month ").lower()
            d25=input("Provide the event location ").lower()
            d24=input("Provide the number describer ").lower()
            print(" ")
            ev=a
            eventfile=d21+"_"+d22+"_"+d23 +".csv"
            if (eventfile) in os.listdir():
                print("Past Values (days , numbers) :") 
                df3=pd.read_csv(eventfile,header=None,index_col=None)
                print(df3)
                q6="y"
                while(q6 =='y'):
                      df3=pd.read_csv(eventfile,header=None,index_col=None)
                      dd=control_input("Day or days of the month : ",list,min_=1,max_=31)
                      dn=control_input("Number or numbers that correspond with day of the month, only whole numbers : ",list)
                      modify_df(df3,dd,dn)
                      df3.to_csv(eventfile, index=None)
                      print (df3)
                      q6=input("Do you want to add more data [Y/N]?").lower()
               
                Q5=input("Generate graph [Y/N]?").lower()
                if Q5=='y':
                  generate_plot(d25,d23,d22,d24,df3)
                  q10=input("save the figure [Y/N]?").lower()
                  print(" ")
                  if q10 == "y":
                     plt.savefig(str(datetime.datetime.now())[:16]+".png" )  
                     im=str(datetime.datetime.now())[:16] + ".png"
                     print(f"figure saved to {os.path.join(os.getcwd(), im )}" ) 
                     print(" ")
                     
                  print(f"Data Saved to  { os.path.join(os.getcwd(),eventfile)}")  
                  plt.show()
            else:
                print(f"Data {eventfile} not found in {os.getcwd()} ")
        elif selection == '3': 
             windll.kernel32.SetConsoleTextAttribute(stdout_handle, 1) 
             print("Have a nice day !")
             windll.kernel32.SetConsoleTextAttribute(stdout_handle, 7)
             break
        else: 
          windll.kernel32.SetConsoleTextAttribute(stdout_handle, 7)
          print("Unknown Option Selected!")










