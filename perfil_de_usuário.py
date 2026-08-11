def build_profile(first,last,**user_info):
    user_info['first name']=first
    user_info['last name']=last
    return user_info

user_profile=build_profile('klaus','augusto', location='campinas', hair='wavy')

print(user_profile)