//
//  Faculty.h
//  HSE+
//
//  Created by Dmitry Lyange on 28.10.12.
//  Copyright (c) 2012 Dmitry Lyange. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Faculty : NSObject {
    NSString *name;                 // Название факультета/отделения;
    int budgetCapacity;             // Количество бюджетных мест на факультете/отделении;
    int commercCapacity;            // Количество коммерческих мест на факультете/отделении;
    int score;                      // Проходной балл прошлого года;
    //    NSMutableArray *professions;    // Список специальностей, получаемых на факультете/отделении;
    //    NSMutableArray *olympiads;      // Учитываемые при поступлении олимпиады;
}

-(NSString *)name;
-(int)budgetCapacity;
-(int)commercCapacity;
-(int)score;
//-(NSMutableArray *)professions;
//-(NSMutableArray *)olympiads;

-(void)setName:(NSString *)_name;
-(void)setBudgetCapacity:(int)_budgetCapacity;
-(void)setCommercCapacity:(int)_commercCapacity;
-(void)setScore:(int)_score;
//-(void)setProfessions:(NSMutableArray *)_professions;
//-(void)setOlympiads:(NSMutableArray *)_olympiads;


@end

