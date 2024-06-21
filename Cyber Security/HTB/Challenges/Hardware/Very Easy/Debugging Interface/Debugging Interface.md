![](images/Pasted%20image%2020240512133213.png)

## CHALLENGE DESCRIPTION

We accessed the embedded device's asynchronous serial debugging interface while it was operational and captured some messages that were being transmitted over it. Can you decode them?

**Begin by downloading the provided zip file containing the challenge materials. Once downloaded, unzip the file using the following command:

`unzip debugging_interface.zip`

![](images/Pasted%20image%2020240512134616.png)

**Understanding .sal Extension**: The file has a .sal extension. This indicates it's a Zip archive. Now, what is .sal? .sal files are typically associated with logic analyzer software.

**To inspect the contents of the .sal file, you'll need a logic analyzer. Download a logic analyzer software like **Saleae** Logic Analyzer from their website.

https://www.saleae.com/pages/downloads

![](images/Pasted%20image%2020240512134658.png)

Once downloaded, make the analyzer executable using the command:

```
chmod +x Logic-2.4.14-linux-x64.AppImage
```


![](images/Pasted%20image%2020240512134740.png)

**Run the logic analyzer software and open the application. Navigate to the menu to select the .sal file from your computer.


![](images/Pasted%20image%2020240512134816.png)


Zoom into the data until you can see each frame in milliseconds. Then, switch to the analyzer tab and choose the table data mode.

![](images/Pasted%20image%2020240512134949.png)

Convert the hexadecimal values to ASCII to make sense of the data.

![](images/Pasted%20image%2020240512135325.png)



![](images/Pasted%20image%2020240512135508.png)


If the converted values still don't make sense, go back to terminal mode and choose the option to edit. 

![](images/Pasted%20image%2020240512140112.png)

Adjust the bit rate value until the terminal values start making sense.

![](images/Pasted%20image%2020240512140413.png)

Finally, when the bit rate is set to 30000, you should be able to see the flag within the data.

![](images/Pasted%20image%2020240512140430.png)