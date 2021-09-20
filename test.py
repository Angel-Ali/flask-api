me = {
    "name": angel
}

# print (type(me))
# print (type(fido))




# print_data()

def test_list():
    print("working with lists")
    names = []

    names.append("Sergio")
    names.append("Angel")
    names.append("Andrew")

    print(names)


    # get the elements
    print(names[0])

for name in names:
    print(names[1:2])


#test_list()

def product_search(id):
    print("search a product in the catalog")

    found = False
    for prod in mock_data:
        if prod["_id"] == id:
            found = True
            print(prod)
            return prod


    if not found:
        print("Error: product not found")
        return None



    product_search("osdfsdasdgf")
    product_search("123")