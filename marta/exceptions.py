class APIKeyError(Exception):
    """Exception thrown for a missing API key"""
    def __init__(self, message: str = None):

        if not message:
            message = 'API Key is missing. Please set MARTA_API_KEY or use api_key kwarg.'
        super(Exception, self).__init__(message)

class InvalidDirectionError(Exception):
    """Exception thrown for an invalid bus/train direction"""
    def __init__(self, direction_provided: str, message: str = None):

        if not message:
            message = f'{direction_provided} is an invalid direction.'
        super(Exception, self).__init__(message)