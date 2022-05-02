# CREATE TABLE contacts(
#     name varchar(100) NOT NULL,
#     phone_number varchar(32),
# );
#
# 数据库中写入示例
# INSERT INTO contacts(name,phone_number)
# VALUES('renyc','12345678901');
#
# contact = Contact(name='renyc',phone_number='12345678901')
#
# import os
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
#           'sqlite:///' + os.path.join(app.root_path,'data.db'))