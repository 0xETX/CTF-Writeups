# Tracking a CEO - Complete (Parts I-III)
Written by: 0xETX (0x03)

## Resources Used
1. Google Maps
2. Pinetools.com - Sharpen Image
3. Igram.io
4. DTMF Decoder (https://github.com/ribt/dtmf-decoder)
5. GHunt (https://github.com/mxrch/GHunt)
6. Sherlock (https://github.com/sherlock-project/sherlock)
7. CyberChef (https://gchq.github.io/CyberChef/)
8. CloudConvert

OSINT is one of the most useful assets in the InfoSec world. People leave behind more digital evidence than they realize - and this challenge is an example of just that. What starts from a fake name with no resources, leads to unmasking a real person. This writeup will follow the process used to unmask the OmniFlags CEO.

This challenge was originally split into 3 seperate parts during the Magpie 2022 CTF, but I have combined them all into this one report. Each following heading will take you through each seperate part of the 3 challenges.

## Part I
To start off the challenge, we're given the challenge prompt. Our objective is to uncover Mae Jelsworth's - a fake name for the OmniFlags CEO - real name.

What we're given is only her name, and the hint that we need to find a Wikipedia page on her hometown. So, the initial question is - where do we begin?

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/1.png "Prompt")

*Figure 1.0: Beginning the challenge with only a name.*

The first thing I always do when beginning an OSINT investigation with a name is to begin searching social media sites. Social media serves as a place where people *purposely* give out plenty of information about themselves. And the more information we have on someone, the more we have to work with!

Starting off, I begin searching for her name on Twitter. And fortunately enough, we discover just that!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/2.png "Mae's Twitter")

*Figure 1.1: Discovering Mae's twitter.*

While there wasn't anything super extrodinary in terms of information shared, the first thing that stood out was the text. A lot of the text was in different sizes and fonts, and I initally thought it stood for some type of code. So, I decided to look further into it.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/3.png "Interesting text?")

*Figure 1.2: Odd text featured on Mae's profile.*

After copying and pasting the text into word and seperating the two fonts, I ended up with text that didn't translate into anything. Even putting it through Cyberchef's magic function yielded nothing special.

Since I had no means to decode it if it meant anything, I decided to try looking at different media outlets.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/4.png "Unknown text from the twitter.")

*Figure 1.3: The odd text that appeared on Mae's twitter.*

Knowing that Mae used her Twitter username as "@MaeJelsworth", I decided to search for any other social media platforms that use the same username. Since it's common for people to use the same handle across different platforms, I find it's one of the most effective ways to perform OSINT.

To do this as efficiently as possible, I use a Python tool called "Sherlock". By supplying a username, Sherlock will look through countless media sites to find if a username exists. By supplying "MaeJelsworth" to Sherlock, I discovered an Instagram profile.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/30.png "Running Sherlock.")

*Figure 1.4: Using Sherlock to discover Mae's instagram.*

After using the supplied URL from Sherlock, we can observe Mae's profile. What immediately stands out are her 4 different posts.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/5.png "Mae's instagram.")

*Figure 1.5: Observing Mae's Instagram.*

Immediately, the first post that captures my attention is one of a building with the text "home <3". Since we're looking for her hometown, my first instict is to try to read the building name or phone number to get a location.

Unfortunately, as Figure 1.6 demonstrates, the image is far too blurry to make out.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/6.png "The interesting photo.")

*Figure 1.6: Attempting to read the building.*

To counter this, I download the Instagram image and used Pinetools to sharpen the image to be able to read it more clearly.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/7.png "Unsharpening the image.")

*Figure 1.7: Sharpening the image.*

After sharpening the image, we can start to clearly read the image!

The first thing I tried to look up was the building name, "Оренда". After throwing it through Google Translate, I realized it translated to "Rent" in Ukrainian. Knowing that it was a Ukrainian name in Cyrillic, it gave a decent direction of where to search.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/8.png "Viewing the building.")

*Figure 1.8: The sharpened image.*

The next thing I did was search up the phone number on the building, "050 430 3322". This lead to the discovery of a location called the "Dominant Plaza" in the Ukrainian city of Lviv.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/9.png "Dominant plaza.")

*Figure 1.9: Viewing "Dominant Plaza".*

In order to confirm that the location we were given is the correct one, I decided to double-check using Google Street View. After moving around just a tad bit, we find that the exact location Mae took the image of, confirming her home city!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/10.png "The 'rent' building.")

*Figure 1.10: Viewing the building in Mae's picture.*

The next step was to look up the city on WikiPedia.

Immediately, nothing in particular stands out, meaning that I might have to look deeper.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/11.png "Mae's home city.")

One of the neatest things about WikiPedia is the ability to review Revision History!

Revision History allows you to see all edits previously made on WikiPedia. Similar to GitHub history, this means that you may be able to find interesting information if you search enough.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/12.png "Revision history.")

*Figure 1.11: Reviewing Lviv's revision history.*

After looking through many revisions, I eventually find it! A flag for Part I and the lead to our next part.

On an additional note, if you want to look for specific strings, you can also use WikiBlame to find specific edits containing said information.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/13.png "Viewing revision history.")

*Figure 1.12: Finding the flag and a link to a discord server.*

## Part II

The most notable thing that occurs when joining the Discord named "The CEOs" is the need for a password. Without it, we can only see the "MaeJelsworth" user, but no other channels or text.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/14.png "Entering the Discord.")

