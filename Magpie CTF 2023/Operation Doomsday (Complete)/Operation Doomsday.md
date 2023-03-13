# Operation Doomsday - Complete (Parts I-II)
Written by: 0xETX (0x03)

## Resources Used
1. Google Maps
2. Tweetdeck
3. Wikipedia
4. Google Search
5. Twitter
6. Instagram
7. GitHub

OSINT is a valuable resource for various fields in cybersecurity. The ability to find information about anything or anyone can change the outcome of your investigation or pentest, and this is one such example of that.

Through both parts of this CTF challenge, you'll be taken through the methodology used to uncover OmniFlags CEO Trenton Blackwell and disarm his doomsday device, alongside some lessons learned and pitfalls I fell through.

## Part I
To begin, we must first examine the requirements of this challenge. As we can see below, we are told that OmniFlags - the nefarious company in the last CTF - now has a new CEO, Trenton Blackwell. Apparently, Trenton has set up a Doomsday Device on some unknown planet. Our job is to recover the location of said planet.

Unfortunately, outside of our objective, we aren't given much further information to work with. So, let's begin by checking the biggest infodumps of OSINT - people. And in this case, that would be Trenton.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/1.png "Prompt")

*Figure 1.0: The CTF challenge prompt.*

One the first places I enjoy checking for OSINT is Twitter. There are few other places that people like to dump as much information about themselves as they do on Twitter - and in just 280 characters or less!

I begin my search on Twitter by just search the name "Trenton Blackwell." As you can see below, there are multiple profiles that come up under this name. Let's see what they uncover...

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/2.png "Twitter Search Results")

*Figure 1.1: Results from the Twitter search.*

While looking through all of these profiles, you'll notice that there isn't much information indicating that the Trenton Blackwells aren't the same as our "lovely" OmniFlags CEO. After all, investigating the wrong person can waste you a lot of time, especially when it comes to OSINT.

Eventually, I got to the @T_Blackwell38 profile. Needless to say, he's not very discrete about his position at all and we know we have the right guy. We see in his second tweet that someone named "Andre Ahman" had attempted to expose him. I wonder what that means? Additionally, there seems to be a reply to this tweet...

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/3.png "Looking at Trenton's Twitter profile")

*Figure 1.2: Analyzing Trenton's twitter profile.*

Unfortunately, after clicking "Show More Replies", the replies show up blank. Checking the Wayback Machine to see if the replies were saved or deleted reveals that there are no archives either. So at this point, it's time to do some research!

Apparently, it's possible for tweet authors to mute replies to their tweets. Is there a way for us to view these tweets?

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/4.png "Analyzing Trenton's tweet")

*Figure 1.3: Analyzing Trenton's odd tweet.*

Turns out, there is - and very easily too! After messing around with some Twitter restriction settings and using Tweetdeck, I now have the ability to "View hidden replies" to this tweet.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/5.png "Selecting view hidden replies")

*Figure 1.4: Enabling the hidden tweets.*

And - aha! We see our good friend Andre has replied to the tweet. This tweet was likely hidden by Trenton himself, as Twitter allows tweet authors to do so.

Andre tells us to "check the place the code is hidden". But, what does that mean? There is only one place that immediately comes to mind... GitHub, a code repository platform.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/6.png "Andre saves the day!")

*Figure 1.5: Viewing the hidden tweet.*

So, we go over to GitHub. The first thing I search for is "Trenton Blackwell", as that is one of most clear queries we have.

And, we immediately find what we're looking for! A code repository on "TrentonBlackwell" by "AndreAhman".

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/7.png "Finding the GitHub repo")

*Figure 1.6: Discovering Andre's GitHub repository.*

Unfortunately, we immediately see that the GitHub page as been griefed - this is evidenced by the very unsubtle message on the repo, along with the fact this update is made by a "c30-bwell", which likely stands for "Blackwell".

However - not all hope is lost yet! We still have many ways to go back in time - one is native to GitHub (by viewing commit history) and if we need to, we can check archive sites like Wayback Machine. We'll begin by checking commits.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/8.png "The griefed GitHub page")

*Figure 1.7: Viewing the griefed GitHub page - not all hope is lost yet though!*

As I expected, the GitHub commits tell us exactly what we are looking for! Observing the screenshot below, we can see Ahmed has left us with critical information - a location for Trenton's blog (URL) and a hint on his password.

Unfortunately, we do not have any of the information Ahmed has supplied us - his pet's name, his mother's maiden name, his favourite food, his favourite place in the world and finally, his birthyear. Looks like we'll have to find this information elsewhere, as there is no further information on Trenton's Twitter or the GitHub.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/9.png "A hint to the next steps.")

*Figure 1.8: Discovering the mysterious blog - but more info is needed!*

Alongside Twitter, my second favourite place to look for OSINT is Instagram. Similar to Twitter, many people tend to post a lot of information about themselves (or who they know) on this platform.

As such, I begin by searching for the name "Trenton Blackwell" in the search bar. And fortunately, looks like we have some results!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/10.png "Instagram accounts discovered")

*Figure 1.9: Discovering accounts with the name "Trenton Blackwell".*

