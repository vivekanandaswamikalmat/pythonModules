class ViveksCal():
    dayName = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    startm = []
    monthName = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    #function to check leap year
    def leap(self,y):
        return y%400==0 or y%4==0 and y%100!=0

    #function to get the starting day of the year

    def starty(self,y):
        x=0
        ans=y%400
        if ans==0:
            return 6

        leaps = (ans-1)//4

        if ans>300:
            leaps-=3
        elif ans>200:
            leaps-=2
        elif ans>100:
            leaps-=1

        nonleaps = ans-leaps
        num = (nonleaps+(2*leaps))%7

        return num

    #funtion to get the number of days in a month of a given year

    def days(self,m,y):
        if m == 2:
            if self.leap(y):
                return 29
            else:
                return 28
        elif m in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30

    #fuction to get the start day of the month
    def startmonth(self,m,y): 
        startm = [self.starty(y)]
        #computing starting days of the months and storing in a list
        for i in range(1,12):
            startm.insert(i,((startm[i-1]+self.days(i,y))%7))
        return startm[m-1]


    #function to display the calendar of a month
    def display(self,m,y):
        col,row,count,wspace=0,0,0,' '
        print('     ',self.monthName[m-1],y)
        print('Su','Mo','Tu','We','Th','Fr','Sa')
        while row<=5:
            for col in range(0,7):
                if (col < self.startmonth(m,y)) and row==0:
                    print('  ',end=' ')
                else:
                    count+=1
                    if(count>self.days(m,y)):
                        break;  
                    if count<10:
                        print(' ',count,end=' ',sep='')
                    else:
                        print(count,end=' ')
            print(end='\n')
            row+=1

ob = ViveksCal()

#function to display the month            
def month(month,year):    
    #list of month names to display   
    ob.display(month,year)
    

#function to display the complete year
def year(y):
    for i in range(0,12):
        print('\n')
        ob.display(i+1,y)
        
#function to get the day of the given date
def day(d,m,y):
    s = ob.startmonth(m,y)
    print(ob.dayName[(s+d)%7-1])