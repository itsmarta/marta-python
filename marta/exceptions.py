class APIKeyError(Exception):
    """Exception thrown for a missing API key"""
    def __init__(self, message=None):

        if not message:
            message = 'API Key is missing. Please set MARTA_API_KEY or use api_key kwarg.'
        super(Exception, self).__init__(message)
