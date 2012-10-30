//
//  Reminder.m
//  
//
//  Created by Olga Kolekonova on 10/29/12.
//
//

#import "Reminder.h"

@implementation Reminder

-(NSString *)DateRemind {return DateRemind;}
-(NSString *)TimeRemind{return TimeRemind;}
-(NSString *)DateEvent{return DateEvent;}
-(NSString *)TimeEvent{return TimeEvent;}
-(NSString *)Contain{return Contain;}
-(NSString *)newsWms{return newsWms;}
-(BOOL *)SendWarden{return SendWarden;}

-(void)setDateRemind:(NSString *)_DateRemind{DateRemind = _DateRemind};
-(void)setTimeRemind:(NSString *)_TimeRemind {TimeRemind = _TimeRemind};
-(void)setDateEvent:(NSString *)_DateEvent{DateEvent = _DateEvent};
-(void)setTimeEvent:(NSString *)_TimeEvent{TimeEvent = _TimeEvent};
-(void)setContain:(NSString *)_Contain {Contain = _Contain};
-(void)setWms:(NSString *)_newsWms {newsWms = _newsWms};
-(void)setSendWarden(BOOL *)_SendWarden {SendWarden = _SendWarden};


@end
