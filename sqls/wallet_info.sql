create table wallet_info
(
    id                bigserial            primary key,
    available_amount  numeric(12, 4) default 0                        not null,
    currency_code     varchar(3)     default 'AZN'::character varying not null,
    user_id           bigint                                          not null,
    wallet_status     smallint       default 1                        not null,
    created_at        timestamp(0)   default CURRENT_TIMESTAMP        not null,
    updated_at        timestamp(0),
    is_active         boolean        default true                     not null
);