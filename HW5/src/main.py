import tkinter as tk
from tkinter import messagebox, Menu
from requests import get

# Match the port used by your HW4 proxy
PROXY_SERVER_URL = "http://127.0.0.1:5000"

class WeatherClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Weather Information Client")
        master.configure(bg="white")

        # Main layout container
        main_frame = tk.Frame(master, bg="white")
        # Header label at the very top
        self.header_label = tk.Label(master, text="Weather Information Client", font=("Arial", 18, "bold"), fg="black", bg="white")
        self.header_label.pack(fill='x')
        main_frame.pack(fill='both', expand=True)

        # Sidebar frame (left)
        sidebar_frame = tk.Frame(main_frame, width=200, bg="white")
        sidebar_frame.pack(side='left', fill='y')

        # Display frame (right)
        display_frame = tk.Frame(main_frame, bg="#5CC6F5")
        display_frame.pack(side='right', fill='both', expand=True)

        # Weather data labels container
        self.label_frame = tk.Frame(display_frame, height=150, bg="#5CC6F5")
        self.label_frame.pack_propagate(False)
        self.label_frame.pack(pady=10, fill='x')

        # Weather display labels
        self.temp_label = tk.Label(self.label_frame, font=("Arial", 14), fg="white", bg="#5CC6F5")
        self.temp_label.pack(pady=2)

        self.humidity_label = tk.Label(self.label_frame, font=("Arial", 14), fg="white", bg="#5CC6F5")
        self.humidity_label.pack(pady=2)

        self.wind_label = tk.Label(self.label_frame, font=("Arial", 14), fg="white", bg="#5CC6F5")
        self.wind_label.pack(pady=2)

        self.airq_label = tk.Label(self.label_frame, font=("Arial", 14), fg="white", bg="#5CC6F5")
        self.airq_label.pack(pady=2)

        # Action buttons in sidebar
        self.temp_button = tk.Button(sidebar_frame, text="Temperature", command=lambda: self.get_data("temp"), bg="white", fg="black", activebackground="#cceeff", relief="groove", borderwidth=2)
        self.temp_button.pack(pady=5, padx=10, fill='x')

        self.humidity_button = tk.Button(sidebar_frame, text="Humidity", command=lambda: self.get_data("humidity"), bg="white", fg="black", activebackground="#cceeff", relief="groove", borderwidth=2)
        self.humidity_button.pack(pady=5, padx=10, fill='x')

        self.wind_button = tk.Button(sidebar_frame, text="Wind", command=lambda: self.get_data("wind"), bg="white", fg="black", activebackground="#cceeff", relief="groove", borderwidth=2)
        self.wind_button.pack(pady=5, padx=10, fill='x')

        self.airq_button = tk.Button(sidebar_frame, text="Air Quality", command=lambda: self.get_data("airq"), bg="white", fg="black", activebackground="#cceeff", relief="groove", borderwidth=2)
        self.airq_button.pack(pady=5, padx=10, fill='x')

        self.show_all_button = tk.Button(sidebar_frame, text="Show All", command=self.show_all, bg="white", fg="black", activebackground="#cceeff", relief="groove", borderwidth=2)
        self.show_all_button.pack(pady=15, padx=10, fill='x')

        # Menu
        menu = Menu(master)
        master.config(menu=menu)
        data_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Select Metric", menu=data_menu)
        data_menu.add_command(label="Temperature", command=lambda: self.get_data("temp"))
        data_menu.add_command(label="Humidity", command=lambda: self.get_data("humidity"))
        data_menu.add_command(label="Wind", command=lambda: self.get_data("wind"))
        data_menu.add_command(label="Air Quality", command=lambda: self.get_data("airq"))
        data_menu.add_separator()
        data_menu.add_command(label="Show All", command=self.show_all)

        # On load, show all data
        self.show_all()

    def show_all_labels(self):
        self.temp_label.pack(pady=2)
        self.humidity_label.pack(pady=2)
        self.wind_label.pack(pady=2)
        self.airq_label.pack(pady=2)

    def show_all(self):
        self.header_label.config(text="Weather Overview")
        self.show_all_labels()
        self.get_data("temp", update_all=True)
        self.get_data("humidity", update_all=True)
        self.get_data("wind", update_all=True)
        self.get_data("airq", update_all=True)

    def hide_others(self, visible):
        # Hide all, then show the one requested
        self.temp_label.pack_forget()
        self.humidity_label.pack_forget()
        self.wind_label.pack_forget()
        self.airq_label.pack_forget()

        if visible == "temp": self.temp_label.pack(pady=10)
        elif visible == "humidity": self.humidity_label.pack(pady=10)
        elif visible == "wind": self.wind_label.pack(pady=10)
        elif visible == "airq": self.airq_label.pack(pady=10)

    def get_data(self, metric, update_all=False):
        try:
            url = f"{PROXY_SERVER_URL}/{metric}"
            response = get(url)
            if response.status_code == 200:
                data = response.json()

                if not update_all:
                    display_map = {
                        "temp": "Temperature",
                        "humidity": "Humidity",
                        "wind": "Wind",
                        "airq": "Air Quality"
                    }
                    self.header_label.config(text=display_map.get(metric, "Weather Overview"))

                if metric == "temp":
                    text = f"Temperature: {data['current']}°F (Feels like: {data['feels like']}°F)"
                    self.temp_label.config(text=text)
                    if not update_all: self.hide_others("temp")

                elif metric == "humidity":
                    text = f"Humidity: {data['humidity']}%"
                    self.humidity_label.config(text=text)
                    if not update_all: self.hide_others("humidity")

                elif metric == "wind":
                    text = f"Wind: {data['wind']} mph"
                    self.wind_label.config(text=text)
                    if not update_all: self.hide_others("wind")

                elif metric == "airq":
                    text = f"Air Quality Index: {data['air quality']}"
                    self.airq_label.config(text=text)
                    if not update_all: self.hide_others("airq")

            else:
                messagebox.showerror("Error", f"Failed to retrieve data: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    gui = WeatherClientGUI(root)
    root.geometry("600x400")
    root.mainloop()
    