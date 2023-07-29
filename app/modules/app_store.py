#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import os
import subprocess

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"


def reopen():
    window.destroy()
    os.system("pkexec /usr/bin/metterxp app_store")

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()
    

if not os.path.isdir("/usr/local/bin/metterxp/settings/lang/"):
    def lang_open():
        messagebox.showerror("Warning","Can't found language setting. When you click 'OK' and enter your true password, language settings will open. ")
        os.system("pkexec /usr/bin/metterxp mxp_options")
        exit()
    if os.path.isfile(debian):
        lang_open()
    elif os.path.isfile(fedora):
        lang_open()
    elif os.path.isfile(solus):
        lang_open()

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/usr/local/bin/metterxp/settings/theme/0.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
if os.path.isfile("/usr/local/bin/metterxp/settings/theme/0_1.txt"):
    bg="darkgrey"
    fg="#376296"
    button_bg="#FFFFFF"
    button_fg="#376296"
    a_button_bg="#376296"
    a_button_fg="#FFA500"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/1.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/2.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/3.txt"):
    bg="#808080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#808080"
    a_button_bg="#808080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/4.txt"):
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/5.txt"):
    bg="#FFA500"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FFA500"
    a_button_bg="#FFA500"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/6.txt"):
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/7.txt"):
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/8.txt"):
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/9.txt"):
    bg="#800080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/10.txt"):
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"
else:
    def theme_open():
        if os.path.isfile("/usr/local/bin/metterxp/settings/lang/en.txt"):
            messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' MetterXP settings will open.")
        elif os.path.isfile("/usr/local/bin/metterxp/settings/lang/tr.txt"):
            messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, MetterXP ayarları 'OK' tuşuna bastığınızda açılacaktır.")
        os.system("pkexec /usr/bin/metterxp mxp_options")
        exit()
    if os.path.isfile(debian):
        theme_open()
    elif os.path.isfile(fedora):
        theme_open()
    elif os.path.isfile(solus):
        theme_open()


window=Tk(className="MetterXP")
if os.path.isfile(lang_en):
    window.title("Application store | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Uygulama mağazası | MetterXP")
window.config(background=bg)
window.resizable(0, 0)
parent = Frame(window)
window.geometry("571x571")
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)
parent.pack(expand=1)


