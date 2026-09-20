# Food-Delivery-Knowledge-Repository

An online food delivery system connects customers with restaurants and delivery partners. A typical system manages customers, restaurants, food items, orders, payments, and deliveries. Based on the information stored in the knowledge repository, different business decisions can be generated using predefined rules.
For example:
If a restaurant has low availability of a food item, a stock alert can be generated.
If a customer is a premium member and places a large order, free delivery can be provided.
If payment fails, the order can be marked as payment pending.
If an order has been delivered, the delivery can be marked as completed.
Thus, the knowledge repository stores the facts and the business rules process those facts to generate useful decisions.

Main Components of the Repository: 
The knowledge repository contains the following major components:
1. Customer
The Customer entity stores information about users who place food orders.
It may contain:
Customer ID
Customer name
Location
Membership type
Example:
C101 → Anusha → Delhi → Premium
2. Restaurant
The Restaurant entity stores information about restaurants available on the food delivery platform.
It may contain:
Restaurant ID
Restaurant name
Cuisine
Location
Rating
Example:
R101 → Spice Hub → Indian → Delhi → 4.5
3. Food Item
The Food Item entity stores information about the food products available for ordering.
It may contain:
Food Item ID
Food item name
Category
Price
Availability
Example:
F101 → Paneer Biryani → Main Course → ₹250 → Available
4. Order
The Order entity stores information about orders placed by customers.
It may contain:
Order ID
Customer ID
Restaurant ID
Food Item ID
Quantity
Total amount
Payment status
Order status
Example:
O101 → C101 → R101 → F101 → Quantity 2 → ₹500
5. Payment
The Payment entity stores information about the payment made for an order.
It may contain:
Payment status
Payment method
Transaction status
Possible payment states include:
Successful
Failed
Pending
6. Delivery
The Delivery entity stores information related to delivery of an order.
It may contain:
Delivery status
Delivery partner
Expected delivery time
Possible delivery states include:
Preparing
Out for Delivery
Delivered
7. Business Rules
Business rules are conditions that are applied to the stored facts to generate decisions.
Some rules used in the system are:
Rule 1: Low Food Availability
If the availability of a food item is less than 10, then generate:
Decision: Low Availability Alert
Rule 2: Premium Customer
If the customer is a Premium member and the order amount is greater than ₹500, then generate:
Decision: Free Delivery
Rule 3: Failed Payment
If the payment status is Failed, then generate:
Decision: Payment Pending
Rule 4: Delivered Order
If the order status is Delivered, then generate:
Decision: Order Successfully Delivered
These rules demonstrate how stored knowledge can be processed to support business decisions.
