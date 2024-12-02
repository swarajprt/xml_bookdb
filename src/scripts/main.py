from lxml import etree
import re
from lib.dbconnection.sqlserver_connect import SQLSERVER

def main():
    tree = etree.parse(r'F:\Python_learning\book.xml')
    root = tree.getroot()
    taglist=["book_id","author","title","price","publish_date","description"]
    for child in root:
        #print(f"Tag: {child.tag}, attributes: {child.attrib}")
        book_id = child.attrib['id']
        print(book_id)
        for c in child:
            if c.tag in taglist:
               # if c.tag=="book_id":
                   # book_id=c.text
                   # book_id = book_id.replace(",", "\\,")
                   # book_id = book_id.replace("'", "''")
                if c.tag=="author":
                    author=c.text
                    author = author.replace(",", "\\,")
                    author = author.replace("'", "''")
                if c.tag=="title":
                    title=c.text
                    title = title.replace(",", "\\,")
                    title = title.replace("'", "''")
                if c.tag=="price":
                    price=c.text
                    price = price.replace(",", "\\,")
                    price = price.replace("'", "''")
                if c.tag=="publish_date":
                    publish_date=c.text
                    publish_date = publish_date.replace(",", "\\,")
                    publish_date = publish_date.replace("'", "''")
                if c.tag=="description":
                    description=c.text
                    description = description.replace(",", "\\,")
                    description = description.replace("\n", " ")
                    description = re.sub(r'\s+', ' ', description)
                    description = description.replace("'", "''")
       # print(f"author={author}\ntitle={title}\nprice={price}\npublish_date={publish_date}\ndescription={description}")   
        sqlquery=f"""insert into book(book_id,author,title,price,publish_date,description) values('{book_id}','{author}','{title}','{price}','{publish_date}','{description}');""" 
        print(sqlquery)
        db = SQLSERVER()
        db.execute_query(sqlquery)

if __name__=='__main__':
    main()