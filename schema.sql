drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username text not null,
  email text not null,
  password password not null
);