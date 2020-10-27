# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.


# # Part A.
def array_2_dict(emails, contacts):
    names = list(contacts.keys())
    for i in range(len(emails)):
        contacts[names[i]] = emails[i]
    return contacts

# # Part B.
def array2d_2_dict(contact_info, contacts):
    contactKeys = list(contacts.keys())
    tmp = []
    key = 0
    for i in contact_info:
        info = {}
        tmp = i
        for x in range(len(i)):
            if (x == 0):
                info["email"] = tmp[x]
            else:
                info["phone"] = tmp[x]
        print(contacts[contactKeys[key]])
        contacts[contactKeys[key]] = info
        key += 1
    return contacts

# # Part C.
def dict_2_array(contacts):
    names = []
    emails = []
    phone = []
    for i in contacts.keys():
        names.append(i)
        emails.append(contacts[i]["email"])
        phone.append(contacts[i]["phone"])
    array = [emails, phone, names]
    return array


