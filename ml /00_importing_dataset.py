from ucimlrepo import fetch_ucirepo

# Fetch the MAGIC Gamma Telescope dataset from UCI
magic_gamma_telescope = fetch_ucirepo(id=159)

# Store the input features in X (10 columns)
X = magic_gamma_telescope.data.features

# Store the target labels in y (the class to predict)
y = magic_gamma_telescope.data.targets

# Print general dataset information
print(magic_gamma_telescope.metadata)

# Print descriptions of each feature and the target
print(magic_gamma_telescope.variables)