![Alt text](https://github.com/TeleSign/ios_verification_sdk/blob/master/APPverify.jpeg)
## Overview

The App Verify SDK allows iOS apps to use custom URL schemes to verify a users phone number. TeleSign service securely sends SMS to the users device which contains a unique URL that the user can click on to complete verification automatically.

## Documentation
Comprehensive documentation is available at https://developer.telesign.com/docs/app-verify-ios-sdk-self

## Requirements 
	- XCode 8.3
	- Swift 3.2
	` You will need to setup a JWT service to use the application. You will need your TeleSign customerID and an API key for authentication `
	` You will also need to register a a Custom URL type for your app in the plist file. Include the CFBundleURLTypes key in your app’s Info.plist file and register the CFBundleURLSchemes to match what was registered with TeleSign  `

	
## Usage 

=======
	
## Usage 
` You will need to setup a JWT service to use the application. You will need your TeleSign customerID and an API key for authentication `

*To run the example project*

- Download or clone repo
- Add your JWT URL in viewcontroller.swift file inside the verifyBtnClicked function
- Build and run the project
		
*To configure your own project*

- Drag and drop the AppVerify.framework into your project
- Copy the module.modulemap file inside AppVerify inside your Source directory
- Add ${SRCROOT}/(yourfoldername) in Build settings > Import Paths 

- Use the prebuilt view controller or create your own UI to send the phone number and the JWT URL using one of the two methods 

```
- verify(phoneNumber: String, jwtURL: URL)
- viewControllerForNumberVerification(withJWTString jwtString: String)
```
- Set the delegate and if you are using your own UI implement this protocol method to show the user that a SMS has been sent and alert them to click on the link
```
- InitiateSucceded(withTTL: TimeInterval)
```

- In your app delegate, implement this protocol method 
```
- application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool
```
- Once the URL is obtained, pass the data using 
```
- finalizeWith(verificationURLString: String)
```
- Implement the following delegate methods to check if the verification succeeded or failed

```
- VerificationFailed(error: TSVerificationError)
- VerificationSuccessful()
```
			 
		
