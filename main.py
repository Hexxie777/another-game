print("""
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     X  Witam w aplikacji firmy ''My tu ten bagno''!  X 
     X            Powoli się rozwijamy!!!             X
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                
        
    """)

print("Masz konto, czy chcesz się zarejstrować?\n1 - Mam konto\n2 - Chcę się zarejstrować")
dec_reg = int(input(">>> "))
if dec_reg == 1:
    import if_acc.exist as exist
if dec_reg == 2:
    import if_acc.doesnt_exist as doesnt_exist