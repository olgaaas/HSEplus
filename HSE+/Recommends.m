//
//  Recommends.m
//  
//
//  Created by Olga Kolekonova on 10/30/12.
//
//

#import "Recommends.h"


@implementation Recommends


-(NSString *)faculty { return faculty; }
-(NSString *)kurs { return kurs; }
-(NSString *)fio { return fio; }
-(NSString *)contact { return contact; }
-(NSString *)body { return body; }
-(BOOL)noflood { return noflood; }


-(void)setFaculty:(NSString *)_faculty { faculty = _faculty; }
-(void)setKurs:(NSString *)_kurs { kurs = _kurs; }
-(void)setFio:(NSString *)_fio { fio = _fio; }
-(void)setContact:(NSString *)_contact { contact = _contact; }
-(void)setBody:(NSString *)_body { body = _body; }
-(void)setFlood:(BOOL)_noflood { noflood = _noflood; }



@end