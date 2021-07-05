import hashlib
def main():
    text=input("Enter the string :")
    url=text.encode("utf-8")
    hash=hashlib.md5(url)
    hexa=hash.hexdigest()
    print(hexa)
    return 0
main()

