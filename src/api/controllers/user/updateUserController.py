from src.api.services.user.findUserByIdService import findUserByIdService
from src.api.services.error.handleError import addError
from src.api.services.user.checkEmailAlredyUsedService import checkEmailAlredyUsedService
from src.api.services.user.updateUserService import updateUserService


async def updateUserController(id,email,password):
    

    user = await findUserByIdService(id)
    if (user is None):
        return addError("Usuário não encontrado na base de dados.") 

    user = await checkEmailAlredyUsedService(email,id)
    if (user):
        return addError("Email já cadastrado") 

    user = await updateUserService(id,email, password)

    return {
        "email": user.email,
    }
    