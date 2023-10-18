# MCFA Identifier Detector

## Overview

[Section 47](http://legislature.mi.gov/doc.aspx?mcl-169-247) of the [Michigan Campaign Finance Act](http://legislature.mi.gov/doc.aspx?mcl-Act-388-of-1976) requires certain election-related materials to bear a statement identifying who paid for the matter. (e.g. "Paid for by..." followed by the committee name and address)

This requirement applies to websites that expressly advocate for the election or defeat of a candidate or ballot proposal. 

The MCFA Identifier Detector can be used to quickly check multiple URLs to see if the phrase `Paid for by` is present or not. 

This tool is intended to *aid* the process of flagging potentially noncompliant websites for further review. It is *not* a substitute for human review or professional legal advice. 

## Configuration

1. Install [Python 3](https://www.python.org/downloads/). 

2. Clone this repository. 

3. Open a terminal in the repository directory, and run the following commands: 

```
python -m ensurepip --upgrade
python -m pip install "selenium"
```

## Usage

Edit `urls_to_check.txt`, specifying one URL on each line, e.g.

```txt
https://www.example.com/index1.html
https://www.example.com/index2.html
https://www.example.com/index3.html
```

Save the file. 

To run the script, enter the following command on the terminal:

```
python detect.py
```

Results are displayed on the terminal and output to the `results.csv` file in the same directory. 

## Limitations

### Summary

The findings of this tool are not conclusive evidence of compliance or noncompliance with MCL 169.247. Human verification of the website contents is necessary to determine if the expected information is present or not. In addition, it is recommended to consult a legal professional to determine whether the material is subject to the Act and if so, whether the Act's requirements have been met. 

### Explanation and examples

The tool uses simple string matching to determine if the phrase `Paid for by` is present. 

Consider the following scenarios in which a website may arguably meet the requirements of the MCFA but would result in a "not found" result using this tool. 
- The website displays the identifier as an image file rather than as text. 
- The identifier contains irregular spellings, spacing, or punctuation. While perhaps legally trivial, these differences could cause the test to fail. 
- - `Paidfor by`
- - `Paid 4 by`

The above examples are provided for illustrative purposes and should not be considered exhaustive. 

### Address checking

In addition, MCL 169.247(1) requires that the identifier contain the payer's address. This tool does not check for the presence of a string resembling an address. 

## Known issues

Sometimes returns inconsistent results (e.g. "found" and "not found" result minutes later on the same URL.) 

Running the script again overwrites `results.csv`. At minimum, add a warning prompt, or better yet, incorporate a datetime stamp into the filename to ensure that a new file is written every time. 

Doesn't handle failed connections. 

Doesn't check for presence of committee address. Consider using regular expressions to check for addresses. 
