import zipfile
from tqdm import tqdm

worldlist="D:\dictionary.txt"
zip_file="D:\\New Text Document.zip"
zip_file=zipfile.ZipFile(zip_file)

n_words=len(list(open(worldlist,"rb")))
print("total password test:",n_words)

with open(worldlist,"rb") as worldlist:
    for word in tqdm(worldlist,total=n_words,unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+]password found:",word.decode().strip())
            exit(0)
print("[!]Password not found,try other worldlist")