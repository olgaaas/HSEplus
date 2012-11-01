//
//  FirstViewController.m
//  HSE+
//
//  Created by  Alexey Khan on 01.11.12.
//  Copyright (c) 2012 Alexey Khan. All rights reserved.
//

#import "FirstViewController.h"

@interface FirstViewController()

@property (weak, nonatomic) IBOutlet UITextField *email;
@property (weak, nonatomic) IBOutlet UITextField *password;

@end

@implementation FirstViewController

- (void)viewDidLoad { [super viewDidLoad]; }
- (void)didReceiveMemoryWarning { [super didReceiveMemoryWarning]; }

// Опустить клавиатуру по нажатию Return
-(IBAction)textFieldDoneEditing:(id)sender { [sender resignFirstResponder]; }

// Опустить клавиатуру по нажатию на background
/* НЕ ПАШЕТ, ЗАРАЗА
-(IBAction)backgroundTap:(id)sender { [sender resignFirstResponder]; }
*/
@end