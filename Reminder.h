//
//  Reminder.h
//  
//
//  Created by Olga Kolekonova on 10/29/12.
//
//

#import <Foundation/Foundation.h>

@interface Reminder : NSObject{
    NSString *DateRemind;   // дата ремайндера ;
    NSString *TimeRemind;   // время события ;
    NSString *DateEvent;    // дата события ;
    NSString *TimeEvent;    // время события ;
    NSString *Contain;      // содержание ремайндера ;
    NSString *newsWms;      // переменная для новость/сообщение от старосты ;
    BOOL *SendWarden;       // если сообщение от старосты, отправлять на почту ;
}

-(NSString *)DateRemind;
-(NSString *)TimeRemind;
-(NSString *)DateEvent;
-(NSString *)TimeEvent;
-(NSString *)Contain;
-(NSString *)newsWms;
-(BOOL *)SendWarden;

-(void)setDateRemind:(NSString *)_DateRemind;
-(void)setTimeRemind:(NSString *)_TimeRemind;
-(void)setDateEvent:(NSString *)_DateEvent;
-(void)setTimeEvent:(NSString *)_TimeEvent;
-(void)setContain:(NSString *)_Contain;
-(void)setWms:(NSString *)_newsWms;
-(void)setSendWarden(BOOL *)_SendWarden;
    
@end
