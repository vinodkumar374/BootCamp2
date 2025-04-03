# Databricks notebook source
# MAGIC %md
# MAGIC #ETL Procesing Notebook

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/bootcamp2/silver/accounts.csv")
display(df)

# COMMAND ----------

df2 = df.withColumnRenamed("Customer_id", "Customer_ID").withColumn("balance", df["balance"].cast("int"))
display(df2)

# COMMAND ----------

df2.createOrReplaceTempView("accounts")

# COMMAND ----------

df1 = spark.read.format("delta").load("/mnt/bootcamp2/silver/customers.csv")
display(df1)

# COMMAND ----------

df1.createOrReplaceTempView("customers")

# COMMAND ----------

# Define the SQL query
query = """
SELECT a.Account_ID, a.account_type, c.customer_id, c.first_name, c.last_name,
       c.address, c.city, c.state, c.zip, a.balance, SUM(a.balance) AS total_balance
FROM customers AS c
JOIN accounts AS a ON c.customer_id = a.customer_id
GROUP BY a.Account_ID, a.account_type, c.customer_id, c.first_name, c.last_name,
         c.address, c.city, c.state, c.zip, a.balance
"""

# Execute the query using Spark SQL and store the results in a DataFrame
df6 = spark.sql(query)

# Show the first few rows of the DataFrame to confirm it's loaded correctly
display(df6)


# COMMAND ----------

df7= df6.withColumnRenamed("Customer_id", "Customer_ID").withColumnRenamed("account_type", "Account_Type").withColumnRenamed("first_name", "First_Name").withColumnRenamed("last_name", "Last_Name").withColumnRenamed("address", "Address").withColumnRenamed("city", "City").withColumnRenamed("state", "State").withColumnRenamed("zip", "Zip").withColumnRenamed("balance", "Balance").withColumnRenamed("total_balance", "Total_Balance")
display(df7)


# COMMAND ----------

df7.write.format("parquet").mode("overwrite").save("/mnt/bootcamp2/gold/CustomerAccounts")

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/bootcamp2/silver/accounts.csv")
display(df)

# COMMAND ----------

df.write.format("parquet").mode("overwrite").save("/mnt/bootcamp2/gold/accounts")

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/bootcamp2/silver/customers.csv")
display(df)

# COMMAND ----------

df.write.format("parquet").mode("overwrite").save("/mnt/bootcamp2/gold/customers")

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/bootcamp2/silver/loan_payments.csv")
display(df)


# COMMAND ----------

df.write.format("parquet").mode("overwrite").save("/mnt/bootcamp2/gold/loan_payments")

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/bootcamp2/silver/loans.csv")
display(df)

# COMMAND ----------

df.write.format("parquet").mode("overwrite").save("/mnt/bootcamp2/gold/loans")

# COMMAND ----------

df = spark.read.format("delta").load("/mnt/bootcamp2/silver/transactions.csv")
display(df)

# COMMAND ----------

df.write.format("parquet").mode("overwrite").save("/mnt/bootcamp2/gold/transactions")