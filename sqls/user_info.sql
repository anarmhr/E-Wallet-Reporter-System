create table user_info
(
    id                  bigserial
        primary key,
    username            varchar(255)                                 not null,
    password            varchar(255),
    user_status         smallint                                     not null,
    user_type           smallint     default 1                       not null,
    created_at          timestamp(0) default CURRENT_TIMESTAMP       not null,
    updated_at          timestamp(0),
    language            varchar(2)   default 'EN'::character varying not null,
    is_active           boolean      default true                    not null,
    description         varchar(255)
);