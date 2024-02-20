# Lab 5

## Team Members
- Sriya Kuruppath
- Victoria Lawton

## Lab Question Answers

  ### Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
  Decibel-milliWatts, or dBm, is the power measurement of RF signals such as Wifi. It is a logarithmic scale, so as dBm increases, the power (or signal strength) increases. -30 to -50 dBm constitutes excellent Wifi strength. Anything below -80 dBm is bad signal strength.
  
  ### Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
  We need to check the OS because each OS has different commands to get the Wifi signal strength. For example, Linux uses iwconfig wlan0, Windows uses netsh wlan show interfaces, and macOS uses /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I.
  
  ### Question 3: In your own words, what is subprocess.check_output doing? What does it return?
  ### HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output

  subprocess.check_output takes a string command as its input and executes the command in the system's shell. For example, this means that iwconfig wlan0 will only be executed on Linux, and not Windows or macOS. Additionally, this command takes the output of the command and funnels it back into the python file rather than simply printing it out. For example, rather than printing the WiFi strength immediately for Windows, it takes the output back in as input so that it can convert it to dBm from signal strength. Finally, the command returns the output as a byte string which the script can use for further analysis after it's converted to a standard string.
  
  ### Question 4: In your own words, what is re.search doing? What does it return?
  ### HINT: https://docs.python.org/3/library/re.html#re.search
re is a Python module that allows for the use of regular expressions (or regex). re.search specifically can analyze a string to try and match it to a regex pattern. Additionally, re.search allows for extracting parts of the matched text, and this information can be used for further analysis. re.search returns a match object if it finds a match, and None if it doesn't find a match.
  
  ### Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
  ### HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN
We need to convert signal quality to dBm for a couple of reasons. First, Linux and macOS both output signal quality in dBm, so if we want to compare the three, they all need to be in the same unit. Secondly, dBm is the standard for measuring WiFi strength (it's universal), so it makes sense to use dBm as a measurement for all three operating systems.
  
  ### Question 6: What is the standard deviation? Why is it useful to calculate it?
  Standard deviation is useful to calculate in this case because if the signal strength measured at one point is good, but the standard deviation is high, this means that the signal strength is not reliable. While some good signal strength values are a good thing, consistency is important for the user. If the signal strength is constantly changing from good to bad, that's not optimal (we want to limit variability). 

  ### Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
  ### HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
  ### HINT: print the dataframe to see what it looks like
A dataframe is a two-dimensional, mutable (in size), and tabular data structure that has labeled axes as provided by pandas (which is a library in Python). Using a dataframe to store the data is useful because in the context of measuring wifi signal strength, it allows storing location, mean signal strength, and standard deviation in a structured way. This structure allows us to extract these variables easily to allow for data analysis and graphing. Then we can compare signal strength variability and plot the results. 

  ### Question 8: Why is it important to plot the error bars? What do they tell us?
  Similar to standard deviation, error bars help us see variability in the signal strength. This is helpful for visualizing fluctuation to see how signal strength changes over time or in different measurement locations. In general, error bars also help us see whether differences in measurements are statistically significant-- if error bars overlap, the difference is not significant.

  ### Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?
  ###             Why do you think signal strength is weaker in certain locations?
  

  ### Question 10: Do you notice any trends in the data?
  ###              How does it differ from Part 1?
  ###              What do you think is causing the differences?
...
