from src.api.services.error.handleError import addError
from src.api.services.user.findUserByIdService import findUserByIdService
from src.api.services.user.deleteUserService import deleteUserService

async def deleteUserController(id):
    
    user = await findUserByIdService(id)

    if (user is None):
        return addError("Usuário não encontrado na base de dados.") 

    await deleteUserService(id)

    return
    