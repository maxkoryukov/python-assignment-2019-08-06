# -*- coding: utf-8 -*-

"""
Demo Middleware
"""

import traceback
from django.utils.deprecation import MiddlewareMixin
from pythonassignment.tasks import save_exception_task


class PersistExceptionsMiddleware(MiddlewareMixin):
    """Save exceptions to the database

    The following info will be saved:
     * the exception string (using str())
     * the exception representation (using repr())
     * the exception args (as a string)
     * the traceback (as a string)
    """
    def process_exception(self, request, exception):
        msg_excp = str(exception)
        msg_repr = repr(exception)
        msg_args = str(exception.args)
        msg_trbk = traceback.format_exc()
        save_exception_task.delay(msg_excp, msg_repr, msg_args, msg_trbk)
