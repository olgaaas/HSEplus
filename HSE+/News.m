//
//  News.m
//  HSE+
//
//  Created by Dmitry Lyange on 27.10.12.
//  Copyright (c) 2012 Dmitry Lyange. All rights reserved.
//

#import "News.h"

@implementation News

-(NSDate *)date { return date; }
-(NSString *)type { return type; }
-(NSString *)author { return author; }
-(NSString *)body { return body; }
-(BOOL)isPublished { return isPublished; }
-(BOOL)Subscribed { return Subscribed; }

-(void)setDate:(NSDate *)_date { date = _date; }
-(void)setType:(NSString *)_type { type = _type; }
-(void)setAuthor:(NSString *)_author { author = _author; }
-(void)setBody:(NSString *)_body { body = _body; }
-(void)setPublisher:(BOOL)_isPublished { isPublished = _isPublished; }
-(void)setSubscriber:(BOOL)_Subscribed { Subscribed = _Subscribed; }

@end
