# **Customer Behaviour Analysis — Python, SQL and Tableau Project**

This project analyses a customer shopping behaviour dataset using Python, PostgreSQL (SQL), and a Tableau dashboard.
It focuses on data cleaning, customer segmentation, purchase behaviour, and revenue insights across age groups and product categories.

---

---

## **Dataset**

The dataset includes:

- Customer demographics  
- Subscription status  
- Product category & item purchased  
- Purchase amount  
- Discount usage  
- Review rating  
- Shipping method  
- Purchase frequency  
- Previous purchases  

## **Python Data Cleaning & Transformation**

The script performs:

- Filling missing `review_rating` using **median rating by category**
- Standardised column names (`snake_case`)
- Renamed `purchase_amount_(usd)` → `purchase_amount`
- Created **age_group** (Young Adult, Adult, Middle-aged, Senior)
- Converted purchase frequency text → numeric days  
- Removed redundant column `promo_code_used`
- Uploaded cleaned data into PostgreSQL table: **customer**

---

## **SQL Analysis**

Questions answered include:

1. Revenue by gender  
2. High-value discount users  
3. Top 5 highest-rated products  
4. Standard vs Express shipping comparison  
5. Subscribers vs non-subscribers revenue  
6. Highest discount-rate products  
7. Customer segmentation (New, Returning, Loyal)  
8. Top 3 products per category  
9. Do repeat buyers subscribe?  
10. Revenue by age group  

---

## **Tableau Dashboard**

The Tableau dashboard visualises:

- KPI Cards  
  - Total Customers  
  - Avg Purchase Amount  
  - Avg Rating  

- Age Group Distribution  
- Revenue by Category  
- Average Rating by Category  
- Interactive filters (Age Group, Category)  


