# Bell: Rational Expressions Are Also Regular Expressions
Written by: 0xETX (0x03)

## Resources Used
1. Notepad++
2. https://regex101.com (Using PCRE2)

In the cybersecurity world, there are many important and useful skills to have. One of these important skills, Regular Expressions - also known as RegEx - demonstrates in strength and utility in the presence of any considerable amount of data. In this CTF challenge, that strength will be demonstrated when one line of RegEx is capable of finding the single malicious URL in 10,000 possible candidates; a literal needle-in-the-haystack.

## Getting Started
Before we begin, we will first need to look at the resources we are given. Within the provided zip file, we have three text files - instructions.txt, weak_entropy_logs.txt (Figure 1.0) and scrambled_logs.txt (Figure 1.1). A quick look at instructions.txt essentially tells us that we need to find a valid URL within scrambled_logs.txt - to do that, we can create a regular expression that works with the discovered valid URLs in weak_entropy_logs.txt.

Taking a quick look at weak_entropy_logs.txt shows that there are 10 URLs we can work with in finding a valid RegEx. We will get back to this later for when we try to figure out the entropy.
![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/weakentropy.PNG "weak_entropy_logs.txt")

*Figure 1.0: Observing the contents of the weak entropy file*

The next file we'll look at is scrambled_logs.txt. Taking a brief look at this file demonstrates how important having sample data like weak_entropy_logs.txt are - without out, the only way we could figure out which sites are valid is by figuring out if it could be a valid URL, which would still leave thousands of samples to go through.
![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/scrambledlogs.PNG "scrambled_logs.txt")

*Figure 1.1: Observing the contents of the scrambled logs file*

After looking through our pieces of evidence, we will begin with the weak_entropy_logs.txt file. For this challenge, I will mainly use https://regex101.com to build my expression, as it will continually update and provide feedback on errors, groups and matching strings.

## Building the Regex
We'll begin by plugging in all of the weak_entropy_logs URLs into the test string box of Regex101. Take a moment to see what they all have in common.
![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/regex101.PNG "🤔")

*Figure 2.0: What do you notice about the URLs and their entropy?*

### Time
We'll begin with the first section. The times we are presented with are:
1581000000, 1581001111, 1581002222, 1581003333, 1581004444, 1581005555, 1581006666, 1581007777, 1581008888, 1581001234

The first thing you may notice is that all the integers begin with 158100. Following that, starting at 1581000000, it would appear all the timestamps increase by 1111. However, observing the final integer shows us that is not the case, as it ends with '1234' which is not divisble by 1111. As a result, there are no additional patterns involving how the numbers scale. Additionally, everything under TIME is also specifically a digit - there are no alphabetical or special characters. With this knowledge, we can create the first part of our regular expression: **^158100\d{4}**.

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/1581.PNG "The first part of the regular expression.")

*Figure 2.1: **^\d{8}** would work perfectly fine too, along with other variations of length. As this is a timestamp, work with what the expected timeframe would be if in a real world scenario!*

**^158100\d{4}** is fairly straight forwards - the very beginning, ^, tells the regular expression to begin at the very start of each new line. Following that, 158100 matches explicitly with anything containing 158100. \d{4} has two parts to it - \d represents 'Any digit'. {4} restricts the digit match to explicity 4 of whatever is specified - in this case, digits. Here is a demonstration of it in action:

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/regexpart1.PNG "Testing part 1")

*Figure 2.2: Demonstration of why and how it works.*

  * Despite the first line, 'Foo 1581005445 Bar', having a number that would match the criteria, it is eliminated solely for breaking the anchor (^) condition, where the line must start with the timestamp.
  * 158100a000 does not match as it contains an alphabetical character, breaking the \d condition.
  * While 158100002 might not have any alphabetical or special characters, it does not meet the criteria of 4 digits past 158100.
  * As 1581002342 beings with 158100 and is followed by 4 numerical characters, it is a valid match.
With that done, we can move onto the second part of the regular expression.

### HTTP.REQUEST.URL
The second section is the HTTP.REQUEST.URL. This part will be the longest section, due to the complexity of the URLs versus timestamps and methods.

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/httpreq.PNG "Request URLS")

*Figure 2.3: All request URLs from the weak entropy log.*

