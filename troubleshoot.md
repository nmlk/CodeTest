
Problem Description:

When using R package "httr" in Power BI, one will get the following error
"Error in iconv(x, "latin1", "ASCII") : unsupported conversion from 'latin1' to 'ASCII' in codepage 1252"
See more details:
https://community.powerbi.com/t5/Service/Script-works-on-Desktop-but-not-on-Service-Says-quot-unsupported/td-p/180713

Problem Diagnosis:
"httr" is one of the packages supported by Power BI.
https://docs.microsoft.com/en-us/power-bi/service-r-packages-support

The error is not due to that "httr library isn't supported".

The reason is that Power BI use different distribution of R version than people typicall will use.
On the server side, Power BI uses Microsoft R Open, users typical use R from https://www.r-project.org/ on their desktop.

Microsoft R Open
[1]  "437" "850" "852" "855" "860" "861" "862" "865"  "866" "869" "ANSI_X3.4-1986"  "ASCII" "ASMO-708" "BIG-5" "BIG-FIVE" 
[2] "big5" "BIG5" "big5-hkscs" "BIG5-HKSCS" "big5hkscs" "BIG5HKSCS" "CP-GR" "CP-IS" "cp1025" "CP1125" "CP1133" "CP1200" 
[3] "CP12000" "CP12001" "CP1201" "CP1250" "CP1251" "CP1252" "CP1254" "CP1255" "CP1256" "CP1257" "CP1258" 
[5] "CP1361" "CP154" "CP437" "CP50221" "CP51932" "CP775" "CP819" "CP850" "CP852" "CP855" "CP857" "CP858" 
[6] "CP860" "CP861" "CP864" "CP865" "cp866" "CP866" "CP869" "CP874" "cp875" "CP932" "CP936" "CP949" "CP950" "CSASCII" "CSIBM855" 
[7] "CSIBM857" "CSIBM860" "CSIBM861" "CSIBM863" "CSIBM864" "CSIBM865" "CSIBM866" "CSIBM869" "csISO2022JP" "CSISOLATIN1" 
[8] "CSPC775BALTIC" "CSPC850MULTILINGUAL" "CSPC862LATINHEBREW" "CSPC8CODEPAGE437" "CSPCP852" "CSPTCP154" "CSWINDOWS31J" 
[9] "CYRILLIC-ASIAN" "DOS-720" "DOS-862" "EUC-CN" "euc-jp" "euc-kr" "EUC-KR" "EUCCN" "eucjp" "euckr" "GB18030" "gb2312" 
[10] "GBK" "hz-gb-2312" "IBM-CP1133" "IBM-Thai" "IBM00858" "IBM00924" "IBM01047" "IBM01140" "IBM01142" "IBM01143" "IBM01144" 
[11] "IBM01145" "IBM01146" "IBM01147" "IBM01148" "IBM01149" "IBM037" "IBM1026" "IBM273" "IBM277" "IBM278" "IBM285" "IBM290" 
[12] "IBM297" "IBM367" "IBM423" "IBM424" "IBM437" "IBM437" "IBM500" "ibm737" "ibm775" "IBM819" "ibm850" "IBM850" "IBM855" "IBM855" 
[13] "ibm857" "IBM857" "ibm861" "IBM861" "IBM862" "IBM863" "IBM863" "IBM864" "IBM864" "IBM865" "IBM865" "IBM866" "IBM869" "IBM870" "IBM871" 
[14] "IBM880" "IBM905" "iso-2022-jp" "ISO-2022-JP" "ISO-2022-JP-MS" "iso-8859-13" "iso-8859-15" "iso-8859-4" "iso-8859-5" "iso-8859-8" "iso-8859-8-i" 
[15] "ISO-IR-6" "ISO_646.IRV:1991" "iso_8859-1" "ISO_8859-1"  "iso_8859-15" "iso_8859-2" "iso_8859-3" "iso_8859-4" "iso_8859-6" "iso_8859-7" "iso_8859-8" 
[16] "iso_8859-8-i" "iso_8859-9" "iso_8859_15" "iso_8859_2" "iso_8859_5" "iso_8859_6" "iso_8859_7" "iso_8859_8" "iso_8859_8-i" "iso_8859_9" "ISO2022-JP" "ISO2022-JP-MS" 
[17] "iso2022-kr" "ISO646-US" "iso8859-1" "ISO8859-1" "iso8859-13" "iso8859-15" "iso8859-2" "iso8859-3" "iso8859-4" "iso8859-5" "iso8859-6" "iso8859-7" 
[18] "iso8859-8-i" "iso8859-9" "Johab"  "JOHAB" "koi8-r" "koi8-u" "ks_c_5601-1987" "L1" "latin-9" "LATIN1" "latin2" "latin3" "latin4" "latin5" "latin7" 
[19] "latin9" "mac" "mac-centraleurope" "mac-is"  "macarabic" "maccentraleurope" "maccyrillic" "macgreek" "machebrew" "maciceland" "macintosh" 
[20] "macis" "macroman" "macromania" "macthai" "macukrainian" "MS-ANSI" "MS-ARAB" "MS-CYRL" "MS-GREEK" "MS-HEBR" "MS-TURK" 
[21] "MS50221" "MS51932" "MS932" "MS936" "PT154" "PTCP154" "SHIFFT_JIS" "SHIFFT_JIS-MS" "shift-jis" "shift_jis" "SJIS" "SJIS-MS" 
[22] "SJIS-OPEN" "SJIS-WIN" "UCS-2" "UCS-2BE" "UCS-2LE" "UCS-4" "UCS-4LE" "UCS-4LE" "UCS2" "UCS2BE" "UCS4" "UCS4BE" "UCS4LE" "US" 
[23] "US-ASCII" "UTF-16" "UTF-16BE" "UTF-32" "UTF-32BE" "UTF-32LE" "UTF-8" "UTF16" "UTF16BE" "UTF16LE" "UTF32" "UTF32BE" 
[24] "UTF32LE" "UTF8" "WINBALTRIM" "windows-1250" "windows-1253" "windows-1254"  "windows-1257" "windows-1258" 
[25] "WINDOWS-31J" "WINDOWS-50221" "WINDOWS-932" "WINDOWS-936" "x-Chinese_CNS" "x-cp20001" "x-cp20004" "x-cp20005" "x-cp20261" 
[26] "x-cp20949" "x-cp50227" "x-EBCDIC-KoreanExtended" "x-Europa" "x-IA5" "x-IA5-German" "x-IA5-Norwegian" "x-IA5-Swedish" "x-iscii-be" 
[27]"x-iscii-de" "x-iscii-gu" "x-iscii-ka" "x-iscii-ma" "x-iscii-pa" "x-iscii-ta" "x-iscii-te" "x-mac-ce" "x-mac-chinesesimp" "x-mac-chinesetrad" 
[28] "x-mac-croatian" "x-mac-cyrillic" "x-mac-hebrew" "x-mac-icelandic" "x-mac-japanese" "x-mac-korean" "x-mac-romanian" "x-mac-thai" "x-mac-turkish" "x-mac-ukrainian" "x_Chinese-Eten" 



