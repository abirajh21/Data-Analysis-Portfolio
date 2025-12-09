# **Airbnb NYC Analysis — Python Project**

This project explores the Airbnb NYC dataset using Python.  
It focuses on data cleaning, exploratory data analysis (EDA), visualisation, and simple modelling to understand price patterns across New York City.

---

## **Project Structure**

```
airbnb-analysis/
│── data/
│   ├── airbnb.csv
│   ├── requirements.txt
│   └── airbnb.py   # main analysis script
│
│── plots/
    ├── price_distribution.png
    ├── price_by_room_type.png
    ├── avg_price_by_neighbourhood_group.png
    ├── availability_vs_price.png
    └── correlation_heatmap.png

```

---

## **Dataset**

This project uses the **2019 Airbnb NYC dataset** from Kaggle.

The dataset includes:

- Listing details  
- Host information  
- Neighbourhood + geolocation  
- Pricing  
- Reviews + monthly activity  

Total rows before cleaning: **48,895 listings**

---

## **Data Cleaning Steps**

- Removed duplicate listings  
- Converted `last_review` to datetime  
- Filled missing `reviews_per_month` with 0  
- Removed rows missing critical fields  
- Converted `price` to numeric  
- Removed unrealistic prices (kept under \$1000)

After cleaning: **48,586 rows remained**

---

## **Key Visualisations**

### **1. Price Distribution**
Most listings fall between **\$50–\$200**.

### **2. Price by Room Type**
Entire home/apartment listings are the most expensive.

### **3. Average Price by Neighbourhood Group**
Manhattan has the highest average price.

### **4. Availability vs Price**
No strong relationship between annual availability and price.

### **5. Correlation Heatmap**
Weak correlations between price and most numeric features.

---

## **Insights Summary**

- Manhattan is the most expensive neighbourhood group.  
- Entire homes/apartments cost significantly more than private/shared rooms.  
- Price distribution is heavily skewed due to luxury listings.  
- Availability does **not** strongly influence price.  
- Most numeric variables show weak correlation with price.

---

## **How to Run the Script**

### 1. Install requirements
```bash
pip install -r data/requirements.txt
```

### 2. Run the analysis
```bash
python airbnb.py
```

Plots will be saved automatically inside the **plots/** folder.
