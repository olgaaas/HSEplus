//
//  Recommends.h
//  
//
//  Created by Olga Kolekonova on 10/30/12.
//
//

#import <UIKit/UIKit.h>

@interface Recommends : NSObject {
    NSString *faculty;      // факультет
    NSString *kurs;         // курс
    NSString *fio;          // Фамилия, имя, отчество
    NSString *contact;      // контакт, возможно опционально
    NSString *body;         // тело рекомендации
    BOOL *noflood;          // проверка на флуд модератором
}

-(NSString *)faculty;
-(NSString *)kurs;
-(NSString *)fio;
-(NSString *)contact;
-(NSString *)body;
-(BOOL *)noflood;

-(void)setFaculty:(NSString *)_faculty;
-(void)setKurs:(NSString *)_kurs;
-(void)setFio:(NSString *)_fio;
-(void)setContact:(NSString *)_contact;
-(void)setBody:(NSString *)_body;
-(void)setFlood:(BOOL *)_noflood;

@end
