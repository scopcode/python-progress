def build_profile(first, last, **userinfo):
    profile = {}
    profile['First name'] = first
    profile['Last name'] = last
    for key,value in userinfo.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstien', 
                             location = "princeton", field = "physics")
print(user_profile)

my_profile = build_profile('shubham', 'choubey', 
                           location = "durg", country = "India", Job = "Cop")
print(my_profile)