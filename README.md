![Alt text](https://github.com/TeleSign/ios_verification_sdk/blob/master/banner.jpg)
## Overview

The App Verify SDK allows iOS apps to use custom URL schemes to verify a users phone number. TeleSign service securely sends SMS to the users device which contains a unique URL that the user can click on to complete verification automatically.

## Documentation
Comprehensive documentation is available at https://enterprise.telesign.com/sdks/app-verify-ios-sdk

Android SDK is available at https://github.com/TeleSign/android_appverify_sdk

## Requirements
	- XCode 9.3+
	- Swift 4.1
` You will need to setup a JWT service to use the application. You will need your TeleSign customerID and an API key for authentication `

` You will also need to register a a Custom URL type for your app in the plist file. Include the CFBundleURLTypes key in your app’s Info.plist file and register the CFBundleURLSchemes to match what was registered with TeleSign  `

## Current Release : v1.3.0
- AppVerify SDK:
  - Updated framework to support Swift 3.3 & Swift 4.1
  - Bug fixes

[Previous releases logs](https://github.com/TeleSign/ios_appverify_sdk/blob/master/RELEASE.md)

## Usage

*To run the example project*

- Download or clone repo
- Add your JWT URL in viewcontroller.swift file inside the verifyBtnClicked function
- Build and run the project

*To configure your own project*

- Drag and drop the AppVerify.framework into your project
- Copy the module.modulemap file inside AppVerifyDemo folder inside your Source directory
- Add ${SRCROOT}/(yourfoldername) in Build settings > Import Paths

- Use the prebuilt view controller or create your own UI to send the phone number and the JWT URL along with the configuration using one of the two methods

```
- verify(phoneNumber: String, jwtURL: URL)
- viewControllerForNumberVerification(withJWTString jwtString: String, andConfiguration configuration: viewConfiguration)
```

- You can configure the viewController with your own colors and logo by doing this

```
let configuration = viewConfiguration(logoImage: YOURIMAGE, themeColor: CUSTOMCOLOR, labelColor: CUSTOMCOLOR, backgroundColor: CUSTOMCOLOR)
```

- Set the delegate and if you are using your own UI implement this protocol method to show the user that a SMS has been sent and alert them to click on the link
```
- InitiateSucceded(withTTL: TimeInterval)
```

- In your app delegate, implement this protocol method
```
- application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool
```
- Once the URL is obtained, pass the data using one of the methods below
```
- finalizeWith(verificationURLString: String)
- finalizeWith(verificationURL: URL)
- finalizeWith(verificationCode: String)
```
- Implement the following delegate methods to check if the verification succeeded or failed

```
- VerificationFailed(error: TSVerificationError)
- VerificationSuccessful()
```
