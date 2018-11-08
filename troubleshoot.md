
## Problem Description:

When using R package "httr" in Power BI, one will get the following error
"Error in iconv(x, "latin1", "ASCII") : unsupported conversion from 'latin1' to 'ASCII' in codepage 1252"
See more details:
https://community.powerbi.com/t5/Service/Script-works-on-Desktop-but-not-on-Service-Says-quot-unsupported/td-p/180713

## Problem Diagnosis:
"httr" is one of the packages supported by Power BI.
https://docs.microsoft.com/en-us/power-bi/service-r-packages-support

The error is not due to that "httr library isn't supported".

The reason is that Power BI use different distribution of R version than people typicall will use.
On the server side, Power BI uses Microsoft R Open, users typical use R from https://www.r-project.org/ on their desktop.

Microsoft R Open
> iconv("123", "latin1", "ASCII")
Loading required package: sysfonts
 [1] "font in use: arial.ttf"
 
 Error in iconv("123", "latin1", "ASCII") : 
 unsupported conversion from 'latin1' to 'ASCII' in codepage 1252
 
 
R (https://www.r-project.org/)
> iconv("123", "latin1", "ASCII")
[1] "123"





## Solution:
Inside the "httr" package, it call the "regmatches", which cause the error.
As mentioned in this page,
https://social.msdn.microsoft.com/Forums/sqlserver/en-US/4d8ac3ee-ea17-42d4-b544-056543c67928/unsupported-conversion-from-latin1-to-ascii-in-codepage-1252?forum=MachineLearning

One can create a customized "regmatches" function, replacing  
asc <- iconv(x, "latin1", "ASCII")  with asc <- iconv(x, to="UTF-8")
This function will mask the original regmatches function in the system and make sure the code work.





