import json
import ssl
import urllib.parse
import urllib.request

# ==========================================
# BLOCK 1: Secure SSL Certificate Bypass (Mac Fix)
# ==========================================
ssl._create_default_https_context = ssl._create_unverified_context

# ==========================================
# BLOCK 2: Collect User Input
# ==========================================
print("📚 WELCOME TO THE GOOGLE BOOKS SEARCH TOOL")
user_keyword = input("Enter a search keyword (e.g., 'python programming', 'history'): ")

# Safety check: Ensure the user didn't just hit enter
if not user_keyword.strip():
    print("Keyword cannot be empty. Exiting.")
    exit()

# Format the input keyword so it is safe to put inside a web URL line
encoded_keyword = urllib.parse.quote(user_keyword)

# URL targeting the Google Books volumes directory
url = f"https://www.googleapis.com/books/v1/volumes?q={encoded_keyword}"

# ==========================================
# BLOCK 3: Fetching and Parsing the API Data
# ==========================================
# ==========================================
# BLOCK 3: Fetching and Parsing the API Data (Network-Safe Variant)
# ==========================================
try:
    print(f"\n🔍 Searching Google Books for: '{user_keyword}'...")
    
    # 1. Create a request object and attach a standard browser identity header
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
    )
    
    # 2. Open using the modified request object instead of the raw URL string
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        book_items = data.get("items", [])
        
        # ==========================================
        # BLOCK 4: Formatting and Displaying Results
        # ==========================================
        if not book_items:
            print("❌ No books found matching that keyword. Try another search term.")
        else:
            print("\n==========================================")
            print(f"📖 TOP BOOK MATCHES FOR '{user_keyword.upper()}'")
            print("==========================================")
            
            for index, item in enumerate(book_items[:10], start=1):
                volume_info = item.get("volumeInfo", {})
                title = volume_info.get("title", "Unknown Title")
                authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
                
                print(f"{index}. Title: {title}")
                print(f"   Author(s): {authors}")
                print("-" * 40)
                
except Exception as e:
    print(f"\n❌ An error occurred while fetching data: {e}")
