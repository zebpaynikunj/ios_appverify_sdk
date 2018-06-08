//
//  TSWebService.h
//  TSM
//
//  Created by TeleSign on 20/12/12.
//  Copyright (c) 2012 TeleSign. All rights reserved.
//

/**

 File: TSWebService.h
 @brief TSWebService class for calling webservice & handle response.
 */

#import <Foundation/Foundation.h>
@protocol TSWebServiceDelegate;

// CLASS INTERFACES:

NS_ASSUME_NONNULL_BEGIN

@interface TSWebService : NSObject {


}

@property(nonatomic, strong) id<TSWebServiceDelegate> delegate;


- (void)request:(NSString *)requestType
    withResourceItems:(nullable NSArray *)resourceItems
        andParameters:(nullable NSDictionary *)params
        andServiceKey:(NSString *)aServicekey;


@end

@protocol TSWebServiceDelegate <NSObject>

@optional
- (void)responsedidreceive:(NSString *)response_string
                    forKey:(NSString *)reskey;
- (void)responsedidfail:(NSString *)response_error forKey:(NSString *)reskey;

@end

NS_ASSUME_NONNULL_END
