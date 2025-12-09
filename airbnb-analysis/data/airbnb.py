# airbnb_analysis.py
# Simple analysis of Airbnb NYC listings

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# -------------------------------
# 1. Load dataset
# -------------------------------

data_path = "data/airbnb.csv"
df = pd.read_csv(data_path)

print("\nDataset preview:")
print(df.head())
print(df.info())
print(df.describe())


# -------------------------------
# 2. Clean dataset
# -------------------------------

df = df.drop_duplicates()

df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

required = ["price", "latitude", "longitude", "room_type", "neighbourhood_group"]
df = df.dropna(subset=required)

df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df[(df["price"] > 0) & (df["price"] < 1000)]  # remove 0 and extreme outliers

print(f"\nRows after cleaning: {df.shape[0]}")
print(df["room_type"].value_counts())
print(df["neighbourhood_group"].value_counts())


# -------------------------------
# 3. Visualisations
# -------------------------------

os.makedirs("plots", exist_ok=True)
sns.set_style("whitegrid")

# Price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["price"], bins=50, kde=True)
plt.title("Price Distribution")
plt.savefig("plots/price_distribution.png")
plt.close()

# Price by room type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="room_type", y="price")
plt.title("Price by Room Type")
plt.savefig("plots/price_by_room_type.png")
plt.close()

# Average price by neighbourhood
avg_price = df.groupby("neighbourhood_group")["price"].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price.index, y=avg_price.values)
plt.title("Average Price by Neighbourhood Group")
plt.savefig("plots/avg_price_by_neighbourhood_group.png")
plt.close()

# Availability vs price
plt.figure(figsize=(10, 6))
sample_df = df.sample(min(5000, len(df)), random_state=42)
sns.scatterplot(data=sample_df, x="availability_365", y="price", alpha=0.5)
plt.title("Availability (365 days) vs Price")
plt.savefig("plots/availability_vs_price.png")
plt.close()

# Correlation heatmap
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("plots/correlation_heatmap.png")
plt.close()

print("\nPlots saved to the 'plots' folder.")


# -------------------------------
# 4. Insights
# -------------------------------

print("\nTop 10 most expensive neighbourhoods:")
print(
    df.groupby(["neighbourhood_group", "neighbourhood"])["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nAverage price by room type:")
print(df.groupby("room_type")["price"].mean())


# -------------------------------
# 5. Simple price prediction model
# -------------------------------

print("\nTraining Linear Regression model...")

features = ["minimum_nights", "number_of_reviews", "reviews_per_month", "availability_365"]
X = df[features]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Performance:")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")

coef_df = pd.DataFrame({
    "feature": features,
    "coefficient": model.coef_
}).sort_values(by="coefficient", key=abs, ascending=False)

print("\nModel coefficients:")
print(coef_df)

print("\nAnalysis complete.")
