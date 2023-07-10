import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MongoDB
client = pymongo.MongoClient("<mongo_connection_string>")
db = client["your_database"]
collection = db["your_collection"]

# Retrieve data from MongoDB
data = collection.find({})  # Query to retrieve all documents

# Convert MongoDB data to pandas DataFrame
df = pd.DataFrame(list(data))

# Perform analytics on the data
# Example: Calculate average stock price by symbol
average_price_by_symbol = df.groupby("symbol")["price"].mean()

# Visualize the results
average_price_by_symbol.plot(kind="bar")
plt.xlabel("Symbol")
plt.ylabel("Average Price")
plt.title("Average Stock Price by Symbol")
plt.show()

# Save the analytics results to a file (e.g., CSV)
average_price_by_symbol.to_csv("average_price_by_symbol.csv")

# Close the MongoDB connection
client.close()
