create database vakcina character set utf8mb4 collate utf8mb4_general_ci;
use vakcina;
create user 'user'@'%' identified by 'Password-1234';
grant all privileges on vakcina.* to 'user'@'%';
flush privileges;
