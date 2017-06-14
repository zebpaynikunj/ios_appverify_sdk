//
//  TSBase64.h
//  TSM
//
//  Created by TeleSign on 20/12/12.
//  Copyright (c) 2012 TeleSign. All rights reserved.
//
/**

 File: TSBase64.h
 @brief TSBase64 class for encode & decode in Base64.
 */

#import <Foundation/Foundation.h>

// CLASS INTERFACES:

@interface TSBase64 : NSObject {
}
+ (void)initialize;
+ (NSString *)encode:(NSData *)rawBytes;
+ (NSData *)decode:(NSString *)string;
@end
