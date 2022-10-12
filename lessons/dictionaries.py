"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str,int]

# Initialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19_400
schools["DUKE"] = 7_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key valuue-value pair from a dictionary by its key
schools.pop("DUKE")

# Test for the existence of a key
if "DUKE" in schools:
    print("Found the key 'DUKE' in schools")
else:
    print("No key 'DUKE' in schools")
# is_duke_present: bool = "DUKE" in schools
# print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 100

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19_400, "DUKE": 6_717, "NCSU": 26_150}
print(schools)

# What happens when a key does not exist
# print(schools["UNCC"])
# It will return a KeyError

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")