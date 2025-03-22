while True:
    try:
        n = int(input())
        cont = 0
        EPR = 0
        EHD = 0
        intrusos = 0

        while cont<n:
            num, sigla = input().split()
            matricula = int(num)
            if sigla == "EPR":
                EPR+=1
            elif sigla =="EHD":
                EHD+=1
            else:
                intrusos +=1
            cont+=1
        print("EPR: ", EPR)
        print("EHD: ", EHD)
        print("INTRUSOS: ", intrusos)
    except EOFError:
        break
        
