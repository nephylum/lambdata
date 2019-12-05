# lambdata - Eric Ramon
a small test collection of Data Science helper functions

# Two Test Functions
### (for DataFrames testing)

- null_check(df)
- train_val_test_split(df, target)

## null_check(df)
- requires a pandas DataFrame
- Goes through a DataFrame column by column
- Totals number of null values found in column
- If null values are found, it reports how many as well as which column it was found in

## train_val_test_split(df, target)
- requires a pandas DataFrame and a column name
- splits DataFrame giving 15% to X_test, y_test
    - second split gives 20% to X_val, y_val, leaving X_train, y_train with the remainder
- returns (in this order): X_train, y_train, X_val, y_val, X_test, y_test

### These functions are dependent on:
- sklearn.model_selection.train_test_split
- numpy
- pandas
