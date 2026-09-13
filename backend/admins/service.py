import backend.admins.repository as repository
def load_all_users():
    rows = repository.get_all_users()
    return [{
        "id":row[0],
        "name":row[1],
        "role":row[2]
    }
        for row in rows
    ]