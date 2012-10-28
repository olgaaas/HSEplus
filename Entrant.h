//
//  Entrant.h
//  HSE+
//
//  Created by  Alexey Khan on 28.10.12.
//  Copyright (c) 2012 Alexey Khan. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Entrant : NSObject {
    
    // Функция проверки, проходит ли абитуриент по баллу на факультет, в стадии продумывания ;
    
    NSMutableArray *subscribedTo;   // Список подписок ;
    BOOL *hasSubscribtions;         // Есть ли подписки? 1 - есть, 0 - нет ;
    BOOL *newUnpublishedNews;       // Есть ли новые неопубликованные новости? 1 - есть, 0 - нет ;
    BOOL *reminderNeeded;           // Спрашивать, нужно ли заносить новости типа "Напоминание" в ремайндер на iPhone. 1 - нужно, 0 - не нужно ;
}

-(NSMutableArray *)subscribedTo;
-(BOOL *)hasSubscribtions;
-(BOOL *)newUnpublishedNews;
-(BOOL *)reminderNeeded;

-(void)setListOfSubscriptions:(NSMutableArray *)_subscribedTo;
-(void)setSubscriptions:(BOOL *)_hasSubscriptions;
-(void)setUnpublishedNews:(BOOL *)_newUnpublishedNews;
-(void)needReminder:(BOOL *)_reminderNeeded;

@end
