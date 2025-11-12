USE telecom_dw;



CREATE TABLE cleaned_cdr (
    Customer_ID INT,
    Call_Date DATE,
    Call_Duration INT,
    Call_Type VARCHAR(20),
    Charges FLOAT,
    Geography VARCHAR(50)
);
CREATE TABLE cleaned_customer_info (
    Customer_ID INT,
    Segment VARCHAR(50),
    Demography VARCHAR(50),
    Product_Code VARCHAR(50)
);
CREATE TABLE cleaned_internet_usage (
    Customer_ID INT,
    Usage_Date DATE,
    Data_Used_MB FLOAT,
    Charges FLOAT
);
CREATE TABLE cleaned_rules (
    Rule_ID INT,
    Rule_Start_Date DATE,
    Rule_End_Date DATE,
    Target_Customer VARCHAR(50),
    Score INT,
    Weightage FLOAT
);

INSERT INTO cleaned_cdr
SELECT DISTINCT Customer_ID, Call_Date, Call_Duration, Call_Type, Charges, Geography
FROM cdr_raw
WHERE Customer_ID IS NOT NULL
  AND Charges IS NOT NULL;

INSERT INTO cleaned_customer_info
SELECT DISTINCT Customer_ID, Segment, Demography, Product_Code
FROM customer_info
WHERE Customer_ID IS NOT NULL;

INSERT INTO cleaned_internet_usage
SELECT DISTINCT Customer_ID, Usage_Date, Data_Used_MB, Charges
FROM internet_usage_raw
WHERE Customer_ID IS NOT NULL
  AND Data_Used_MB > 0;

INSERT INTO cleaned_rules
SELECT DISTINCT Rule_ID, Rule_Start_Date, Rule_End_Date, Target_Customer, Score, Weightage
FROM rules
WHERE Rule_ID IS NOT NULL;

SELECT * FROM cleaned_cdr;
SELECT * FROM cleaned_customer_info;
SELECT * FROM cleaned_internet_usage;
SELECT * FROM cleaned_rules;
INSERT INTO customer_profitability
SELECT 
    c.Customer_ID,
    DATE_FORMAT(cd.Call_Date, '%Y-%m-01') AS Month,
    SUM(cd.Call_Duration * r.Weightage + cd.Charges * r.Score) AS Profitability_Score,
    AVG(SUM(cd.Call_Duration * r.Weightage + cd.Charges * r.Score)) OVER (PARTITION BY c.Segment, cd.Geography) AS Aggregated_Score,
    c.Segment,
    cd.Geography,
    SUM(cd.Charges) AS Total_Revenue,
    COUNT(DISTINCT c.Customer_ID) AS Customer_Count
FROM cdr_raw cd
JOIN customer_profiles_raw c ON cd.Customer_ID = c.Customer_ID
JOIN rules_master_raw r ON c.Segment = r.Target_Customer
WHERE cd.Call_Date BETWEEN r.Rule_Start_Date AND r.Rule_End_Date
GROUP BY c.Customer_ID, Month, c.Segment, cd.Geography;

select*from customer_profitability;
SELECT AVG(Aggregated_Score) FROM customer_profitability WHERE Segment='Premium';
SELECT MIN(Aggregated_Score), MAX(Aggregated_Score) FROM customer_profitability;
