# Forensics: Reminiscent
Written by: 0xETX (0x03)

## Resources Used
1. Volatility
2. Base64 CLI Tool

Reminiscent is a medium-difficulty forensics challenge that involves a memory file of a Windows machine, along with a description that a possible resume file may be suspect. Using volatility, we can examine the memory image to determine the source of the infection.

## Getting Started
Before we begin, something to note is a text file we're given alongside the image file named "imageinfo.txt".

Something to note about this text file is the presence of "Suggest Profile(s)", which is something Volatility uses when examining images to account for differences between operating systems. In the file we're given, we can see that our suggested profiles are for either a Windows 7 or Windows Server 2008 machine. Since we know it's from a recruiter's virtual PC, we'll be going with the Windows 7 SP1 profile.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/1.png "Suggested profile.")

*Figure 1.0: Viewing the suggested profile of our image.*

## Investigating with Volatility
The first action I'll perform on the image with volatility is checking the processes using *pslist*. From here, I can make note of any notable processes that may be running, such as a strange .exe or .vba process.

At first, the processes look pretty normal.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/2.png "Viewing pslist.")

*Figure 2.0: Viewing processes with pslist.*

However, at the bottom of the list, I take note of a couple of PowerShell processes running. This is because Windows doesn't have any PowerShell scripts it runs on its own. Considering this is also a recruiter's PC, it's unlikely they ran it on their own. The two most likely cases is that either a PowerShell script is running because of IT policy, or that the computer has been compromised. Considering the situation, the second option seems the most likely.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/3.png "Viewing the PowerShell processes.")

*Figure 2.1: Investigating the intriguing PowerShell process.*

With my eyes being suspect of the PowerShell process, I decide to see if there's any network activity coming from the script. To view this, I used the Volatility module *netscan*.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/5.png "Running netscan.")

*Figure 2.2: Viewing any network activity in the image.*

As suspected, the PowerShell process is (or was) communicating with a foreign host. Notably, the PowerShell process was running on port 49246 on the machine, while communicating with the host at IPv4 address 10.10.99.55 over at port 80.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/6.png "Network activity from the PowerShell process.")

*Figure 2.3: Viewing network activity from the PowerShell process.*

Being very suspect of the PowerShell process, I decide to start looking for it's source.

Using *dumpfiles*, I look for any file with "resume" in the name due to the information we were given from the recruiter. After dumpfiles completed, we found two dumps from .lnk files for a file named "resume.pdf". What's fantastic about .lnk files in Windows is that you can see either startup execution code or see what was executed.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/7.png "Resume dumps.")

*Figure 2.4: Dumping the .lnk files from resume.pdf.*

I decide to then read the contents of the .lnk files to see if we can find anything interesting.

Immediately, we are presented with a PowerShell script that contained two seperate parts encoded in what appears to be Base64. I decide to copy these two portions and save it as a text file.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/8.png "Viewing an odd PowerShell script.")

*Figure 2.5: Viewing the contents of the script.*

Here, I start to decode the Base64 text using the Base64 CLI tool. The first code isn't anything too special. The only main thing to note is that it appears to read for a Base64 string, which will likely be the second portion.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/9.png "Decoding the B64.")

*Figure 2.6: Decoding the first Base64 string.*

The second part of the script becomes a lot more interesting, as it reveals another PowerShell script, except that it appears to run as a command line argument. Most notably, we observe another Base64 string.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/10.png "Viewing a third B64 encoding.")

*Figure 2.7: Viewing a third Base64 encoding.*

Finally, after decoding another Base64 encoded string, we are given the entire payload along with the flag. Hence, we have proven that the Resume file was indeed the source of the attack.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/Reminiscent/Images/11.png "Observing the flag.")

*Figure 2.8: Observing the decoded script.*