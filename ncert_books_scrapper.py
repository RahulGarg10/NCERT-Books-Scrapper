import os
import httpx
import zipfile
import time

# Mapping boooks with their url end codes
books_with_linkcodes = {
    "Class_11_Maths_Part1": "kemh1dd",
    "Class_11_Physics_Part1": "keph1dd",
    "Class_11_Physics_Part2": "keph2dd",
    "Class_12_Maths_Part1": "lemh1dd",
    "Class_12_Maths_Part2": "lemh2dd",
    "Class_12_Physics_Part1": "leph1dd",
    "Class_12_Physics_Part2": "leph2dd"
}

def books_scrapper():
    # Setup working folders
    base_dir = "NCERT Books"
    os.makedirs(base_dir, exist_ok=True)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # Initialize connection pipeline
    base_url = "https://ncert.nic.in/textbook/pdf"
    with httpx.Client(headers=headers, timeout=1200.0) as client:
        for book_name, code in books_with_linkcodes.items():
            target_url = f"{base_url}/{code}.zip"
            zip_file_path = os.path.join(base_dir, f"{book_name}.zip")
            extraction_folder = os.path.join(base_dir, book_name)
            
            print(f"[INFO] Fetching full archive for {book_name}...")
            
            try:
                response = client.get(target_url)
                
                if response.status_code == 200:
                    # 1. Save the downloaded binary data as a .zip file
                    with open(zip_file_path, "wb") as f:
                        f.write(response.content)
                    print(f"[SUCCESS] Downloaded archive: {zip_file_path}")
                    
                    # 2. Extract the content automatically on-the-fly
                    print(f"[PROCESS] Unzipping chapters into '{book_name}/'...")
                    os.makedirs(extraction_folder, exist_ok=True)
                    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                        zip_ref.extractall(extraction_folder)
                    
                    # 3. Clean up the residual .zip file to save storage space
                    os.remove(zip_file_path)
                    print(f"[CLEANUP] Deleted raw zip file. Book files are organized.\n")
                    
                else:
                    print(f"[ERROR] NCERT returned an error code {response.status_code} for {book_name}\n")
                    
            except Exception as e:
                print(f"[CRITICAL] Connection failure on {book_name}: {e}\n")
                
            # Polite cooldown buffer for government infrastructure servers
            time.sleep(5)

if __name__ == "__main__":
    books_scrapper()
    print("[FINISHED] All requested Mathematics and Physics volumes are downloaded! as pdf at ", zip_file_path)
