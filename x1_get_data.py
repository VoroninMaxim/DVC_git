import os
import wget
import zipfile

# Download the zipped dataset
#url = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'
url_test = 'https://storage.googleapis.com/kaggle-data-sets/522275/959195/compressed/test.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240708%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240708T205337Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=7ffc36de48e07f8c58f72faaea548f11b12256beaf2e121bc538a607ca7a127f9881c6d088768dcef1e0fa89a115d13b9ff170110dad88d749a5f64cb01da66b86fda65b9b1d458416983263b2c1590d5dec80ba39c0288c89859aed6c76feb3b4f71702b3153a76d925d0fb99c734cc65508c5c22961efab6187a30a5cc8688a5b7c38b3cd9c166bbc39a7e6d0b9c5aef5d257642d38047cdced157fd89a47d99afd3668a4739f62dc92cfc8c8ff7604b75864d044842c39f15cabab1928c80a17c9e6ca882c20a2d481ddc2967d7717ca91565a10c0ed2310bb17ad17880e4e77d0e8b5f397730d867af976842f58c1379ff1721a3bad02c383c54d07000ad'
zip_name_test = "test.csv.zip"


wget.download(url_test, zip_name_test)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name_test, "r") as zip_ref:
	zip_ref.extractall()
os.remove(zip_name_test)

print('\nAll files are being extracted.')

url ='https://storage.googleapis.com/kaggle-data-sets/522275/959195/compressed/train.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240708%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240708T205904Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=2d9e78a1e4fbfc4ff30f40bd9a1ddd7496913cb7bb889546ec335c12c75636b46c760eb5af23ddb98b533025e343d045d606db448a99235387c23c53cd81d155370eb174e82759e3823a49526a2b92a9115b3a54f15abbf0ca14b4bda28f3b6130700d69f512c8cbb739bd40999c8be20610fa5fcd1f6f199369df0b76e4467cbb01bd0fbe1f46df4c8f6776fb33faab7e08e3291b0f4be14c3d45353b07a92d59bca705ef6ee31a9eb765c2763e1e4cdf5aff106250c4472aab978de9bcd555a87addab6704ce62ec91741d6ce087d050ced3ae40fb50fbdf2ae4d6ef76e6a0c6c4d540c75d66b949b278b13cfa1328f5ae90d53676b019e0b22c27d9396967'
zip_name = "train.csv.zip"

wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()
os.remove(zip_name)

print('\nAll files are being extracted.')
