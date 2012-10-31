//
//  Entrant.m
//  HSE+
//
//  Created by  Alexey Khan on 28.10.12.
//  Copyright (c) 2012 Alexey Khan. All rights reserved.
//

#import "Entrant.h"

@implementation Entrant

// Описание методов для получения значений полей объекта класса Entrant;
-(NSMutableArray *)subscribedTo { return subscribedTo; }
-(BOOL *)hasSubscriptions { return hasSubscriptions; }
-(BOOL *)newUnpublishedNews { return newUnpublishedNews; }
-(BOOL *)reminderNeeded { return reminderNeeded; }


// Описание методов для изменения значений полей объекта класса Entrant;
-(void)setSubscriptions:(BOOL *)_hasSubscriptions { hasSubscriptions = _hasSubscriptions; }
-(void)setUnpublishedNews:(BOOL *)_newUnpublishedNews { newUnpublishedNews = _newUnpublishedNews; }
-(void)needReminder:(BOOL *)_reminderNeeded { reminderNeeded = _reminderNeeded; }
-(void)setListOfSubscriptions:(NSMutableArray *)_subscribedTo {
    if (!hasSubscriptions) NSLog(@"Подписок нет. Создать подписку.");
    else NSLog(@"Уже есть подписки. Надо либо добавить, либо удалить.");
}

@end
