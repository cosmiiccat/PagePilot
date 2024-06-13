from utils import custom_exceptions

class TypeChecker:

    def __init__():
        pass

    def IntegerField(data, schema_name): 
        if type(data) != int: 
            raise custom_exceptions.CustomError(f'Error not int')