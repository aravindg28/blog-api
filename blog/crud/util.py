from fastapi import HTTPException, status

def check_resource_exists(id, db, model):
    resource = db.query(model).filter(model.id == id).first()
    if resource:
        return
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Resource of type {model} with id {id} is not found")
    