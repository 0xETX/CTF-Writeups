# Mobile: Manager
Written by: 0xETX (0x03)

## Resources Used:
1. Bluestacks
2. Wireshark
3. Curl

We often see Web and Binary exploitation in CTFs. However, one of the more uncommon things is Mobile exploitation. Unfortunately, the Mobile App world has yet to catch up to Desktop software in terms of security, leaving them ripe for exploitation. In this challenge, we'll see an Android app being taken advantage of for weak security controls. I had a blast completing this challenge and this is definitley one of the ones I'm most proud to showcase.

## Getting Started
The first order of business is to launch the application in Bluestacks. The first thing we're prompted is for a server's IP Address and Port. This is needed to complete the challenge, as the challenge requires an instance of the app's server to function correctly.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/1.png "Server address information.")

*Figure 1.0: Starting prompt to connect to server.*

After connecting with the generated server's IP and Port, I run Wireshark in the background to check for any notable traffic while completing the challenge.

## Understanding the Application
The first thing we see after connecting is a prompt for login, alongside a "register" button.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/2.png "Viewing the default homepage.")

*Figure 2.0: The login page of the app.*

Before we can progress, the first thing it seems I'll need is an account, so I click register.

Thankfully, the registration process is easy, only requiring and username and password.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/3.png "Registering.")

*Figure 2.1: Registering with new account "a".*

After creating and logging into our newly registered account, we get a page that allows us to change our password.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/4.png "Password page.")

*Figure 2.2: Viewing the password update page.*

There is nothing else that the app seems to support functionaliy-wise, so I decided to take a look at my captured traffic.

And the very first thing I see is the registration page - in cleartext, with the username and password blatantly visible. It seems simple in functionality, where the app uses a POST request with the username and password in body to the register.php page to create an account.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/5.png "Viewing the cleartext registration."

*Figure 2.3: Viewing the traffic in cleartext.*

Knowing that the registration is in cleartext, I decide to see if the same thing occurs with the password update page. So, I log back into the "a" account and change the password to "helloWorld!".
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/6.png "Updating the password.")

*Figure 2.4: Updating "a"'s password.*

After checking the Wireshark capture, it is once again set in cleartext. It seems to work the exact same way as the previous capture, although this time it uses "manage.php" instead of register.

What I believe to be most likely at this point (as seen from the poor controls so far) is that the script simply just takes in the username and replaces it with the password it's given in the body text... Which gives me an idea of how to easily exploit this.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/7.png "Observing the manage.php capture.")

*Figure 2.5: Observing the packet capture.*

## The Attack
Using Curl and our old "a" account, I decide to do a test run on the account by filling out the text body with a new password (abc123) and using a POST request on the server's manage.php page. My theory here is that the page will update the password, regardless if I'm logged in or not.

After running the command, we get a very concerning message - "Password updated successfully."
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/8.png "Possible success?")

*Figure 3.0: A concerning message is present...*

After trying to log in with the new credentials, we find that it fortunately (unfortunate for the developers) works just as theorized - we are able to log in with "abc123" rather than "helloWorld!", meaning that I performed a password change without authentication.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/9.png "Using the new password to log in.")

*Figure 3.1: Successfully logging in with the password created through Curl.*

So, what do you do when you have the ability to change anyone's password without authentication? Obviously, go for an admin account!

Using the same Curl command as before while changing the username to "admin", we see that it runs successfully once again.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/10.png "Changing the admin's password."

*Figure 3.2: Changing the admin's password via Curl.*

And as expected, using the new password "abc123", we are able to successfully infiltrate the admin account and receive our well deserved flag!
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Mobile/Manager/Images/11.png "Hijacking the admin's account."

*Figure 3.3: Successfully logging into the administrator's account.*