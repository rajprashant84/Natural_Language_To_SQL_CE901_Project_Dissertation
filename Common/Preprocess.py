from Common.DataConversion import DataConversion

# Create a tokenized dataset for the train, test and validation datasets
# Enables model to run faster during actual training since all data is already
# preprocessed
data_converter = DataConversion()
print("train Start")
data_converter.build_tokenized_dataset("train")
print("dev Start")
data_converter.build_tokenized_dataset("dev")
print("dev test")
data_converter.build_tokenized_dataset("test")
print("End")