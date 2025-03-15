create table payment_order
(
    id                    bigserial
        primary key,
    order_uuid            uuid            not null,
    order_date            timestamp      default CURRENT_TIMESTAMP                                                   not null,
    user_id               bigint                                                                                     not null,
    target_user_id        bigint,
    amount                numeric(14, 4)                                                                             not null,
    currency_code         varchar(3)                                                                                 not null,
    additional_fee        numeric(12, 4) default 0                                                                   not null,
    order_type            smallint                                                                                   not null,
    order_status          smallint,
    order_additional_data jsonb,
    order_details         jsonb,
    payment_channel       smallint,
    created_at            timestamp(0)   default CURRENT_TIMESTAMP                                                   not null,
    updated_at            timestamp(0),
    is_active             boolean        default true                                                                not null,
    error_message         text,
    is_auto_payment       boolean
);