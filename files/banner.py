import os
from rgbprint import gradient_print
import platform

logo = f"""
            ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗               
            ██║   ██║██║██╔══██╗██║   ██║██╔════╝               
            ██║   ██║██║██████╔╝██║   ██║███████╗               
            ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║               
             ╚████╔╝ ██║██║  ██║╚██████╔╝███████║               
              ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝               
                                                                
            ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
            ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
            ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
            ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
            ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
            ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                 Creator: Palău Liță Dinu        (V4.0)M.R.X
        =============================================================
                        [+] Github LitaDinu
                        [+] Instagram mrx_8990                          
        =============================================================
"""




def banner():
    gradient_print(logo , start_color='cyan' , end_color='yellow')


def clear():
    os.system("cls") if 'Windows' in platform.platform() else os.system("clear")
