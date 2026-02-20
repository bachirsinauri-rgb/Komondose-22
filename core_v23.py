import os
def activate():
    key = os.getenv("SECRET_LIFE_KEY")
    if key:
        print("V23.0 - Sovereignty Active | Satellite Link Secure")
    else:
        print("System Waiting for Secret Life Key...")
if __name__ == "__main__":
    activate()
