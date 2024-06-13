from utils import custom_exceptions
# import custom_exceptions

class Type:

    @staticmethod
    def IntegerField(data, schema_name): 
        if not isinstance(data, int):
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be an integer, but received {type(data).__name__}.')
        return data 
        
    @staticmethod
    def CharField(data, schema_name, max_length = 100): 
        if not isinstance(data, str):
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be a string, but received {type(data).__name__}.')
        if len(data) > max_length:
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be a {max_length} length string, but received {len(data)} length string.')
        return data 
    
    @staticmethod
    def BooleanField(data, schema_name):
        if not isinstance(data, bool):
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be a boolean, but received {type(data).__name__}.')
        return data

    @staticmethod
    def FloatField(data, schema_name):
        if not isinstance(data, float):
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be a float, but received {type(data).__name__}.')
        return data

    @staticmethod
    def ListField(data, schema_name):
        if not isinstance(data, list):
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be a list, but received {type(data).__name__}.')
        return data

    @staticmethod
    def DictField(data, schema_name):
        if not isinstance(data, dict):
            raise custom_exceptions.CustomError(f'The field "{schema_name}" should be a dictionary, but received {type(data).__name__}.')
        return data