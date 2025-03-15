create table wallet_transaction
(
    id                     bigint       primary key not null,
    txn_date               timestamp(0) default CURRENT_TIMESTAMP                                       not null,
    user_id                bigint                                                                       not null,
    transfer_wallet_id     bigint,
    txn_amount             numeric(14, 4)                                                               not null,
    final_available_amount numeric(14, 4),
    currency_code          varchar(3)   default 'AZN'::character varying                                not null,
    txn_type               smallint,
    txn_direction          varchar(1)                                                                   not null,
    txn_status             smallint     default 1                                                       not null,
    order_id               bigint                                                                       not null,
    created_at             timestamp(0) default CURRENT_TIMESTAMP                                       not null,
    updated_at             timestamp(0),
    is_active              boolean      default true                                                    not null
)