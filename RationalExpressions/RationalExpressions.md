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
