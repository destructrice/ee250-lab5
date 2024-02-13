# Lab 5

## Team Members
- Sriya Kuruppath
- Victoria Lawton

## Lab Question Answers

  ### Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
  Decibel-milliWatts, or dBm, is the power measurement of RF signals such as Wifi. It is a logarithmic scale, so as dBm increases, the power (or signal strength) increases. -30 to -50 dBm constitutes excellent Wifi strength. Anything below -80 dBm is bad signal strength.
  
  ### Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
  
  
  ### Question 3: In your own words, what is subprocess.check_output doing? What does it return?
  ### HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output
  
  ### Question 4: In your own words, what is re.search doing? What does it return?
  ### HINT: https://docs.python.org/3/library/re.html#re.search
  
  ### Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
  ### HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN
  
  ### Question 6: What is the standard deviation? Why is it useful to calculate it?
  Standard deviation is useful to calculate in this case because if the signal strength measured at one point is good, but the standard deviation is high, this means that the signal strength is not reliable. While some good signal strength values are a good thing, consistency is important for the user. If the signal strength is constantly changing from good to bad, that's not optimal (we want to limit variability). 

  ### Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
  ### HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
  ### HINT: print the dataframe to see what it looks like

  ### Question 8: Why is it important to plot the error bars? What do they tell us?
  Similar to standard deviation, error bars help us see variability in the signal strength. This is helpful for visualizing fluctuation to see how signal strength changes over time or in different measurement locations. In general, error bars also help us see whether differences in measurements are statistically significant-- if error bars overlap, the difference is not significant.

  ### Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?
  ###             Why do you think signal strength is weaker in certain locations?

  ### Question 10: Do you notice any trends in the data?
  ###              How does it differ from Part 1?
  ###              What do you think is causing the differences?
...
