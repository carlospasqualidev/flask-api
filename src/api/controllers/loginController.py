from src.api.services.user.findUserByEmailService import findUserByEmailService

async def loginController(email,password):
    
    user = await findUserByEmailService(email)

    if(user == None):
        raise ValueError("Usuário ou senha incorretos")
   
    if(user.password != password):
        raise ValueError("Usuário ou senha incorretos")


    return {
        "email": user.email,
    }
    