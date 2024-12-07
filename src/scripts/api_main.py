from fastapi import FastAPI
from mainselect import main
from book_model import Book
from lib.dbconnection.sqlserver_connect import SQLSERVER


    
app=FastAPI()   #instance of fastapi class

@app.get('/books')  #decorator
def getbooks():    #async - synchronization
    result =  main()

    #for val in result:
    #    book_id = val

    return {'message': result }

    ##return {'message':'all books displayed'}


@app.post('/book/insert')
def insert_book(book:Book):
    sqlquery=f"""insert into book(book_id,author,title,price,publish_date,description) values('{book.book_id}','{book.author}','{book.title}','{book.price}','{book.publish_date}','{book.description}');""" 
    print(sqlquery)
    db = SQLSERVER()
    db.insert_query(sqlquery)
    return {'message': "row inserted" }