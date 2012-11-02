//
//  Student.m
//  HSE+
//
//  Created by  Alexey Khan on 27.10.12.
//  Copyright (c) 2012 Alexey Khan. All rights reserved.
//

#import "Student.h"

@implementation Student

// Описание методов для получения значений полей объекта класса Student;
-(NSString *)name { return name; }
-(NSString *)email { return email; }
-(NSString *)group { return group; }
-(NSString *)faculty { return faculty; }
-(BOOL)isWarden { return isWarden; }
-(BOOL)hasReminder { return hasReminder; }
-(BOOL)knockedOut { return knockedOut; }

// Описание методов для изменения значений полей объекта класса Student;
-(void)setName:(NSString *)_name { name = _name; }
-(void)setEmail:(NSString *)_email { email = _email; }
-(void)setGroup:(NSString *)_group { group = _group; }
-(void)setFaculty:(NSString *)_faculty { faculty = _faculty; }
-(void)setWarden:(BOOL)_isWarden { isWarden = _isWarden; }
-(void)setReminder:(BOOL)_hasReminder { hasReminder = _hasReminder; }
-(void)setStatus:(BOOL)_knockedOut { knockedOut = _knockedOut; }


@end
