import pyvisa

class IntrumentDiscover():
    def call():
        rm = pyvisa.ResourceManager()
        resources_list = rm.list_resources()
        active_resource_list = []
        for resource in resources_list:
            try:
                visa_resource = rm.open_resource(resource) #  gives you an instance of a subclass of the more generic Resource
                visa_resource.timeout = 1000 #  timeout is set in miliseconds.
                idn = visa_resource.query('*IDN?') # Returns the instruments identity. 
                active_resource_list.append({ "resource" : resource , "idn" : idn })
            except Exception as error:
                pass
        rm.close()
        return active_resource_list

        