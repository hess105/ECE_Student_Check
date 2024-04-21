import customtkinter as ctk
import tkinter as tk
import csv

# Sets the theme of the window
ctk.set_appearance_mode("Dark")   
 
# Sets the color theme
ctk.set_default_color_theme("dark-blue")    
 
# App Class
class App(ctk.CTk):
    # The layout of the window will be written in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        # Sets the title of the window
        self.title("ECE ID Checker") 

        # Sets the dimensions of the window to wxh
        self.geometry(f"{1000}x{600}")

        # Card ID Entry Label
        self.nameLabel = ctk.CTkLabel(self, text="Card ID Entry")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
 
        # Card Entry Field
        self.cardEntry = ctk.CTkEntry(self, placeholder_text="10 digit ID or Card Reader format")
        self.cardEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        self.cardEntry.bind('<Return>', self.saveID)
 
        # Day of the Week Label
        self.nameLabel = ctk.CTkLabel(self, text="Day of the Week")
        self.nameLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
 
        # Gender Radio Buttons
        self.dowVar = tk.StringVar(value="ERROR NONE SELECTED")
 
        self.mondayRadioButton = ctk.CTkRadioButton(self, text="Monday", variable=self.dowVar, value="Monday")
        self.mondayRadioButton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
 
        self.tuesdayRadioButton = ctk.CTkRadioButton(self, text="Tuesday", variable=self.dowVar, value="Tuesday")
        self.tuesdayRadioButton.grid(row=1, column=2, padx=20, pady=20, sticky="ew")
         
        self.wednesdayRadioButton = ctk.CTkRadioButton(self, text="Wednesday", variable=self.dowVar, value="Wednesday")
        self.wednesdayRadioButton.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

        self.thursdayRadioButton = ctk.CTkRadioButton(self, text="Thursday", variable=self.dowVar, value="Thursday")
        self.thursdayRadioButton.grid(row=1, column=4, padx=20, pady=20, sticky="ew")

        self.fridayRadioButton = ctk.CTkRadioButton(self, text="Friday", variable=self.dowVar, value="Friday")
        self.fridayRadioButton.grid(row=1, column=5, padx=20, pady=20, sticky="ew")

        # Load ECE Database Button
        self.loadECEButton = ctk.CTkButton(self, text="Load ECE Database", command=self.loadECEdatabase)
        self.loadECEButton.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Load Daily Database Button
        self.loadDailyButton = ctk.CTkButton(self, text="Load Daily Database", command=self.loadDailyDatabase)
        self.loadDailyButton.grid(row=2, column=2, columnspan=2, padx=20, pady=20, sticky="ew")

        # Load Daily Database Button
        self.saveDailyButton = ctk.CTkButton(self, text="Save Daily Database", command=self.saveDailyDatabase)
        self.saveDailyButton.grid(row=2, column=4, columnspan=2, padx=20, pady=20, sticky="ew")
 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200, height=300)
        self.displayBox.grid(row=3, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

        # Init arrays
        self.eceDatabase: set[str] = set()
        self.dailyDatabase: set[str] = set()
        self.loadECEdatabase()
        self.displayBox.insert("3.0", "Please select a day and load the daily database\n")

        # Init recurring function to save daily database every 10 minutes
        self.after(10 * 60 * 1000, self.saveDaily)

    def saveDailyDatabase(self) -> None:
        self.after_cancel("saveDaily")
        self.saveDaily()

    def saveDaily(self) -> str:
        dow = self.dowVar.get()
        self.displayBox.delete("1.0", "end")
        if dow == "ERROR NONE SELECTED":
            self.displayBox.insert("1.0", "Failed to save daily database, no database loaded\n")
        else:
            self.csv_write(self.dowVar.get())
            self.displayBox.insert("1.0", f"Saved {dow} database\n")
            self.displayBox.insert("2.0", f"{len(self.dailyDatabase)} students\n")
        self.after(10 * 60 * 1000, self.saveDaily)
        return "saveDaily"

    def saveID(self, event: tk.Event) -> None:
        self.displayBox.delete("1.0", "end")
        id = self.cardEntry.get()
        if id.startswith(';'):
            id = id.split('=')[2]
        self.cardEntry.delete(0, "end")
        dow = self.dowVar.get()
        if dow == "ERROR NONE SELECTED":
            return self.displayBox.insert("1.0", "No daily database loaded, please load first\n")
        if len(id) != 10:
            return self.displayBox.insert("1.0", "Invalid ID format\n")
        if id not in self.eceDatabase:
            return self.displayBox.insert("1.0", "Not an ECE student\n")
        if id in self.dailyDatabase:
            return self.displayBox.insert("1.0", "Student already checked in today\n")
        self.dailyDatabase.add(id)
        self.displayBox.insert("1.0", f"Student {id} entered\n")
        self.displayBox.insert("2.0", f'{len(self.dailyDatabase)} students\n')

    def loadECEdatabase(self) -> None:
        self.displayBox.delete("1.0", "end")
        self.eceDatabase = self.csv_read("ece_database")
        self.displayBox.insert("1.0", "ECE Database Loaded\n")
        self.displayBox.insert("2.0", f"{len(self.eceDatabase)} students\n")

    def loadDailyDatabase(self) -> None:
        dow = self.dowVar.get()
        self.displayBox.delete("1.0", "end")
        if dow == "ERROR NONE SELECTED":
            self.displayBox.insert("1.0", "Please select a day first\n")
        else:
            self.dailyDatabase = self.csv_read(self.dowVar.get())
            self.displayBox.insert("1.0", f"{dow} Database Loaded\n")
            self.displayBox.insert("2.0", f"{len(self.dailyDatabase)} students\n")

    def csv_read(self, filename: str) -> set[str]:
        with open(f'records/{filename}.csv') as file:
            reader = csv.reader(file, delimiter=',', dialect='unix')
            return set(reader.__next__())

    def csv_write(self, filename: str) -> None:
        with open(f'records/{filename}.csv', 'w') as file:
            writer = csv.writer(file, delimiter=',', dialect='unix', quoting=csv.QUOTE_NONE)
            writer.writerow(self.dailyDatabase)

if __name__ == "__main__":
    app = App()
    app.mainloop()  
