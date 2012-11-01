//
//  HSEplusViewController.m
//  HSE+
//
//  Created by  Alexey Khan on 01.11.12.
//  Copyright (c) 2012 Alexey Khan. All rights reserved.
//

#import "HSEplusViewController.h"

@interface HSEplusViewController()

@property (weak, nonatomic) IBOutlet UITextField *email;
@property (weak, nonatomic) IBOutlet UITextField *password;

@end

@implementation HSEplusViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad { [super viewDidLoad]; }
- (void)didReceiveMemoryWarning { [super didReceiveMemoryWarning]; }

// Опускать клавиатуру при нажатии Return
-(IBAction)textFieldDoneEditing:(id)sender { [sender resignFirstResponder]; }
// Опускать клавиатуру при нажатии на background - НЕ ПАШЕТ, ЗАРАЗА
-(IBAction)backgroundTap:(id)sender { [sender resignFirstResponder]; }

@end