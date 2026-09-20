# Food-Delivery-Knowledge-Repository

## 📌 About the Project

An **Online Food Delivery System** connects customers with restaurants and delivery partners. A typical system manages customers, restaurants, food items, orders, payments, and deliveries.

This project creates a **Knowledge Repository** for an online food delivery business system. The repository stores facts about the different entities involved in the system and applies predefined **business rules** to generate useful business decisions.

### Examples of Business Decisions

* If a restaurant has low availability of a food item, a **low availability alert** can be generated.
* If a customer is a premium member and places a large order, **free delivery** can be provided.
* If payment fails, the order can be marked as **payment pending**.
* If an order has been delivered, the delivery can be marked as **completed**.

Thus, the knowledge repository stores the facts, while business rules process these facts to generate useful decisions.

---

## 🧠 Main Components of the Repository

The knowledge repository contains the following major components:

### 1. Customer

The **Customer** entity stores information about users who place food orders.

**It may contain:**

* Customer ID
* Customer Name
* Location
* Membership Type

**Example:**

```text
C101 → Anusha → Delhi → Premium
```

---

### 2. Restaurant

The **Restaurant** entity stores information about restaurants available on the food delivery platform.

**It may contain:**

* Restaurant ID
* Restaurant Name
* Cuisine
* Location
* Rating

**Example:**

```text
R101 → Spice Hub → Indian → Delhi → 4.5
```

---

### 3. Food Item

The **Food Item** entity stores information about the food products available for ordering.

**It may contain:**

* Food Item ID
* Food Item Name
* Category
* Price
* Availability

**Example:**

```text
F101 → Paneer Biryani → Main Course → ₹250 → Available
```

---

### 4. Order

The **Order** entity stores information about orders placed by customers.

**It may contain:**

* Order ID
* Customer ID
* Restaurant ID
* Food Item ID
* Quantity
* Total Amount
* Payment Status
* Order Status

**Example:**

```text
O101 → C101 → R101 → F101 → Quantity 2 → ₹500
```

---

### 5. Payment

The **Payment** entity stores information about the payment made for an order.

**It may contain:**

* Payment Status
* Payment Method
* Transaction Status

**Possible payment states include:**

* Successful
* Failed
* Pending

---

### 6. Delivery

The **Delivery** entity stores information related to the delivery of an order.

**It may contain:**

* Delivery Status
* Delivery Partner
* Expected Delivery Time

**Possible delivery states include:**

* Preparing
* Out for Delivery
* Delivered

---

## 📂 Repository Structure

```text
Food-Delivery-Knowledge-Repository/
│
├── knowledge_base.py
├── business_rules.txt
└── README.md
```

### Files

* **`knowledge_base.py`** – Contains the knowledge repository and Python program for applying business rules.
* **`business_rules.txt`** – Contains the business rules used for decision-making.
* **`README.md`** – Provides project documentation and information about the knowledge repository.

---

## 🎯 Objective

The objective of this project is to demonstrate how a **knowledge repository** can store facts related to a real-world business system and apply predefined rules to generate meaningful decisions.

---

## 🛠️ Technologies Used

* **Python**
* **GitHub**
* **Knowledge Representation**
* **Rule-Based Decision Making**

---

## ☁️ Cloud-Based Repository

The knowledge repository can be uploaded to a **public GitHub repository**, making the knowledge base, business rules, and project documentation accessible to other users.

**Repository Visibility:** Public

**GitHub Repository:**

```text
https://github.com/Anusha5D/Food-Delivery-Knowledge-Repository/
```

---

## ✅ Conclusion

The **Food Delivery Knowledge Repository** demonstrates the representation of real-world business knowledge using structured facts and predefined business rules. The stored information about customers, restaurants, food items, orders, payments, and deliveries can be processed to generate useful business decisions.

The repository can be hosted publicly on GitHub, making it accessible, reusable, and easy to maintain.
