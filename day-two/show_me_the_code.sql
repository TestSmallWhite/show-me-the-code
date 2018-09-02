-- day two sql

drop database if exists show_me_the_code;

create database show_me_the_code;

use show_me_the_code;

create table day_two(
	`id` int(10) primary key,
	`key` varchar(40) not null,
	`isUse` int(1) default 0 not null,
	`createTime` varchar(20) not null,
	`useTime` varchar(20) not null
)engine=innodb default charset=utf8;