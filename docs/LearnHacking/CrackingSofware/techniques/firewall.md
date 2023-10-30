# Firewall

> This is not really cracking a software, you may still have to pay.
> This method also has some limitations which could prevent it to work.

## Solution

Some softwares uses a subscription model (SaaS) and limits the number of machines that can be activated at the same time. Example software: [Typora](https://typora.io/).
When you install it on a new computer, you can deactivate a previous activation (this doesn't require you to deactivate it in the old computer).
In this scenario, the subbscription status is likely checked with a server everytime the app is open. 
If the server replies that the activation is deactivated, the software will block you from using it.

The **hack** to this type of software could be cutting its connection with internet with some firewall softwares. If it cannot check the status it may not block you from using the app.
Everytime you install the app on a new machine, you can activate it with a license and block it from communicating with internet with a firewall.


## Limitation

> There are many methods software companies can implement to prevent this method, some could affect user experience.

- Softwares can enforce internet requirement, i.e. block you from using the app without checking status with internet.
	- User experience can be very bad in this case, as offline scenarios are very common, e.g. travelling, outdoor, etc.
	- A variant of this could be a activation expire time. Without refreshing activation with internet for a certain time (e.g. a few weeks), the app blocks user from using it. This will improve user experience.
- Softwares can enforce deactivation of on old machine, e.g. Alfred

## Softwares

- Mac
	- Radio Silence (Tested)
	- Mac's built-in firewall doesn't block outgoing traffic, which won't work in our scenario
- Linux
- Windows
