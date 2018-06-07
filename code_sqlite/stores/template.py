

def dbObject_to_json(store):
    return {
             'id' : store.id,
             'name': store.name,
             'address': store.address,
             'phone': store.phone


    }