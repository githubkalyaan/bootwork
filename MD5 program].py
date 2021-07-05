import hashlib
def main():
    string=input("Enter the string :")
    url=string.encode("utf-8")
    a=hashlib.md5(url)
    word=a.hexdigest()
    print(word)
    return 0
main()

