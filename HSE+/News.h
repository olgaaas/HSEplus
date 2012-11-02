//
//  News.h
//  HSE+
//
//  Created by Dmitry Lyange on 27.10.12.
//  Copyright (c) 2012 Dmitry Lyange. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface News : NSObject {
    NSString *author;      // Факультет или отделение, выложивший новость;
    NSString *type;        // Тип новости;
    NSDate *date;          // Дата публикации новости;
    NSString *body;        // Сам текст новости;
    BOOL isPublished;     // Вывешена ли новость в ленту;
    BOOL Subscribed;      // Подписан ли на новости;
}

-(NSDate *)date;
-(NSString *)type;
-(NSString *)author;
-(NSString *)body;
-(BOOL)isPublished;
-(BOOL)Subscribed;

-(void)setDate:(NSDate *)_date;
-(void)setType:(NSString *)_type;
-(void)setAuthor:(NSString *)_author;
-(void)setBody:(NSString *)_body;
-(void)setPublisher:(BOOL)_isPublished;
-(void)setSubscriber:(BOOL)_Subscribed;


@end

