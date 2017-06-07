//
//  VerifiedViewController.swift
//  VerifySDKDemo
//
//  Created by Krishna Jagadish on 1/18/17.
//  Copyright © 2017 telesign. All rights reserved.
//

import UIKit
import SceneKit
import SpriteKit

class VerifiedViewController: UIViewController {
    
    @IBOutlet weak var particleView: SKView!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let sk:SKView = SKView()
        sk.frame = particleView.bounds
        sk.backgroundColor = UIColor.clear
        particleView.addSubview(sk)
        
        let scene: SKScene = SKScene(size: particleView.bounds.size)
        scene.scaleMode = .aspectFit
        scene.backgroundColor = .clear
        
        let en = SKEmitterNode(fileNamed: "Bokeh.sks")
        en?.position = sk.center
        scene.addChild(en!)
        sk.presentScene(scene)
    }
    
}

