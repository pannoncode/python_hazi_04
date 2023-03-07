from utils.statistic_gen import book_statistic, all_book_statistic


def user_choice():
    choice = input("Választásod: ")
    return choice


exit_loop = False

while not exit_loop:
    print("="*30)
    print("Válassz a lehetőségek között!")
    print("="*30)
    print("-"*60)
    print("-- 1 -- Minden file-hoz készüljön egy statisztika")
    print("-- 2 -- Egyetlen egy file készül, az összes könyvet megvizsgálva")
    print("-- 3 -- Kilépés")
    print("-"*60)

    choice = user_choice()

    if int(choice) == 1:
        try:
            book_statistic()
            print("*"*50)
            print("")
            print("Minden fájlhoz elkészült a statisztika!!!")
            print("")
            print("*"*50)
        except:
            print("!"*50)
            print("")
            print("Hiba a statisztika generálás során")
            print("")
            print("!"*50)
    elif int(choice) == 2:
        try:
            all_book_statistic()
            print("*"*50)
            print("")
            print("Elkészült az egyetlen fájlban lévő statisztika!!!")
            print("")
            print("*"*50)
        except:
            print("!"*50)
            print("")
            print(
                "\"Minden file-hoz készüljön egy statisztika\" -t futtasd le először!!!")
            print("")
            print("!"*50)
    elif int(choice) == 3:
        print("Kiléptél!")
        exit_loop = True
    else:
        print("Hibás vagy nem megfelelő sorszámú választás!")
