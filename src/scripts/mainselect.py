from lxml import etree
import re
from lib.dbconnection.sqlserver_connect import SQLSERVER

def main():
# Get user input
    option = input("Enter 1 for author name or 2 for book name: ")
    if option == 1:

        author_name = input("Enter author name: ")
        sqlquery = f"SELECT * FROM book WHERE author = '{author_name}'"
    else:

        book_name = input("Enter book name: ")
        sqlquery = f"SELECT * FROM book WHERE title = '{book_name}'"

    
    print(sqlquery)
    db = SQLSERVER()
    res = db.select_query(sqlquery)
    return res

if __name__=='__main__':
    main()