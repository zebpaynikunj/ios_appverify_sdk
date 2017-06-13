//
//  TSCountryPickerView.h
//  PushVerifySDK
//
//  Created by Krishna Jagadish on 12/8/16.
//  Copyright © 2016 Telesign. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol TSCountryPickerViewDelegate <NSObject>

-(void) didPickCountryWithiso:(NSString*) iso countryCode:(NSString*)countryCode;

@end

@interface TSCountryPickerView : UIView
@property ( nonatomic, weak) id<TSCountryPickerViewDelegate> delegate;
@end
