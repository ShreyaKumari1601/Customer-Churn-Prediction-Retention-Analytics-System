-- =====================================================================
-- Analytical SQL queries for the Customer Churn Warehouse (SQLite)
-- Run against: data/processed/churn_warehouse.db, table: customer_churn
-- =====================================================================

-- 1. Overall churn rate
SELECT
    ROUND(100.0 * SUM(is_churned) / COUNT(*), 2) AS churn_rate_pct,
    COUNT(*) AS total_customers,
    SUM(is_churned) AS churned_customers
FROM customer_churn;

-- 2. Churn rate by contract type
SELECT
    contract,
    COUNT(*) AS customers,
    SUM(is_churned) AS churned,
    ROUND(100.0 * SUM(is_churned) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn
GROUP BY contract
ORDER BY churn_rate_pct DESC;

-- 3. Churn rate by tenure group
SELECT
    tenure_group,
    COUNT(*) AS customers,
    ROUND(100.0 * SUM(is_churned) / COUNT(*), 2) AS churn_rate_pct,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges
FROM customer_churn
GROUP BY tenure_group
ORDER BY tenure_group;

-- 4. Churn rate by internet service & payment method
SELECT
    internet_service,
    payment_method,
    COUNT(*) AS customers,
    ROUND(100.0 * SUM(is_churned) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn
GROUP BY internet_service, payment_method
ORDER BY churn_rate_pct DESC;

-- 5. Revenue at risk (sum of monthly charges for churned customers)
SELECT
    ROUND(SUM(monthly_charges), 2) AS monthly_revenue_at_risk,
    ROUND(SUM(clv_estimate), 2) AS lifetime_value_lost
FROM customer_churn
WHERE is_churned = 1;

-- 6. Top 10 highest-value churned customers (for win-back targeting)
SELECT customer_id, tenure, monthly_charges, clv_estimate, contract, payment_method
FROM customer_churn
WHERE is_churned = 1
ORDER BY clv_estimate DESC
LIMIT 10;

-- 7. Number of add-on services vs churn rate (does bundling reduce churn?)
SELECT
    num_services,
    COUNT(*) AS customers,
    ROUND(100.0 * SUM(is_churned) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn
GROUP BY num_services
ORDER BY num_services;

-- 8. Senior citizens vs churn
SELECT
    senior_citizen,
    COUNT(*) AS customers,
    ROUND(100.0 * SUM(is_churned) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn
GROUP BY senior_citizen;
