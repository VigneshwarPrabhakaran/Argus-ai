
import gdown
import os

url = 'https://drive.google.com/uc?id=1VwViHDdc4W8t28rMiuGjxChiAtFxMAjN'
output = 'best_weights.h5'

if not os.path.exists(output):
    print(f"Downloading {output}...")
    gdown.download(url, output, quiet=False)
    print("Download complete.")
else:
    print(f"{output} already exists.")
