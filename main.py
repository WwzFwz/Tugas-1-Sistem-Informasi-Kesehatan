
import requests
import csv


url_api = "https://ghoapi.azureedge.net/api/SA_0000001445"

print("Mengirim permintaan ke API...")
response = requests.get(url_api)

if response.status_code == 200:
    data_json = response.json()
    records = data_json.get("value", [])
    csv_file = "liver_cancer_data_who.csv"

    if records:
        header = records[0].keys()
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            
            writer.writerows(records)
            
        print(f"Data berhasil disimpan ke {csv_file}")
    else:
        print("Data tidak ditemukan.")

else:
    print(f"Permintaan gagal dengan kode status: {response.status_code}")