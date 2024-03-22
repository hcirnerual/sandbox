from pyspark.sql import SparkSession

def load_big_data(input_file_path):
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("BigDataLoad") \
        .getOrCreate()
    
    try:
        # Read the input file into a DataFrame
        df = spark.read.load(input_file_path, format="csv", inferSchema="true", header="true")
        
        # Perform operations on the DataFrame (if needed)
        # For example:
        # df_transformed = df.select(...)
        
        # Write the transformed DataFrame to an output location
        # For example, writing to Parquet format:
        # df_transformed.write.mode("overwrite").parquet(output_file_path)
        
        # Alternatively, you can return the DataFrame for further processing
        return df
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop the SparkSession to release resources
        spark.stop()

# Example usage:
input_file_path = "/path/to/input/file.csv"
# output_file_path = "/path/to/output/destination/"

# Load big data from the input file
loaded_data = load_big_data(input_file_path)

# Perform further processing or analysis on the loaded data
# For example:
# loaded_data.show()
# loaded_data_analysis = loaded_data.groupBy(...).agg(...)

# Optionally, write the processed data to an output location
# loaded_data_analysis.write.mode("overwrite").parquet(output_file_path)
