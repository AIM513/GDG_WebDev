import urllib
class WrongInputError(Exception):
    pass
con=1
dic={}
def url2code():
    global con
    import random as r
    import webbrowser as wb
    import urllib.request as ub
    while True:
        try:
            link=input('Enter the URL that you want to turn into a code: ')
            if not link.startswith('http://www.') and not link.startswith('https://www.') and not link.startswith('http://') and not link.startswith('https://'):
                link='https://www.'+link
            if not link.endswith('.com'):
                link+='.com'
            req=urllib.request.Request(link, method="HEAD")
            urllib.request.urlopen(req, timeout=5)
            break
        except:
            print('Invalid URL. Please enter a valid URL.')
    domain=link.replace('https://','').replace('http://','').replace('www.','').replace('.com','')
    code=''
    cus=1
    for key,value in dic.items():
        if value[0]==link:
            print('The code for the given URL already exits and is:', key)
            cus=0
            break
    global con
    if cus==1:
        
        while True:
            global con
            try:
                global con
                custom=input('Do you want to enter a custom code for the URL? (1 for Yes, 0 for No): ')
                if custom not in ['1','0']:
                    raise WrongInputError() 
                else:
                    global con
                    custom=int(custom)
                    if con==0:
                        print('Thank you for using my GDG Project! Have a great day!')
                    break
            except:
                print('Invalid input. Please enter either 1 or 0.')
        if custom==1:
            while True:
                code=input('Enter the custom code you want to use for the URL: ')
                if code in dic:
                    print('The code you have entered is already in use')
                else:
                    break
            dic[code]=[link,0]
            print(f'The code made for the URL inputed is: {code}')
        else:
            if len(dic)<=26**3*7**3:
                for i in range(3):
                    code+=domain[r.randint(0,len(domain)-1)]
                for i in range(3):
                    code+=str(r.randint(0,6))
                while code in dic:
                    code=''
                    for i in range(3):
                        code+=domain[r.randint(0,len(domain)-1)]
            else:
                for i in range(4):
                    code+=domain[r.randint(0,len(domain)-1)]
                while code in dic:
                    code=''
                    for i in range(4):
                        code+=domain[r.randint(0,len(domain)-1)]
            dic[code]=[link,0]
            print(f' The code generated for the given URL is: {code}')
    while True:  
        try:
            con=input('Do you want to continue with the program? (1 for Yes, 0 for No): ')
            if con not in ['1','0']:
                raise WrongInputError()
            else:
                con=int(con)
                if con==0:
                    print('Thank you for using my GDG Project! Have a great day!')    
                break
        except:
            print('Invalid input. Please enter either 1 or 0.')

def generatedcode():
    if len(dic)==0:
        print('No codes have been generated yet.')
    else:
        print('The list of generated codes are as follows: ')
        for code in dic:
            print(code ,':', dic[code][0], '-', dic[code][1], 'times opened')
        global con
        while True:
                global con
                try:
                    con=input('Do you want to continue with the program? (1 for Yes, 0 for No): ')
                    if con not in ['1','0']:
                        raise WrongInputError()
                    else:
                        con=int(con)
                        break
                except:
                    print('Invalid input. Please enter either 1 or 0.')
def openURL():
    global con
    import webbrowser as wb
    code=input('Enter the code for the URL you want to open: ')
    if code in dic:
        wb.open(dic[code][0])
        dic[code][1]+=1
    else:
        print('The code you entered does not exist.')
        global con
        while True:
                try:
                    con=input('Do you want to continue with the program? (1 for Yes, 0 for No): ')
                    if con not in ['1','0']:
                        raise WrongInputError()
                    else:
                        con=int(con)
                    break
                except:
                    print('Invalid input. Please enter either 1 or 0.')
while con==1:
    while True:
        try:
            select=input('''Welcome to my GDG Project! Please select one of the following options:
            1. Turn a URL into a code
            2. Check all the codes currently generated
            3. Open URL via code
            4. Exit 
            ''')
            select=int(select)
            if select not in [1,2,3,4]:
                raise WrongInputError()
            else:
                break
        except:
            print('Invalid input. Please enter a number between 1 and 4.')

    if select==1:
        url2code()
    elif select==2:
        generatedcode()
    elif select==3:
        openURL()
    elif select==4:
        print('Thank you for using my GDG Project! Have a great day!')
        con=0


        

        