After browsing through some of the results, we finally end up with this profile of "Trenton Blackwell". While the name matches, how do we *really* know that this is the Trenton we're looking for?

Well, while this wouldn't be your traditional way of verifying someone's identity in a real world scenario, ultimately, it came down to seeing that the account was created in-between this MagpieCTF and the last, along with some of the very robotic and clear signs of things that indicate his password hints.

So, let's get to cracking this password!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/11.png "Finding Trenton")

*Figure 1.10: Discovering Trenton's instagram account.*

The first thing that sticks out to me is Trenton's followers and the accounts he is following. One look, and we see several different names. We can assume by the mutual follows that these people are important to Trenton.

And since they are important to Trenton, there's a good chance we may find some information on their profiles about him...

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/12.png "Trenton's followers")

*Figure 1.11: Discovering people that are close to Trenton.*

The next thing I begin to look at Trenton's profile are his pictures. Immediately, we find critical information about Trenton - his favourite food!

This means that we have cracked on part of the password - his favourite food, which is shrimp. Right now, our password is: *x_x_shrimp_x_x*, where x = unknown.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/13.png "Discovering Trenton's favourite food")

*Figure 1.12: Discovering Trenton's favourite food.*

Looking through the rest of the pictures on Trenton's page reveals nothing too notable (yet!). So, our next lead is to begin checking some of Trenton's friends.

The first friend I check is "lucky_carps68". Upon observing their page, we see they posted a picture of the cat. Upon clicking the image, we find out it is actually Trenton's cat! Talk about convenient.

And now, our password is: *oliver_x_shrimp_x_x*.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/14.png "Finding out Trenton's cat's name")

*Figure 1.13: Discovering the name of Trenton's cat.*

The next follower we observe is "o_walters73". Just like lucky_carps, they make our investigation easy for us by having one picture and it being about Trenton! I'm starting to think Trenton doesn't actually have any friends, and he made these accounts to make himself feel better. Brutal.

Anyways, we see on the birthday cake picture that apparently Trenton turned 55 in December 2022 (based on the picture upload date). We do some quick maths, 2022 (year of birthday) - 55 (Trenton's age), and we can assume that Trenton was born in 1967.

Now, we have the majority of our password discovered with: *oliver_x_shrimp_x_1967*.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/15.png "Discovering Trenton's age")

*Figure 1.14: Using the power of math to discover Trenton's birthyear.*

Unfortunately, we don't find any further information on the other follower's accounts. However, one account - lazerblackwell - is following a "ctblackwell38", which is not one discovered on the previous list. Let's investigate.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/16.png "Checking out lazerblackwell.")

*Figure 1.15: Finding a new account.*

And boom! We have discovered that ctblackwell38 is actually Trenton's mom (for some reason he is not following.)

Upon looking at her bio, we see that one line specifically says "formerly Catheryn Olson". This means that either Trenton's mom's maiden name is Olson, or Catheryn's ex-husband may live rent-free in her head.

Now, we only have one part of the password left: *oliver_olson_shrimp_x_1967*.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/17.png "Catheryn Olson")

*Figure 1.16: Discovering Trenton's mother's maiden name.*

The last part of the password is supposedly Trenton's favourite place in the world. Going back to his profile, we can see this one picture where he discusses the best day of his life, where he met his wife.

While this may appear to be his favourite place - it actuallly isn't, which will be clarified later! However, don't let this image slip your mind just yet - it is still important!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/18.png "The mysterious place")

*Figure 1.17: Discovering a very notable picture.*

After running through each profile and coming up with a dead-end, I check the last thing I can on Trenton's profile - his tags.

And lo-and-behold, we discover something! A post by a j_robles55, featuring Trenton as seen by his comment. Ignoring that Trenton is apparently a shapeshifting lizardman or just ages very poorly, we see that he uses the phrase "vacation was my favourite place in the world.".

Now, we just need to discover where this vacation occured! Unfortunately, we see no direct clues or geotagging on the picture, so we'll have to dig further. Let's begin with j_robles55's profile, as we haven't seen this yet.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/19.png "Trenton's new friend")

*Figure 1.18: Trenton's new friend.*

Upon observing j_robles55's profile, we can see only one notable thing other than the post - and that is that he is following Cristiano Ronaldo.

The only clue that I have here is that Cristiano is Portugese. So, if j_robles55 loves Portugal as much as he loves Ronaldo, why not go for it's capital, Lisbon?

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/20.png "Messi is better btw")

*Figure 1.19: Observing j_robles55's following.*

And upon inserting the passcode "oliver_olson_shrimp_lisbon_1967"... we're in!

We have entered the locked site. It's time to investigate this blog...

The first thing we are prompted with is an endless series of QR Codes with dates. What could these mean?

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/21.png "Entering the blog")

*Figure 1.20: The front page of the blog.*

After moving to the end of the blog, we discover the first coordinate and the flag of the challenge. However, we now have a new problem...

In order to obtain the Y-axis, we now have to figure out Trenton's favourite day. And according to the CTFd challenge page, we only have 5 tries before we lose this challenge for good.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/22.png "The end of the first challenge")

*Figure 1.21: Ending the first part of this challenge.*