def main():
    def others():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        text1.destroy()
        space1.destroy()
        space2.destroy()
    def to_other():
        others()
        other()
    def to_flatpak():
        others()
        flatpak()
        
    def firefox():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install firefox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install firefox -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install firefox -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Mozilla Firefox was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall firefox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall firefox -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install firefox -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Mozilla Firefox was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge firefox* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove firefox* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove firefox -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Mozilla Firefox was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Mozilla Firefox browser?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Mozilla Firefox internet tarayıcısı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def brave():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install apt-transport-https curl")
                os.system(" curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
                os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"| tee /etc/apt/sources.list.d/brave-browser-release.list')
                os.system(" apt update")
                os.system(" apt install brave-browser")
            elif os.path.isfile(fedora):
                os.system(" dnf install dnf-plugins-core")
                os.system(" dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64")
                os.system(' rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc')
                os.system(" dnf install brave-browser")                
            elif os.path.isfile(solus):
                os.system(" eopkg install brave -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Brave was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall brave-browser -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall brave-browser -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install brave -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Brave was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge brave-browser* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove brave-browser* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove brave -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Brave rwas uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Brave browser?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Brave internet tarayıcısı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def vlc():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install vlc -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install vlc -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install vlc -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! VLC was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall vlc -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall vlc -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install vlc -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! VLC was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge vlc* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove vlc* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove vlc -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! VLC was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for VLC media player?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="VLC medya oynatıcıs için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def libreoffice():
        def it():
            if os.path.isfile(debian):
                os.system(" add-apt-repository ppa:libreoffice/ppa")
                os.system(" apt update")
                os.system(" apt install libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install libreoffice -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install libreoffice -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! LibreOffice was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall libreoffice -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install libtreoffice -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! LibreOffice was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge libreoffice* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove libreoffice* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove libreoffice -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! LibreOffice was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for LibreOffice office suite?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="LibreOffice ofis programı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def cups():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install cups -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install cups -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install cups -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Cups was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall cups -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall cups -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install cups -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Cups was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge cups* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove cups* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove cups -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Cups was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Cups printer manager?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Cups yazıcı yöneticisi için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def gparted():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install gparted -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install gparted -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gparted -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! GParted was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall gparted -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall gparted -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gparted -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! GParted was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge gparted* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove gparted* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove gparted -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! GParted was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for GParted disk part editor?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="GParted disk bölümü düzenleyicisi için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def gimp():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install gimp -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install gimp -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gimp -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! GIMP was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall gimp -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall gimp -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gimp -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! GIMP was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge gimp* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove gimp* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove gimp -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! GIMP was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for GIMP image manipulation?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="GIMP görüntü işleme programı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def wine():
        def it():
            if os.path.isfile(debian):
                os.system(" dpkg --add-architecture i386")
                os.system(" apt install wine-stable -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install wine -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install wine -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Wine was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall wine -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall wine -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install wine -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Wine was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge wine-stable* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove wine* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove wine -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Wine was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Wine?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Wine için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def plank():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install plank -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install plank -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install plank -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Plank was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall plank -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall plank -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install plank -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Plank was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge plank* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove plank* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove plank -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Plank was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Plank dock?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Plank rıhtımı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def yasfetch():
        def it():
            os.system("pkexec metterxp install_yasfetch")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Yasfetch was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yasfetch başarıyla kuruldu.")
        def reit():
            os.system("pkexec metterxp reinstall_yasfetch")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Yasfetch was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yasfetch başarıyla yeniden kuruldu.")
        def rm():
            os.system("pkexec metterxp uninstall_yasfetch")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Yasfetch was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yasfetch başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Yasfetch simple fetch application?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Yasfetch basit bilgi alma uygulaması için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    if os.path.isfile(lang_en):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which program do you want to install or reinstall or remove?")
        space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Mozilla Firefox browser",command=firefox)
        button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Brave browser",command=brave)
        button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="VLC media player",command=vlc)
        button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="LibreOffice office suite",command=libreoffice)
        button5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Cups printer manager",command=cups)
        button6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GParted disk part editor",command=gparted)
        button7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GIMP image manipulation",command=gimp)
        button8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Wine",command=wine)
        button9=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Plank dock",command=plank)
        button10=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yasfetch simple fetch application",command=yasfetch)
        space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 1")
        button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Other", command=to_other)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Flatpak", command=to_flatpak)    
    elif os.path.isfile(lang_tr):    
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangi programı kurmak veya yeniden kurmak veya kaldırmak istiyorsunuz?")
        space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Mozilla Firefox internet tarayıcısı",command=firefox)
        button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Brave internet tarayıcısı",command=brave)
        button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="VLC medya oynatıcısı",command=vlc)
        button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="LibreOffice ofis programı",command=libreoffice)
        button5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Cups yazıcı yöneticisi",command=cups)
        button6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GParted disk bölümü düzenleyicisi",command=gparted)
        button7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GIMP görüntü işleme programı",command=gimp)
        button8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Wine",command=wine)
        button9=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Plank rıhtımı",command=plank)
        button10=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yasfetch basit bilgi alma uygulaması",command=yasfetch)
        space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 1")
        button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Diğer", command=to_other)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Flatpak", command=to_flatpak)
    text1.pack(fill="x")
    space1.pack(fill="x")
    button1.pack(fill="x")
    button2.pack(fill="x")
    button3.pack(fill="x")
    button4.pack(fill="x")
    button5.pack(fill="x")
    button6.pack(fill="x")
    button7.pack(fill="x")
    button8.pack(fill="x")
    button9.pack(fill="x")
    button10.pack(fill="x")
    space2.pack(fill="x")
    button_1.pack(fill="x")
    button_2.pack(fill="x")

