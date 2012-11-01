//
//  Faculty.m
//  HSE+
//
//  Created by Dmitry Lyange on 28.10.12.
//  Copyright (c) 2012 Dmitry Lyange. All rights reserved.
//

#import "Faculty.h"

@implementation Faculty


-(NSString *)name { return name; }
-(int)budgetCapacity { return budgetCapacity; }
-(int)commercCapacity { return commercCapacity; }
-(int)score { return score; }
//-(NSMutableArray *)professions { return professions; }
//-(NSMutableArray *)olympiads { return olympiads; }


-(void)setName:(NSString *)_name { name = _name; }
-(void)setBudgetCapacity:(int)_budgetCapacity { budgetCapacity = _budgetCapacity; }
-(void)setCommercCapacity:(int)_commercCapacity { commercCapacity = _commercCapacity; }
-(void)setScore:(int)_score { score = _score; }
//-(void)setListOfProfessions:(NSMutableArray *)_professions{;}
//-(void)setListOfOlympiads:(NSMutableArray *)_olympiads{;}


@end

