
# Problem Description:

When using R package "httr" in Power BI service (Power BI online), one may get the following error
"Error in iconv(x, "latin1", "ASCII") : unsupported conversion from 'latin1' to 'ASCII' in codepage 1252"
See more details in the following article:
https://community.powerbi.com/t5/Service/Script-works-on-Desktop-but-not-on-Service-Says-quot-unsupported/td-p/180713

# Problem Diagnosis:
## Potential Reason: "httr" is not supported by Power BI.
## Fact: "httr" is one of the packages supported by Power BI as describle in the following post
https://docs.microsoft.com/en-us/power-bi/service-r-packages-support

## Conclusion: This error is not due to that "httr library isn't supported".

# Reason
The reason is that Power BI service uses a different distribution of R version rather than the cran version people typicallly use.
On the server side, Power BI uses Microsoft R Open, while people usually use R from CRAN(https://www.r-project.org/) on their desktop.

We can reproduce the error in Microsoft R Open
## Microsoft R Open
> iconv("123", "latin1", "ASCII")
Loading required package: sysfonts
 [1] "font in use: arial.ttf"
 
 Error in iconv("123", "latin1", "ASCII") : 
 unsupported conversion from 'latin1' to 'ASCII' in codepage 1252
 
The same code can run on CRAN R
## R (https://www.r-project.org/)
> iconv("123", "latin1", "ASCII")
[1] "123"



# Solution:
## Solution 1
Inside the "httr" package, it call the "regmatches", which cause the error.
As mentioned in the following post, one can create a customized "regmatches" function by replacing  
asc <- iconv(x, "latin1", "ASCII")  with  asc <- iconv(x, to="UTF-8")
https://social.msdn.microsoft.com/Forums/sqlserver/en-US/4d8ac3ee-ea17-42d4-b544-056543c67928/unsupported-conversion-from-latin1-to-ascii-in-codepage-1252?forum=MachineLearning

This new function will mask the original regmatches function in the system and make sure the code work.

## Solution 2
Use the library "RCurl" instead of "httr"
It has the same functionalities and avoid this issue.





