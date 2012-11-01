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

-(IBAction)textFieldDoneEditing:(id)sender { [sender resignFirstResponder]; }
-(IBAction)backgroundTap:(id)sender { [sender resignFirstResponder]; }

@end