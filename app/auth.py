from fastapi import Depends, HTTPException

usuarios = {
    "admin": {"username": "admin", "role": "admin"},
    "lector": {"username": "lector", "role": "lector"},
}

def get_current_user(username: str = "admin"):
    user = usuarios.get(username)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user
