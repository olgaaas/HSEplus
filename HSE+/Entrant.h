//
//  Entrant.h
//  HSE+
//
//  Created by  Alexey Khan on 27.10.12.
//  Copyright (c) 2012 Alexey Khan. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Entrant : NSObject {
    
    NSString *faculty;      // Факультет или отделение;
    NSString *group;        // Номер академической группы;
    NSString *name;         // Полное имя;
    NSString *email;        // Корпоративный email с @edu.hse.ru;
    BOOL *isWarden;         // Является старостой;
    BOOL *hasReminder;      // Установил приложение, значит, можно присылать напоминания;
    BOOL *knockedOut;       // Вылетел за незачи
}

-(NSString *)name;
-(NSString *)email;
-(NSString *)group;
-(NSString *)faculty;
-(BOOL *)isWarden;
-(BOOL *)hasReminder;
-(BOOL *)knockedOut;

-(void)setName:(NSString *)_name;
-(void)setEmail:(NSString *)_email;
-(void)setGroup:(NSString *)_group;
-(void)setFaculty:(NSString *)_faculty;
-(void)setWarden:(BOOL *)_isWarden;
-(void)setReminder:(BOOL *)_hasReminder;
-(void)setStatus:(BOOL *)_knockedOut;


@end
