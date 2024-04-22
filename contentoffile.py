filepath="file.txt"
try:
     with open(filepath,"r") as file:         
        content=file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"an error occurred:{e}")
finally:
    print("closing the file")