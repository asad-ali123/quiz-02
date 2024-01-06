import tkinter as tk
import requests

def send_to_api():
    data = {
        "name": name_entry.get(),
        "age": age_entry.get(),
        "city": city_entry.get()
    }
    response = requests.post('http://127.0.0.1:5000/api/data', json=data)
    result_label.config(text=response.json()["message"])

def update_data():
    # Delete previous data from MongoDB
    collection.delete_many({})

    # Delete previous data from label
    result_label.config(text="")

    # Add new data entered by the user
    send_to_api()

def upload_data():
    # Fetch all data from MongoDB
    all_data = collection.find()

    # Display all data on the label
    result_text = "\n".join([f"Name: {data['name']}, Age: {data['age']}, City: {data['city']}" for data in all_data])
    result_label.config(text=result_text)

root = tk.Tk()
root.title("Tkinter App with Flask and MongoDB")

# Entry Widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Buttons
send_button = tk.Button(root, text="Send Data", command=send_to_api)
send_button.pack()

update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack()

upload_button = tk.Button(root, text="Upload", command=upload_data)
upload_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
