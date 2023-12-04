

from src.api.services.error.handleError import addError
from src.api.services.user.findUserByEmailService import findUserByEmailService


async def loginController(email,password):
    
    user = await findUserByEmailService(email)

    if(user == None):
       return addError('Usuário ou senha incorretos')
   
    if(user.password != password):
       return addError('Usuário ou senha incorretos')
    
    return {
        "id": user.id,
        "email": user.email,
    }
    