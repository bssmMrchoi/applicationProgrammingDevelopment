```create table images(
    id int auto_increment primary key,
    filename varchar(255) not null,
    filepath text not null,
    upload_at datetime default CURRENT_TIMESTAMP,
    content_tpye varchar(100) default null
)
```
__패키지 설치__
1. Python-Multipart