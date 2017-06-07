//
//  ViewController.swift
//  VerifySDKDemo
//
//  Created by Krishna Jagadish on 1/17/17.
//  Copyright © 2017 telesign. All rights reserved.
//

import UIKit
import VerifySDK

class ViewController: UIViewController, TSVerificationViewControllerDelegate {

    let verification = TSVerification()

    
    @IBOutlet weak var codeTextField: UITextField!
    @IBOutlet weak var verifyButton: UIButton!
    @IBOutlet weak var messageLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
        self.verifyButton.layer.cornerRadius = 7.0
        self.messageLabel.text = ""
       
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        // Hide the navigation bar on the this view controller
        self.navigationController?.setNavigationBarHidden(true, animated: animated)
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        
        // Show the navigation bar on other view controllers
        self.navigationController?.setNavigationBarHidden(false, animated: animated)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    // MARK: - VerifySDK methods
    @IBAction func verifyBtnClicked(_ sender: Any) {
        
        // Add your JWT URL here
        let jwtURL = ""
        // Get the prebuilt verification view controller
        let vc =   self.verification.viewControllerForNumberVerification(withJWTString: jwtURL)
        // Set the delegate
        vc.delegate = self
        // Present the view controller
        self.present(vc, animated: true, completion: nil)
        
    }
    
    // MARK: - VerificationViewController Delegate
    
    public func didSuccessfullyCompleteVerificationFor(phoneNumber: String) {
        performSegue(withIdentifier: "verifiedController", sender: nil)
    }
    
    public func didFailToCompleteVerificationFor(phoneNumber: String, error: TSVerificationError) {
        print("Verification Failed with code \(error.errorCode)")
        self.messageLabel.text = error.errorMessage
    }
    
   
    // The finalize method called when the URL is clicked by the user
    public func finalize(verificationCode: String) {
        self.verification.finalizeWith(verificationCode: verificationCode)
    }
    
    
    // If you are not using the prebuilt controller, add these two delegate methods
    // MARK: - VerifySDK Delegate Methods
    /*
     public func VerificationFailed(errorMessage: String) {
     print("Verification Failed because \(errorMessage)")
     }
     
     public func VerificationSuccessful() {
     self.messageLabel.text = ""
     self.verifyButton.setTitle("Verify", for: .normal)
     self.verifyButton.isEnabled = true
     performSegue(withIdentifier: "verifiedController", sender: nil)
     }
     */
}