*Figure 2.0: Entering Mae's Discord.*

The first thing that popped into my head was Mae's Instagram profile, where there was a video post with dial tones being pressed from a flip-phone. In that video description, she had also called the person a fellow CEO.

Discord is also widely used on phones, so it made me wonder - what if she was typing the password?

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/15.png "Viewing the Instagram post.")

*Figure 2.1: The Instagram post with the video.*

Using a Python program called the DTMF Decoder, we can decode the tones into key presses/numbers. The first thing I did was use Igram.io to download the image, then use CloudConvert to change it from MP4 to WAV.

After plugging the WAV file into the script, we get a string of "99586647". Initally, I thought this was the password, but a failed submission meant that I had to dig deeper.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/16.png "Finding the keys pressed.")

*Figure 2.2: Converting the dial tones into numbers.*

One of the things with flip-phones is that mutliple button presses are required to get some specific characters. Seeing 9 and 6 being repeated in groups made me think that this was what was happening. As a result, they weren't numbers - rather, they were characters.

Looking up a keypad online, I grabbed notepad and tried to convert the numbers to characters. After finishing the conversion, I got the string "xjtngp".

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/17.png "Converting the numbers to text.")

*Figure 2.3: Converting the numbers to characters.*

After posting the new string into the Discord chat, it unlocked and we were then revealed the second flag!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/18.png "Unlocking the Discord.")

*Figure 2.4: Unlocking Mae's Discord.*

## Part III

Once we unlocked Mae's Discord, our next steps were to use this information to discover Mae's identity.

I decided to start looking through the Discord to find identifying information, such as names or addresses. Unfortunately, all the Discord member's were revealed to be using fake names similar to Mae's, and searches using Sherlock (or manually) also yielded nothing for them either. I decided to look further.

Eventually, I discovered an interesting string of text, where Mae talks about a fall guy of hers being arrested. Since the fall guy was arrested, we have a real person who was apart of Mae's operation available to begin searching. I decided to look further to find more about the fall guy.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/19.png "Mae's fall guy.")

*Figure 3.0: Discovering interesting news regarding a relation to Mae.*

Eventually, it leads us to discover a new name - Myall Snowbird.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/20.png "Discovering the name of the fall guy.")

*Figure 3.1: Discovering the name of Mae's fall guy.*

Repeating my methodology from Part I, I begin to look for any social media that may belong to Myall.

As luck would have it again, I've once again discovered a new account with the same name!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/21.png "Myall's twitter.")

*Figure 3.2: Myall's Twitter.*

While Myall's profile didn't have anything too interesting from the get-go, his latest Tweet had 2 replies but only 1 visible.

Twitter has a feature that allows you to view hidden tweets, so I decided to try viewing this.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/22.png "Observing the Hidden Tweet button.")

*Figure 3.3: The hidden tweet button on Myall's profile.*

After clicking the hidden tweet button, we find a new tweet from a new account, Fla6 Crea70r. Since I had no other leads, I decided to look further into this account.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/23.png "Fla6's account.")

*Figure 3.4: Viewing the tweet from the new account.*

Initally from viewing Fla6's account, the thing that stood out the most was that it was written in a foreign language. After translating his tweets, we discover something interesting: the account seems to have been made for us, the investigator.

The account claims that they are worried about the company setting him as the fall guy, so they made this account as a trail to lead to the identity of Mae.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/24.png "The interesting tweet.")

*Figure 3.5: Viewing the start of Myall's interesting tweets.*

After viewing more, we have a very subtle hint to a future clue.

In this tweet, we see Fla6 mention that the CEO "has Pretty Good Privacy". While this might seem like they're making a general comment on the CEO's privacy, the key is the capitalization. They've been consistent on their grammar up to this, so this stands out in particular.

"Pretty Good Privacy" is actually an acronym for PGP. And this will be important when we view Fla6's hint.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/31.png "PGP Acronym.")

*Figure 3.6: A discreet hint from Fla6.*

As mentioned earlier, PGP is a hint to discovering more information and we see that especially true with a tweet with an 8-character hex.

For PGP, 8-character hexes are actually used as key signatures. They are kept short to make it more readable for other people in casual settings. Knowing this, we can begin the next steps.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/25.png "Fla6's hint.")

*Figure 3.7: The second part of Fla6's hint.*

Using that hex, we can discover a new Gmail account from "OmniCEO" by using the PGP Global Directory. Now, we can continue re-investigating Mae.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/26.png "Hunting for Mae's gmail.")

*Figure 3.8: Discovering Mae's gmail account with the PGP directory.*

With a Gmail address, we can perform OSINT on her Google account.

The main tool I use for Google OSINT is GHunt, where I can use her Gmail to find more details about her, or at least, this account.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/27.png "Using GHunt to find more about Mae.")

*Figure 3.9: Getting started to use GHunt on the account.*

After running GHunt, we find her name - Madelina Saharan!

Following what Fla6 said earlier about the CEO having PGP, I figured it's worth checking the PGP Directory once again.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/28.png "Discovering Madelina with GHunt.")

*Figure 3.10: Discovering the CEO's name.*

After re-using her name on the PGP Global Directory, we discover the flag and confirm this is indeed the CEO's name!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202022/Tracking%20a%20CEO%20(Complete)/Images/29.png "Revealing Madelina.")

*Figure 3.11: Obtaining the flag.*