def flatpak():
    if not os.path.isfile("/usr/bin/flatpak") or not os.path.isfile("/bin/flatpak"):
        if os.path.isfile(lang_en):
            messagebox.showwarning("Warning","Flatpak can't found. When you click 'OK', package manager installer will be open.")
        elif os.path.isfile(lang_tr):
            messagebox.showwarning("Uyarı","Flatpak bulunamadı. 'OK' tuşuna bastığınızda paket yöneticisi yükleyicisi açılacaktır.")
        window.destroy()
        os.system("pkexec /usr/bin/metterxp pm_it")
    def packageit():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want nstalling a package, please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi kuracaksanız lütfen paket adını yazın.")
            return
        c1_package="flatpak install "
        get_packagename=packagename.get()
        c2_package=" -y"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagereit():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want reinstalling a package, please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi yeniden kuracaksanız lütfen paket adını yazın.")
            return
        c1_package="flatpak install "
        get_packagename=packagename.get()
        c2_package=" -y --reinstall"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")      
    def packagerm():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want uninstalling a package please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket kaldıracaksınız lütfen paket adını yazın.")
            return
        c1_package="flatpak uninstall "
        get_packagename=packagename.get()
        c2_package=" -y"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagesearch():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want searching a package, please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket aratacaksınız lütfen paket adını yazın.")
            return
        c1_package="flatpak search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)

        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")        
    if os.path.isfile(lang_en):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please enter the Flatpak package name.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Install",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Reinstall",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Uninstall",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Seacrh",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic italic", text="Lütfen Flatpak paketi adı giriniz.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kur",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Yeniden kur",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kaldır",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Ara",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Menüye dön", command=reopen)
    text2.pack(fill="x")
    space4.pack(fill="x")
    packagename.pack(fill="x")
    b_packageit.pack(fill="x")
    b_packagereit.pack(fill="x")
    b_packagerm.pack(fill="x")
    b_packagesearch.pack(fill="x")
    space5.pack(fill="x")
    reopen_button_1.pack(fill="x")

def other():
    def packageit():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want nstalling a package, please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi kuracaksanız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package=" apt install "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(fedora):
            c1_package=" dnf install "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(solus):
            c1_package=" eopkg install "
            get_packagename=packagename.get()
            c2_package=" -y"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagereit():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want reinstalling a package, please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi yeniden kuracaksanız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package=" apt reinstall "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(fedora):
            c1_package=" dnf reinstall "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(solus):
            c1_package=" eopkg install "
            get_packagename=packagename.get()
            c2_package=" -y --rei"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")      
    def packagerm():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want uninstalling a package please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket kaldıracaksınız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package=" apt purge "
            get_packagename=packagename.get()
            c2_package="* -y"
        elif os.path.isfile(fedora):
            c1_package=" dnf remove "
            get_packagename=packagename.get()
            c2_package="* -y"
        elif os.path.isfile(solus):
            c1_package=" eopkg remove "
            get_packagename=packagename.get()
            c2_package=" -y --purge"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagesearch():
        if packagename.get() == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You did not write anything, if you want searching a package, please write the package name.")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket aratacaksınız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package="apt search "
        elif os.path.isfile(fedora):
            c1_package="dnf search "
        elif os.path.isfile(solus):
            c1_package="eopkg search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(lang_en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(lang_tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return
        window_2=Toplevel()
        if os.path.isfile(lang_en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(lang_tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")        
    if os.path.isfile(lang_en):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please enter the name package name.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Install",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Reinstall",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Uninstall",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Seacrh",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic italic", text="Lütfen paket adı giriniz.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kur",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Yeniden kur",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kaldır",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Ara",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Menüye dön", command=reopen)
    text2.pack(fill="x")
    space4.pack(fill="x")
    packagename.pack(fill="x")
    b_packageit.pack(fill="x")
    b_packagereit.pack(fill="x")
    b_packagerm.pack(fill="x")
    b_packagesearch.pack(fill="x")
    space5.pack(fill="x")
    reopen_button_1.pack(fill="x")


main()
mainloop()