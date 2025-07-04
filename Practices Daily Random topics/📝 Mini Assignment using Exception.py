filename  = input(" Enter your file name ")
try:
    with open(filename , 'r') as file:
        content = file.read()
        print("📄 File Content:\n" , content)
except FileNotFoundError :
    print (" filename does not exists ")
except Exception as e :
    print("❌ Unexpected error:", e)
else : 
    print("✅ File read successfully.")
finally:
    print("🔚 File operation completed.")