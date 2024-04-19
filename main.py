from functions import extract_id
import customtkinter as ctk
import tkinter as tk

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
        self.geometry(f"{800}x{600}")    
 
        # Manual ID Entry Label
        self.nameLabel = ctk.CTkLabel(self, text="Manual ID Entry")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
 
        # Manual Entry Field
        self.manualEntry = ctk.CTkEntry(self, placeholder_text="0123456789")
        self.manualEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
 
        # Card ID Entry Label
        self.nameLabel = ctk.CTkLabel(self, text="Card ID Entry")
        self.nameLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
 
        # Card Entry Field
        self.cardEntry = ctk.CTkEntry(self, placeholder_text=";000000000=1229=0032628840=01?")
        self.cardEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
 
        # Day of the Week Label
        self.nameLabel = ctk.CTkLabel(self, text="Day of the Week")
        self.nameLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
 
        # Gender Radio Buttons
        self.dowVar = tk.StringVar(value="ERROR NONE SELECTED")
 
        self.mondayRadioButton = ctk.CTkRadioButton(self, text="Monday", variable=self.dowVar, value="Monday")
        self.mondayRadioButton.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
 
        self.tuesdayRadioButton = ctk.CTkRadioButton(self, text="Tuesday", variable=self.dowVar, value="Tuesday")
        self.tuesdayRadioButton.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
         
        self.wednesdayRadioButton = ctk.CTkRadioButton(self, text="Wednesday", variable=self.dowVar, value="Wednesday")
        self.wednesdayRadioButton.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

        self.thursdayRadioButton = ctk.CTkRadioButton(self, text="Thursday", variable=self.dowVar, value="Thursday")
        self.thursdayRadioButton.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

        self.fridayRadioButton = ctk.CTkRadioButton(self, text="Friday", variable=self.dowVar, value="Friday")
        self.fridayRadioButton.grid(row=2, column=5, padx=20, pady=20, sticky="ew")
 
        # Commit Manual Entry Button
        self.generateResultsButton = ctk.CTkButton(self, text="Log Snack Redemption (Manual)", command=self.generateResultsManual)
        self.generateResultsButton.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Commit Card Entry Button
        self.generateResultsButton = ctk.CTkButton(self, text="Log Snack Redemption (Card)", command=self.generateResultsCard)
        self.generateResultsButton.grid(row=5, column=2, columnspan=2, padx=20, pady=20, sticky="ew")
 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200, height=300)
        self.displayBox.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
 
 
    # This function is used to insert the details entered by users into the textbox
    def generateResultsManual(self):
        self.displayBox.delete("0.0", "200.0")

        dow = self.dowVar.get()
        text1 = "Day of the Week: " + dow + "\n"

        card_id = self.manualEntry.get()
        if (len(card_id) != 10):
            text2 = "ID: " + "ERROR LENGTH" + "\n"
        else:
            text2 = "ID: " + card_id + "\n"

        # NEED TO ADD
        text3 = ""
        #ece_student = is_ece_student(card_id)  
        #if (is_ece_student):
        #    text3 = "ECE Student: " + "Yes" + "\n"
        #else:
        #    text3 = "ECE Student: " + "No" + "\n"

        text4 = ""
        #redeemable = is_redeemable(card_id, dow)
        # if (redeemable):
        #     text4 = "Redeemable: " + "Yes" + "\n"
        # else:
        #     text4 = "Redeemable: " + "No" + "\n"

        text5 = ""
        #logged = log_snack_redemption(card_id, dow)
        # if (logged):
        #     text5 = "Logged: " + "Yes" + "\n"
        # else:
        #     text5 = "Logged: " + "No" + "\n"

        text = text1 + text2 + text3 + text4 + text5
        self.displayBox.insert("0.0", text)
  

    def generateResultsCard(self):
        self.displayBox.delete("0.0", "200.0")

        dow = self.dowVar.get()
        text1 = "Day of the Week: " + dow + "\n"

        card_id = extract_id(self.cardEntry.get())
        if (len(self.cardEntry.get()) != 30):
            text2 = "ID: " + "ERROR LENGTH" + "\n"
        else:
            text2 = "ID: " + card_id + "\n"

        text = text1 + text2

        self.displayBox.insert("0.0", text)
 
if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()  


