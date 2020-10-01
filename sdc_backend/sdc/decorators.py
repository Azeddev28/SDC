#from logging import getLogger, info
from json import dumps

from functools import wraps
from datetime import datetime

from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response



#def store_log_info(request):
    #info('Request URL: ' + request.get_full_path() + ', Request Time: ' + str(
        #datetime.now()) + ', Request Params:' + dumps(request.data))



def log_api(error_msg):

    def inner_function(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            try:
                #$store_log_info(request)
                return function(request, *args, **kwargs)
            except Exception as err:
                #logger.error(err)
                #STORE ERROR IN LOG
                print(str(err))
                return Response({"message": "" + error_msg + str(err)},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
        return wrapper
    return inner_function
