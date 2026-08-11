current_users=['adam','jaine','karl','mises','ulrich']
new_users=['stalin','lenin','Karl','MISES']

for new_user in new_users:

    if new_user.lower() in current_users:
        print("Nome já existente")
    else:
        print("Nome aceito")
