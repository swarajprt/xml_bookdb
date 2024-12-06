from fastapi import FastAPI
from mainselect import main
app=FastAPI()   #instance of fastapi class

@app.get('/books')  #decorator
def getbooks():    #async - synchronization
    result =  main()
    return {'message': str(result)}

    ##return {'message':'all books displayed'}

