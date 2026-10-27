a=int(input("Enter Pay level"))
b=int(input("Enter basic pay"))
c=input("Enter A for Class A city or B for Class B city or C for any other ")
if c not in ["A","B","C"]:
    print("Invalid Input")
elif a<1 or 18<a:
    print("Invalid Input")
elif b<18000 or b>250000:
    print("Invalid Input")
else:
    DA=b*0.63
    HRA=0
    if c=="A":
        HRA=b*0.30
    elif c=="B":
        HRA=b*0.20
    else:
        HRA=b=0.10
    TA=0
    if a>=9 and a<14:
        if c!="A":
            TA=7200+7200*0.63
        else:
            TA=3600+3600*0.63
    elif a>=3 and a<=8:
        if c!="A":
            TA=3600+3600*0.63
        else:
            TA=1800+1800*0.63
    elif a>=1 and a<=2:
        if c!="A":
            TA=3600+3600*0.63
        else:
            TA=1800+1800*0.63
    elif a>=14 and a<=18:
        TA=15750+15750*0.63

    Gross=b+DA+HRA+TA
    NPS=b*0.1
    Net=Gross-NPS
    print(f"BASIC SALARY: {b}")
    print(f"DEARNES ALLOWANCE: {round(DA,2)}")
    print(f"HOUSE RENT ALLOWANCE: {round(HRA,2)}")
    print(f"TRAVELLING ALLOWANCE:{round(TA,2)}")
    print(f"GROSS SALARY:{round(Gross,2)}")
    print(f"NPS DEDUCTION:{round(NPS,2)}")
    print(f"NET SALARY:{round(Net,2)}")




