

from src.api.services.error.handleError import addError
from src.api.services.user.checkEmailAlredyUsedService import checkEmailAlredyUsedService
from src.api.services.user.createUserService import createUserService


async def createUserController(email,password):
    

    
    user = await checkEmailAlredyUsedService(email)

    if (user):
        return addError("Email já cadastrado") 

    user = await createUserService(email, password)

    return {
        "email": user.email,
        "id": user.id,
    }
    