# Upgrades
Written by: 0xETX (0x03)

## Resources Used
1. Applications: Microsoft PowerPoint, WinRAR
2. Editors: HxD

Upgrades is a reversing challenge that was available during the HackTheBox University CTF 2021. This challenge is centered around a suspicious PowerPoint Macro-Enabled Presentation (.pptm) file. The flag is hidden within the macro, however, the macro is password protected.

## Getting Started
The first thing that stands out with this challenge upon first glace is that there is PowerPoint Macro-Enabled Presentation (.pptm) file. Normally, in any situation involving suspicious files, macros should not be run on live machines due to the risk of malware, system compromise, etc. As this is just a CTF challenge, that risk is not a concern - however, in any other situation, these types of files should be contained in a secure forensic/reversing enviorment when contents are not known or known to be malicious.

That being said, after running the file, one of the first things you'll see is the following:

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/1.png "Macro security warning.")

*Figure 1.0: The default security settings disabling the macro from running.*

In this case, we can enable the macro as the file is safe.

When heading to the macro editor, you'll notice immediately that there is a macro named "OnSlideShowPageChange". We'll attempt to edit it.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/2.png "Viewing the macros on this document.")

*Figure 1.1: Viewing the macros on this document.*

Once clicking "edit", the following shows up:

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/3.png "VBAProject Password.")

*Figure 1.2: Blocked from viewing the macro due to the VBA Project password.*

Unfortunately, we now know that in order to proceed further in the challenge, we must get past the protected project. Guessing the password can be a solution, but brute-forcing can be both lengthy and ineffective. So, what is the best way to proceed?

## Unlocking the Document

Something that the average person may not know about Microsoft Office documents is that many of them are actually structured similar to a ZIP file. Using a ZIP program will allow you to view each component of the file - including the VBAProject. To begin, we'll open the PowerPoint document using WinRAR.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/4.png "Opening the file using WinRAR.")

*Figure 2.0: Viewing the listing of files in the PowerPoint file.*

After a bit of exploring, we come across what we're looking for - **vbaProject.bin**. We'll extract this file and open it on HxD, a hex editor. As the file is password protected, this means the contents are encrypted, signifying that we will not be able to view any cleartext of the script just yet. However, this is where the key part of this challenge begins. First, we'll look for the string "**DPB=**".

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/5.png "Viewing the vbaProject.bin file.")

*Figure 2.1: Viewing the vbaProject.bin file in HxD with the "DPB=" string.*

The reason we're looking for this string in particular is because this is what Word/PowerPoint/Excel etc. use for password authentication on macros. We'll change this string to "**DBx**". This will be important later on. For now, save the file and close HxD.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/6.png "Editing the vbaProject.bin file.")

*Figure 2.2: Editing the vbaProject.bin file.*

Now, replace the old vbaProject.bin file with the new vbaProject.bin file by adding it to the PowerPoint file using your ZIP program again.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/7.png "Replacing the vbaProject.bin file.")

*Figure 2.3: Replacing the vbaProject.bin file.*

When you next open the PowerPoint document, you'll get an interesting dialogue box from PowerPoint telling you that the file contains "**...invalid key 'DPx'**". Select 'Yes'. You may be prompted with more dialogue boxes, but just keep clicking "Okay" and head to the Editor. After you're in the VBA Editor, go to "Tools" -> "VBAProject Properties".

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/8.png "The interesting dialogue box.")

*Figure 2.4: An interesting dialogue box that informs the user of an invalid key.*

After you open the menu and go to "Protection", you'll notice the dialogue box in Figure 2.5. This is because PowerPoint will actually allow you to set a new **password** over the invalid key. By changing the DPB key to DPx, we created an invalid key which could not be understood by PowerPoint. And, as a result, PowerPoint ignores the old password and allows the user to overwrite the password.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/9.png "PowerPoint allowing you to add a new password.")

*Figure 2.5: Overwriting the old password with a new password.*

Finally, you'll be able to view the contents of the macro.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/10.png "Viewing the macro contents.")

*Figure 2.6: Viewing the contents of the macro.*

After a bit of looking at the script, you may notice that the string "q" is used a lot. In addition to this, the string seems to take in characters through some obfuscated means. Since I want to read the output "q" produces in these operations, I'll add "**Debug.Print(q)**" to the macro and run it.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/11.png "Editing the macro.")

*Figure 2.7: Editing the macro.*

And finally, after running the macro, we conclude the challenge by seeing the flag outputted in the Immediate console!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Universities%20CTF%202021/Upgrades/Images/12.png "The flag outputted.")

*Figure 2.8: The outputted flag.*