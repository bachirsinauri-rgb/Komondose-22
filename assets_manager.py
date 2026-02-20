import os

class AssetsManager:
    def __init__(self):
        self.base_dir = "assets"
        self.sub_dirs = ["icons", "fonts", "backgrounds"]
        self.setup_structure()

    def setup_structure(self):
        print("🎨 [ASSETS]: جاري بناء هيكل الموارد البصرية الفاخرة...")
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        for folder in self.sub_dirs:
            path = os.path.join(self.base_dir, folder)
            if not os.path.exists(path):
                os.makedirs(path)
        print(f"✅ [READY]: المجلدات {self.sub_dirs} جاهزة للاستيعاب.")

if __name__ == "__main__":
    manager = AssetsManager()
