# Bell: Rational Expressions Are Also Regular Expressions
Written by: 0xETX (0x03)

In the cybersecurity world, there are many important and useful skills to have. One of these important skills, Regular Expressions - also known as RegEx - demonstrates in strength and utility in the presence of any considerable amount of data. In this CTF challenge, that strength will be demonstrated when one line of RegEx is capable of finding the single malicious URL in 10,001 possible candidates; a literal needle-in-the-haystack.


## Getting Started
Before we begin, we will first need to look at the resources we are given. Within the provided zip file, we have three text files - instructions.txt, weak_entropy_logs.txt (Figure 1.0) and scrambled_logs.txt (Figure 1.1). A quick look at instructions.txt essentially tells us that we need to find a valid URL within scrambled_logs.txt - to do that, we can create a regular expression that works with the discovered valid URLs in weak_entropy_logs.txt.

Taking a quick look at weak_entropy_logs.txt
![alt-text](https://github.com/0xETX/ISSessions-2021-CTF/blob/main/RationalExpressions/Images/weakentropy.PNG "weak_entropy_logs.txt")