We'll begin with the protocol section - as expected from the name, all of the URLs are using HTTP or HTTPS. In regex, we can turn this into '**https?:**'. The '?' character represents a possible match that is not required. Both HTTP and HTTPS contain 'HTTP', meaning that part will match without issue. By adding 's?', we can also include 'HTTPS' without excluding 'HTTP' for not ending with an 'S'.

Moving onto the domain section, the first thing that stands out is that each URL begins with a vowel or the letter 'y', followed by a period - resulting in "**[aeiouy]\\.**". \[aeiouy] will match any of the specified letters once, while \\. will match to a single period - the backslash is required, as in regex a period will match *anything*. The escape character will ensure a period is strictly matched.

Past that, we can see the second level domain. Observing these, we'll notice that they come in no particular order and contain both numbers and alphabetical characters, but no special characters. The length of the second-level domains is also between 10 and 64 characters long. The resulting regex will be '**[\w\d]\{10,64}**'. The square brackets surrounding \w and \d means that either digits or letters (\w) can be matched. For example:
  * aaaaaaaaaaaaaaaaaaaaaaa will match.
  * 000000000000000 will match.
  * b5k2o3i4aeerer91230uwu will match.
  * aaaaaaaaaaaaaaa&bbbbbbbbbbbbbb will only match up to the final *a* as the *&* symbol cuts it off before the *b* section. While this may seem like a problem at first, the top-level domain section will ensure wrong strings like these do not match.

Observing the top level domains, we'll notice that they come in a variety of ways. Some of these examples are .net, .game, .meme, .mom and so on. While it may seem like \w{3,4} (range of 3-4) would be a good idea, there is one problem - you'd be including top level domains that *don't exist*. Unlike second-level domains, top-level domains can't just be created with a couple of simple steps like a second-level domain. Top-level domains are managed by ICANN which is absolutely not worth the effort of any malicious actor. To keep it simple, we'll just match any top-level domain that has appeared in the sample data. Our resulting regular expression is '**\.(net|moe|game|meme|mom|org|art|car|com|team)**'. \\. is to keep the period before the top-level domain. The circle brackets contain each top-level domain being used - the addition of the | character is essentially an 'or' statement. As long as one matches, it will be considered valid.

The final part of the request URL is the file section. As standard, it begins with '/'. Observing each file name, the most noticable thing is that they all end in .html. While not apparent at first, the names of the files seem to be a random assortment of numbers and letters - and while somewhat true, there is one thing to note - it follows a hex format, where numbers 0-9 are valid, but only letters from a-f are valid - you'll notice that not a single file name contains a letter between g-z. The size is also fixed at explicity 10 characters. The resulting regex will appear as so: **\/[a-f0-9]{10}\.html**.
\\/ will ensure the special character '/' is stricly matched to a forward-slash (similar to .), \[a-f0-9]{10} will ensure only hex characters that are 10 characters in length are considered valid (- is used as a range, i.e: 0-9 is numbers from 0 to 9, and a-f is letters a to f.). Finally, \\.html will strictly look for .html.

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/validrequest.PNG "Matching the proper URLs")

*Figure 2.4: The resulting regular expression.*

### REQUEST.METHOD
Don't worry, you'll be spared my rambling for this one and you'll see why:

The only HTTP methods seen in the sample are POST and GET, so that's what we'll stricly look for. The resulting regex is **(POST|GET)**, which literally just looks for POST or GET.

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/brainblast.PNG "Sometimes its nice to enjoy the simpler things in life.")

*Figure 2.6: Easy peasy, lemon squeezy!*

### RESULT
Once we string the three seperate regular expressions together (with a space between each to follow the format of the document), our resulting regex is: 

**^158100\d{4} https?:[aeiouy]\\.[\w\d]{10,64}\\.(net|moe|game|meme|mom|org|art|car|com|team)\\/[a-f0-9]{10}\\.html (POST|GET)**

Now, we'll paste the scrambled_logs.txt file into Regex101 along with the regular expression and hope for the best!

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/woo.PNG "The correct URL is revealed!")
*Figure 2.7: The malicious URL detected by RegEx*
As seen in Figure 2.7, a single URL is displayed, just as we hoped! Following the instructions.txt, we now have our flag: **FLAG{ffec78f98d}**.

## Final Comments
As demonstrated above, RegEx is an immensely powerful tool that can quickly filter through colossal amounts of data to match *exactly* what you are looking for. By mastering your skill, you will notice considerable growth in what you are able do in terms of data analysis and even programming.
