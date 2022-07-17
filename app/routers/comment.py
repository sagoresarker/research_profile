# from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
# from sqlalchemy.orm import Session
# from .. import schemas, database, models, oauth2
# from ..database import get_db


# router = APIRouter(
#     prefix="/comment",
#     tags=['Comments']
# )

# def create_comment(db: Session,post_id:int,comment:schemas.CommentBase):
#     db_comment = models.Comment(post_id=post_id,**comment.dict())
#     db.add(db_comment)
#     db.commit()
#     db.refresh(db_comment)
#     return db_comment

# @router.post("/posts/{post_id}/comment",response_model=schemas.CommentList)
# def create_comment(comment:schemas.CommentBase ,post_id:int,db:Session = Depends(get_db)):
#     return  create_comment(db=db,post_id=post_id,comment=comment)