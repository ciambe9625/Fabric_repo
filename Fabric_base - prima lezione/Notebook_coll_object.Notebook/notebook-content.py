# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ca0e1c52-29c5-4810-a36a-fe064a3ec8a8",
# META       "default_lakehouse_name": "LK_education",
# META       "default_lakehouse_workspace_id": "335ac7eb-80b5-4d82-9a57-72cc4ca6bbd2",
# META       "known_lakehouses": [
# META         {
# META           "id": "ca0e1c52-29c5-4810-a36a-fe064a3ec8a8"
# META         }
# META       ]
# META     },
# META     "warehouse": {}
# META   }
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM LK_education.dbo.products LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
