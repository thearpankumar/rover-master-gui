import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=1, column=1, padx=20)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("GUI Application")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.sidebar_frame.grid_rowconfigure(5, weight=3)
        self.sidebar_frame.grid_rowconfigure((6,7,8,9), weight=0)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.controller, text="Sabertooth Motor Controller")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.streaming, text="Video Streaming")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.communication, text="Serial Communication")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.visualizer, text="Maze Visualization")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))





    def controller(self):
        self.my_frame1 = MyFrame(master=self)
        self.my_frame1.grid(row=0, column=1, padx=20, pady=20, sticky="new")

        self.controller_button = customtkinter.CTkButton(self.my_frame1, command=self.dummy_func, text="SABERTOOTH CONTROLLER")
        self.controller_button.grid(row=0, column=1, padx=20, pady=20)


    def streaming(self):
        self.my_frame2 = MyFrame(master=self)
        self.my_frame2.grid(row=0, column=1, padx=20, pady=20, sticky="new")

        self.streaming_button = customtkinter.CTkButton(self.my_frame2, command=self.dummy_func, text="VIDEO STREAMING")
        self.streaming_button.grid(row=0, column=1, padx=20, pady=20)


    def communication(self):
        self.my_frame3 = MyFrame(master=self)
        self.my_frame3.grid(row=0, column=1, padx=20, pady=20, sticky="new")

        self.communication_button = customtkinter.CTkButton(self.my_frame3, command=self.dummy_func, text="SERIAL COMMUNICATION")
        self.communication_button.grid(row=0, column=1, padx=20, pady=20)


    def visualizer(self):
        self.my_frame4 = MyFrame(master=self)
        self.my_frame4.grid(row=0, column=1, padx=20, pady=20, sticky="new")

        self.visualizer_button = customtkinter.CTkButton(self.my_frame4, command=self.dummy_func, text="MAZE VISUALIZER")
        self.visualizer_button.grid(row=0, column=1, padx=20, pady=20)



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def dummy_func(self):
        print("YET TO BE UPDATED")



if __name__ == "__main__":
    app = App()
    app.mainloop()
