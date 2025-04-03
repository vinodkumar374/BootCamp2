# Databricks notebook source
# MAGIC %md
# MAGIC #Delta Processing Notebook

# COMMAND ----------


df = spark.read.csv("/mnt/bootcamp2/raw/customers.csv", header=True)
display(df)

# COMMAND ----------

df1 = df.fillna("ON", "state").fillna("P0J0A3", "Zip")
display(df1)

# COMMAND ----------

df2 = df1.withColumn("Customer_ID", df1["customer_id"].cast("int"))
display(df2)

# COMMAND ----------

df3= df2.write.mode("append").format("delta").save("/mnt/bootcamp2/silver/customers.csv")

# COMMAND ----------

df = spark.read.csv("/mnt/bootcamp2/raw/accounts.csv", header=True)
display(df)

# COMMAND ----------

df1 = df.withColumn("Account_ID", df["account_id"].cast("int")).withColumn("Customer_id", df["customer_id"].cast("int"))
display(df1)

# COMMAND ----------

df2 = df1.write.mode("append").format("delta").save("/mnt/bootcamp2/silver/accounts.csv")

# COMMAND ----------

df = spark.read.csv("/mnt/bootcamp2/raw/transactions.csv", header=True)
display(df)

# COMMAND ----------

df1 = df.withColumn("Transaction_ID", df["transaction_id"].cast("int")).withColumn("Account_ID", df["account_id"].cast("int"))
display(df1)

# COMMAND ----------

df2 = df1.write.mode("append").format("delta").save("/mnt/bootcamp2/silver/transactions.csv")

# COMMAND ----------

df = spark.read.csv("/mnt/bootcamp2/raw/loans.csv", header=True)
display(df)

# COMMAND ----------

df1 = df.withColumn("Loan_ID", df["loan_id"].cast("int")).withColumn("Customer_ID", df["customer_id"].cast("int")).withColumn("Loan_Term", df["loan_term"].cast("int"))
display(df1)

# COMMAND ----------

df2 = df1.write.mode("append").format("delta").save("/mnt/bootcamp2/silver/loans.csv")

# COMMAND ----------

df = spark.read.csv("/mnt/bootcamp2/raw/loan_payments.csv", header=True)
display(df) 

# COMMAND ----------

df1 = df.withColumn("Payment_ID", df["payment_id"].cast("int")).withColumn("Loan_ID", df["loan_id"].cast("int"))
display(df1)

# COMMAND ----------

df2 = df1.write.mode("append").format("delta").save("/mnt/bootcamp2/silver/loan_payments.csv")