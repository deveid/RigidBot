import time
print('Hello! Welcome to Pizza Hut')
print('Its ',time.asctime())
print('What kind of pizza would you like? Veg or Non-Veg')
ptype=['veg','non-veg']
Veg=['margherita',
     'double-cheese-margherita',
     'farm-house',
     'deluxe-veggie',
     'peppy-panner']
Non_veg=['chicken-tikka',
         'chicken-fiesta',
         'peri-peri-chicken',
         'cheese-pepperoni',]
size=['large','medium','small']
custom=['Crust','Toppings', 'Cheese']
time=['ASAP 30 mins','1 hour','1.5 hour','2 hours','3 hours']

def pizzatype():
    res1=input('')
    res1=res1.lower()
    if res1 in ptype:
            print('What kind of ',res1,'pizza do you want?')
            if res1=='veg':
                for x in Veg:
                    print('-',x)
                ch1=input('')
                if ch1 in Veg:
                    print('Good Choice!That is my favourite too')
                else:
                    print('Incorrect words')
                    pizzatype()
            elif res1=='non-veg':
                for x in Non_veg:
                    print('-',x)
                ch1=input('')
                if ch1 in Non_veg:
                     print('Good Choice! That is my favourite too')
                else:
                    print('Incorrect words')
                    pizzatype()
                return ch1
    elif(res1 not in ptype):
        print('Invalid Option')
        print('Input right option')
        pizzatype()
def sizes():
    print('How Large?')
    for x in size:
        print('-',x)
    ch2=input('')
    if ch2==x:
         print('Okay')
    elif ch2!=x:
        print('Unavailable Size')
    return ch2
def customs():
    print('Do you want to customise your pizza? yes or no')
    ch3=input('')
    ch3=ch3.lower()
    if ch3=='yes':
        print('Choose')
        for x in custom:
            print('-',x)
        custom1=input()
    if ch3=='no':
        print('Okay')
    return ch3
        
def howmany():
    print('How many do you want')
    ch4=input('')
    print('Do you want to add more pizza to your order? yes or no')
    ch5=input('')
    ch5=ch5.lower()
    if ch5=='yes':
        print('How many do you want to add')
        ch6=input('')
        print('Got it')
    if ch5=='no':
            print('Got it')
    return ch4,ch5
            
def info():
    print('Let me take your info')
    print('Your Name:')
    name=input('')
    print('Your Mobile Number:')
    number=input('')
    print('Finally your delivery address:')
    address=input('')
    return name,number,address
    
def ordertime():
    print('When do you want it?')
    for x in time:
        print('-',x)
    time1=input('')
    if time1 in time:
        print('Your order is placed')
        print("You'll soon get a call for confrimation")
    else:
        print('Wrong input')
        print('Use the available options above')
        ordertime()
    return time1
        
pizzatype=pizzatype()
sizes=sizes()
customs=customs()
howmany=howmany()
info=info()
ordertime=ordertime()
wait()

