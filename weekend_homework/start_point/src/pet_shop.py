# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    name = pet_shop["name"]
    return name

def get_total_cash(pet_shop):
    sum = pet_shop["admin"]["total_cash"]
    return sum

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    
def get_pets_sold(pet_shop):
    sold = pet_shop["admin"]["pets_sold"]
    return sold

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    
    new_list = []

    for pet in pet_shop["pets"]:

        if pet["breed"] == breed:
            new_list.append(pet)

    return new_list

def find_pet_by_name(pet_shop, name):

    for pet in pet_shop["pets"]:

        if pet["name"] == name:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):

    found_pet = find_pet_by_name(pet_shop, name)

    pet_shop["pets"].remove(found_pet)


def add_pet_to_stock(pet_shop, new_pet):

    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    name = customers["cash"]
    return (name)


def remove_customer_cash(customers, num):
    customers["cash"] -= num

def get_customer_pet_count(customers):
    pets = customers["pets"]
    return len(pets)


def add_pet_to_customer(customers, new_pet):
    return customers["pets"].append(new_pet)


def customer_can_afford_pet(customers, pet_shop):

    afford_pet = False

    if customers["cash"] >= pet_shop["price"]:
        afford_pet = True
    elif  customers["cash"] < pet_shop["price"]:
        afford_pet = False
    return afford_pet

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
