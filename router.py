from fastapi import HTTPException, Depends, Request
from fastapi import APIRouter
from model import *
from database import Database

router = APIRouter()

#######################ACCOUNT#######################
@router.post("/account/add")
def addAcc(acc: Account):
    return{Database().addAcc(acc.dict())}

@router.get("/account/list")
def listAcc():
    return{"list": Database().listAcc()}

@router.post("/account/find/email")
def findAcc(acc: SEmail):
    return{"result": Database().findAcc(acc.dict())}

"""
@router.post("/account/update")
def updateAcc(up: UpdateAccount):
    return{Database().updateAcc(up.username,up.dict())}
"""