
from src.api.services.user.createUserService import createUserService
from src.api.services.user.checkEmailAlredyUsedService import checkEmailAlredyUsedService

async def createUserController(email,password):
    
    await checkEmailAlredyUsedService(email)

    user = await createUserService(email, password)

    return {
        "email": user.email,
        "password": user.password
    }
    