import tkinter as tk
from tkinter import messagebox
import hashlib

# -------------------- BLOOM FILTER CLASS --------------------
class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate multiple hash values for the item"""
        hashes = []
        for i in range(self.hash_count):
            hash_value = int(hashlib.sha256((item + str(i)).encode()).hexdigest(), 16)
            hashes.append(hash_value % self.size)
        return hashes

    def add(self, item):
        """Add an item to the Bloom Filter"""
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def check(self, item):
        """Check if an item might be present"""
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))

# -------------------- APPLICATION LOGIC --------------------
class URLCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloom Filter - Safe URL Checker")
        self.root.geometry("500x400")
        self.root.config(bg="#f8f9fa")

        self.bloom = BloomFilter(size=2000, hash_count=4)
        self.safe_urls = []

        tk.Label(root, text="🌐 Bloom Filter URL Checker", font=("Helvetica", 16, "bold"), bg="#f8f9fa", fg="#0d6efd").pack(pady=10)

        tk.Label(root, text="Enter URL:", bg="#f8f9fa").pack()
        self.url_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.url_entry.pack(pady=5)

        tk.Button(root, text="Add to Safe List", command=self.add_url, bg="#198754", fg="white", width=18, font=("Arial", 11)).pack(pady=5)
        tk.Button(root, text="Check URL", command=self.check_url, bg="#0d6efd", fg="white", width=18, font=("Arial", 11)).pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f8f9fa")
        self.result_label.pack(pady=15)

        self.safe_list_box = tk.Listbox(root, width=50, height=8)
        self.safe_list_box.pack(pady=10)

    def add_url(self):
        url = self.url_entry.get().strip().lower()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL!")
            return
        if url in self.safe_urls:
            messagebox.showinfo("Duplicate", f"'{url}' is already in the safe list.")
            return
        self.safe_urls.append(url)
        self.bloom.add(url)
        self.safe_list_box.insert(tk.END, url)
        self.url_entry.delete(0, tk.END)
        self.result_label.config(text=f"✅ '{url}' added as safe!", fg="#198754")

    def check_url(self):
        url = self.url_entry.get().strip().lower()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL to check!")
            return
        if self.bloom.check(url):
            self.result_label.config(text=f"⚠️ '{url}' might be SAFE or a False Positive.", fg="#fd7e14")
        else:
            self.result_label.config(text=f"❌ '{url}' is NOT SAFE or unknown.", fg="#dc3545")

# -------------------- MAIN --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = URLCheckerApp(root)
    root.mainloop()
