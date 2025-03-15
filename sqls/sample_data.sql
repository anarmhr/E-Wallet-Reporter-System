INSERT INTO user_info (id, username, password, user_status, user_type, created_at, updated_at, language, is_active, description)
VALUES
(1, 'john_doe', 'secure123', 1, 1, '2024-03-14 10:00:00', NULL, 'EN', TRUE, 'Regular user'),
(2, 'alice_smith', 'password456', 1, 2, '2024-03-14 11:15:00', NULL, 'EN', TRUE, 'Premium user');

INSERT INTO product_info (id, name, description, tag, purchase_flow, params, is_debt, created_at, updated_at, is_active)
VALUES
(1, 'E-Wallet Premium Subscription', 'Monthly premium membership', 'subscription', '{"step1":"select","step2":"pay"}'::jsonb, '{"renewal":"yes"}'::jsonb, FALSE, '2024-03-14 12:30:00', NULL, TRUE),
(2, 'Gift Card', 'Prepaid digital gift card', 'giftcard', '{"step1":"choose","step2":"send"}'::jsonb, '{"validity":"1 year"}'::jsonb, FALSE, '2024-03-14 12:45:00', NULL, TRUE);

INSERT INTO payment_order (id, order_uuid, order_date, user_id, target_user_id, amount, currency_code, additional_fee, order_type, order_status, order_additional_data, order_details, payment_channel, created_at, updated_at, is_active, error_message, is_auto_payment)
VALUES
(1, '550e8400-e29b-41d4-a716-446655440000', '2024-03-14 13:00:00', 1, 2, 49.99, 'USD', 0.50, 1, 2, '{}'::jsonb, '{}'::jsonb, 1, '2024-03-14 13:00:00', NULL, TRUE, NULL, FALSE),
(2, '660e8400-e29b-41d4-a716-446655440111', '2024-03-14 13:30:00', 2, 1, 25.00, 'EUR', 0.25, 2, 1, '{}'::jsonb, '{}'::jsonb, 2, '2024-03-14 13:30:00', NULL, TRUE, NULL, TRUE);

INSERT INTO wallet_info (id, available_amount, currency_code, user_id, wallet_status, created_at, updated_at, is_active)
VALUES
(1, 100.00, 'USD', 1, 1, '2024-03-14 14:00:00', NULL, TRUE),
(2, 200.00, 'EUR', 2, 1, '2024-03-14 14:15:00', NULL, TRUE);

INSERT INTO wallet_transaction (id, txn_date, user_id, transfer_wallet_id, txn_amount, final_available_amount, currency_code, txn_type, txn_direction, txn_status, order_id, created_at, updated_at, is_active)
VALUES
(1, '2024-03-14 15:00:00', 1, NULL, 50.00, 50.00, 'USD', 1, 'D', 2, 1, '2024-03-14 15:00:00', NULL, TRUE),
(2, '2024-03-14 15:30:00', 2, NULL, 25.00, 175.00, 'EUR', 2, 'C', 1, 2, '2024-03-14 15:30:00', NULL, TRUE);
