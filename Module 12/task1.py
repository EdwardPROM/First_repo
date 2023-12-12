import pickle

def write_contacts_to_file(filename, contacts):

    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

def read_contacts_from_file(filename):
   
    try:
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
            return contacts
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Повертаю порожній список.")
        return []
