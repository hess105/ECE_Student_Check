from functions import read_card, getID
import customtkinter as ctk
import tkinter as tk

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to 
# the appearance mode of the system
ctk.set_appearance_mode("Dark")   
 
# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue    
ctk.set_default_color_theme("dark-blue")    
 
# App Class
class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        # Sets the title of the window
        self.title("ECE ID Checker") 

        # Sets the dimensions of the window to 600x700
        self.geometry(f"{600}x{700}")    
 
        # Name Label
        self.nameLabel = ctk.CTkLabel(self, text="Manual ID Entry")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
 
        # Name Entry Field
        self.manualEntry = ctk.CTkEntry(self, placeholder_text="0123456789")
        self.manualEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
 
        # Age Label
        self.nameLabel = ctk.CTkLabel(self, text="Card ID Entry")
        self.nameLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
 
        # Age Entry Field
        self.cardEntry = ctk.CTkEntry(self, placeholder_text=";000000000=1229=0032628840=01?")
        self.cardEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
 
        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                  text="Day of the Week")
        self.genderLabel.grid(row=2, column=0, 
                              padx=20, pady=20,
                              sticky="ew")
 
        # Gender Radio Buttons
        self.dowVar = tk.StringVar(value="4")
 
        self.mondayRadioButton = ctk.CTkRadioButton(self, text="Monday", variable=self.dowVar, value="1")
        self.mondayRadioButton.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
 
        self.tuesdayRadioButton = ctk.CTkRadioButton(self, text="Tuesday", variable=self.dowVar, value="2")
        self.tuesdayRadioButton.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
         
        self.wednesdayRadioButton = ctk.CTkRadioButton(self, text="Wednesday", variable=self.dowVar, value="3")
        self.wednesdayRadioButton.grid(row=2, column=3, padx=20, pady=20, sticky="ew")
 
        # Commit Manual Entry Button
        self.generateResultsButton = ctk.CTkButton(self, text="Log Snack Redemption (Manual)", command=self.generateResultsManual)
        self.generateResultsButton.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Commit Card Entry Button
        self.generateResultsButton = ctk.CTkButton(self, text="Log Snack Redemption (Card)", command=self.generateResultsCard)
        self.generateResultsButton.grid(row=5, column=2, columnspan=2, padx=20, pady=20, sticky="ew")
 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200, height=100)
        self.displayBox.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
 
 
    # This function is used to insert the details entered by users into the textbox
    def generateResultsManual(self):
        self.displayBox.delete("0.0", "200.0")
        text1, text2 = self.createTextManual()
        #text = self.createTextManual()
        self.displayBox.insert("0.0", text1)
        self.displayBox.insert("1.0", text2)

    def generateResultsCard(self):
        self.displayBox.delete("0.0", "200.0")
        entry1 = self.cardEntry.get()
        self.displayBox.insert("0.0", entry1 + "\n")
        entry2 = "Testing"
        self.displayBox.insert("0.0", entry2 + "\n")
 
if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()  


