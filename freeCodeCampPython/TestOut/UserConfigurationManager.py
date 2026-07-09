def add_setting(settings,pair_to_add):
    key, value = pair_to_add                                                               #convert key and value to lowercase
    key = key.lower()
    value = value.lower() 
    if pair_to_add in settings.items() or key in settings:                                 #decline to add if already in dictionary
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    elif not (pair_to_add in settings.items()):                                            #add if it wasn't there before
        settings[key] = value
        print(settings)
        return f"Setting '{key}' added with value '{value}' successfully!" 
    else: 
        print("something went wrong when adding a setting")


def update_setting(settings,pair_to_change):
    key, value = pair_to_change     #convert key and value to lowercase
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value 
        return f"Setting '{key}' updated to '{value}' successfully!"
    elif not key in settings.items():
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting." 
    else:
        print("something went wrong when updating a setting")
      
def delete_setting(settings,key):
    #Convert the key passed to lowercase.
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    elif not key in settings: 
        return "Setting not found!"
    else:
      print("something went wrong when deleting a setting")
      
def view_settings(settings):
    if not settings:
        return "No settings available."    
    elif settings:
        returnriff = ""
        for key,value in settings.items():
            key = key.capitalize()
            returnriff += f"{key}: {value}\n"
        return (
        f"Current User Settings:\n{returnriff}"
        )
    else:  
        print("something went wrong when viewing settings")


test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}


print(add_setting({'theme': 'light'}, ('THEME', 'dark'))) #6
print(add_setting({'theme': 'light'}, ('volume', 'high'))) #7 
print(update_setting({'theme': 'light'}, ('theme', 'dark'))) #13
print(update_setting({'theme': 'light'}, ('volume', 'high')))#14
print(delete_setting({'theme': 'light'}, 'theme')) # 19
print(delete_setting({'theme': 'light'}, 'opit')) #20
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
