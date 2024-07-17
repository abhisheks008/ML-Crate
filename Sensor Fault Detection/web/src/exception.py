import sys

def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        # `super().__init__(error_message)` is calling the constructor of the parent class of
        # `CustomException`, which is `Exception`. By calling `super().__init__(error_message)`, the
        # `error_message` is passed to the constructor of the `Exception` class, which sets the error
        # message for the custom exception. This allows the custom exception `CustomException` to
        # inherit behavior from the `Exception` class and set the error message when an instance of
        # `CustomException` is created.
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)
        
    def __str__(self):
        """
        This function is used to return a string representation of an object when the `str()` function
        is called on it.
        """
        return self.error_message