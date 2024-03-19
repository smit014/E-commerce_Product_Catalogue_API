
def serializer_for_getuser(users_data):
    if not isinstance(users_data, list):
        users_data = [users_data]
    filter_data=[]
    
    for record in users_data:
        filter_data.append(
            {
                "fname":record.first_name,
                "lname" :record.last_name,
                "name":record.name,
                "phone_no " :record.phone_no,
                "active":record.is_active,
                "admin":record.is_admin, 
            }
        )
    return filter_data


def serializer_for_login(users_data):
    if not isinstance(users_data, list):
        users_data = [users_data]
    users_data = users_data[0]
    filter_data={   
                "id":users_data.id,
                "name":users_data.name,
                "email " :users_data.email,
                "phone_no":users_data.phone_no,
                "is_admin " :users_data.is_admin,
            }
    return filter_data
