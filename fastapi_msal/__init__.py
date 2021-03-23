"""
FastAPI/MSAL - MSAL (Microsoft Authentication Library) plugin for the FastAPI ASGI framewaork

FastAPI - https://github.com/tiangolo/fastapi
MSAL for Python - https://github.com/AzureAD/microsoft-authentication-library-for-python
"""

__version__ = "0.0.1"

from . import security
from .security import MSALAuthCodeHandler
from . import routing
from .routing import MSALAuthorizationRouter
from . import core
from . import clients
from . import models
