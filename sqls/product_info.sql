create table product_info
(
    id                   serial
            primary key,
    name                 varchar(255)                           not null,
    description          varchar(255),
    tag                  varchar(255),
    purchase_flow        jsonb,
    params               jsonb,
    is_debt              boolean      default false             not null,
    created_at           timestamp(0) default CURRENT_TIMESTAMP not null,
    updated_at           timestamp(0),
    is_active            boolean      default true              not null
);