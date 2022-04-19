import time
import qrcode
list_kala = []
temp = {}
temp_basket_kala = {}
# counter_faktor = 1000
h = 0
###########################################################

file_counter = open('counter.txt', 'r')
counter_faktor = file_counter.read()
file_counter.close()
counter_faktor = int(counter_faktor) + 1
##################################################################################
def save_file(list_kala, counter_faktor):
    file = open("database.txt", "w")
    str = repr(list_kala)
    file.write(str)
    file.close()
    file = open('counter.txt', 'w')
    str = repr(counter_faktor)
    file.write(str)
    file.close()


def load_file(list, h):
    for i in range(len(list)//4):
        globals()[f"basket_kala{len(list_kala)}"] = {}
        globals()[f"basket_kala{len(list_kala)}"]["id"] = list[h]
        globals()[f"basket_kala{len(list_kala)}"]["name"] = list[h + 1]
        globals()[f"basket_kala{len(list_kala)}"]["price"] = list[h + 2]
        globals()[f"basket_kala{len(list_kala)}"]["mojodi"] = list[h + 3]
        list_kala.append(globals()[f"basket_kala{len(list_kala)}"])
        h += 4
    return

def add_kala():
    while True:
        globals()[f"kala_add{len(list_kala)}"] = {}
        print(list_kala)
        temp_add_kala = input("Please Inter Code Kala for add or return to Menu typed 'menu': ")
        if temp_add_kala == 'menu':
            menu_def()
        for i in range(len(list_kala)):
            if list_kala[i]["id"] == temp_add_kala:
                print("Kala Existing")
                return
        globals()[f"kala_add{len(list_kala)}"]["id"] = temp_add_kala
        globals()[f"kala_add{len(list_kala)}"]["name"] = input("Please Inter Name Kala: ")
        globals()[f"kala_add{len(list_kala)}"]["price"] = int(input("Please Inter Price Kala: "))
        globals()[f"kala_add{len(list_kala)}"]["mojodi"] = int(input("Please Inter Mojodi Kala: "))
        list_kala.append(globals()[f"kala_add{len(list_kala)}"])
        print(list_kala)

    return

def edit_kala():
    while True:
        status_edit = False
        temp_edit_kala = input("Please Inter Code Kala for edit or return to Menu typed 'menu': ")
        if temp_edit_kala == 'menu':
            break
        for i in range(len(list_kala)):
            if list_kala[i]["id"] == temp_edit_kala:
                print(f'Name = {list_kala[i]["name"]}')
                list_kala[i]["name"] = input("Please Inter New Name Kala: ")
                print(f'Price = {list_kala[i]["price"]}')
                list_kala[i]["price"] = int(input("Please Inter New Price Kala: "))
                print(f'Mojodo = {list_kala[i]["mojodi"]}')
                list_kala[i]["mojodi"] = int(input("Please Inter New Mojodi Kala: "))
                status_edit = True
        if status_edit:
            print(f"Editing OK.")
        else:
            print("Not Existing Kala")


def delete_kala():
    while True:
        status_delete = False
        temp_delete_kala = input("Please Inter Code Kala for Delete or return to Menu typed 'menu': ")
        if temp_delete_kala == 'menu':
            break
        for i in range(len(list_kala)):
            if list_kala[i]["id"] == temp_delete_kala:
                print(f'{list_kala[i]["name"]} Deleting')
                list_kala[i]["id"] = ""
                list_kala[i]["name"] = ""
                list_kala[i]["price"] = ""
                list_kala[i]["mojodi"] = ""
                status_delete = True
        if status_delete:
            print(f"Deleting OK.")
        else:
            print("Not Deleting Kala")
        menu_def()


def basket_kala_add(temp_kala_name, price, tedad_sefaresh):

    temp_basket_kala[f"{temp_kala_name}"] = f"{price}"
    temp_basket_kala["temp_tedad_kala"] = f"{tedad_sefaresh}"
    temp_basket_kala["temp_price_kala_name"] = f"{tedad_sefaresh * price}"
    return temp_basket_kala

def search_kala_def():
    list_search = []
    search_kala = input("Please Inter Name Kala or Code Kala For print the last Faktor Inter 'exit' For return to menu Press 'menu': ")
    if search_kala == "exit":
        return list_search, search_kala
    for i in range(len(list_kala)):
        if search_kala in list_kala[i]["id"]:
            list_search.append(list_kala[i]["id"])
            print(f"Kala Name: {list_kala[i]['name']} ** Code Kala: {list_kala[i]['id']}")
        elif search_kala in list_kala[i]["name"]:
            list_search.append(list_kala[i]["id"])
            print(f"Kala Name: {list_kala[i]['name']} ** Code Kala: {list_kala[i]['id']}")
    return list_search, search_kala


def menu_def():
    print("1- Manage Kala")
    print("2- Buy Kala")
    print("3- Stor Kala QR-Code")
    print("4- Save")
    choose_menu_item = int(input("Please Inter Choice Item: "))

    if choose_menu_item == 1:
        print("1- Add Kala ")
        print("2- Edit Kala ")
        print("3- Delete Kala ")
        print("4- Save ")
        print("5- For Return Menu ")
        choose_manage_item = int(input("Please Inter Choice Item: "))


        if choose_manage_item == 1:
            add_kala()
            menu_def()
        if choose_manage_item == 2:
            edit_kala()
            menu_def()
        if choose_manage_item == 3:
            delete_kala()
            menu_def()

        if choose_manage_item == 4:
            save_file(list_kala, counter_faktor)
            menu_def()

        if choose_manage_item == 5:
            menu_def()

    if choose_menu_item == 2:
        buy_kala_test(counter_faktor)
        menu_def()
    if choose_menu_item == 3:
        qrcode_kala()
        menu_def()
    if choose_menu_item == 4:
        save_file(list_kala, counter_faktor)
        menu_def()
def buy_kala_test(counter_faktor):
    while True:
        print("Number Faktor", end="\t")
        number_faktor = f'{time.strftime("%y%m%d", time.localtime())}{counter_faktor}'
        print(number_faktor)
        # list_search = []
        basket_kala = []
        total = 0
        while True:
            globals()[f"dic{counter_faktor}"] = {}
            list_search, search_kala = search_kala_def()
            if search_kala == "menu":
                menu_def()
            if search_kala == "exit": # for print last faktor
                save_file(list_kala, counter_faktor)
                if len(basket_kala) != 0:
                    print(f'Shomare_Faktor: {basket_kala[-1]["number_faktor"]}')
                    for i in range(len(basket_kala)):
                        if basket_kala[i]["number_faktor"] == number_faktor:
                            for key, value in basket_kala[i].items():
                                if key != "number_faktor" and key != "total-faktor":
                                    print(key, ': ', value)
                    print(f'Total_Faktor: {basket_kala[-1]["total-faktor"]}')
                break

            if len(list_search) == 0:
                print("No kala in Shopping")
                continue

            if len(list_search) == 1:
                for i in range(len(list_kala)):
                    if list_search[0] == list_kala[i]["id"]:
                        while True:
                            numbers_kala = int(input(f"Please Inter Numbers {list_kala[i]['name']} = {list_kala[i]['price']} ** meghdar mojod dar anbar  {list_kala[i]['mojodi']}"))
                            if numbers_kala == 0:
                                print("This kala would remove from your basket")
                                break
                            print(list_kala[i]["mojodi"])
                            list_kala[i]["mojodi"] = int(list_kala[i]["mojodi"])
                            list_kala[i]["price"] = int(list_kala[i]["price"])
                            if numbers_kala <= list_kala[i]["mojodi"]:
                                list_kala[i]["mojodi"] -= numbers_kala
                                globals()[f"dic{counter_faktor}"]["number_faktor"] = number_faktor
                                globals()[f"dic{counter_faktor}"][list_kala[i]["name"]] = f'Meghdar = {numbers_kala} adad ** Total Price = {list_kala[i]["price"] * numbers_kala}'
                                total += list_kala[i]["price"] * numbers_kala
                                globals()[f"dic{counter_faktor}"]["total-faktor"] = total
                                basket_kala.append(globals()[f"dic{counter_faktor}"])
                                print(list_kala[i])
                                break
                            if numbers_kala > list_kala[i]["mojodi"]:
                                print(f"maximum selecting of kala: {list_kala[i]['mojodi']}")
                                continue

            list_search.clear()
        if len(basket_kala) != 0:
            counter_faktor += 1

def qrcode_kala():
    flag_qr = False
    while True:
        # status_delete = False
        temp_qr_kala = input("Please Inter Code Kala for Qr-Code or return to Menu typed 'menu': ")
        if temp_qr_kala == 'menu':
            break
        for i in range(len(list_kala)):
            if list_kala[i]["id"] == temp_qr_kala:
                print(f'{list_kala[i]["name"]} Generate')
                img_id = qrcode.make(list_kala[i]["id"])
                img_name = qrcode.make(list_kala[i]["name"])
                a = list_kala[i]["name"]
                img_id.save(f'{a}.png')
                # img_id.save(f'{img_name}/{img_id}.png')
                flag_qr = True
        if flag_qr:
            print("Make QR-Code OK")
        else:
            print("try again")

        menu_def()

############################################################################
f = open('database.txt', 'r')
text = f.readlines()
for line in text:
    line = line.replace("[", '')
    line = line.replace("\n", '')
    line = line.replace("]", '')
    line = line.replace("}", '')
    line = line.replace("{", '')
    line = line.replace("id", '')
    line = line.replace('"', '')
    line = line.replace("'", '')
    line = line.replace(':', '')
    line = line.replace('name', '')
    line = line.replace('price', '')
    line = line.replace('mojodi', '')
    line = line.replace(' ', '')
    list = line.split(",")
    load_file(list, h)
f.close()

while True:
    menu_def()



