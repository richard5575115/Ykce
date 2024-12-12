import pymssql


class ykcemssql():
    def __init__(self): 
       self.conn = pymssql.connect(
          server='220.130.213.6:1433',
          user='api',
          password='Ykce4523!@#',
          database='API專用',
          as_dict=True
        ) 

    def get_teacher_dataset(self, query):   
       cursor = self.conn.cursor()
       sql_query = "SELECT [園所簡稱],[年度],[開班編號],[班級代號],[年度屬性],[班導],[副班導],[年級],[班別],[班級名稱] FROM  [ZOHO_Class] where [班級代號] < 50 and [園所簡稱] = '" + query + "' order by [開班編號]" 
       cursor.execute(sql_query)
       return cursor
    
    def get_all_student_dataset(self, kind,class_name):   
       cursor = self.conn.cursor()
       sql_query = "SELECT [zoho_kind],[zoho_ClassDifferent],[zoho_ClassGrade],[zoho_ClassName],[zoho_OPEN_no],[zoho_stnno] ,[zoho_Teacher],[zoho_EducareGiver_id] FROM  [zoho_class_teacher]   where zoho_mode = '學生' and zoho_kind = '" + kind + "'    and zoho_ClassName = '" + class_name + "'  order by zoho_stnno"
       cursor.execute(sql_query)
       return cursor

#conn = ykcemssql()
#cursor = conn.get_all_student_dataset('員林園','倫敦')
#records = cursor.fetchall()
#for row in records:
#     print (row)
#     row = cursor.fetchone()
#cursor.close()
#conn.close()      
      