# Bell: Rational Expressions Are Also Regular Expressions
Written by: 0xETX (0x03)

## Resources Used
1. Notepad++
2. https://regex101.com

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

![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/regex101.PNG "🤔")