## Part II

Remember that picture from earlier? If not, here it is again below.

Trenton specifically said that this was his favourite day of his life. So, the first thing I do is go to the QR Code of the date it was posted, December 10th - and I'm wrong! Four more attempts to go.

Something that is worth noting is that Trenton describes the time of the post as "roughly" for his favourite day, so let's see what else we can do to narrow down the date a bit closer. The first thing I observe is the text on the sign, "Being Human". This event apparently takes place on "29 April - 22 May", so let's see if we can find more about it using the power of Google!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/18.png "Reviewing the old post from earlier")

*Figure 2.0: Reviewing the post from earlier.*

Using a bit of Google-Fu, I search "being human" "29 April - 22 May" using quotation marks. This makes Google strictly look for these terms, which will allow us to get more specific results.

The first thing we discover is that it is apparently a theme for Photo event, that takes place in Melbourne. We're slowly getting somewhere!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/23.png "Discovering the location of the event.")

*Figure 2.1: Discovering the location of the event.*

Unfortunately, Melbourne is a pretty big place. So, what else can we look for?

In the picture we looked at the start of this part, we can see in the background something that appears to be a resturant with some words written on the glass. Unfortunately, the words are hard to read with the pixilation and cursive, but it appears to say something among the lines of "federuci".

Since we know this place is likely in Melbourne, we can use Google Maps to search for this place. Even if it is incorrect, Google Maps will show us the next closest result... and it does, as we discover a place named "Federici" in Melbourne.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/24.png "Discovering Federici")

*Figure 2.2: Discovering Federici.*

Upon looking at Google Maps for Federici, we find something interesting. Apparently, Federici isn't on its own - it's actually apart of a bigger building, called "The Princess Theatre"!

Since we now have a location, let's check Google Street View to see if we got the correct place.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/25.png "An interesting discovery")

*Figure 2.3: Learning more about Federici.*

And what do you know - we have found the place! We also get to observe a larger area, and we can see the attached Princess Theatre - the building screening "Harry Potter and the Cursed Child".

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/26.png "Google Street View")

*Figure 2.4: Confirming we have gotten the correct place with Google Street View.*

While it's great that we have discovered more about the place including the location, it's not enough to figure out what Trenton's best day of his life was. Let's take a step back and see if we can find more details.

Something that now feels a lot more noticable on the original post is the quotation. Why is it here?

With the context that there is also a theatre here, is it possible that this could be a quote from a play? There's only one way to find out.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/27.png "Backtracking our steps")

*Figure 2.5: Re-observing a notable quote.*

Upon searching Google with this quote, we figure out that it is indeed a quote from a very well-known play - Les Misérables.

It's very possible that Trenton is quoting a play that he may have seen on his special day. Now we're getting somewhere!

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/28.png "Finding out about the play")

*Figure 2.6: Tracing back our steps to a specific play.*

Now that we have a possible play Trenton may associate with this day, it's time for us to find some screening dates at the theatre. So, we crack open Google once again and search with these queries.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/29.png "Searching for screenings")

*Figure 2.7: Searching for screening dates at the Princess Theatre.*

Aha! It appears that Les Misérables did play at the Princess Theatre on December 9th, 1989. Trenton also says that this day occured 34 years ago, so if we do 2023 - 34, we get 1989. That confirms these two events were on the same year!

We may have found our date, and there's only one way to check...

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/30.png "Finding a special date")

*Figure 2.8: Observing a very notable date from the play.*

We head back to this QR Code and hope for the best... And voila, it works! Once entering the QR Code, we end up with both the flag and the final Y coordinate, thus saving the world from Doomsday.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/Magpie%20CTF%202023/Operation%20Doomsday%20(Complete)/Images/31.png "Entering the QR Code")

*Figure 2.9: Cracking the final part of the puzzle!*

## Reflections

While this writeup may seem like I did nearly everything correctly in the right sequence, the truth is, it was a lot messier than that. I can only count the number of times I got the city wrong for the password! I remember specifically looking up the quotation Trenton used to describe the city, and ended up putting in random locations from Japan and Turkey to no avail. It didn't help either that I actually located The Princess Theatre a lot earlier, and tried putting in variations of the resturant, theatre, Australia and Australian cities with no luck!

I also was stuck trying to locate anything after investigating the Twitter and Instagram pages, because I didn't know how to pull up hidden tweets. I ended up searching on Google how to unhide tweets, found the first link saying you can't and just dropped it for the longest time while ignoring my gut feeling. Beliving the first thing I read on the internet - so much for being a Cyber Security professional, right? I owe a shoutout to my teammate Blake, who found Ahmed's tweet first. I can only count the amount of times I used theHarvester to search for variations of the usernames we discovered to try to get past this dead-end!

Overall, the most important thing I learned from this challenge is to take my time and to learn to analyze things very carefully. Giving up too early is never a good thing - especially when you have a gut feeling! Overall, I had a lot of fun with this challenge. This was also the first challenge I attempted that had a limit on the number of submissions you could attempt, so I found the pressure on Part II to be extremely exciting.

Thank you to the MagpieCTF team for creating such an awesome event this year!