R (https://www.r-project.org/)
> iconvlist()
  [1] "437"                     "850"                     "852"                     "855"                     "857"                    
  [6] "860"                     "861"                     "862"                     "863"                     "865"                    
 [11] "866"                     "869"                     "ANSI_X3.4-1968"          "ANSI_X3.4-1986"          "ASCII"                  
 [16] "ASMO-708"                "BIG-5"                   "BIG-FIVE"                "big5"                    "BIG5"                   
 [21] "big5-hkscs"              "BIG5-HKSCS"              "big5hkscs"               "BIG5HKSCS"               "CP-GR"                  
 [26] "CP-IS"                   "cp1025"                  "CP1125"                  "CP1133"                  "CP1200"                 
 [31] "CP12000"                 "CP12001"                 "CP1201"                  "CP1250"                  "CP1251"                 
 [36] "CP1252"                  "CP1253"                  "CP1254"                  "CP1255"                  "CP1256"                 
 [41] "CP1257"                  "CP1258"                  "CP1361"                  "CP154"                   "CP367"                  
 [46] "CP437"                   "CP50221"                 "CP51932"                 "CP65001"                 "CP737"                  
 [51] "CP775"                   "CP819"                   "CP850"                   "CP852"                   "CP853"                  
 [56] "CP855"                   "CP857"                   "CP858"                   "CP860"                   "CP861"                  
 [61] "CP862"                   "CP863"                   "CP864"                   "CP865"                   "cp866"                  
 [66] "CP866"                   "CP869"                   "CP874"                   "cp875"                   "CP932"                  
 [71] "CP936"                   "CP949"                   "CP950"                   "CSASCII"                 "CSIBM855"               
 [76] "CSIBM857"                "CSIBM860"                "CSIBM861"                "CSIBM863"                "CSIBM864"               
 [81] "CSIBM865"                "CSIBM866"                "CSIBM869"                "csISO2022JP"             "CSISOLATIN1"            
 [86] "CSPC775BALTIC"           "CSPC850MULTILINGUAL"     "CSPC862LATINHEBREW"      "CSPC8CODEPAGE437"        "CSPCP852"               
 [91] "CSPTCP154"               "CSWINDOWS31J"            "CYRILLIC-ASIAN"          "DOS-720"                 "DOS-862"                
 [96] "EUC-CN"                  "euc-jp"                  "euc-kr"                  "EUC-KR"                  "EUCCN"                  
[101] "eucjp"                   "euckr"                   "GB18030"                 "gb2312"                  "GBK"                    
[106] "hz-gb-2312"              "IBM-CP1133"              "IBM-Thai"                "IBM00858"                "IBM00924"               
[111] "IBM01047"                "IBM01140"                "IBM01141"                "IBM01142"                "IBM01143"               
[116] "IBM01144"                "IBM01145"                "IBM01146"                "IBM01147"                "IBM01148"               
[121] "IBM01149"                "IBM037"                  "IBM1026"                 "IBM273"                  "IBM277"                 
[126] "IBM278"                  "IBM280"                  "IBM284"                  "IBM285"                  "IBM290"                 
[131] "IBM297"                  "IBM367"                  "IBM420"                  "IBM423"                  "IBM424"                 
[136] "IBM437"                  "IBM437"                  "IBM500"                  "ibm737"                  "ibm775"                 
[141] "IBM775"                  "IBM819"                  "ibm850"                  "IBM850"                  "ibm852"                 
[146] "IBM852"                  "IBM855"                  "IBM855"                  "ibm857"                  "IBM857"                 
[151] "IBM860"                  "IBM860"                  "ibm861"                  "IBM861"                  "IBM862"                 
[156] "IBM863"                  "IBM863"                  "IBM864"                  "IBM864"                  "IBM865"                 
[161] "IBM865"                  "IBM866"                  "ibm869"                  "IBM869"                  "IBM870"                 
[166] "IBM871"                  "IBM880"                  "IBM905"                  "iso-2022-jp"             "iso-2022-jp"            
[171] "ISO-2022-JP"             "ISO-2022-JP-MS"          "iso-2022-kr"             "ISO-8859-1"              "iso-8859-13"            
[176] "iso-8859-15"             "iso-8859-2"              "iso-8859-3"              "iso-8859-4"              "iso-8859-5"             
[181] "iso-8859-6"              "iso-8859-7"              "iso-8859-8"              "iso-8859-8-i"            "iso-8859-9"             
[186] "ISO-IR-100"              "ISO-IR-6"                "ISO_646.IRV:1991"        "iso_8859-1"              "ISO_8859-1"             
[191] "ISO_8859-1:1987"         "iso_8859-13"             "iso_8859-15"             "iso_8859-2"              "iso_8859-3"             
[196] "iso_8859-4"              "iso_8859-5"              "iso_8859-6"              "iso_8859-7"              "iso_8859-8"             
[201] "iso_8859-8-i"            "iso_8859-9"              "iso_8859_1"              "iso_8859_13"             "iso_8859_15"            
[206] "iso_8859_2"              "iso_8859_3"              "iso_8859_4"              "iso_8859_5"              "iso_8859_6"             
[211] "iso_8859_7"              "iso_8859_8"              "iso_8859_8-i"            "iso_8859_9"              "ISO2022-JP"             
[216] "ISO2022-JP-MS"           "iso2022-kr"              "ISO646-US"               "iso8859-1"               "ISO8859-1"              
[221] "iso8859-13"              "iso8859-15"              "iso8859-2"               "iso8859-3"               "iso8859-4"              
[226] "iso8859-5"               "iso8859-6"               "iso8859-7"               "iso8859-8"               "iso8859-8-i"            
[231] "iso8859-9"               "Johab"                   "JOHAB"                   "koi8-r"                  "koi8-u"                 
[236] "ks_c_5601-1987"          "L1"                      "latin-9"                 "LATIN1"                  "latin2"                 
[241] "latin3"                  "latin4"                  "latin5"                  "latin7"                  "latin9"                 
[246] "mac"                     "mac-centraleurope"       "mac-is"                  "macarabic"               "maccentraleurope"       
[251] "maccroatian"             "maccyrillic"             "macgreek"                "machebrew"               "maciceland"             
[256] "macintosh"               "macis"                   "macroman"                "macromania"              "macthai"                
[261] "macturkish"              "macukraine"              "macukrainian"            "MS-ANSI"                 "MS-ARAB"                
[266] "MS-CYRL"                 "MS-EE"                   "MS-GREEK"                "MS-HEBR"                 "MS-TURK"                
[271] "MS50221"                 "MS51932"                 "MS932"                   "MS936"                   "PT154"                  
[276] "PTCP154"                 "SHIFFT_JIS"              "SHIFFT_JIS-MS"           "shift-jis"               "shift_jis"              
[281] "SJIS"                    "SJIS-MS"                 "SJIS-OPEN"               "SJIS-WIN"                "UCS-2"                  
[286] "UCS-2BE"                 "UCS-2LE"                 "UCS-4"                   "UCS-4BE"                 "UCS-4BE"                
[291] "UCS-4LE"                 "UCS-4LE"                 "UCS2"                    "UCS2BE"                  "UCS2LE"                 
[296] "UCS4"                    "UCS4BE"                  "UCS4LE"                  "UHC"                     "unicodeFFFE"            
[301] "US"                      "US-ASCII"                "UTF-16"                  "UTF-16BE"                "UTF-16LE"               
[306] "UTF-32"                  "UTF-32BE"                "UTF-32LE"                "UTF-8"                   "UTF16"                  
[311] "UTF16BE"                 "UTF16LE"                 "UTF32"                   "UTF32BE"                 "UTF32LE"                
[316] "UTF8"                    "WINBALTRIM"              "windows-1250"            "windows-1251"            "windows-1252"           
[321] "windows-1253"            "windows-1254"            "windows-1255"            "windows-1256"            "windows-1257"           
[326] "windows-1258"            "WINDOWS-31J"             "WINDOWS-50221"           "WINDOWS-51932"           "windows-874"            
[331] "WINDOWS-932"             "WINDOWS-936"             "x-Chinese_CNS"           "x-cp20001"               "x-cp20003"              
[336] "x-cp20004"               "x-cp20005"               "x-cp20261"               "x-cp20269"               "x-cp20936"              
[341] "x-cp20949"               "x-cp50227"               "x-EBCDIC-KoreanExtended" "x-Europa"                "x-IA5"                  
[346] "x-IA5-German"            "x-IA5-Norwegian"         "x-IA5-Swedish"           "x-iscii-as"              "x-iscii-be"             
[351] "x-iscii-de"              "x-iscii-gu"              "x-iscii-ka"              "x-iscii-ma"              "x-iscii-or"             
[356] "x-iscii-pa"              "x-iscii-ta"              "x-iscii-te"              "x-mac-arabic"            "x-mac-ce"               
[361] "x-mac-chinesesimp"       "x-mac-chinesetrad"       "x-mac-croatian"          "x-mac-cyrillic"          "x-mac-greek"            
[366] "x-mac-hebrew"            "x-mac-icelandic"         "x-mac-japanese"          "x-mac-korean"            "x-mac-romanian"         
[371] "x-mac-thai"              "x-mac-turkish"           "x-mac-ukrainian"         "x_Chinese-Eten"         


Solution:
Inside the "httr" package, it call the "regmatches", which cause the error.
As mentioned in this page,
https://social.msdn.microsoft.com/Forums/sqlserver/en-US/4d8ac3ee-ea17-42d4-b544-056543c67928/unsupported-conversion-from-latin1-to-ascii-in-codepage-1252?forum=MachineLearning

One can create a customized "regmatches" function, replacing  
asc <- iconv(x, "latin1", "ASCII")  with asc <- iconv(x, to="UTF-8")
This function will mask the original regmatches function in the system and make sure the code work.





