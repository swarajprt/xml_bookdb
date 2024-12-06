import pyodbc

class SQLSERVER:
    def __init__(self):

        # Connection details #instance variable
        self.server = 'DESKTOP-I7UOETL\MSSQLSERVER2021'  # Example: 'localhost', 'DESKTOP\SQLSERVER'
        self.database = 'dbrisk'
        self.conn=None
        self.cursor=None
        self.connect()

# Establish connection

    def connect(self):
        self.conn = pyodbc.connect(
                        f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;'
                    )   

        print("Connection successful!")


    def close_connection(self):    
        if self.conn: 
            if self.cursor:
                self.cursor.close()
            self.conn.close()              

    def insert_query(self,query):
        if self.conn:
            if not self.cursor:
                self.cursor = self.conn.cursor()

            self.cursor.execute(query)
            self.conn.commit()
            self.close_connection()    
           ## self.cursor.close()    

    def select_query(self,query):
        if self.conn:
            if not self.cursor:
                self.cursor = self.conn.cursor()

            self.cursor.execute(query)

            # Step 4: Fetch and process results
            rows = self.cursor.fetchall()  # Fetch all rows that match the query
            return rows
            #for row in rows:
                #print(row)  # Print each row

            self.close_connection()     


            

        
if __name__ == '__main__':
    conn_obj = SQLSERVER() 
    ###conn_obj.connect()