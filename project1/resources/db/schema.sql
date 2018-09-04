-- BOOKS TABLE
create table books
(
  id               serial       not null
    constraint books_pkey
    primary key,
  isbn             varchar(13)  not null,
  author           varchar(200),
  title            varchar(200) not null,
  publication_year integer
);

create unique index books_id_uindex
  on books (id);

create unique index books_isbn_uindex
  on books (isbn);

-- REVIEWS TABLE
create table reviews
(
  id        serial        not null
    constraint reviews_pkey
    primary key,
  book_isbn varchar(13)   not null,
  rating    integer       not null,
  review    varchar(2000) not null
);

create unique index reviews_id_uindex
  on reviews (id);


-- USER TABLE
create table users
(
  user_id  serial      not null
    constraint users_pkey
    primary key,
  nick     varchar(30) not null,
  email    varchar(50) not null,
  password char(100)    not null
);

create unique index users_user_id_uindex
  on users (user_id);

create unique index users_nick_uindex
  on users (nick);

create unique index users_email_uindex
  on users (email);


ALTER TABLE public.reviews ADD reviwer VARCHAR(30) NOT NULL;
ALTER TABLE public.reviews
ADD CONSTRAINT fk_user_id
FOREIGN KEY (reviewer) REFERENCES public.users (nick);

CREATE UNIQUE INDEX isbn_reviewer_idx ON reviews (book_isbn, reviewer);
