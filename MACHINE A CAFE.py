Menu = {
    "Expresso":{
        "ingredients":{
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    
    "Latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    
    "Capucinno":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.5,  
    }
}

ressources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def verify_input(text: str) -> int:
    data = input(text)
    try:
        data = int(data)
    except:
        data = verify_input(text)
    return data if data >= 0 else verify_input(text)

def update_res (water:int, milk:int, coffe:int, money:int):
    ressources["water"] -= water
    ressources["milk"] -= milk
    ressources["coffee"] -= coffe
    ressources["money"] += money

def servir(name:str) -> str:
    res1 = Menu[name]
    res = Menu[name]["ingredients"]
    if ressources["water"] >= res["water"]:
        if ressources["milk"] >= res["milk"]:
            if ressources["coffee"] >= res["coffee"]:
                print("Insérez des pièces")
                quart = verify_input("\nNombre de quarts : ")
                dixieme = verify_input("\nNombre de dixièmes : ")
                nickel = verify_input("\nNombre de nickels : ")
                centime = verify_input("\nNombre de centimes : ")

                money = (0.25*quart) + (0.1*dixieme) + (0.05*nickel) + (0.01*centime)
                if money == res1["cost"]:
                    update_res(res["water"], res["milk"], res["coffee"], money)
                elif money > res1["cost"]:
                    print(f"\n\nVoici {round(money - res1['cost'], 2)} dollars en monnaie.")
                    update_res(res["water"], res["milk"], res["coffee"], res1["cost"])
                else:
                    return "\n\nDésolé, le montant est insuffisant. Argent remboursé.\n\n"
                return (f"\n\nVoici votre {name}. Bonne dégustation !\n\n")
            else:
                return "\n\nDésolé, il n'y a pas assez de café.\n\n"
        else:
            return "\n\nDésolé, il n'y a pas assez de lait.\n\n"
    else:
        return "\n\nDésolé, il n'y a pas assez d'eau.\n\n"

test = True

while test:
    choice = input("Qu'est-ce que souhaitez avoir ?\n 1. Expresso\n 2. Capucinno\n 3. Latte\n")
    if str(choice) == "rapport":
        print(f"\n Eau : {ressources['water']} ml\n Lait : {ressources['milk']} ml\n Café : {ressources['coffee']} g\n Argent : {ressources['money']} $\n\n")
    elif str(choice) == "off":
        test = False
    elif str(choice).strip() == "1":
        print(servir("Expresso"))
    elif str(choice).strip() == "2":
        print(servir("Capucinno"))
    elif str(choice).strip() == "3":
        print(servir("Latte"))
    else:
        print("\n\nMauvaise entrée\n\n")            